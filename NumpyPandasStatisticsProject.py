import numpy as np
import pandas as pd

#4x4’lük 2 adet matrisin toplamının ve farkının
# 4x4’lük bir matris ile gösterilmesi

dizi1=np.random.randint(20,size=(4,4))
print(dizi1)
dizi2=np.random.randint(20,size=(4,4))
print(dizi2)

dizi_top=dizi1+dizi2
print(dizi_top)

dizi_fark=dizi2-dizi1
print(dizi_fark)

#Yeni matrisin istatistiki değerlerini
#ekrana yazdıran program

df = pd.DataFrame(dizi_top)
description = df.describe()
print(description)

'''[[12  5 15 12]
 [ 0 13  4  6]
 [ 3  6 18  2]
 [17 19  2 10]]
[[ 1 16  7  8]
 [10  8  2 15]
 [ 9 16 17 18]
 [12  7 17 19]]
[[13 21 22 20]
 [10 21  6 21]
 [12 22 35 20]
 [29 26 19 29]]
[[-11  11  -8  -4]
 [ 10  -5  -2   9]
 [  6  10  -1  16]
 [ -5 -12  15   9]]
              0          1          2          3
count   4.00000   4.000000   4.000000   4.000000
mean   16.00000  22.500000  20.500000  22.500000
std     8.75595   2.380476  11.902381   4.358899
min    10.00000  21.000000   6.000000  20.000000
25%    11.50000  21.000000  15.750000  20.000000
50%    12.50000  21.500000  20.500000  20.500000
75%    17.00000  23.000000  25.250000  23.000000
max    29.00000  26.000000  35.000000  29.000000'''