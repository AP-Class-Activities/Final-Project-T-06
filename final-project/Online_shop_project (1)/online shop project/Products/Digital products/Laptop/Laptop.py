class Laptop:
    def __init__(self,brand,model,color,OS,storage,RAM,processor,graphic_processor,screen_size,price):
        self.brand=brand
        self.model=model
        self.color=color
        self.OS=OS
        self.storage=storage
        self.RAM=RAM
        self.graphic_processor=graphic_processor
        self.processor=processor
        self.price=price


    def to_be_sold(self):
        self.brand=str(input("Enter laptop's brand:"))
        self.model=str(input("Enter laptop's model:"))
        self.color=str(input("Enter laptop's color:"))
        self.OS=str(input("Enter laptop's OS:"))
        self.storage=str(input("Enter laptop's internal storage:"))
        self.RAM=str(input("Enter laptop's RAM:"))
        self.graphic_processor=str(input("Enter laptop's graphic processor:"))
        self.processor=str(input("Enter laptop's processor:"))
        self.price=str(input("Enter laptop's price:"))
    def to_be_bought(self):
        print(self.brand)
        print(self.model)
        print(self.color)
        print(self.OS)
        print(self.storage)
        print(self.RAM)
        print(self.graphic_processor)
        print(self.processor)
        print(self.price)



s=Laptop(' ',' ',' ',' ',' ',' ',' ',' ',' ',' ')
s.to_be_sold()
s.to_be_bought()
