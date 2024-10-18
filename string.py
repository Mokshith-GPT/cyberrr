
def string_both_ends(string):
    if len(string) < 2:
        return ''
    
    return string[0:2] + string[-10:]

print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))