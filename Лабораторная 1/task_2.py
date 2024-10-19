# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44 * 1024 * 1024
numberofcharacters = 100 * 50 * 25 * 4
numberofbooks = volume / numberofcharacters

print("Количество книг, помещающихся на дискету:", int(numberofbooks))
