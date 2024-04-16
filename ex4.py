# author: Milosz Cygan


PI = 3.14
A = 1.20

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    try:
        return a / b
    except Exception as E:
        print(E)
    
def multi(a, b):
    return a * b

def pow(a, x):
    return a ** x


# print(sum(1,2))
# print(sub(1,2))
# print(div(1,0))
# print(multi(1,1))
# print(sum(1,2))
# print(pow(2,3))


# in another file

# import ex4
# print(ex4.PI)
# print(ex4.sum(1,2)) 