num1 = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))

answer = 1
count = 0

while count < n:
    answer = answer * num1
    count = count + 1

print("The first number was:")
print(num1)
print("The power n was:")
print(n)
print("The final calculation result is:")
print(answer)