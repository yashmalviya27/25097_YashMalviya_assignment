# Part C: Difficult Complexity (2 Exercises)
# Exercise 9: The Josephus Elimination Game
def The_Josephus_Elimination_Game():
    n = int(input("Enter the N num: "))
    k = int(input("Enter the K num: "))
    n = [i for i in range(1, n + 1)]
    index = 0
    while len(n) > 1:
        index = ((index + k) - 1) % len(n)
        pop_itm = n.pop(index)
        print(f"Eliminated soldier: {pop_itm} (Remaining: {n})")

    print(f"The sole survivor is: {n[0]}")


The_Josephus_Elimination_Game()
