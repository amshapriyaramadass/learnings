#
# Example file for working with classes
#
class myWheels():
  def wheel1(self):
    print("wheel is alloy")

  def wheel2(self,SomeString):
    print("this is steel rim" + SomeString) 

class myCar(myWheels):
  def wheel1(self):
    myWheels.wheel1(self)
    print("this is car wheel dia 30inch")

  def wheel2(self,someString):
    print("this is car wheel2 uses alloy rim")      

def main():
  
  c = myWheels()
  c.wheel1()
  c.wheel2("this is back wheel")

  c1 =myCar()
  c1.wheel1()
  c1.wheel2("this is car wheel")

  
if __name__ == "__main__":
  main()
