def transformIntger():
    n = int(input("Enter A Number : \n"))
    nn = int(str(n) + str(n))
    nnn = int(str(n) + str(n) + str(n))
    result = n + nn + nnn
    result = str(n) + " + " + str(nn) + " + " + str(nnn) + " = " + str(result)
    return result

print(transformIntger())
