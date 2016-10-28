numbers = [12,37,5,42,8,3]
impares = []
pares = []

while len(numbers) > 0:
    number = numbers.pop()
    if (number % 2 == 0):
        pares.append(number)
    else:
        impares.append(number)
                
print(str(pares) + " Estes são os números pares")
print (str(impares) + " Estes são os números impares")
