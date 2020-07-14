# Notes
This is basically a streamline of my brainstorming. So i will ask, and then answer my own questions.
Yes i'm keeping all of that in.

## Modules
Modules are the things which allow you to do stuff. Such as craft and smelt resources.

Modules: 
    - Powerplant
    - Smelter
    - Constructor

Multiple of the same module give you different bonuses, such as the output, or the time taken to do something.

## Materials & Items
Materials are materials. Basically, these are like raw resources such as Coal, Wood Stone.
But, they can also include processed ores.
Items are what you get when you combine materials.

## Hierarchy Structure
This section describes the general hierarchy of the game. Basically how all the process work together.

### General Hierarchy
This section describes the different interactions
in the game.

#### Game Instance
This is the game. It takes care of gravity engine, runs the structures, updates the civilization and so on.

#### Civilization
This is the civilization instance. Basically, this is what runs you algo. The algo runs commands from the Game Instance
such as create a structure at this coordinate.

#### Gravity
This is the gravity engine. It takes care of the grid, keeping it up to date, rendering it and so on.
It's more of a framework, but calling it an engine sounds cooler.

## Structures
Notes on structures theory, and their technical side.
### Theory
Structures can be built upon units.
Structures are not able to move, but can interact
with other units around it.

The farther away a unit is from the structure,
the more energy it takes to actually interact with the unit.
This is so, a structure at 0, 0 cannot interact
with a unit at 10000, 10000

Structures can interact with units in these ways:
 - Mine
 - Build
 
Each Structure has it's own energy capacity.
Energy can be transferred to the structures.
Structures can also transfer energy to the civilization itself.

Should there be a "memory" variable? This could limit the structure 
from being overpowered, like creating it's own energy while also
building more things. But how should this work?

~~No. Energy capacity already does that, i just need to fully figure out how Mining, Building, and getting energy works.~~
Nope! Modules do that already!

Structures have health aswell.
This can be increased once it reaches 0, poof. Gone.


How should we determine the cost to build one structure though? It would make sense to make it cost materials,
yet how do we determine the cost of it?

1. We could make each structure cost energy.
    -  Probably not. This would work, but this would make it too easy on the algorithm.
2. We could make the structures price in material go up with each new structure.
    - This would work, but it's a very cheap solution, and does not fit with the theme of the project.
3. We could determine the size of the code of the structure, and do some calculations off that.
    - Probably this one. It isn't the best, but it definitely will work. So i'm choosing this one.

To make Solution 3 work, we will use pympler's function asizeof().
sys also provides getsizeof(), yet it's not accurate on custom made classes (which structures are.)

### Technical
Each structure is a class with the metaclass of Structure, which will be contained inside game.
Structures take in their current position, and their energy capacity. energy capacity will be edited as the algorithm
researches new things in the tech tree.


#### Variables
Each structure also has an Inventory object. It's their inventory. This is only edited by the game itself,
for example, if the structure mines some coal, the coal will be added to it's inventory.

New variables will be added as time goes on, and as the game develops.


#### Non-game made changes
We will allow changes to be made, since there is really no point. Anyone could just change the code for it
allowing editing. So might as well just allow it.

Though, if a competition is based of off this game, they will need to make sure that the game is fully
unedited, and that the algo is not editing any variables as it goes through the game.

#### Structure running
To actually run a structure, you have to call upon runtime(). This is put into metaclass Structure()

When the game is going through it's normal runtime, it first lets the civilization go through it's actions,
then loops through every structure and calls runtime(). This is also how variables get changed.


## Workers
This section talks about workers.

### Theory
~~UNSURE IF WORKERS WILL BE ADDED!~~
Alright, i'm adding them. Mobile structures are really needed.

Workers are like moving structures. Except they are more limited. 
They have less energy, and can't perform as many tasks as a structure.

They do also have modules
Some modules:
    - idk
   
### Technical
Workers are classes, like everything else is.
It has modules, kept track of by the ModuleManager.

The game itself, on each cycle, runs runtime().
