from algociv.engine.game.structures.building import Building
from algociv.engine.game.structures.worker import Worker
from algociv.engine.gravity.grid.assets import Coordinates, Unit
from algociv.engine.game.items.items import *
from algociv.engine.game.game.errors import DoesNotHaveRequiredItems, NotCraftable, NotMineable
from .internal import is_mineable, is_craftable, check_required_materials


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
        if not is_mineable(unit.value.kwargs['material'], self.__game__.__traits__.__mineables__):
            raise NotMineable(f"The material {unit.value.kwargs['material']} is not mineable.")

        structure.__inventory__.append(unit.value.kwargs['material'])

    def craft(self, structure, item: Item):
        """
        Crafts an item
        :param structure:
        :param item:
        :return:
        """

        if not is_craftable(item, self.__game__.__traits__.__craftables__):
            raise NotCraftable("This item is not craftable.")

        if not check_required_materials(item.craft, structure.__inventory__.inventory):
            raise DoesNotHaveRequiredItems(f'You do not have enough materials to craft {item.name}')

        else:
            for required_item in item.craft:
                structure.__inventory__.inventory.remove(required_item)
            structure.__inventory__.inventory.append(item)

    def initialize_building(self, building: Building, coordinates: Coordinates):
        """
        Initializes a building.
        :param structure:
        :param coordinates:
        :return:
        """

        # Apologies for this amount of errors, you may ignore this.
        # I had to do building() and not building.__init__(), because __init__ does not return the proper object instance.
        # Or maybe it does, and i'm just an awful programmer. Who knows.
        result = building(self.__game__.__traits__.__building_energy_cap__,
                            coordinates,
                            self.__game__.__traits__.__building_inventory_cap__,
                            self.__game__.__traits__.__building_module_cap__,
                            self.__game__.__traits__.__building_health__,
                            self.__game__.__traits__.__building_dim__,
                            self.__game__.__grid__,
                            self)

        self.__game__.__structures__.__buildings__.append(result)
        return result

    def initialize_worker(self, worker: Worker, coordinates: Coordinates):
        """
        Initializes a worker
        :param worker:
        :param coordinates:
        :return:
        """
        # Apologies for this amount of errors, you may ignore this.
        # I had to do worker() and not worker.__init__(), because __init__ does not return the proper object instance.
        result = worker(
            self.__game__.__traits__.__worker_module_cap__,
            self.__game__.__traits__.__worker_health__,
            self.__game__.__grid__,
            self.__game__.__traits__.__worker_dim__,
            coordinates)

        self.__game__.__structures__.__workers__.append(result)
        return result
