def swap(fn):  
                  
    def wrap(n,m):
        if n<m:
            n,m=m,n
        return fn(n,m)
    return wrap

def round_dec(fn):

    def wraper(n,m):
        n=round(n)
        m=round(m)
        return fn(n,m)
    return wraper

@round_dec 
@swap
def add(n,m):
    return n+m 
@round_dec
@swap 
def subract(n,m):
    return n-m
@round_dec
@swap 
def div(n,m):
    return n/m  

print(add(4,5))

print(subract(4,5))

print(div(4,5))

print(subract(2.7,10.3))



