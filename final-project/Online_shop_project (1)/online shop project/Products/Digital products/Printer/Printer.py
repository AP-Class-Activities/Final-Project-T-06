class Printer:
    def __init__(self,brand,model,printing_size,printing_type,coler_printing,being_wireless,price):
        self.brand=brand
        self.model=model
        self.printing_size=printing_size
        self.printing_type=printing_type
        self.coler_printing=coler_printing
        self.being_wireless=being_wireless
        self.price=price
    def to_be_sold(self):
        self.brand=str(input("Enter printer's brand:"))
        self.model=str(input("Enter printer's model:"))
        self.printing_size=str(input("Enter printer's printing size:"))
        self.printing_type=str(input("Enter printer's printing type:"))
        self.coler_printing=str(input("Type if this printer can coler print or not:"))
        self.being_wireless=str(input("Type if this printer is wireless or not:"))
        self.price=str(input("Enter printer's price:"))
    def to_be_bought(self):
        print(self.brand)
        print(self.model)
        print(self.printing_size)
        print(self.printing_type)
        print(self.coler_printing)
        print(self.being_wireless)
        print(self.price)
s=Printer(' ',' ',' ',' ',' ',' ',' ')
s.to_be_sold()
s.to_be_bought()
