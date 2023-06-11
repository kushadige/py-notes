# generator'ler fonksiyonlar gibi tanımlanır. ancak "return" yazmak yerine "yield" keyword'ü kullanılıyor.

def square(l):
    res = []
    for e in l:
        res.append(e*e)
    return res

l = [1, 2, 3]
print(square(l))

# tüm cevapları bir anda hesaplayıp döndürmesin de
# biz sordukça bir sonraki adımı hesaplasın istiyorsak
# generatorler'i kullanırız.

# generator'ler bütün cevabı hafızada tutmazlar. biz sordukça
# değerleri döndürürler.

# generator'ler iterator'dır. "next" ile sonraki değerlerine
# erişebiliriz.

def square_generator(l):
    for e in l:
        yield e*e

g = square_generator(l)
print(next(g))
print(next(g))
print(next(g))
# print(next(g))

# exhaust oldu. bir daha baştan başlamak istiyorsak
# bir daha yaratmamız lazım.
print("1. iterator")
for res in g:
    print(res)

g = square_generator(l)

print("2. iterator")
for res in g:
    print(res)


## tek satırda generator oluşturmak.
# list comprehension:
l = [x*x for x in [1,2,3,4,5]]
print(l)

# tek satıda generator:
g = (x*x for x in [1,2,3,4,5])
next(g)
for e in g:
    print(e)


# range() benzeri fonksiyon oluşturma
print("###############")
def range_generator(start, end, step):
    current = start

    while current < end:
        yield current
        current += step

r = range_generator(1, 20, 3)

for i in r:
    print(i)