
def parser(sentence):
    tokens = sentence.lower().split()
    tokens.append('EOS')


    #symbols definition
    non_terminal = ['S', 'SU', 'V', 'O', 'P']
    terminals = ['au','ibana','haha','injam','marmeam','mengaut','manjait','marinda','bal','abit','tas', 'taho']

    #parse table definition
    parse_table= {}

    parse_table[('S','au')] = ['SU', 'V', 'O']
    parse_table[('S','ibana')] = ['SU', 'V', 'O']
    parse_table[('S','haha')] = ['SU', 'V', 'O']
    parse_table[('S','injam')] = ['error']
    parse_table[('S','marmeam')] = ['error']
    parse_table[('S','mangaut')] = ['error']
    parse_table[('S','manjait')] = ['error']
    parse_table[('S','marinda')] = ['error']
    parse_table[('S','bal')] = ['error']
    parse_table[('S','abit')] = ['error']
    parse_table[('S','taho')] = ['error']
    parse_table[('S','tas')] = ['error']
    parse_table[('S','EOS')] = ['error']

    parse_table[('SU','au')] = ['au']
    parse_table[('SU','ibana')] = ['ibana']
    parse_table[('SU','haha')] = ['haha']
    parse_table[('SU','injam')] = ['error']
    parse_table[('SU','marmeam')] = ['error']
    parse_table[('SU','mangaut')] = ['error']
    parse_table[('SU','manjait')] = ['error']
    parse_table[('SU','marinda')] = ['error']
    parse_table[('SU','bal')] = ['error']
    parse_table[('SU','abit')] = ['error']
    parse_table[('SU','taho')] = ['error']
    parse_table[('SU','tas')] = ['error']
    parse_table[('SU','EOS')] = ['error']

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
    parse_table[('V','taho')] = ['P', 'V']
    parse_table[('V','tas')] = ['error']
    parse_table[('V','EOS')] = ['error']

    parse_table[('P','au')] = ['error']
    parse_table[('P','ibana')] = ['error']
    parse_table[('P','haha')] = ['error']
    parse_table[('P','injam')] = ['error']
    parse_table[('P','marmeam')] = ['error']
    parse_table[('P','mangaut')] = ['error']
    parse_table[('P','manjait')] = ['error']
    parse_table[('P','marinda')] = ['error']
    parse_table[('P','bal')] = ['error']
    parse_table[('P','abit')] = ['error']
    parse_table[('P','taho')] = ['taho']
    parse_table[('P','tas')] = ['error']
    parse_table[('P','EOS')] = ['accept']

    parse_table[('O','au')] = ['error']
    parse_table[('O','ibana')] = ['error']
    parse_table[('O','haha')] = ['error']
    parse_table[('O','injam')] = ['error']
    parse_table[('O','marmeam')] = ['error']
    parse_table[('O','mangaut')] = ['error']
    parse_table[('O','manjait')] = ['error']
    parse_table[('O','marinda')] = ['error']
    parse_table[('O','bal')] = ['bal']
    parse_table[('O','abit')] = ['abit']
    parse_table[('O','taho')] = ['error']
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
