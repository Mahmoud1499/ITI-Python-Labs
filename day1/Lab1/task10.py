string = input("Enter a string: ")

digits=letters=0

for char in string:
    if char.isdigit():
        digits=digits+1
    elif char.isalpha():
        letters=letters+1

print("Number of digits:", digits)
print("Number of letters:", letters)

