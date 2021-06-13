class TV:
    def __init__(self,brand,model,color,screen_size,resolution,is_smart,price):
        self.brand=brand
        self.model=model
        self.color=color
        self.screen_size=screen_size
        self.resolution=resolution
        self.is_smart=is_smart
        self.price=price


    def to_be_sold(self):
        self.brand=str(input("Enter TV's brand:"))
        self.model=str(input("Enter TV's model:"))
        self.color=str(input("Enter TV's color:"))
        self.screen_size=str(input("Enter TV's screen_size:"))
        self.resolution=str(input("Enter TV's resolution:"))
        self.is_smart=str(input("Type if this TV is smart or not:"))
        self.price=str(input("Enter TV's price:"))
    def to_be_bought(self):
        print(self.brand)
        print(self.model)
        print(self.color)
        print(self.screen_size)
        print(self.resolution)
        print(self.is_smart)
        print(self.price)



s=TV(' ',' ',' ',' ',' ',' ',' ')
s.to_be_sold()
s.to_be_bought()
