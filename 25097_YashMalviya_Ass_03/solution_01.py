# Part A: Easy Complexity (3 Exercises)
# Exercise 1: The Wizard's Magic Bag
def The_Wizard_Magic_Bag():
    magic_bag = ["staff", "potion", "spellbook"]
    new_item = input("Enter new item: ")
    print("Portal transition activated!")
    removed_item = magic_bag.pop(0)
    print(f"Ejected oldest item: {removed_item}")
    magic_bag.append(new_item)
    print(f"Current items in the magic bag: {magic_bag}")


The_Wizard_Magic_Bag()