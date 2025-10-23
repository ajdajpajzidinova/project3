print('hello world')


def check_word(name):
    if name == name[::-1]:
        print('Палиндром')
    else:
        print('Палиндром эмес')

check_word('ata')
check_word('car')
check_word('python')
check_word('madam')