sayı= int(input("Sayı giriniz"))   #kullanıcıdan değer alınır
sayi1= sayı//2 #sayi1 değerine sayı değerini ikiye böldüğümüzdeki bölümü atıyoruz
elde = sayı%2 #elde değerine sayı değerini 2 ye bölüp kalan değerini atıyoruz.
ikilik=""
ikilik= ikilik + str(elde)
while(sayi1!= 0):
    ilerleme = sayi1        #Girdiğimiz Ondalık Değerdeki Sayıyı İkilik Değere dönüştürecek döngüyü While Komutu ile Yazıyoruz
    sayi1 = ilerleme// 2
    elde = ilerleme % 2
    ikilik = ikilik + str(elde)
print(ikilik[::-1])         #Bilgisayara Çıkardığımız Değeri Alttan Başlatarak Yazdırıyoruz
