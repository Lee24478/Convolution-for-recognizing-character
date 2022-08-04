### 我李健立自己思考解決、絕無抄襲 ###
from PIL import Image
import numpy as np

img = Image.open('虎.jpg').convert('L')

A = np.array(img)
m,n = A.shape
a = np.min(A)
b = np.max(A)
s = 3   #
F = np.ones((s,s))
a = int((s-1)/2)
for i in range(s):
    for j in range(s):
        if np.sqrt((a - i)**2 + (a - j)**2) != 0:
            F[i,j] /= np.sqrt((a - i)**2 + (a - j)**2)
F[a,a] = 0
F[a,a] = -np.sum(F)
B = np.zeros((m-s+1,n-s+1))
for i in range(m-s+1):
    for j in range(n-s+1):
        B[i,j] = np.sum(A[i:i+s,j:j+s]*F)
c = np.min(B)
d = np.max(B)
B += a-c
B *= (b-a)/(d-c)
im = Image.fromarray(B)#
im.show()#
#im.convert('L').save('1st-da.jpg')

num , bkt = np.histogram(B)
bnd = bkt[np.argmax(num)+1]
C = B.copy()
for i in range(m-s+1):
    for j in range(n-s+1):
        if C[i,j] > bnd : C[i,j] = 255
        else: C[i,j] = 0
        
bnw = Image.fromarray(C)
bnw.show()#
#bnw.convert('L').save('b&w-Zhai.jpg')

### 縮小圖 ###
m,n = C.shape
p = 3   #池化層   #p越小，圖越大
B2 = np.zeros( (int((m-p)/p+1),int((n-p)/p+1)) , dtype = float)
for i in range(int((m-p)/p+1)):
    for j in range(int((n-p)/p+1)):
        B2[i,j] = np.sum(C[p*i:p*(i+1),p*j:p*(j+1)])/(p*p)

a = 10   #分幾桶
num , bkt = np.histogram(B2,a)
for i in range(B2.shape[0]):
    for j in range(B2.shape[1]):
        if B2[i,j] > bkt[1] : B2[i,j] = 255
        else: B2[i,j] = 0
        
bnw2 = Image.fromarray(B2)
bnw2.show()#

word = list("$ ") 
 
# 將灰度值轉為字元 
def get_char(gray_number):
    if gray_number  == 0:   #0
        return word[1]   #背景
    else : return word[0]   #形狀$
    
txt = "" 
for i in range(B2.shape[0]):
    for j in range(B2.shape[1]):
        txt += get_char(B2[i,j]) 
    txt += '\n' 
print('縮小後 :' , txt) 

f = open('虎-字元檔.txt','w') 
f.write(txt)
f.close()


