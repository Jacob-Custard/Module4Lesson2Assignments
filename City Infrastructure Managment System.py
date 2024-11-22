# Objective: The aim of this assignment is to apply the concepts of Object-Oriented
#Programming in Python to build a simulated City Infrastructure Management System. This
#system will incorporate classes, objects, methods, and data structures to manage different
#aspects of a city, such as buildings, traffic, and events.

# Task 1 Vehicle Registration System: Create a Python class Vehicle with attributes registration_number,
#type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few
#instances of Vehicle and demonstrate changing the owner.

class Vehicle:                                                                                                               #established class called Vehicle
    def __init__(self, reg_num, type, owner):                                                                                #defining object initialization
        self.reg_num = reg_num                                                                                                 
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):                                                                                       #defining update_owner method to change the owner of a registered vehicle
        self.owner = new_owner    

    def display(self):                                                                                                       #defining a method to display registered vehicles
        print(f"{self.owner} - {self.type} - {self.reg_num}")        

vehicles = {}                                                                                                                #establishing an empty dictionary

while True:                                                                                                                  #while loop to run through a series of choices and call the methods from the vehicle class
    print("\n1.Register vehicle.\n2.Update Owner\n3.Display registered vehicles\n4.Exit")
    choice = input("Please select the which function you would like to perform (1-4): ")

    if choice == "1":
        reg_num = input("What is the reg num of the vehicle you would like to register? ")
        type = input("What type of vehicle is being registered? ")
        owner = input("Who is the owner of the vehicle being registered? ")
        if reg_num in vehicles:
            print("This vehicle is already registered.")
        else:
            vehicles[reg_num] = Vehicle(reg_num, type, owner)

    elif choice == "2":
        reg_num = input("What is the reg num of the vehicle you would like to update? ")
        new_owner = input("Who is the new owner of the vehicle? ")
        if reg_num in vehicles:
            vehicles[reg_num].update_owner(new_owner)
        else:
            print("Vehicle not found")

    elif choice == "3":
        for vehicle in vehicles.values():
            vehicle.display()

    elif choice == "4":
        break

    else:
        print("Input not recognized.")


#Task 2 Event Management System Enhancement: Extend an existing Event class by adding a feature to keep 
#track of the number of participants. Implement a method add_participant that increases the count and a
#method get_participant_count to retrieve the current count.

class Event:                                                                                                              #establishing class 'Event' 
    def __init__(self, name, date):                                                                                       #defining initialization of Event objects
        self.name = name
        self.date = date
        self.participants = []

    def add_participant(self, participant):                                                                              #defining a method to add participants to an event
        self.participants.append(participant)

    def get_participant_count(self):                                                                                     #defining a method to count the number of registered participants for an event
        print(f"The number of registered participants is {len(self.participants)}")    

events = {}                                                                                                               #establishing an empty dictionary

while True:                                                                                                              #while loop with a series of 'if', 'elif' statements to run through series of functions calling the methods from the Event class
    print("\n1.Add event\n2.Add participant\n3.Get registered participant count\n4.Exit")
    choice = input("What function would you like to perform (1-4): ")
    
    if choice == "1":
        new_event = input("What is the name of the new event? ")
        event_date = input("What is the date of the new event (MM/DD/YYYY)? ")
        if new_event not in events:
            events[new_event] = Event(new_event, event_date)
        else:
            print("Event already exits.")    

    elif choice == "2":
        event = input("What event would you like to register a participant for? ")
        new_participant = input("What is the name of the participant you would like to register? ")
        if event in events:
            events[event].add_participant(new_participant)
        else:
            print("Event does not exist, please register event before adding participants.")    

    elif choice == "3":
        event = input("What event would you like to get a participant count for? ")
        events[event].get_participant_count()

    elif choice == "4":
        break

    else:
        print("Input not recognized.")




