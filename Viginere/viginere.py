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

plain_text = ""
with open('plain_text.txt', 'r') as file:
    for sentence in file:
        plain_text += sentence

kata_pembangkit = input("Masukan Kata Pembangkit: ")

plain_text = plain_text.upper().replace(" ", "").replace("\n", "")

clean_plain_text = ""

for char in plain_text:
    if char in alphabet:
        clean_plain_text += char

kata_pembangkit = kata_pembangkit.upper().replace(" ", "")

kunci = ""

for index in range(len(clean_plain_text)):
    kunci += kata_pembangkit[index%len(kata_pembangkit)]

cipher = []

for i in range(len(clean_plain_text)):
    plain_text_index = alphabet.index(clean_plain_text[i])
    kunci_index = alphabet.index(kunci[i])
    
    result_index = (plain_text_index + kunci_index)%26
    
    cipher.append(alphabet[result_index])
    
    print("Plain Char = {}, index = {}".format(clean_plain_text[i], plain_text_index))
    print("Kunci Char = {}, index = {}".format(kunci[i], kunci_index))
    print("Formula = ({} + {})mod 26 = {} ".format(plain_text_index, kunci_index, result_index))
    print("Cipher Char = {}".format(alphabet[result_index]))
    print()

cipher_text = ""
for char in cipher:
    cipher_text += char
    
print("Result = {}".format(cipher_text))

with open('cipher_text.txt', 'w') as file:
    file.write(cipher_text)

print("Success Generate Cipher Text File!")