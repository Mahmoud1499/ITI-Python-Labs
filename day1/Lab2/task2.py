def front_back_combine(a, b):
    a_len = len(a)
    b_len = len(b)
    a_front = a[:(a_len+1)//2]
    a_back = a[(a_len+1)//2:]
    b_front = b[:(b_len+1)//2]  
    b_back = b[(b_len+1)//2:]
    
    return (a_front + b_front) +" "+ (a_back + b_back)


print("Input abced , abcdef -> ",front_back_combine("abced","abcdef"))