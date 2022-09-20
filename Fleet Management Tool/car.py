import json # For serialisation and deserialisation of the car (data) structure

"""
This class implements features of a car. 
If you want to save the details of the car you can serialise it to json format and write to a file
There a several methods that allow you to drive, refuel and print info about the car.
The class car provides one constructor that requires several parameters. 
"""
class Car:
  # Class members
  model = None
  year = None
  colour = None
  fuelcapacity = None #as litres
  fuelintank = None #as litres
  fuelconsumption = None #as mpg
  mileage = None #in miles
  regnumber = None
  
  # Class methods
  # This method returns a json string containing all of the memebers from the class car
  def serialise(self):     
    serial = {"model": str(self.model),        #serial is a local dictionary that we have created. 
              "year": str(self.year),
              "colour":str(self.colour),
              "fuelcapacity":str(self.fuelcapacity),
              "fuelintank":str(self.fuelintank),
              "fuelconsumption":str(self.fuelconsumption),
              "mileage":str(self.mileage),
              "regnumber":str(self.regnumber)}
    return json.dumps(serial)      # json.dumps converts a python object (local dictionary in this casse)
                                   # to a json string 
  
  # This is a constructor of the class car
  # Required parameters are:
  # model - specifies the model of the car
  # year - year of manufacturing
  # colour - specifies the colour of the car
  # fuelcapacity - specifies the maximum volume of fuel the car can hold
  # fuelconsumption - specifies how much fuel the car is using
  # reg - the registration plate of the car
  def __init__ (self, model, year, colour, fuelcapacity, fuelconsumption, reg):
    self.model = model   #we are accessing each member and setting it to what we want to feed to the constructor
    self.year = year
    self.colour = colour
    self.fuelcapacity = fuelcapacity
    self.fuelconsumption = fuelconsumption
    self.fuelintank = fuelcapacity
    self.mileage = 0
    self.regnumber = reg
  
  # This method "drives" the car for a given distance
  # Driving the car increases the car mileage and reduces the fuel in tank
  # This method will raise an exception when the car range is less than the intended distance to travel
  def drive(self,distance):
    print("we are going to drive for " +  str(distance))
    carrange = (self.fuelintank - (self.fuelcapacity*0.05))*self.fuelconsumption/4.54609 #this tells us the car range in miles
    if carrange<distance:
       raise Exception(carrange)    
    self.mileage = self.mileage + distance #cumulative mileage of the car
    consumedfuel = distance / self.fuelconsumption
    consumedfuel_l = consumedfuel * 4.54609 # One imperial gallon in litres
    self.fuelintank = self.fuelintank - consumedfuel_l
    print("we have been driving for " +  str(distance))
  
  # This method "refuels" the car by increasing the value of the fuelintank member by the fueltopup parameter
  # The returned value is how much fuel you have topped up 
  def refuel(self,fueltopup):
    if fueltopup < (self.fuelcapacity - self.fuelintank):
      # all fuel topup is going into the tank
      self.fuelintank = self.fuelintank + fueltopup
      return fueltopup
    else:
      # This covers the case of wanting to top up more fuel than the tank can hold
      fueltop_2 = self.fuelcapacity - self.fuelintank   
      self.fuelintank = self.fuelcapacity
      return fueltop_2
      
  # This method prints the details of the object car
  def info(self):
    # Our print should look like:
    # Car: chr (midnight black) KF21CMX
    #   Manufacturing year: 2021
    #   Tank: 25l/45l
    #   Average fuel consumption: 61.2 mpg
    #   Mileage: 100000000 miles
    print("Car: " + self.model + " ( " + self.colour + " ) " + self.regnumber)
    print("  Manufacturing year: " + str(self.year ))
    print("  Tank: " + str(self.fuelintank) + " l " + " / " + str(self.fuelcapacity) + " l ")
    print("  Average fuel consumption: " + str(self.fuelconsumption) + " mpg ")
    print("  Mileage: " + str(self.mileage) + " miles" )

# Public functions 

# The purpose of this function is to convert the json string back to a Python object Car.
def deserialisecar(jsontxt): 
  loaddata = json.loads(jsontxt) # This converts the json string into a Python dictionary
  car = Car(loaddata["model"],       #we are accessing the value of the dictionary by the key as set in the serialise method
            int(loaddata["year"]),        
            loaddata["colour"],
            float(loaddata["fuelcapacity"]),
            float(loaddata["fuelconsumption"]),
            loaddata["regnumber"])
  car.fuelintank = float(loaddata["fuelintank"])
  car.mileage = float(loaddata["mileage"])
  return car 
            
  
     