# Расчет количества книг на дискете

volume = 1.44
pages = 100
lines = 50
chars = 25
BYTES_ONE_CHARS = 4

book_chars = pages * lines * chars
book_volume = book_chars * BYTES_ONE_CHARS

disk_size = volume * 1024 * 1024
num_books = disk_size // book_volume


# volume=x
# puges=a
# lines=b
# chars=c
# BYTES_ONE_CHARS=d
# x =a * b * c * d

print("Количество книг на дискете:", num_books)

#Расчет периметра и площади геометрических фигур

#space = pi * radius^2
pi = 3.1415
#C = 2 * pi * radius
#perimeter = 4 * side
#space = side^2

radius = 5
side = 5

S.c = pi * radius^2
C = 2 * pi * radius

print("Площадь круга:", S.c )
print("Длина окружности:", C )

P.s = 4 * side
S.s = side^2

print("Периметр квадрата:", P.s )
print("Площадь квадрата:", S.s )

