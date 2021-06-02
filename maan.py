from typing import TextIO
kuralicinkural = ["a","b","c","d","e","f","g","h","j","k","l","o","p","u","A","B","C","D","E","F","G"]
listeharf = []
listesayi = []
Listesayikopya = []
print("şifreleme yapabilmemiz için önce 20 adet harf, sonrasında 20 adet sayı tanımlamanız gerekiyor. Ek olarak bir adet istediğiniz metni yazın.")
for a in range (20):
    b = input()
    listeharf.append(b)
print("\nşimdi rakam giriniz")
for D in range (20):
    c= int(input())
    listesayi.append(c)
print("\nşimdi 30 karakterden fazla bir metin giriniz")
metin = input()
metinleni = len(metin)
MaksGecenEleman = max(set(metin), key = metin.count)
metindekiikiharf = metin[1]
y = 20
h = 0
u = 0
p = 20
z = 0
kopya = []
kopyabir = []
kopyaiki = []
kopyauc = []
kopyadort = []
kopyabes = []
kopyaalti = []
kopyayedi = []
kopyaiki = kuralicinkural.copy()
kopya = kuralicinkural.copy()
while y > h:
    kopya[h]= metin[h]+listeharf[h]
    kopyabir = kopya[h]
    h = h+1
for z in range(0,19,2):
    kopyaiki[z]= metin[z]+listeharf[z]
    kopyauc = kopyaiki[z]
for u in range(0,19,3):
    kopyaiki[u]= metin[u]+listeharf[u]
    kopyauc = kopyaiki[u]
Listesayikopya = listesayi.copy()
o = listesayi[0]+0
w = listesayi[1]+0
x = listesayi[2]+0
file = open("sifresonuclar.txt", "a", encoding="utf-8")
    file.write(int(listesayi))
    file.write(str(listeharf))
    file.write(str(metin))
    file.close()

