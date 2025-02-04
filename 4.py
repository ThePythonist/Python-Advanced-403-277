from faker import Faker

fake = Faker()
people = []

for i in range(4):
    name = fake.name()
    person = {
        "name": name,
        "email": f"{name.split()[0]}@gmail.com",
        "birth": str(fake.date_of_birth()),
        "country": fake.country(),
    }

    people.append(person)

print(people)
