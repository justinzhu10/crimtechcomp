
def say_hello():
    print("Hello, world!")

# Color: blue

# TODO: implement
def echo_me(msg):
    print(msg)

# TODO: understand formatting - can you eliminate the redundancy here?
def append_msg(msg):
    print("Your message should have been: {}!".format(msg))

# TODO: understanding classes (an introduction)
class QuickMaths():
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

# TODO: implement - can you do this more efficiently?
def increment_by_one(lst):
    new_lst = list()

    for x in lst:
        new_lst.append(x + 1)

    return new_lst

# TODO: understand - do we need a return statement here? why?
def update_name(person, new_name):
    person["name"] = new_name

    return person

# TODO: implement - these are still required, but are combinations of learned skills + some
def challenge1(lst):
    new_lst = list()
    for i in reversed(lst):
        new_lst.append(i[::-1])
    print(new_lst)

# TODO: implement
def challenge2(n):
    ans = list()
    lower = 1
    upper = n
    while lower < upper:
        if n % lower == 0:
            upper = int(n / lower)
            ans.append((lower,upper))
        lower += 1

    return ans
