# Solution source for Mono Shift

f = open('ciphertext.txt', 'r')
ciphertext = f.read()

for i in range(26):
    plain = ""
    for char in ciphertext:
        if char.isalpha():
            num = ord(char) + i
            if num > ord('z'):
                num -= 26
            plain += chr(num)
        else:
            plain += char
    print plain
