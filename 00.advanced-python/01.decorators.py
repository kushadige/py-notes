# decorator'ler bir fonksiyon olarak düşünülebilir.
# bu fonksiyonlar başka fonksiyonları input olarak alıp
# bunlara yeni fonksiyonalite kazandırıp bunları döndürecekler.
# input olarak verdiğimiz fonksiyonu değiştirmezler.

def print_func1():
    print("hey")

def decorator_func(func):
    def wrapper_func():
        print(f"name of the function is: {func.__name__}")
        func()    
    return wrapper_func

decorated_print = decorator_func(print_func1)
decorated_print()

# şununla aynı: print_func2 = decorator_func2(print_func)
@decorator_func
def print_func2():
    print("hi")

print_func2()