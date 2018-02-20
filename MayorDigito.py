def mayor(n):
    if n < 10:
        return n
    else :
        if n%10 > mayor((n//10)):
            return n%10
        else :
            return mayor(n//10)

