def genereatePattern(n):
    
    # Upper half of the pattern
    for i in range(n):
        for j in range(i+1):
            print("*", end=" " )
        print()
        
    # Lower half of the pattern
    for i in range(n-1):
        for j in range(n-i-1):
            print("*", end=" ")
        print()
        
genereatePattern(5)

