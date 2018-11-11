f_input = input('Введите название текстового файла: ')
while True:
    try:
        f_in = open(f_input, 'r')
    except FileNotFoundError:
        print('Такого файла нет :с')
        f_input = input('Введите название текстового файла: ')
    else:
        f_in = open(f_input, 'r')
        break

letter = input('Введите букву: ')

with open ('input.txt') as f_in:
    with open('output.txt','w') as f_out:
        lines = f_in.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                if letter in word:
                    print(word, file=f_out,end=' ')
if len(f_out) == 0:
    print('Таких букв в файле нет:с',file=f_out)