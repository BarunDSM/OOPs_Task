class car:
    def __init__(self,speed,company,model,price):
        self.__speed=speed
        self.__model=model
        self.__company=company
        self.__price=price
    def setspeed(self,v):
        self.__speed=0 if v<0 else v
    def getspeed(self):
        print(self.__speed)
        
c1=car(123,"Porche","xyz",120000000)
c1.setspeed(9123)
c1.getspeed()