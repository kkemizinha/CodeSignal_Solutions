import re
def amendTheSentence(s):
    aux = re.findall('[A-Za-z][a-z]*', s)
    
    for i in range(len(aux)):
        if aux[i][0].isupper():
            aux[i] = aux[i].lower()
    
    return ' '.join(aux)