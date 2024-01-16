#1
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

# შევქმნათ ობიექტები
obj1 = Rectangle(4, 5)

# გამოვიძახოთ ფუნქციები
area = obj1.calculate_area()
perimeter = obj1.calculate_perimeter()

# დაბეჭდეთ შედეგები
print("მართკუხედის ფართობი:", area)
print("მართკუხედის პერიმეტრი:", perimeter)
#2
class Car:
    def __init__(self, model, velocity, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.velocity = velocity

    def full_information(self):
        print(f"{self.model} არის {self.year}-ს წლის, ფერია {self.color}")

    def how_old_is_it(self):
        print(f"{self.model} არის {2023 - self.year} წლის")

    def show_velocity(self):
        print(f"{self.model}-ს სურთია {self.velocity} კმ/სთ")

obj1 = Car("BMW", 300, 2013, "მწვანე")
obj2 = Car("Mercedes", 290, 2010, "ლურჯი")
obj3 = Car("Supra", 350, 2015, "სტაფილოსფერი")

obj1.full_information()
obj2.full_information()
obj3.full_information()

obj1.how_old_is_it()
obj2.how_old_is_it()
obj3.how_old_is_it()

obj1.show_velocity()
obj2.show_velocity()
obj3.show_velocity()
#3
class dog:
    def __init__(self,breed,size,age,color):
      self.breed = breed
      self.size = size
      self.age = age
      self.color = color

    def dog_full_information(self):
        print(f"ჯიში {self.breed},ზომა {self.size},ასაკი {2023- self.age} წელი, ძაღლის ფერი {self.color}.")

obj1 = dog("ლაბრადორ რეტრივერი",1.50,2018,"მოთეთრო-მოყავისფრო")
obj2 = dog("Გერმანული ნაგაზი",1.60,2015,"მოყავისფრო-მოშავო")
obj3 = dog("გოლდენ რეტრივერი",1.70,2019,"ყვითელი")

obj1.dog_full_information()
obj2.dog_full_information()
obj3.dog_full_information()
##4
class Calculator:
    def add_num(self, x, y):
        return x + y
    def divide_num(self, x, y):
        if y != 0:
            return x / y
        else:
            return "ნოლზე არ გაიყოფა"
    def subtract_num(self, x, y):
        return x - y
    def multiply_num(self, x, y):
        return x * y
calculator = Calculator()
result1 = calculator.add_num(10, 3)
result2 = calculator.divide_num(10, 3)
result3 = calculator.subtract_num(10, 3)
result4 = calculator.multiply_num(10, 3)
print(result1)
print(result2)
print(result3)
print(result4)
#5
class People:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age
    def full_info(self):
        print(f"მისი სახელია {self.name}, გვარი {self.lastname}, ის არის {self.age} წლის.")
class Student(People):
    def __init__(self, name, lastname, subject):
        super().__init__(name, lastname, age=None)
        self.subject = subject
    def full_info(self):
        print(f"ამ მოსწავლის სახელი და გვარია {self.name} {self.lastname}, ის სწავლობს {self.subject}.")
class Lecturer(People):
    def __init__(self, name, lastname, subject):
        super().__init__(name, lastname, age=None)
        self.subject = subject
    def full_info(self):
        print(f"ამ მასწავლებლის სახელი და გვარია {self.name} {self.lastname}, ის ასწავლის {self.subject}.")
obj1 = People("დათო", "დათვიაშვილი", 23)
obj2 = Student("ნინი", "ნინიაშვილი", "ხელოვნებას")
obj3 = Lecturer("ლალი", "გრიგალაშვილი", "მათემატიკას")
obj1.full_info()
obj2.full_info()
obj3.full_info()
#7
class Bank_Account:
    def __init__(self, account_name, balance=0):
        self.account_name = account_name
        self.balance = balance
    def get_name(self):
        print(f"გამარჯობა {self.account_name}, თქვენ გაქვთ ბალანსი: {self.balance}")
    def set_name(self, new_account_name):
        self.account_name = new_account_name
    def get_balance(self):
        return self.balance
    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"თანხის შეტანა შესრულებულია,ამჟამად თქვენ ანგარიშზე გაქვთ {self.balance} ლარი.")
        else:
            print("შეცდომა: მიუთითეთ თანხა, რომელიც მეტია 0.")
    def withdraw(self, money1):
        if 0 < money1 <= self.balance:
            self.balance -= money1
            print(f"თანხის გამოტანა შესრულებულია. ამჟამად თქვენ ანგარიშზე გაქვთ {self.balance} ლარი")
        else:
            print("შეცდომა,თანხის გამოტანა შეუძლებელია, რადგან არ არის საკმარისი თანხა ანგარიშზე.")
x = input("გამარჯობა,შეიყვანეთ თქვენი სახელი: ")
account = Bank_Account(x, 0)
y = int(input("შეიყვანეთ თანხა რომლის შეტანაც გინდათ ანგარიშზე: "))
account.deposit(y)
z = int(input("შეიყვანეთ თანხა რომლის გამოტანაც გინდათ ანგარიშიდან: "))
account.withdraw(z)


