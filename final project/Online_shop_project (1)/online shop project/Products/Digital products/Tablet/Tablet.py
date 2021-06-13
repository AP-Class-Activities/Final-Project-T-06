class Tablet:
    def __init__(self,brand,model,color,OS,storage,RAM,processor,screen_size,price):
        self.brand=brand
        self.model=model
        self.color=color
        self.OS=OS
        self.storage=storage
        self.RAM=RAM
        self.processor=processor
        self.price=price


    def to_be_sold(self):
        self.brand=str(input("Enter tablet's brand:"))
        self.model=str(input("Enter tablet's model:"))
        self.color=str(input("Enter tablet's color:"))
        self.OS=str(input("Enter tablet's OS:"))
        self.storage=str(input("Enter tablet's internal storage:"))
        self.RAM=str(input("Enter tablet's RAM:"))
        self.processor=str(input("Enter tablet's processor:"))
        self.price=str(input("Enter tablet's price:"))
    def to_be_bought(self):
        print(self.brand)
        print(self.model)
        print(self.color)
        print(self.OS)
        print(self.storage)
        print(self.RAM)
        print(self.processor)
        print(self.price)



s=Tablet(' ',' ',' ',' ',' ',' ',' ',' ',' ')
s.to_be_sold()
s.to_be_bought()
