class Person:
    # constructor
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    # INSTANCE methods, apply to instances of the Person class
    def __str__(self):
        return f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}"

    def greet(self, person2):
        print(f'Hello {person2.name}, I am {self.name}!')

    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}")

    # STATIC method - applies to the class, not an instance of the class
    def is_valid_phone(phone):
        return len(phone) == 10

sonny = Person('Sonny', 'sonny@aol.com', '864-555-1234')
jordan = Person('Jordan', 'jordan@nike.com', '815-555-1111')
slef = Person('SLEF', 'slef@self.com', '864-864-8644')

sonny.print_contact_info()

phone = '123456'
phone2 = '1234567890'

def register_user(user_name, phone_number):
    # check the phone number
    if Person.is_valid_phone(phone_number):
        new_user = Person(user_name, 'something@mail.com', phone_number)
        new_user.print_contact_info()
        return new_user
    else:
        print('INVALID PHONE NUMBER')
        return False

register_user('Frank', phone)
register_user('Barney', phone2)
