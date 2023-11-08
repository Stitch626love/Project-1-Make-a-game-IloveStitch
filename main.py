

def openingScene():
  Options = ["ESCAPE", "FIGHT"]
  print("You are trapped in an alien spaceship.")
  print("You have two options.")
  print("You can FIGHT or ESCAPE")

  userInput = input();
  if userInput == "FIGHT":
      stitchDeath()
  elif userInput == "ESCAPE":
      stitchEscape()
  else:
      print("Please enter a valid option.");

def stitchDeath():
  Options = ["Y", "N"]
  print("You have killed Stitch")
  print("Would you like to play again Y/N")
  userInput = input();
  if userInput == "Y":
    openingScene()
  elif userInput == "N":
    print("Thank you for Playing!");

def stitchEscape():
  Options = ["LAND","WATER"]
  print("You have found a spaceship to escape in")
  print("You fly to earth and find the island of Kaua’i, Hawaii.")
  print("You can choose to fly towards LAND or WATER");
  userInput = input();
  if userInput == "WATER":
    stitchDeath()
  elif userInput == "LAND":
    stitchLanded() 

def stitchLanded():
  Options = ["FIGHT","PEACE"]
  print("You find yourself on land but are captured immediately")
  print("You are taken to the dogpound.")
  print("You can choose to FIGHT the dogs or choose PEACE");
  userInput = input();
  if userInput == "FIGHT":
    stitchDeath()
  elif userInput == "PEACE":
    stitchAdopted() 

def stitchAdopted():
  print("You have been adopted by Lilo and her Sister")
  print("Congratulations on Winnng the Game.")
  print("Do you want to play again?");
  userInput = input();
  if userInput == "Y":
    openingScene()
  elif userInput == "N":
    print("Thank you for Playing!");


openingScene();
