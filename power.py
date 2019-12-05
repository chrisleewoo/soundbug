"""
    calculating powers

"""
   
def pow(r, n):
    return r**n

def pow_loop(r, n):
    x = r
    for i in range(n-1):
        print("x:", x)
        x *= r
    return x

def pow_of_two(n):
    return 2 << n

"""def pow_loop_add(r, n):
    x = 0
    for i in range(n-1):
        for j in range(r):
            x += r
            print("x:", x)
        print("loop")
    return x
this will need to be recursive
"""

print('test\n')


print ("4^2", pow_loop(4,2) )
print ( "4^3", pow_loop(4,3) )