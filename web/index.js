document.getElementById("button").onclick = function() {
    var sentence = document.getElementById("sentence").value;
    var tokens = input.split(" ");
    tokens.push("EOS");

    // symbols definition

    non_terminal = ['S', 'SU', 'V', 'O']
    terminal =['au','ibana','haha','injam','marmeam','mengaut','manjait','marnida','bal','abit','tas']

    // parse table definition

    parse_table = {}

    parse_table['S'] = {
        'au': ['SU', 'V', 'O'],
        'ibana': ['SU', 'V', 'O'],
        'haha': ['SU', 'V', 'O'],
        'injam': ['SU', 'V', 'O'],
        'marmeam': ['SU', 'V', 'O'],
        'mengaut': ['SU', 'V', 'O'],
        'manjait': ['SU', 'V', 'O'],
        'marnida': ['SU', 'V', 'O'],
        'bal': ['SU', 'V', 'O'],
        'abit': ['SU', 'V', 'O'],
        'tas': ['SU', 'V', 'O'],
        'EOS': ['error']
    }

    parse_table['SU'] = {
        'au': ['au'],
        'ibana': ['ibana'],
        'haha': ['haha'],
        'marmeam': ['marmeam'],
        'mengaut': ['mengaut'],
        'manjait': ['manjait'],
        'marnida': ['marnida'],
        'bal': ['error'],
        'abit': ['error'],
        'tas': ['error'],
        'EOS': ['error']
    }

    parse_table['V'] = {
        'au': ['error'],
        'ibana': ['error'],
        'haha': ['error'],
        'injam': ['injam'],
        'marmeam': ['marmeam'],
        'mengaut': ['mengaut'],
        'manjait': ['manjait'],
        'marnida': ['marnida'],
        'bal': ['error'],
        'abit': ['error'],
        'tas': ['error'],
        'EOS': ['error']
    }

    parse_table['O'] = {
        'au': ['error'],
        'ibana': ['error'],
        'haha': ['error'],
        'injam': ['error'],
        'marmeam': ['error'],
        'mengaut': ['error'],
        'manjait': ['error'],
        'marnida': ['error'],
        'bal': ['bal'],
        'abit': ['abit'],
        'tas': ['tas'],
        'EOS': ['accept']
    }

    // stack initialization
    var stack = []
    stack.push('#')
    stack.push('S')

    var idx_token = 0
    var symbol = tokens[idx_token]

    while (stack.length > 0) {
        var top = stack[stack.length - 1]
        console.log('top = ', top)
        console.log('symbol = ', symbol)
        if (terminal.includes(top)) {
            console.log('top adalah simbol terminal')
            console.log('top = ', top)
            if (top == symbol) {
                stack.pop()
                idx_token += 1
                symbol = tokens[idx_token]
                if (symbol == 'EOS') {
                    console.log('stack = ', stack)
                    stack.pop()
                }
            } else {
                console.log('error')
                break
            }
        } else if (non_terminal.includes(top)) {
            console.log('top adalah simbol non terminal')
            if (parse_table[top][symbol] &&  parse_table[top][symbol][0] != 'error') {
                stack.pop()
                var symbols_to_be_pushed = parse_table[top][symbol]
                for (var i = symbols_to_be_pushed.length - 1; i >= 0; i--) {
                    stack.push(symbols_to_be_pushed[i])
                }
            } else {
                console.log('error')
                break
            }
        } else {
            console.log('error')
            break
        }
        console.log('stack = ', stack)
        console.log('\n')
    }
    
    // conclusion:
    console.log('\n')
    if (symbol == 'EOS' && stack.length == 0) {
        console.log('input string', input, 'diterima sesuai grammar')
    } else {
        console.log('input string', input, 'tidak diterima sesuai grammar')
    }
}
