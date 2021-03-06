from algociv.engine.game.structures.building import Building
from algociv.engine.game.structures.worker import Worker
from algociv.engine.gravity.grid.assets import Coordinates, Unit
from algociv.engine.game.items.items import *
from algociv.engine.game.research.research import *
from algociv.engine.game.game.errors import DoesNotHaveRequiredItems, NotCraftable, NotMineable, CannotCraft
from algociv.engine.game.game.errors import CannotMine, NotEnoughEnergy, InvalidStructureType, ReachedCap, CannotProduceEnergy
from .internal import *
from algociv.engine.game.structures.updater import update_structures
from algociv.engine.game.modules.modules import Module


class Actions:
    """
    All the actions civilizations can take use of
    """
    def __init__(self, gameinstance):
        self.__game__ = gameinstance

    def mine(self, structure, unit: Unit):
        """
        Mines a unit, and puts the resources into the building inventory.
        :return:
        """
        if structure.__can_mine__ is False:
            raise CannotMine("This structure is not able to mine.")

        if not is_mineable(unit.value.kwargs['material'], self.__game__.__traits__.__mineables__):
            raise NotMineable(f"The material {unit.value.kwargs['material']} is not mineable.")

        structure.__inventory__.append(unit.value.kwargs['material'])

    def produce_energy(self, structure, materials: list):
        """
        Generates energy by going through the materials given.
        :param structure:
        :param materials:
        :return:
        """
        if not structure.__can_produce_energy__:
            raise CannotProduceEnergy('This structure cannot produce energy.')

        for material in materials:
            structure.energy += material.__energy__

    def scan(self, structure):
        """
        Basically uses generate() on __grid__
        :return:
        """
        return structure.__grid__.generate(structure.__coordinates__, structure.__dimensions__)

    def build_module(self, structure, module: Module):
        """
        Builds a module to a structure
        :param structure:
        :param module:
        :return:
        """
        structure.energy -= module.__cost__
        structure.__modules__.add(module)

    def destroy_module(self, structure, module):
        """
        Destory a module from a structure
        :param structure:
        :param module:
        :return:
        """
        structure.__modules__.remove(module)

    def craft(self, structure, item: Item):
        """
        Crafts an item
        :param structure:
        :param item:
        :return:
        """
        if structure.__can_craft__ is False:
            raise CannotCraft("This structure is not able to craft.")

        if not is_craftable(item, self.__game__.__traits__.__craftables__):
            raise NotCraftable("This item is not craftable.")

        if not check_required_materials(item.craft, structure.__inventory__.inventory):
            raise DoesNotHaveRequiredItems(f'You do not have enough materials to craft {item.name}')

        else:
            for required_item in item.craft:
                structure.__inventory__.inventory.remove(required_item)
            structure.__inventory__.inventory.append(item)

    def move(self, structure, coordinates: Coordinates):
        """
        Moves a worker to new coordinates
        :param structure:
        :param coordinates:
        :return:
        """
        if structure.__structure_type__ != "WORKER":
            raise InvalidStructureType("Only worker structures are able to use the action move.")

        # Later, we can use find_distance to calculate the amount of energy it takes to move
        self.__game__.__grid__.delete_saved_unit(structure.__coordinates__)
        structure.__coordinates__ = coordinates

        build_structure_on_grid(structure, coordinates, self.__game__.__grid__)

    def repair(self, structure, amount):
        """
        Adds an amount of health to the structure. At the cost of energy
        :param structure:
        :param amount:
        :return:
        """
        if amount+structure.health > structure.__health_cap__:
            raise ReachedCap('Cannot repair, because health cap has been reached.')

        if amount > structure.energy:
            raise NotEnoughEnergy(f"You do not have enough energy to heal by {amount}")

        structure.energy -= amount
        structure.health += amount

    def research(self, structure, research: ResearchItem):
        """
        Researches something.
        :param structure:
        :param research:
        :return:
        """
        structure.energy -= research.__cost__
        self.__game__.__research__.apply_material_costs(structure, research.__material_cost__)
        self.__game__.__research__.research(research)
        update_structures(self.__game__.__structures__.__workers__, self.__game__.__structures__.__buildings__)

    def initialize_structure(self, structure, coordinates: Coordinates):
        """
        Initializes a structure.
        :param building:
        :param coordinates:
        :return:
        """
        result = structure(self.__game__.__grid__, coordinates, self, self.__game__.__traits__)
        build_structure_on_grid(structure, coordinates, self.__game__.__grid__)
        self.__game__.__structures__.__buildings__.append(result)
        return result
