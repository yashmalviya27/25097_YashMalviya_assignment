# Part B: Medium Complexity (5 Exercises)
# Exercise 4: Nightclub VIP Queue
def Nightclub_VIP_Queue():
    vip_guests_list = ["Guido", "Esha", "Rajan", "Kishori"]
    while True:
        gust_name = input("Enter guest name: ")
        if gust_name in vip_guests_list:
            index = vip_guests_list.index(gust_name)
            add_name = vip_guests_list.pop(index)
            vip_guests_list.insert(0, add_name)
            print(
                f"{add_name} moved to the front!\nCurrent VIP queue: {vip_guests_list}"
            )
        elif gust_name.lower() == "exit":
            break
        else:
            print(
                f"Access denied. Not on the VIP list.\nCurrent VIP queue: {vip_guests_list}"
            )


Nightclub_VIP_Queue()
