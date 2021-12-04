import sys

def xor_bytes(chunk,key):
    result = bytearray()
    for i in range(len(chunk)):
        result.append(chunk[i]^key[i])
    return result

crypted_folder = sys.argv[1]
text_folder = sys.argv[2]

f = open(crypted_folder,'rb')
g = open(text_folder, 'rb')

crypted_bit = f.read(45)
og_text = g.read(45)

print(xor_bytes(crypted_bit,og_text))
g.close()
f.close()