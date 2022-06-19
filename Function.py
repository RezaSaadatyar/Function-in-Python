# =================================== Presented by Reza Saadatyar ============================================
# ===================================     Function in Python       ===========================================
import time
# Explain no input and no output
def my_func():
    """
    The is a summary line for myfunc

    Arg:
         no arg
    Return:
          no return
    """
    print("Function")


my_func()
print(my_func.__doc__)

# Explain has input and has output
def my_func1(Var):
    return Var


print(my_func1(3))

# Explain has input and has output (continue)
def my_func2(Var: int) -> int:  # Input my_func2 equal int or str, output equal int because of Var equal int
    return Var


print(my_func2("3"))
# Explain global and local variables
y = 1  # global variable
def my_func3():  # Output this function equal y=1
    print("global variable:", y)


my_func3()

def my_func4():  # Output this function equal y=2
    y = 2  # local variable
    print("local variable:", y)


my_func4()

def my_func5():  # Output this function equal y=5, and also y=1 in line 20 also equal 5
    global y
    y = 5  # y=1 convert y=5
    print("my_func5:", y)


my_func5()

# Explain multi input  in function
def my_func6(a=3, b=2, c=1):  # When function input equals one variable, a, and two variables, a and b, and  so on
    print(a + b + c)


my_func6(10)  # a=10, b=2, c=1
my_func6(10, 3)  # a=10, b=3, c=1
my_func6(c=3)  # a=10, b=2, c=1

# Explain return, pass and yield
def my_func7(r):  # pass function i.e. run other lines of code after it
    r = r + 1
    print('r:', r)
    pass
    s = r + 5
    print('s is:', s)


my_func7(2)

def my_func8(i):  # The code will run until the return (line: return i)
    i = i + 1
    print('i:', i)
    return i
    si = i + 5
    print('si is:', si)


my_func8(3)

def my_func9():  # yield function i.e. Running other lines of code will pause until operation related to the yield
    # function is complete
    yield 1
    yield 2
    yield 3


for val in my_func9():
    print('yield:', val)


# Explain return multivalues
def my_func10():  # using tuple
    stri = "world"
    x = 10
    return stri, x


print(my_func10())

def my_func11():  # using list
    stri = "world"
    x = 10
    return [stri, x]


print(my_func11())

def my_func12():  # using dictionary
    d = dict()
    d['str'] = "world"
    d['x'] = 10
    return d


print(my_func12())

# Explain *arg
def myfunc(*args):
    for i in args:
        print(i)


myfunc("ab", 13, "cd")

def myfunc1(arg, *args):
    print(arg)
    for i in args:
        print(i)


myfunc1("abc", "13c", "cdc")

# Explain **kwargs
def myfunc2(**kwargs):
    for key, value in kwargs.items():
        print("%s=%s" % (key, value))


myfunc2(first="ad", second="asd")

# Example of *args and **kwargs
def myfunc3(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


ar = ("Yes", "Hi", "No")
myfunc3(*ar)
kwar = {"arg1": "Hi", "arg2": "No", "arg3": "Yes"}
myfunc3(**kwar)

# Explain Nested function
def fun(mess):
    def fun1():
        nonlocal mess
        mess = mess * 2
        print(mess)

    fun1()


fun("2")

# Explain closures
def fun_clos(msg):
    def print_fun_clos():
        print(msg)

    return print_fun_clos


a = fun_clos(3)
a()

# Explain closures (continue)
def fun_clos1(msg):
    def print_fun_clos1(msg1):
        return msg * msg1

    return print_fun_clos1


a = fun_clos1(3)  # msg = 3
print(a(4))  # msg1 = 4 >>>> 3*4 = 12
print(a(a(4)))  # msg1 = 12 >>>> 3*12 = 36
print(a(a(a(4))))  # msg1 = 12 >>>> 3*36 = 108

def funct(Fun):
    def app(*args):
        Fun(*args)
        # return Fun(*args)

    return app
@funct  # @funct >>>> funct1 = funct(funct1)
def funct1(name):
    print(f"abcd {name}")
    # return f"abcd {name}"


funct1("fdf")
are = funct1("fdf")
print(are)  # Output is None because of in def app and funct1 have no return or they are inactive (i.e., return Fun(name))
@funct  # @funct >>>> funct2 = funct(funct2)
def funct2():
    print("hello")
    # return "hello"


funct2()

# Explain Time
def a(func):
    def b():
        t1 = time.time()
        func()
        t2 = time.time()
        return str(t2 - t1)

    return b
@a
def func_1():
    mylist = []
    for n in range(0, 10 ** 5):
        mylist.append(n)
@a
def func_2():
    mylist = [n for n in range(0, 10 ** 5)]


print(func_1())
print(func_2())
