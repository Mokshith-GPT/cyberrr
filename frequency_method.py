
def count_char_frequency(input_string):
    frequency = {}
    
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

input_string = "helloworld"
char_frequency = count_char_frequency(input_string)

print("Character Frequency:")
for char, freq in char_frequency.items():
    print(f"{char}: {freq}")