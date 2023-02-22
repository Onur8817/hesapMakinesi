#print("Hello")
# toplama fonksiyonu
def topla(x,y):
    return (x+y)

# cikarma islemi
def cikarma(x,y):
    return x-y

# carpma fonksiyonu
def carp(x,y):
    return x*y

def bolm(x,y):
    return x/y
number =int(input("1.sayıyı girin"))
number2 =int(input("2.sayıyı girin"))
print("toplama için 1'i çıkarma için 2'yi çarpma için 3'ü bölme için 4'ü girin")
secim=int(input())
if secim==1:
    print(topla(number, number2))
elif  secim==2:
    print(cikarma(number, number2))
elif secim == 3:
    print(carp(number, number2))
elif secim == 4:
    print(bolm(number, number2))
