# An elementary base 64 decoder. 

dictionary = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12,
'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S': 18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25, 
'a':26, 'b':27, 'c':28, 'd':29, 'e':30, 'f':31, 'g':32, 'h':33, 'i':34, 'j':35, 'k':36, 'l':37, 'm':38, 'n':39,
'o':40, 'p':41, 'q':42, 'r':43, 's':44, 't':45, 'u':46, 'v':47, 'w':48, 'x':49, 'y':50, 'z':51, '0':52, '1': 53,
'2':54, '3':55, '4':56, '5':57, '6':58, '7':59, '8':60, '9':61, '+':62, '/':63, '=':0}

def decode(string):
    decoded = []
    if len(string) % 4 != 0:
        raise ValueError('length of string not a multiple of 4')
    for i in xrange(0, len(string) / 4):
        temp = str(string[i*4:i*4+4])
        binary = bin((dictionary[temp[0]] << 18) + (dictionary[temp[1]] << 12) + (dictionary[temp[2]] << 6) + dictionary[temp[3]])
        decoded.append(binToString(binary))
    return ''.join(map(str, decoded))

def binToString(binary):
    size = len(binary) - 2
    if size < 9:
        result = 0, 0, int(binary[-size:], 2)
    elif size < 17:
        result = 0, int(binary[-size:-8], 2), int(binary[-8:], 2)
    else:
        result = (int(binary[2:-16], 2), int(binary[-16:-8], 2),
                  int(binary[-8:], 2))

    return ''.join(map(chr, result))
