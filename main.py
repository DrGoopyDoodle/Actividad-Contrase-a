import random
e =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
l = int(input("Longitud de la contreseña"))
p = ""
for i in range(l):
    p += random.choice (e)
print (p)
