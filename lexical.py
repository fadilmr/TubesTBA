import string

sentence = input('masukkan sentence: ')
inputString = sentence.lower()+'#'

alphabetList = list(string.ascii_lowercase)
stateList = ['q0', 'q1', 'q2',  'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',
            'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20',
            'q21', 'q22', 'q23', 'q24', 'q25', 'q26']
        
transitionTable = {}

for state in stateList:
    for alphabet in alphabetList:
        transitionTable[(state, alphabet)] = 'error'
    transitionTable[(state, '#')] = 'error'
    transitionTable[(state, ' ')] = 'error'

transitionTable['q0', ' '] = 'q0'

# au
transitionTable['q0', 'a'] = 'q1'
transitionTable['q1', 'u'] = 'q2'

# abit
transitionTable['q1', 'b'] = 'q3'
transitionTable['q3', 'i'] = 'q4'
transitionTable['q4', 't'] = 'q2'

# manjait
transitionTable['q0', 'm'] = 'q5'
transitionTable['q5', 'a'] = 'q6'
transitionTable['q6', 'n'] = 'q7'
transitionTable['q7', 'j'] = 'q8'
transitionTable['q8', 'a'] = 'q3'

# mangaut
transitionTable['q7', 'g'] = 'q9'
transitionTable['q9', 'a'] = 'q10'
transitionTable['q10', 'u'] = 'q4'

# marmeam
transitionTable['q6', 'r'] = 'q11'
transitionTable['q11', 'm'] = 'q12'
transitionTable['q12', 'e'] = 'q13'
transitionTable['q13', 'a'] = 'q14'
transitionTable['q14', 'm'] = 'q2'

# marnida
transitionTable['q11', 'n'] = 'q15'
transitionTable['q15', 'i'] = 'q16'
transitionTable['q16', 'd'] = 'q17'
transitionTable['q17', 'a'] = 'q2'

# ibana
transitionTable['q0', 'i'] = 'q18'
transitionTable['q18', 'b'] = 'q19'
transitionTable['q19', 'a'] = 'q20'
transitionTable['q20', 'n'] = 'q17'

# injam
transitionTable['q18', 'n'] = 'q21'
transitionTable['q21', 'j'] = 'q13'

# tas
transitionTable['q0', 't'] = 'q22'
transitionTable['q22', 'a'] = 'q23'
transitionTable['q23', 's'] = 'q2'

# taho
transitionTable['q23', 'h'] = 'q24'
transitionTable['q24', 'o'] = 'q2'

# bal 
transitionTable['q0', 'b'] = 'q25'
transitionTable['q25', 'a'] = 'q26'
transitionTable['q26', 'l'] = 'q2'

# accept
transitionTable['q2', ' '] = 'q0'
transitionTable['q0', '#'] = 'accept'
transitionTable['q0', ' '] = 'q0'
transitionTable['q2', '#'] = 'accept'


idxChar = 0
currenToken = ''
state = 'q0'
while state != 'accept':
    currenChar = inputString[idxChar]
    currenToken += currenChar
    state = transitionTable[(state, currenChar)]
    if state == 'q2':
        print('Current token:', currenToken, ', valid')
        currenToken = ' '
    if state == 'error':
        print('Current token:', currenToken, ', Error')
        break
    idxChar += 1

if state == 'accept':
    print('Semua token di input: ', sentence, ', valid')

