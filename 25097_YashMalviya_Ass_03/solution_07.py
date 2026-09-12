# Exercise 7: Treasure Map Coordinate Filter
def Treasure_Map_Coordinate_Filter():
    coordinate = [[12, 5], [-3, 14], [8, -2], [15, 9], [-5, -6]]
    posative_coordinate = [i for i in coordinate if i[0] > 0 and i[1] > 0]
    print(f"the posative Coordinate: {posative_coordinate}")


Treasure_Map_Coordinate_Filter()