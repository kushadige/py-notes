# *args -> unpack args'ın unpack edilmiş hali.
# örn: args = (1,2,3,4) - *args = 1, 2, 3, 4 

def sum(*args) -> int:
    res = 0
    for e in args:
        res += e
    return res

print(sum(1,2,3,4,5))

pack = (5,6,7,8)
print(pack, *pack)

# kwargs: keyword arguements
def students(**kwargs):
    print(*kwargs)
    print(kwargs)
    for e in kwargs.values():
        print(e)

students(name="oguzhan", std_number="401")

str_list = set([*"hey this is a string"])
print(str_list)