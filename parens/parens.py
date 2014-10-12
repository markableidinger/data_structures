def is_closed(str):
    '''Checks to see if all of the parentheses are in ordered sets'''
    count = 0
    for c in str:
        if c == '(':
            count += 1
        if c == ')':
            count -= 1
        if count < 0:
            return -1
    if count == 0:
        return 0
    else:
        return 1
