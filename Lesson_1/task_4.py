number = '18925'
number = int(number)
result = 0

while number > 0:
    if number % 10 > result:
        result = number % 10
    number = number // 10

print(result)
