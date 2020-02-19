burger = float('inf')
drink = float('inf')
for _ in range(3):
    burger = min(burger, int(input()))
for _ in range(2):
    drink = min(drink, int(input()))
print(burger+drink-50)

