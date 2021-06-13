import random
import math
import sqlite3

con = sqlite3.connect("Personal informations.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS marketers(id intager, username text,password text,name text,family_name text,phone text,email text,storage_address text,wallet_currency integer)") 
con.commit()
""" 
this class is definding marketer in a Online shop 
this code may change in future

Author: Amirali Bisheban & Ali Mohammadi
Email: bisheban79@gamil.com

usage:
    1)create a new Marketer:
        a=marketer(random.randint(1000,9999),'asdfa','asdfasdf',"ali","ghadery", "09370686566" , [] , 10 , {} , 0 , [] , 0 , 0 , 0 , 0 , 10  )

    2)print Marketer information:
        print(a)
            

  

"""
class marketer:
    def  __init__(self,id,username,password , name , family_name , phone ,email, products , score , storage_address , wallet_currency ,sold_list ,income , profit , expence , orders ,rate ):
        self.__id=id
        self.__username =username

        self.__password=password
        self.__name =name
        self.__family_name=family_name
        self.__wallet_currency=wallet_currency
        self.__storage_address=storage_address
        self.__phone=phone
        self.__email=email
        self.__products=products
        self.__score=score
        self.__sold_list=sold_list
        self.__income=income
        self.__profit=profit
        self.__expence=expence
        self.__orders=orders
        self.__rate=rate


        
    #setter and getters
    @property
    def id(self):
        return self.__id
            
    @id.setter
    def id(self,value):

        self.__id =value
    @property
    def name(self):
        return self.__name
            
    @name.setter
    def name(self,value):

        self.__name =value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self,value):

        self.__phone=value
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self,value):

        self.__email=value
    @property
    def products (self):

        return self.__products

    @products.setter
    def products (self,value):
        self.__products=value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,value):
        self.__score=value
    

    @property
    def wallet_currency(self):
        return self.__wallet_currency

    @wallet_currency.setter
    def wallet_currency(self,value):
        self.__wallet_currency= value

    
    @property
    def family_name(self):
        return self.__family_name
    

    @family_name.setter
    def family_name(self,value):
        self.__family_name = value
    
    @property 
    def storage_address(self):
        return self.__storage_address

    @storage_address.setter
    def storage_address(self,value):
         self.__storage_address=value

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self,value):
        self.__income=value
    
    @property 
    def profit(self):
        return self.__profit
    
    @profit.setter
    def profit(self,value):
        self.__profit=value 

    @property 
    def expence(self):
        return self.__expence

    @expence.setter
    def expence(self,value):
        self.__expence = value

    @property 
    def orders (self):
        return self.__orders
    
    @orders.setter
    def orders (self,value):
        self.__orders= value
    
    @property 
    def rate (self):
        return self.__rate

    @rate.setter
    def rate(self,value):
        self.__rate=value
    @property
    def sold_list(self):
        return self.__sold_list
    
    @sold_list.setter
    def sold_list(self,value):
        self.__sold_list = value

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,value):


        self.__username=value
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,value):

        self.__password=value
    #this part is registraton
    def registeration (self,password2):
        self.name = input("enter your name : ")
        f1=True
        while True:
            for i in self.name :
                f1=True
                if i.isdigit()  == True  :
                    f1=False
            if f1==False:
                print('name should only be characters')
                self.name = input("enter your name : ")
            else:
                break

            
        self.family_name =input("enter your family name : ")
        f2=True
        while True:
            for i in self.family_name :
                f2=True
                if i.isdigit()  == True  :
                    f2=False
            if f2==False:
                print('family name should only be characters')
                self.family_name = input("enter your family name : ")
            else:
                break

        self.username = input('enter your username:')
        all_usernames = cur.execute("SELECT username FROM marketers")
        cur.fetchall
        L1=()
        for i in all_usernames:
            L1=i+L1
        f5=True
        while True:
            while len(str(self.username)) < 5:
                print('username should have more than 5 charachters')
                self.username = input('enter your username:')
            
            if str(self.username) in L1:
                f5=False
            else:
                f5=True

            if f5==False:
                print("This username exists!")
                self.username=input("enter your username:")
            else:
                break
        self.password = input('enter your password:')    
        while len(str(self.password)) < 8:
            print('password should have more than 8 charachters')
            self.password = input('enter your password:')
            
        while self.password != password2 :
            password2 = input('enter your password again:')
            if self.password!=password2:
                print('your passwords does not match')



        self.email = input ("enter your email : ")
        self.email = str(self.email)
        while (self.email[-1:-5:-1]!='moc.') or ('@' not in self.email):
            self.email = str(self.email)
            print('email is invalid')
            self.email = input ("enter your email : ")
    

        
        self.phone = str(input('enter your phone number :'))
        f3=True
        f4=True
        while True:
            
            while True:
                for i in str(self.phone) :
                    f2=True
                    if i.isdigit()  == False  :
                        f2=False
                if f2==False:
                    print('phone numbers should only be digits')
                    self.phone = str(input('enter your phone number :'))
                else:
                    break
            if (int(self.phone) < 0) or (len(str(self.phone)) != 11) :
                print('the number should be posetive or only have 11 digits')
                self.phone = str(input('enter your phone number :'))
            else:
                break
        self.storage_address = input("enter your storage's address:")

        self.id="SL" + str(random.randint(100000,999999))
        self.wallet_currency=0
        gh = (str(self.id),str(self.username),str(self.password),str(self.name),str(self.family_name),str(self.phone),str(self.email),str(self.storage_address),str(self.wallet_currency))
        cur.execute("INSERT INTO marketers VALUES(?,?,?,?,?,?,?,?,?)",gh)
        con.commit()

        return (self)

    
    def login(self):
        a=input('Enter your username:')
        b=input('Enter your password:')
        all_usernames = cur.execute("SELECT username FROM marketers")
        cur.fetchall
        L1=()
        for i in all_usernames:
            L1=i+L1
        all_passwords = cur.execute("SELECT password FROM marketers")
        cur.fetchall
        L2=()
        for i in all_passwords:
            L2=i+L2
        f1 = True
        while True:
            if (a not in L1) or (b not in L2):
                f1=False
            else:
                f1=True
            if f1==False:
                print('username or password invalid!')
                a=input('Enter your username:')
                b=input('Enter your password:')
            else:
                print("You logged in succesfully!")
                break
        return(self)
    def deposit(self):
        a=input('Enter your username:')
        b=input('Enter your password:')
        all_usernames = cur.execute("SELECT username FROM marketers")
        cur.fetchall
        L1=()
        for i in all_usernames:
            L1=i+L1
        all_passwords = cur.execute("SELECT password FROM marketers")
        cur.fetchall
        L2=()
        for i in all_passwords:
            L2=i+L2
        f1 = True
        while True:
            if (a not in L1) or (b not in L2):
                f1=False
            else:
                f1=True
            if f1==False:
                print('username or password invalid!')
                a=input('Enter your username:')
                b=input('Enter your password:')
            else:
                break
        c=int(input("How much do you want to deposit?"))
        x=cur.execute("SELECT wallet_currency FROM marketers WHERE username = '"+a+"'")
        l=()
        for i in x:
            l=i+l
        c=l[0]+c
        cur.execute("UPDATE marketers SET wallet_currency ='"+str(c)+"'"+"WHERE username ='"+a+"'") 
        con.commit()
    
    def __str__(self):
        return 'id: {} username:{},password:{}, name:{} , family_name:{} , phone:{},email:{} , products:{} , score:{} , storage_address:{} , wallet_currency:{} ,sold_list:{} ,income:{} , profit:{} , expence:{} , orders:{} ,rate:{}'\
            .format(self.id ,self.username,self.password , self.name , self.family_name , self.phone , self.email , self.products , self.score , self.storage_address , self.wallet_currency , self.sold_list , self.income , self.profit , self.expence , self.orders ,self.rate)            

#example clint code
a=marketer('sdfgh','adsdfg','asdfa','asdfasdf',"ali","ghadery", "09370686566" , [] , 10 , {} , 0 , [] , 0 , 0 , 0 , 0 , 10  )
#a.registeration(password2=0)
#a.login()
#print(a)
a.deposit()