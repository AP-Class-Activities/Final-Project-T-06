import sqlite3


con = sqlite3.connect("Personal informations.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS customers( id integer ,username text,password text,name text,family_name text,email text,wallet_currency integer,address text,phone text)") 
con.commit()

import random
import math
class customer : 
    def  __init__(self,id,username,password ,name ,family_name , email  , wallet_currency, address  ,cart ,purchases ,favorites , phone ):
        self.__id=id
        
        self.__username =username

        self.__password=password
        
        self.__name =name
        
        self.__family_name=family_name
        
        self.__wallet_currency=wallet_currency
        
        self.__email=email
        
        self.__address=address
        
        self.__cart=cart
        
        self.__purchases=purchases
        
        self.__favorites=favorites
        
        self.__phone=phone
        
    #setter and getters


    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self , value):
        self.__id=value
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self , value):
        self.__email=value
    
    @property
    def name(self):
        return self.__name            
    @name.setter
    def name(self,value):
        self.__name =value

        
    @property
    def family_name(self):
        return self.__family_name
    @family_name.setter
    def family_name(self,value):
        self.__family_name =value
        

        
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self,value):
        self.__phone = value 


    
    @property
    def wallet_currency(self):
        return self.__wallet_currency
    @wallet_currency.setter
    def wallet_currency(self,value):
        self.__wallet_currency=value


        
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self,value):
        self.__address=value

        

    @property
    def cart(self):
        return self.__cart
    @cart.setter
    def cart(self,value):
        self.__cart=value



    @property
    def purchases(self):
        return self.__purchases
    @purchases.setter
    def purchases(self,value):
        self.__purchases=value




    @property
    def favorites(self):
        return self.__favorites
    @favorites.setter
    def favorites(self,value):
        self.__favorites=value
        



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
        all_usernames = cur.execute("SELECT username FROM customers")
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


            
        
        self.address = input("enter your address : ")

        
        
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
                print('the number should be posetive and only have 11 digits')
                self.phone = str(input('enter your phone number :'))
            else:
                break

        self.id="CU" + str(random.randint(100000,999999))
        self.wallet_currency=0
        gh = (str(self.id),str(self.username),str(self.password),str(self.name),str(self.family_name),str(self.email),str(self.wallet_currency),str(self.address),str(self.phone))
        cur.execute("INSERT INTO customers VALUES(?,?,?,?,?,?,?,?,?)",gh)
        con.commit()
        return (self)
    
    def login(self):
        a=input('Enter your username:')
        b=input('Enter your password:')
        all_usernames = cur.execute("SELECT username FROM customers")
        cur.fetchall
        L1=()
        for i in all_usernames:
            L1=i+L1
        all_passwords = cur.execute("SELECT password FROM customers")
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
        
        return self
    def deposit(self):
        a=input('Enter your username:')
        b=input('Enter your password:')
        all_usernames = cur.execute("SELECT username FROM customers")
        cur.fetchall
        L1=()
        for i in all_usernames:
            L1=i+L1
        all_passwords = cur.execute("SELECT password FROM customers")
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
        x=cur.execute("SELECT wallet_currency FROM customers WHERE username = '"+a+"'")
        l=()
        for i in x:
            l=i+l
        c=l[0]+c
        cur.execute("UPDATE customers SET wallet_currency ='"+str(c)+"'"+"WHERE username ='"+a+"'") 
        con.commit()
    def __str__(self):
        return 'id:{} username:{} password:{} name:{} family_name:{} email:{} wallet_currency:{} address:{} cart:{} purchases:{} favorites:{} phone:{}'\
            .format(self.id,self.username,self.password, self.name , self.family_name,self.email , self.wallet_currency, self.address ,self.cart ,self.purchases ,self.favorites , self.phone)


              
s = customer ('ffsdfdas','asdfg','iluahsasfh', 'fg', 'gj' , 'qwert@qwer.com' , 1234 , 'tehran' ,1234 ,[] ,[] , '09113816466')
#s.registeration(password2=123)
#s.login()
s.deposit()

