'''Aritmetik ortalama- 1 basılınca veya ‘a’ ● Geometrik ortalama- 2 basılınca veya ‘b’ ● Frekans bulma- 3 basılınca veya ‘c’ ● Küçükten büyüğe dizme- 4 basılınca veya ‘d’
● Tek sayıların sayısı- 5 basılınca veya ‘e’ ● Çift sayıların ortalamaları- 6 basılınca veya ‘f’ ● Büyükten küçüğe sıralama- 7 basılınca veya ‘g’ ● En büyük ve en küçük değerleri bulma- 8 basılınca veya ‘h’ ● 10’a bölünenlerin sayısını bulma- 9 basılınca veya ‘i’	'''

import numpy
dizi=numpy.random.randint(100,200,50)
print(dizi)
secenek=input("seçenek seçiniz:")
if((secenek==1) or (secenek=='1') or (secenek=='a')):
  print(numpy.mean(dizi))

elif((secenek==2) or (secenek=='2') or (secenek=='b')):
   x = numpy.array([1, 2, 3, 4, 5])
   geo_ortalama = numpy.prod(x) ** (1 / len(x))

elif ((secenek==3) or (secenek=='3') or (secenek=='c')):
  print("dizide en sık görülen değer:")
  print(numpy.bincount(dizi).argmax())
  print(dizi.flatten())

elif((secenek==4) or (secenek=='4') or (secenek=='d')):
   print("dizi",numpy.sort(dizi))

elif ((secenek==5) or (secenek=='5') or (secenek=='e')):
  tek_sayilar = 0
  for sayi in dizi:
    #for sayi in dizi:Bu döngü, listenin her bir elemanını (sayi),
    #listenin başından sonuna kadar dönmek için kullanılır.
    if sayi % 2 == 1:
        tek_sayilar += 1
  print("Listedeki tek sayıların sayısı:", tek_sayilar)

elif ((secenek==6) or (secenek=='6') or (secenek=='f')):
  toplam_cift_sayilar=0
  cift_sayilar=[]
  #Çift sayıların ortalamaları
  for sayi in dizi:
    if sayi % 2 == 0:
      cift_sayilar.append(sayi)
      toplam_cift_sayilar +=sayi
  cift_sayi_adedi = len(cift_sayilar)
  ortalama_cift_sayilar = toplam_cift_sayilar / cift_sayi_adedi
  print("Çift sayıların ortalaması:", ortalama_cift_sayilar)

elif ((secenek==7) or (secenek=='7') or (secenek=='g')):
 #●	Büyükten küçüğe sıralama
 print(numpy.sort(dizi))
 print("dizi",dizi.reverse())

elif ((secenek==8) or (secenek=='8') or (secenek=='h')):
 minimum=print(min(dizi))
 maximum=print(max(dizi))

elif ((secenek==9) or (secenek=='9') or (secenek=='i')):
   topbol_say=0
   bolunebilen_sayilar=[]
   for i in dizi:
    if(i%2==0 and i%5==0):
      bolunebilen_sayilar.append(i)
      topbol_say += i
   bol_say_aded=print(len(bolunebilen_sayilar))

else:
 print("Geçersiz seçenek.")

