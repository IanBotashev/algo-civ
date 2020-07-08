from AlgoCiv.engine.gravity.grid import Grid, Seed, Value, Coordinates

values = [Value('Dirt', 65), Value('Wood', 40), Value('Stone', 40), Value('Coal', 20), Value('Iron', 10)]
seed = Seed(1234567890, values, 3, 3)
center = Coordinates(0, 0)
grid = Grid(seed, center)

grid.generate()
for unit in grid.loaded_units:
    print(unit, end='\n')