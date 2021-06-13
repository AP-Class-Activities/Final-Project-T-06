class Phone:
    def __init__(self,brand,model,color,camera_specificatios,OS,storage,RAM,processor,price):
        self.brand=brand
        self.model=model
        self.color=color
        self.camera_specificatios=camera_specificatios
        self.OS=OS
        self.storage=storage
        self.RAM=RAM
        self.processor=processor
        self.price=price


    def to_be_sold(self):
        self.brand=str(input("Enter phone's brand:"))
        self.model=str(input("Enter phone's model:"))
        self.color=str(input("Enter phone's color:"))
        self.camera_specificatios=str(input("Enter phone's camera specificatios:"))
        self.OS=str(input("Enter phone's OS:"))
        self.storage=str(input("Enter phone's internal storage:"))
        self.RAM=str(input("Enter phone's RAM:"))
        self.processor=str(input("Enter phone's processor:"))
        self.price=str(input("Enter phone's price:"))
    def to_be_bought(self):
        print(self.brand)
        print(self.model)
        print(self.color)
        print(self.camera_specificatios)
        print(self.OS)
        print(self.storage)
        print(self.RAM)
        print(self.processor)
        print(self.price)



s=Phone(' ',' ',' ',' ',' ',' ',' ',' ',' ')
s.to_be_sold()
s.to_be_bought()
