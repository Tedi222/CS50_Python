import csv

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} from {house}")

students = []

# with open("students.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         student = {"name": name, "home": home}
#         students.append(student)

# we can use a csv module instead

# with open("students.csv") as file:
#     reader = csv.reader(file, delimiter=',')
#     for name, home in reader:
#         students.append({"name": name, "home": home})

def get_name(student):
    return student["name"]


def get_house(student):
    return student["home"]


# for student in sorted(students, key=get_name):
#     print(f"{student['name']} from {student['house']}")

# instead of the above ^^^
# we can also use lambda function

with open("students.csv") as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} from {student['home']}")
