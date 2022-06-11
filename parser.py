sentence = input("Masukkan Kata: ")
tokens = sentence.lower().split()
tokens.append('EOS')


#symbols definition
non_terminal = ['S','V','O']
terminals = ['au','ibana','haha','injam','marmeam','mengaut','manjait','marinda','bal','abit','tas']

#parse table definition
parse_table= {}

parse_table[('S','au')] = ['O','V','O']
parse_table[('S','ibana')] = ['O','V','O']
parse_table[('S','haha')] = ['O','V','O']
parse_table[('S','injam')] = ['O','V','O']
parse_table[('S','marmeam')] = ['O','V','O']
parse_table[('S','mangaut')] = ['O','V','O']
parse_table[('S','manjait')] = ['O','V','O']
parse_table[('S','marinda')] = ['O','V','O']
parse_table[('S','bal')] = ['O','V','O']
parse_table[('S','abit')] = ['O','V','O']
parse_table[('S','tas')] = ['O','V','O']
parse_table[('S','EOS')] = ['error']

parse_table[('V','au')] = ['error']
parse_table[('V','ibana')] = ['error']
parse_table[('V','haha')] = ['error']
parse_table[('V','injam')] = ['injam']
parse_table[('V','marmeam')] = ['marmeam']
parse_table[('V','mangaut')] = ['mangaut']
parse_table[('V','manjait')] = ['manjait']
parse_table[('V','marinda')] = ['marinda']
parse_table[('V','bal')] = ['error']
parse_table[('V','abit')] = ['error']
parse_table[('V','tas')] = ['error']
parse_table[('V','EOS')] = ['error']

parse_table[('O','au')] = ['au']
parse_table[('O','ibana')] = ['ibana']
parse_table[('O','haha')] = ['haha']
parse_table[('O','injam')] = ['error']
parse_table[('O','marmeam')] = ['error']
parse_table[('O','mangaut')] = ['error']
parse_table[('O','manjait')] = ['error']
parse_table[('O','marinda')] = ['error']
parse_table[('O','bal')] = ['bal']
parse_table[('O','abit')] = ['abit']
parse_table[('O','tas')] = ['tas']
parse_table[('O','EOS')] = ['accept']

#stack initialization
stack = []
stack.append('#')
stack.append('S')

#input reading initialization
idx_token = 0
symbol = tokens[idx_token]

#parsing process
while (len(stack) > 0):
    top = stack[len(stack)-1]
    print('top = ', top)
    print('symbol = ', symbol)
    if top in terminals:
        print('top adalah simbol terminal')
        if top == symbol:
            stack.pop()
            idx_token = idx_token + 1
            symbol = tokens[idx_token]
            if symbol == 'EOS' :
                print('isi stack: ', stack)
                stack.pop()
        else:
            print('error')
            break;
    elif top in non_terminal:
        print('top adalah simbol non terminal')
        if parse_table[(top,symbol)][0] != 'error':
            stack.pop()
            symbols_to_be_pushed = parse_table[(top, symbol)]
            for i in range(len(symbols_to_be_pushed)-1,-1,-1):
                stack.append(symbols_to_be_pushed[i])
        else:
            print('error')
            break;
    else:
        print('error')
        break;
    print('isi stack: ',stack)
    print()

#conclusion
print()
if symbol == 'EOS' and len(stack) == 0:
    print('input string ', sentence, ' diterima sesuai Grammar')
else:
    print('Error, input string: ', sentence, 'tidak diterima. tidak sesuai Grammar')
