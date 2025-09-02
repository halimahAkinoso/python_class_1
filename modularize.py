# class Student:
#     def __init__(self, name, course, level): # This runs automatically
#         print("Creating a new student...")
#         self.name = name
#         self.course = course
#         self.level = level
#         print(f"Student {name} with the {course} and {level} has been created!")

#         # When you create a student. __init__ runs automatically
# kemi = Student("Kemi Adebayo", "Computer Science", 300)



# class NigerianStudent:
#     def __init__(self, name, state, course):
#         print(f"Step 1: Creating student object...")
#         self.name = name #STEP 2: aSSIGN NAME TO this OBJECT
#         self.state_of_origin = state #STEP 3: aSSIGN State TO this OBJECT
#         self.course = course #STEP 4: aSSIGN course TO this OBJECT
#         self.student_id = self.generate_id() #STEP 5: Generate ID for this OBJECT
#         print(f"Step 6: {self.name} from {self.state_of_origin} is ready!")
    
#     def generate_id(self):
#         import random
#         return f"UNISAIL{random.randint(1000, 9999)}"
    
# # When you create an object, her's what happens:
# ayo = NigerianStudent("Ayo Daniel", "Lagos", "Street Statistics")    

# print(ayo.name)
# print(ayo.student_id)



# class PhoneUser:
#     def __init__(self, name, network):
#         self.name = name
#         self.network = network
#         self.airtime = 0
#         print(f"{self.name} joined {self.network} network")

#     def buy_airtime(self, amount):
#         self.airtime += amount  # self ensures it goes to the RIGHT person
#         return f"{self.name} now has ₦{self.airtime} airtime"
    
# # Creating multiple users
# abeeb = PhoneUser("Abeeb Bakare", "MTN")
# onisemo = PhoneUser("Onisemo Williams", "Airtel")

# # Each person's actions affect only their own account
# print(abeeb.buy_airtime(500))
# print(onisemo.buy_airtime(1000))
# print(abeeb.airtime)
# print(onisemo.airtime)

# Defining Attributes of a student
# class Student:
#     def __init__(self, name, course, level, state_of_origin):
#         self.name = name                   
#         self.course = course              
#         self.level = level                
#         self.state_of_origin = state_of_origin  
#         self.cgpa = 0.0
#         print(self.name) 
#         print(level)          

# # Creating a student object
# Fathia = Student("Fathia Abdul", "Biochemistry", 300, "Ogun State")

# # Accessing attributes
# print(Fathia.name)
# print(Fathia.course)        
# print(Fathia.state_of_origin)
        
# # 1. Instance Attributes - Unique to each object

# student1 = Student("Anthony Johnson", "Engineering", 200, "Ogun")
# student2 = Student("Fadilat Hassan", "Medicine", 400, "Lagos")

# print(student1.name)  
# print(student2.level) 



# # 2. Class Attributes - Shared by all objects of the class
# class Student:
#      university = "Federal University of Technology Akure" 
#      def __init__(self, name, course):
#           self.name = name         
#           self.course = course


# print(Student.university)     
# # print(student1.university)   
# # print(student2.university)     

# # ### Methods: The Actions (What Objects CAN DO)
# class Student:
#     def __init__(self, name, course, level):
#         # Attributes
#         self.name = name
#         self.course = course
#         self.level = level
#         self.cgpa = 0.0
#         self.fees_paid = False
    

#      # Method: action the student can do
#     def pay_school_fees(self):                   
#         self.fees_paid = True
#         return f"{self.name} has paid school fees for {self.level} level"
    
#     # Method: another action
#     def register_courses(self):                   
#         if self.fees_paid:
#             return f"{self.name} has registered courses for {self.course}"
#         else:
#             return f"{self.name} must pay school fees first!"
    
#       # Method: calculates CGPA
#     def calculate_cgpa(self, grades):           
#         if grades:
#             self.cgpa = sum(grades) / len(grades)
#             return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
#         return "No grades provided"
      

# # Using methods
# Abiodun = Student("Abiodun Akinola", "Gistology", 600)
# print(Abiodun.pay_school_fees())        
# print(Abiodun.register_courses())       
# print(Abiodun.calculate_cgpa([4.2, 3.8, 4.0, 3.5])) 

# #### Types of Methods

# # 1. Instance Methods - Work with specific object data

# # 'self' refers to the specific student
# def pay_school_fees(self):  
#     return f"{self.name} has paid school fees"

# #2. Class Methods - Work with class-level data

# @classmethod
# def get_university(cls):
#     return cls.university

# #3. Static Methods - Don't need object or class data

# @staticmethod
# def academic_calendar():
#     return "Academic session runs from September to July"


# #**How Attributes and Methods Work Together**

class BankAccount:
    def __init__(self, owner, bank_name, balance=0):
        # ATTRIBUTES - What the account HAS
        self.owner = owner
        self.bank_name = bank_name
        self.balance = balance
        self.account_number = self.generate_account_number()
    
    # METHODS - What the account can DO
    def deposit(self, amount):
        """Add money to the account"""
        if amount > 0:
            self.balance += amount  # Method changes attribute
            return f"₦{amount:,} deposited to {self.owner}'s {self.bank_name} account. New balance: ₦{self.balance:,}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Remove money from the account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount  # Method changes attribute
            return f"₦{amount:,} withdrawn from {self.owner}'s account. New balance: ₦{self.balance:,}"
        return "Insufficient funds or invalid amount"
    
    def transfer(self, amount, recipient):
        """Transfer money to another account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"₦{amount:,} transferred from {self.owner} to {recipient}. Remaining balance: ₦{self.balance:,}"
        return "Transfer failed: Insufficient funds"
    
    def check_balance(self):
        """Check current balance"""
        return f"{self.owner}'s {self.bank_name} account balance: ₦{self.balance:,}"
    
    def generate_account_number(self):
        """Generate a unique account number"""
        import random
        return f"2025{random.randint(10000000, 99999999)}"
    
    # Creating and using the account
adunni_account = BankAccount("Adunni Olaleye", "AXT Bank", 50000)

# Attributes (characteristics)
print(f"Owner: {adunni_account.owner}")
print(f"Bank: {adunni_account.bank_name}")
print(f"Account Number: {adunni_account.account_number}")

# Methods (actions)
print(adunni_account.deposit(25000))    
print(adunni_account.withdraw(10000))  
print(adunni_account.transfer(15000, "Sunday James"))  
print(adunni_account.check_balance())   

### Encapsulation
class NigerianBankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self._balance = initial_balance        # Protected attribute
        self.__pin = "1234"                   # Private attribute
        self._transaction_history = []        # Protected attribute
    
    # Public methods - anyone can use these
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transaction_history.append(f"Deposited ₦{amount:,}")
            return f"₦{amount:,} deposited successfully"
        return "Invalid deposit amount"
    
    def withdraw(self, amount, pin):
        if self.__verify_pin(pin):  # Uses private method
            if amount <= self._balance:
                self._balance -= amount
                self._transaction_history.append(f"Withdrew ₦{amount:,}")
                return f"₦{amount:,} withdrawn successfully"
            return "Insufficient funds"
        return "Invalid PIN"
    
    def check_balance(self, pin):
        if self.__verify_pin(pin):
            return f"Current balance: ₦{self._balance:,}"
        return "Invalid PIN"
    
    # Private method - only the class can use this
    def __verify_pin(self, entered_pin):
        return entered_pin == self.__pin
    
    # Protected method - subclasses can use this
    def _get_transaction_history(self):
        return self._transaction_history.copy()
    

    # Using the encapsulated account
ibrahim_account = NigerianBankAccount("Ibrahim Orekunrin", 50000)

# These work - public interface
print(ibrahim_account.deposit(10000))      # ₦10,000 deposited successfully
print(ibrahim_account.withdraw(5000, "1234"))  # ₦5,000 withdrawn successfully
print(ibrahim_account.check_balance("1234"))   # Current balance: ₦55,000