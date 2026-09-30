a=1000

def f1():
    a=2000
    b=3000
    print(globals()['a'])
    
    
def f2():
    print(a)
    
f1()
f2()
