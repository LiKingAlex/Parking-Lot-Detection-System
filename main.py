import math


def park_direction(selected_spot):

  #convert selected_spot to int to determine distance to parking spot
  distance = 2 * (math.ceil(int(selected_spot) / 2))

  #Determine direction
  right_side = ["2", "4", "6", "8", "10"]
  left_side = ["1", "3", "5", "7", "9"]

  #Output of the directions to the desired parking spot
  print("***************************************")
  print("DIRECTIONS TO PARKING LOT", selected_spot)
  print("****************************************")

  if selected_spot in right_side:
    print("Go straight", distance, "m then turn right to get to parking lot")

  elif selected_spot in left_side:
    print("Go straight", distance, "m then turn left to get to parking lot")


#DICTIONARY STORING THE PARKING SPACE AVAILABLE OR NOT
parking_space = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": 0
}

while True:
  #Telling user available parking spaces
  print("Here are all available parking spaces: ")
  for key, value in parking_space.items():
    if value == 0:
      print("Lot ", key)

  #Let user select which space they want to park in
  while True:
    park = input("Please enter which parking lot you would like to enter: ")

    if parking_space.get(park) == 0:
      #User selected spot and make it full
      parking_space[park] = 1
      print("You have chosen lot ", park, ".")
      break

    elif parking_space.get(park) == 1:
      print("SORRY, parking lot", park, "is full right now.\n")
    else:
      print("Sorry, that is not a valid parking lot.\n")

  #RETURN PARK DIRECTION
  park_direction(park)
  control = input("\n Would you like to exit? (yes/no) ")
  if control.lower() == "yes":
    break
'''
Diagram for parking spaces
END
|9| 10m from entrance |10|  --> PARKING SPACES 9&10

|7|  8m from entrance |8|  --> PARKING SPACES 7&8

|5|  6m from entrance |6|  --> PARKING SPACES 5&6

|3|  4m from entrance |4|  -->PARKING SPACES  3&4

|1|  2m from entrance |2|  --> PARKING SPACES 1&2

START
'''
