string = "mississippi"
char_freq = {}
for ch in string:
    char_freq[ch] = char_freq.get(ch, 0) + 1
print(char_freq)