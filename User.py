# Create a file with the User class, including the __init__ with all the attributes, parameters and default values. 

class User: 
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_reward_member)
        print(self.gold_card_points)

    def enroll(self):
        if self.is_reward_member == True:
            print("User is already a member.")
            return False
        self.is_reward_member = True
        self.gold_card_points = 200

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("You don't have enoug points!")
            return 
        self.gold_card_points = self.gold_card_points - amount

Steven = User("Steven", "DeTeso", "sadeteso@gmail.com", 32) # this creates an instance of the User class and assigns it to the variable "Steven", the variable "Steven" was passed arguments that correspond to the parameters specified in the class and assigned to them. 

print(Steven.display_info()) # here I call the print function and give it the Steven glass and call the method "display_info" on that class to print all the info that was laid out in the method. 

Steven.enroll() # here i am envoking the enroll() method onto the Steven class.

print(Steven.display_info()) # I am checking if the enroll() method is working on the Steven class by printing the results. It does work. 

John = User("John", "Smith", "jsmith@gmail.com", 24) 

Maggie = User("Maggie", "Buns", "mbuns@gmail.com", 19)

Steven.spend_points(50) # checking that the spend_points method works and it does. On output in terminal, 200 decreases to 150. 
print(Steven.display_info())

print(John.display_info())
John.enroll() #I'm enrolling john in the gold card points membership, this changes his points from 0 to 200. 
print(John.display_info())

John.spend_points(80) #John is spending 80 points from his 200 total with the method() "spend_points(self, amount)"
print(John.display_info())

print(Maggie.display_info()) #testing Maggie's info is displayed correctly and it is. 

Steven.enroll() # since i set up a conditional under the enroll method, this will return a string that says "User is already a member" - basically i can't re-enroll here or I'll get that str message

Maggie.spend_points(40) # getting a str message "You don't hae enough points!" in the output because i haven't invoked the enroll method on maggie yet and thus her points are still at 0. 