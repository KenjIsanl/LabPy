# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44 * 1024 * 1024
number_of_characters = 100 * 50 * 25 * 4
number_of_books = volume / number_of_characters

print("Количество книг, помещающихся на дискету:", int(number_of_books))
