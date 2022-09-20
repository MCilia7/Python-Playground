# This script will provide a set of functions to support a functionality for managing a fleet of cars

import haversine # import module that calculates the distance between two points
import car     # import module that provides the declaration of the class car
import json   # we will use this to convert the dictionary from and to the JSON string (serialisation of the Car objects) 

# create a global fleet dictionary, the key is the reg, which we will use as a unique ID to find individual cars. 
fleet = dict()  

# this provides a function to present the menu options to a user for the fleet management of cars
# the function will return the selected choice as an integer value
def menu():
  print("menu")
  print("1: List cars ")
  print("2: Modify car")
  print("3: Add car")
  print("4: Delete car")
  print("5: Save")
  print("6: Load")
  print("0: Exit")
  
  choice = input("Select: ")       
  return int(choice)             # the menu function is returning the value of choice

# listcars provides a function to list the details of the cars stored in the global dictionary 'fleet'
def listcars():
  print("listcars")
  global fleet         # making it explicit that fleet is a global variable
  for carreg in fleet:       # iterate through each of the keys  
    fleet[carreg].info()     

# selectcar implements a function to find a car in the dictionary
# this function will return the registration number entered by the user if the car has been found
# otherwise the returned value will be set to None
def selectcar():
  carreg = input("Enter car reg: ")
  global fleet
  # check if entered car registration number exists as a key in the 'fleet' dictionary
  if carreg in fleet:
    return carreg
  else:
    return None

# This function implements a function of driving the car by a given distance entered by the user
def drivedistance():     
  print("Drive distance")
  carreg = selectcar()
  # check if selected car exists in the dictionary (selectcar will return None if it does not)
  if carreg != None:
    # read the mileage from user
    mileage = int(input("Enter mileage covered: "))
    global fleet
    # access the method drive of the selected car to cover the mileage
    fleet[carreg].drive(mileage) # todo: add the exception handling     
  else:
    print("Car not found")
  
# this function implements an option of driving the car by a distance between two geographical points
# distance will be calculated using the haversine method
def drivecoords():          
  print("Drive coords")
  carreg = selectcar()
  # check if selected car exists in the dictionary (selectcar will return None if it does not)
  if carreg != None:           
    lat1 = float(input("Enter starting lat: "))
    lon1 = float(input("Enter starting lon: "))
    lat2 = float(input("Enter ending lat: "))
    lon2 = float(input("Enter enidng lon: "))
    global fleet
    distance = haversine.haversine(lat1,lon1,lat2,lon2) #calling the haversine module and then accessing the haversine function
    fleet[carreg].drive(distance) # todo: add the exception handling       
  else:
    print("Car not found")

# this function implements an option of refueling the car
def refuel():
  print("Refuel")
  carreg = selectcar()
  # check if selected car exists in the dictionary (selectcar will return None if it does not)
  if carreg != None:
    refuel = float(input("Enter amount: "))
    global fleet
    topup = fleet[carreg].refuel(refuel) # get the actual volume of the fuel top up to print it to the user
    print("You have topped up " + str(topup) + " litres of fuel")
  else:
    print("Car not found")

# this function provides options to modify the car from the fleet
def modifycar():
  print("modifycar")
  print("Option 1: Add distance")
  print("Option 2: Add mileage based on coordinates")
  print("Option 3: Refuel")
  print("Option 4: Go back")
  foo = int(input("Select: "))
  if foo == 1:
    drivedistance()
  elif foo == 2:
    drivecoords()
  elif foo == 3:
    refuel()
    
# addcar provides the function of adding a new car to the global dictionary
# user will be asked to input all of the car details from keyboard
def addcar():
  print("addcar")
  model = input("model: ") 
  year = int(input("year: "))
  colour = input("colur: ")
  fuelcapacity = float(input("fuelcapacity: "))
  fuelconsumption = float(input("fuelconsumption: "))
  reg = input("reg: ")
  # Create a new object car that we will assign to the dictionary
  thecar = car.Car(model,year,colour,fuelcapacity,fuelconsumption,reg)  
  global fleet 
  fleet[reg] = thecar  # assign the car to the key in the dictionary
  
# this function removes the car from the dictionary (if found)
def deletecar():
  print("delete car")
  foo = input('car reg')
  global fleet
  # check if the car reg exists in the dictionary
  if foo in fleet: 
   fleet.pop(foo) # we call the 'pop' a method within the dictionary fleet, it has only 1 paramter. 
                  # when the reg (foo) matches what is found in the fleet then the 'pop' method deletes 
                  # the whole entry. 
  else:
   print("reg" + foo + "not found")     

# This function saves the dictionary to a file using the car serialisation method 
# todo: ask the user for a file name to save the fleet into
def save():
   localdict = dict()
   global fleet
   for carreg in fleet:
     localdict[carreg] = fleet[carreg].serialise()
   data = json.dumps(localdict) 
   myfile = open("fleet.json", "w")
   myfile.write(data)
   myfile.close()
  
# This function loads the serialised fleet from a file
# Function reads the json string from a file and deserialises the cars using the car deserialisecar function
# from the car module
# todo: ask the user for a file name from which to load the dictionary
def load():
  myfile = open("fleet.json", "r")    # this opens the file for reading
  data = myfile.read()                # this reads the opened file
  myfile.close()
  localdict = json.loads(data)
  global fleet
  for thekey in localdict: 
    fleet[thekey] = car.deserialisecar(localdict[thekey]) 

# Create infinite loop that will keep asking the user to select
# an option from the main menu
while True:
  userop= menu()
  if userop == 1:
    #list cars
    listcars()
  elif userop == 2:
    #modify car
    modifycar()
  elif userop == 3:
    #add car
    addcar()
  elif userop == 4:
    #delete car
    deletecar()
  elif userop == 5:
    #save car
    save()
  elif userop == 6:
    #load car
    load()
  else: # unsupported choice - break the loop and exit the program
    #exit
    print("exit")
    break
 