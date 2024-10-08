def password(number):
    n_ = ''
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                n_ += str(i) + str(j)
    return n_

print('Введите число: ')
print(password(int(input())))