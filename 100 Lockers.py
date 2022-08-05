open = 0
closed = 0
open_list = []
def locker(num_lockers):
    global open, closed
    num = 1
    while num**2 <= num_lockers:
        open_list.append(num**2)
        num += 1
    open = len(open_list)
    closed = num_lockers - len(open_list)
def run():
    global open_list, closed, open
    open_list = []
    open = 0
    closed = 0
    endings = ["st", "nd", "rd", "th"]
    try:
        user_input = int(input("Enter a number of lockers: "))
    except ValueError:
        print ("Enter any whole number")
    if user_input == 1:
        print("No lockers will be open")
    else:
        user_input = user_input + 1
        locker(user_input)
        return_str = "The "
        for index in range(0, len(open_list)):
            if index == (len(open_list) - 1):
                if str(open_list[index])[-1:] == "1":
                    return_str += (str(open_list[index]) + endings[0])
                elif str(open_list[index])[-1:] == "2":
                    return_str += ("and " + str(open_list[index]) + endings[1])
                elif str(open_list[index])[-1:] == "3":
                    return_str += ("and " + str(open_list[index]) + endings[2])
                else:
                    return_str += ("and " + str(open_list[index]) + endings[3])
            else:
                if str(open_list[index])[-1:] == "1":
                    return_str += (str(open_list[index]) + endings[0] + ", ")
                elif str(open_list[index])[-1:] == "2":
                    return_str += (str(open_list[index]) + endings[1] + ", ")
                elif str(open_list[index])[-1:] == "3":
                    return_str += (str(open_list[index]) + endings[2] + ", ")
                else:
                    return_str += (str(open_list[index]) + endings[3] + ", ")
        if len(str(open)) == 1:
            return_str += " \nlocker will be open."
        else:
            return_str += " \nlockers will be open."
        print (return_str)
while True:
    run()
    print ("Open Lockers: " + str(open))
    print ("Closed Lockers: " + str(closed-1) , "\n")