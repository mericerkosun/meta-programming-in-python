# args -> Fonskiyonun n sayıda parametre almasını sağlar.

def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_of(1,3,6,2))

# Sınırsız sayıda parametreli fonksiyon oluşturmak için parametremizin önüne tek yıldız (*) koyarız.
# Burada, fonksiyon parametresinden önce tek yıldız(*) kullandığımız için sonucumuz tuple olarak döner.

def rakamlari_goster(*rakamlar):
    print(rakamlar)
 
rakamlari_goster(1,2,3,4)
rakamlari_goster(15,'burak')
#Sonuç
#(1, 2, 3, 4)
#(15, 'burak')


# kwargs -> Çift yıldızlı (**) parametrelerin tek yıldızlı (*) parametrelerden en önemli farkı, fonksiyonu çağırırken anahtar değer ilişkisiyle çağırabilmemizdir.

def fonksiyon1(**parametre):
    print(parametre)
 
fonksiyon1(deger1='Burak', deger2=20)
fonksiyon1(deger1='Burak', deger2=20, deger3=True, deger4=15.2)

# Burada, fonksiyon parametresinden önce çift yıldız(**) kullandığımız için sonucumuz sözlük (dictionary) olarak döner.