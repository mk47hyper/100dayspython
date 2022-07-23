def foo(a, b=4, c=6):
    print(a,b,c)
foo(20, c=12)
#
# def all_aboard(a, *args, **kw):
#     print(a, args, kw)
# all_aboard(4,7,3,0,x=10,y=64)

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
result = outer_function(5, 10)
print(result)