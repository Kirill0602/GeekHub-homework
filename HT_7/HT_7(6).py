

def f(a):
    
    b = [i for i in sorted(map(len, a.split()))]
    return b[0]
string = 'Geek Hub Python 2022'
print(f(string))
