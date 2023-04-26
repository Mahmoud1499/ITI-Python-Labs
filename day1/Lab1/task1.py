def reverse_name():
    fName = input("Enter Your First Name : \n")
    lName = input("Enter Your Last Name :\n")
    
    reversedLastName=lName[::-1] 
    reversedFirstName=fName[::-1] 
    
    return reversedLastName + " " + reversedFirstName


print("Welcome ,  Your Reversed Name is " + reverse_name())
