
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ,. '
key = alpha


while True:
    print('''1) Enter an encoding "key" string.
2) Encode a section of text using the current key.
3) Decode a section of text using the current key.
4) Exit the program.''')
    x = input('Choice? ')


    if x == '1':
        key = list(dict.fromkeys(input('key? ').upper()))
        key1 = ''
        string = list(alpha)
        for i in key:
            if i in string:
                key1 += i
                string.remove(i)
        key1 += ''.join(string)
        key = key1
        print(f'key: {key}')
    elif x == '2':
        toEncode = input('Enter Message (250 characters max) with # to finish. ')
        while len(toEncode) > 250:
            toEncode = input('Try again: ')
        message = ''
        for c in toEncode.upper():
            if c == '#':
                break
            if c in alpha:
                message += c





        p = 0
        out = ''
        for c in message:
            p = (p + alpha.index(c)+1)% 29
            out += key[p]
        line = ''
        for c in out:
            line += c
            if len(line) == 50:
                print(line + '\\')
                line = ''
        print(line + '#')
    elif x == '3':
        toDecode = input('Enter Message with # to finish. ')
        message = ''
        for c in toDecode.upper():
            if c == '#':
                break
            if c in key:
                message += c



        p = 0
        out = ''
        for c in message:
            q = key.index(c)
            out += alpha[(q-p- 1) % 29]
            p = q
        line = ''
        for c in out:
            line += c
            if len(line) == 50:
                print(line + '\\')
                line = ''
        print(line + '#')
    elif x == '4':
        print('exiting...')
        break
