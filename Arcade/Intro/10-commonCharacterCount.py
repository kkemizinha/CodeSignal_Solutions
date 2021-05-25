def commonCharacterCount(s1, s2):
    ans = 0
    dicts1 = {}
    for element in s1:
       if element in dicts1:
          dicts1[element] += 1
       else:
           dicts1[element] = 1
    
    for element in s2:
        if (element in dicts1) and (dicts1[element] > 0):
            dicts1[element] -= 1
            ans +=1
    return ans