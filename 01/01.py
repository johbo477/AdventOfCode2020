file = open('input.txt', 'r') 
lines = file.readlines()
numbers = []
for line in lines:
    number = int(line)
    numbers.append(number)

# part 1
for i in range(0, len(numbers) - 2):
    for j in range(i + 1, len(numbers) - 1):
        if (numbers[i] + numbers[j] == 2020):
            product = numbers[i] * numbers[j]
            #print(numbers[i])
            #print(numbers[j])

            print("Produkten är " + str(product))

# part 2
for i in range(0, len(numbers) - 3):
    for j in range(i + 1, len(numbers) - 2):
        for k in range(j + 1, len(numbers) - 1):
            if (numbers[i] + numbers[j] + numbers[k] == 2020):
                product = numbers[i] * numbers[j] * numbers[k]
                #print(numbers[i])
                #print(numbers[j])
                #print(numbers[k])

                print("Produkten är " + str(product))
