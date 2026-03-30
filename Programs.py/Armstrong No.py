num = int(input("Enter a number: "))
original = num
sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** 3   # for 3-digit numbers
    num = num // 10

if sum == original:
    print("Armstrong")
else:
    print("Not Armstrong")
