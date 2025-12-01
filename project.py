import datetime

parking_slots = {'A':[None]*10,'B':[None]*10,'C':[None]*10,'D':[None]*10}
entry_times = {}

def is_parking_full():        
    for section in parking_slots:
        for place in parking_slots[section]:
            if place is None:
                return False 
            else:
                return True

def show_available_sections():
    print("available sections are:")
    for section in parking_slots:
        if None in parking_slots[section]:
            print(section)

def show_available_palce(section):
    for i in range(10):
        if parking_slots[section][i] is None:
            print(f"available place in section {section} is: {i + 1}")

def park_car():         
    car_plate = input("Enter car plate number:")

    show_available_sections()
    section = input("Enter section:").upper()

    if section not in parking_slots or None not in parking_slots[section]:
        print("Invalid")
        return

    show_available_palce(section)
    place = int(input("Enter place number:"))
    if parking_slots[section][place-1] is not None:
        print("This place is already taken")
    else:
        parking_slots[section][place-1] = car_plate
        entry_times[car_plate] = datetime.datetime.now()
        print("car parked succcessfully")
        print(f"you parked at section {section} , place {place} , at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        

def exit_car ():
    car_plate = input("Enter your car plate to exit")
    if car_plate not in entry_times:
        print("This car is not registered as parked.please check the plate number.")
        return
    else:
      for section in parking_slots:
         for i in range(10):
             if parking_slots[section][i] == car_plate:
                parking_slots[section][i] = None
                entry_time = entry_times[car_plate]
                duration = datetime.datetime.now() - entry_time
                total_minutes = duration.total_seconds()/60
                total_hours = total_minutes/60
                cost = total_hours*100
                print(f"You have spend{total_minutes:.2f} minutes")
                print(f"Total cost is {cost:.2f}EGP")

while True:
   print("") 
   print("To park car choose 1")
   print("To exit car choose 2")
   choice = input("Enter choice ")
   if choice == "1":
        if is_parking_full():
            print("sorry,parking is full")
        else :
            park_car()
   elif choice == "2":
        exit_car()
   else:
        print("Invalid choice")