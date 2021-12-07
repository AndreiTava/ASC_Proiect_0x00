import sys
#scuffed code dar l-am facut repede intr-o dimineata
nume_fisier = sys.argv[1]
psswrdstr="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
validstr="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_+*=^&%$#@~`|[]{\}()/<> \"\'?!.,;:\n"
f = open(nume_fisier, "rb")
#g = open("crackOutputs.txt", "w") #for debugging

for i in range(10,16):
    key=[]
    for j in range(i):
        for achr in psswrdstr:
            f.close()
            f = open(nume_fisier, "rb")
            mybytes = f.read(i)
            cont=1
            while mybytes:
                if j < len(mybytes):
                    decoded = chr(mybytes[j] ^ ord(achr))
                    if decoded.isascii() and decoded not in validstr:
                        #g.write(f"size {i}, chr {achr}, itt:{cont}, {mybytes[j]} -> {decoded} \n")
                        break
                mybytes = f.read(i)
                cont += 1
            else:
                key.append(achr)
                break
    print(i,key)
f.close()
#g.close()

        
