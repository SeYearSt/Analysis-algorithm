def get_shift(substr):
    shift = {}
    for i in range(0,len(substr)-1):
        shift[substr[i]] = len(substr)-i-1
    if substr[len(substr)-1] not in shift:
        shift[substr[len(substr)-1]] = len(substr)
    return shift
 
def horspul(str, substr):
    shift = get_shift(substr)
    i = len(substr) -1
    while i < len(str):
        for j in range(0, len(substr)):
            if str[i-j] != substr[len(substr)-1-j]:
                if str[i-j] in shift:
                    i = i+shift[str[i-j]]
                    break
                else:
                    i+= len(substr)
                    break
 
            if j >= len(substr) - 1:
                return (i - len(substr) +1)
 
    return -1
 
print(get_shift('ad'))
print(horspul('adad', 'ad'))