#SOIT107_BASE_005

x, y = list(map(int, input().split() ))
# a[0] becomes x
# a[1] becomes y

print( 'Enter two numbers: The remainer is' , x % y )

x, y = list(map(int, input().split() ))

#SOIT107_BASE_006
if x==y:
    print( 'Enter two numbers:  It is a square ', end='')
else:
    print( 'Enter two numbers:  It is not a square ', end='')