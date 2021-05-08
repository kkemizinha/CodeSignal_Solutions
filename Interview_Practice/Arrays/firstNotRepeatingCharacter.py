from collections import defaultdict
def firstNotRepeatingCharacter(s):
    character_dict = defaultdict(int)
    for i in range(len(s)):
        character_dict[s[i]] += 1
    
    answer = '_'
    for idx,value in enumerate(character_dict):
        if character_dict[value] == 1:
            return value

    return answer