def int_func(words):
    if words.islower():
        return words.title()
    else:
        return ('You do not need use upper method')

print(int_func('i wanna be a python-programmer'))
