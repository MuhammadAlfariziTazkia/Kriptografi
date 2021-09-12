alphabet = [
    'A', 
    'B', 
    'C', 
    'D', 
    'E', 
    'F', 
    'G', 
    'H', 
    'I', 
    'J', 
    'K', 
    'L', 
    'M', 
    'N', 
    'O', 
    'P', 
    'Q', 
    'R', 
    'S', 
    'T', 
    'U', 
    'V',
    'W',
    'X',
    'Y',
    'Z',
]

text = ""
with open('cipher_text.txt', 'r') as file:
    for sentence in file:
        text += sentence

kata_pembangkit = input("Masukan Kata Pembangkit: ")

cipher_text = text

kata_pembangkit = kata_pembangkit.upper().replace(" ", "")

kunci = ""

for index in range(len(cipher_text)):
    kunci += kata_pembangkit[index%len(kata_pembangkit)]

plain = []

for i in range(len(cipher_text)):
    cipher_index = alphabet.index(cipher_text[i])
    kunci_index = alphabet.index(kunci[i])
    
    result_index = (cipher_index - kunci_index)%26
    
    plain.append(alphabet[result_index])
    
    # print("Plain Char = {}, index = {}".format(clean_plain_text[i], plain_text_index))
    # print("Kunci Char = {}, index = {}".format(kunci[i], kunci_index))
    # print("Formula = ({} + {})mod 26 = {} ".format(plain_text_index, kunci_index, result_index))
    # print("Cipher Char = {}".format(alphabet[result_index]))
    # print()

plain_text = ""
for char in plain:
    plain_text += char

print()
print()
print("Text :")
print(text)
print("Cipher Text : ")
print(cipher_text)
print()
print("Key : ")
print(kunci)
print()
print("Plain Text : ")
print(plain_text)

with open('decripted_cipher_text.txt', 'w') as file:
    file.write(plain_text)

print("Success Generate Cipher Text File!")