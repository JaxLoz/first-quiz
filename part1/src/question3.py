################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!


class oven():
  
  
   
  def __init__(self):
    self.ingredientes = []
    self.boiled = False;
    self.freezed = False;

  def add(self,item):
    
    self.ingredientes.append(item)
    ##print(f"Ingredientes agregados al horno: {self.ingredientes}")
    return self.ingredientes
  
  def freeze(self):
    
    for i in range(len(self.ingredientes)):
      item = self.ingredientes[i]
      self.ingredientes[i] = "frozen "+ item
    ##print(f"Elementos congelados: {self.ingredientes}")
    self.freezed = True; 
  
  def boil(self):
    for i in range(len(self.ingredientes)):
      item = self.ingredientes[i]
      self.ingredientes[i] = "boiled "+ item
    ##print(f"Elementos hervidos: {self.ingredientes}")
    self.boiled = True;
      
  
  def wait(self):
    print("En espera")
  
  def get_output(self):
    if self.ingredientes == ['boiled lead', 'boiled mercury'] and self.boiled:
      return "gold"
    elif self.ingredientes == ['frozen water', 'frozen air'] and self.freezed:
      return "snow"
    elif self.ingredientes == ["boiled cheese", "boiled dough", "boiled tomato"] and self.boiled:
      return "pizza"
    else:
      return "Receta no encontrada"



def make_oven():
  horno=oven()
  return horno

def alchemy_combine(oven, ingredients, temperature):
  
  for item in ingredients:
    oven.add(item)

  if temperature < 0:
    oven.freeze()
  elif temperature >= 100:
    oven.boil()
  else:
    oven.wait()

  return oven.get_output()
  




alchemy_combine(make_oven(), ["lead", "mercury"], 5000)
