import random

number = random.randint(1, 10)
print(number)

numbers = random.shuffle([1,2,3,4,5])
print(numbers)

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

print(numbers is [1, 2, 3, 4, 5])




