import maan
from maan import metin
topsay = 0
DEGISKEN = 0
sifre = []
sifreler =[]
def sifrealma(sifreler):
    ekleme = 1
    cikarma = 1
    sifre = input("şifrenizi her karakterden sonra 1 boşluk bırakarak  giriniz").split()
    uzunluk = len(sifre)
    if uzunluk < 6:
        print("şifrenizin ham hali de 6 karakterden uzun olmalıdır.")
        while ekleme !=0:
            sifre.append(ekleme)
            ekleme = 6-len(sifre)
    if uzunluk > 16:
        print("şifreniz 16 karakteri geçmemelidir")
        print("şifrenizden 16 karakterden sonrası eksiltilecektir")
        KereSil=uzunluk-25
        while cikarma != 0:
            sifre.pop(-1)
            cikarma = len(sifre)-16
    else:
        print("şifreniz kurallara uygundur")
    print("yeni şifreniz: {}".format(sifre))
    sifre[maan.o] = maan.kopya[maan.o]
    sifre.append(sifre)
    sifrebir=sifre.copy()
    sifrebir[maan.w] = maan.kopya[maan.w]
    sifre.append(sifrebir)
    sifreiki=sifre.copy()
    sifreiki[maan.x] = maan.kopya[maan.x]
    sifreler.append(sifreiki)
    return sifreler
sifrealma(sifreler)
print(sifreler)
def sezar(sifreler):
    alfabe=['a','b' ,'c' , 'd', 'e', 'f', 'g' ,'h' ,'i' ,'j','k' ,'l' ,'m' ,'n' ,'o' ,'p' ,'r' ,'s' ,'t' ,'u' ,'v', 'y' ,'z','A','B' ,'C' , 'D', 'E', 'F', 'G' ,'H','I','İ' ,'J','K' ,'L' ,'M' ,'N' ,'O' ,'P' ,'R' ,'S' ,'T' ,'U' ,'V', 'Y','Ü','Ö','Ç','Ğ','!','Z','ı','ö','ç','ş','ü',';',',','.','>','<','}','=',']',')','(','[','{','/','&','%','$','+','#','^','!','*','?','0','9','8','7','6','5','4','3','2','1']
    for i in sifreler:
        sifreler += alfabe[(alfabe.index(i)+3)%len(alfabe)]
    print("sifre :",sifreler)
    return sifreler
print(sifreler)
f = open("sifresonuclar.txt","a")
print(sifreler)
f.close()
