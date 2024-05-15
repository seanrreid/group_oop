class Car:
    def __init__(self, make , model, year):
        self.make = make
        self.model = model
        self.year = year

    def vroom(self):
        return f' {self.model} goes vroom'

    def __str__(self):
        return f'The make is {self.make}, the model {self.model}, the year {self.year}'

    def car_info(self):
        print(f"i am a {self.make}, i was made in {self.year}!")

mickey = Car("Volkswagen", "Golf", "2018")

print(mickey)

print(mickey.vroom())

mickey.car_info()