import numpy as np
sinif_vize_not=np.random.randint(1,101,30)
print(sinif_vize_not)
max_vize_not=sinif_vize_not.max()
print(max_vize_not)
top_artt_deger=100-max_vize_not
tam=max_vize_not+(top_artt_deger)
print(tam)
yeni_vize_not=[]
for i in sinif_vize_not:
 yeni_vize_not1=top_artt_deger+i
 yeni_vize_not.append(yeni_vize_not1)
print(yeni_vize_not)

#Numpy, Random, Array, max(), Append, Len kullanılmıştır.
#Numpy kütüphanesi kullanılarak random 30 sayılık bir dizi oluşturulmuştur
#Bu kod, sınıftaki tüm vize notlarını, en yüksek notu 100 yapacak şekilde artırır.
# Bu işlemi yaparken, tüm notlara aynı miktarda (en yüksek notun 100 olması için gereken fark kadar) ekleme yapılır.
# Böylece notlar göreceli olarak aynı kalırken, en yüksek not 100 olur ve diğer notlar da bu artışa paralel olarak artar.

#--------------------
import numpy as np
import math
kk_dizi=[]
for i in range(1,11):
  kk_ici=i*i
  karekok_islem=math.sqrt(kk_ici)
  kk_dizi.append(karekok_islem)
toplam_kk = np.sum(kk_dizi)
print(toplam_kk)

#Math - Numpy kütüphanesi, sqrt(), append(), sum()
#Bu kod, 1'den 10'a kadar olan sayıların kareköklerinin toplamını hesaplar.

#--------------------
import numpy as np
import math
s=[]
for i in range(1,11):
 islem=math.pow(i,i)/math.factorial(i)
 s.append(islem)
toplam_islem=np.sum(s)
print(toplam_islem)

#Bu kod 1'den 10'a kadar olan sayıların i üssü i değerlerinin, i faktöriyele bölünmesi işlemlerinin toplamını hesaplar.

#--------------------
import numpy as np
import math
kk_dizi=[]
for i in range(1,11):
  kk_ici=i*(i+1)
  karekok_islem=math.sqrt(kk_ici)
  kk_dizi.append(karekok_islem)
toplam_kk = np.sum(kk_dizi)
print(toplam_kk)

#Bu kod, 1'den 10'a kadar olan sayıların, her sayının kendisiyle bir fazlasının çarpımının kareköklerinin toplamını hesaplar.

#--------------------
import numpy as np
import math
s=[]
for i in range(1,11):
  islem=i/math.sqrt(i)
  s.append(islem)
toplam_islem=np.sum(s)
print(toplam_islem)

#Bu kod, 1'den 10'a kadar olan her sayının kendisinin kareköküne bölünmesi işlemlerinin toplamını hesaplar.