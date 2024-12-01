#doubledecorator
def decor(fun):
    def inner():
        result= fun()
        return result*2
    return inner
@decor
def num():
    return 5

resultfun=decor(num)
print(resultfun())

#decorator string
def decorfun(fun):
    def inner(n):
        result = fun(n)
        result += " How are you?"
        return result
    return inner

@decorfun
def hello(name):
    return "Hello " +name

print(hello("john"))