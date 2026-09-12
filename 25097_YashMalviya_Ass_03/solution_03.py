# Exercise 3: The Cargo Train Scanner
def The_Cargo_Train_Scanner():
    resources = ["coal", "iron", "gold", "coal", "timber", "coal"]
    search_resources = input("Enter the resources name you want to search for: ")
    if search_resources in resources:
        total_wagons = resources.count(search_resources)
        ind_wagons = resources.index(search_resources)
        print(f"Number of coal wagons: {total_wagons}")
        print(f"First coal wagon is at index: {ind_wagons}")
    else:
        print(f"Resource not found on train!")


The_Cargo_Train_Scanner()