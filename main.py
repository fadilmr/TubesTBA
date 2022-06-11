from lexical_analyzer import lexical
from parser_program import parser   

sentence = input('masukkan sentence: ')

if lexical(sentence):
    parser(sentence)
else:
    print('format sentence tidak diterima')