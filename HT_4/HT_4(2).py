enter = input()
 
def func(enter):
    return enter

def sum_func(a, b):
    return a + b

def multiplication_func(q, w):
    return q * w

def launch_all(enter, sum_func, multiplication_func):
    return enter, sum_func, multiplication_func

print(launch_all(func(enter), sum_func(1, 3), multiplication_func(5, 5)))
