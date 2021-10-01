#assigning variable is ease in python
#if we put some sort of value in any alphabet or word, without any indication it works as variable
#eg

x = "Nepal"
Favourite_Hero = "Iron Man"

print(x)
print(Favourite_Hero)

#naming rule
#legal variables name

myvar = 1
my_var = 2
_myvar = 3
MYVAR = 4
MyVar1 = 5

#illegal variables name

# 2myvar = "a"    my-var = "b"  my var = "c"

#single value to multiple variable and multiple variable

x,y,z = 10,20,30
m =n =o ="Java"

# print() statement prints the value stored in variable
print(m)
print(o)
print(n)

# + character is used to conccate variables

a = "Ram"
b = " and "
c = "Shyam"
print(a+b+c)


#global variable and local variable
#variable in global scope is global variable i.e not inside any function
#variable inside a function is local variable and can ve used in that funcction only

name = "harry"

def function():
    name1 = "garry"
    print (name1)
    print(name)

#inside this function both name and name1 are printed
print(name)
#print(name1)
#name1 cant be printed as it is not global variable

#variable inside function can be made global variable using global keyword but function should be called before that.
def function2():
     global name2
     name2 = "marry"

function2()
print(name2)
