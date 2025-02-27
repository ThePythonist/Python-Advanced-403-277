import datetime


class Person:
    def __init__(self, name, birth, city, job):
        self.name = name
        self.birth = birth
        self.city = city
        self.job = job
        self.age = self.calculate_age()

    def calculate_age(self):
        return datetime.datetime.now().year - self.birth

    def talk(self):
        print(f"""
Hi
My name is {self.name} and I'm a {self.job}
I'm {self.age} years old and I live in {self.city}
""")


prsn1 = Person(job="python developer", name="ali", birth=2005, city="tehran")

prsn1.talk()
