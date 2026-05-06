import numpy as np
import pandas as pd
fruits=['蘋果','橘子','梨子','櫻桃']
quantities=[15,33,45,55]
#1.將quantities轉為ndarray 指定給 n1 變數
n1 = np.array(quantities)
#2.利用 pd.Series() 將 quantities 轉為 Series 指定給 s1
s1 = pd.Series(quantities)
# print(type(s1))
#3.利用 pd.Series() 將 quantities 轉為 Series 並設定 index=fruits 指定給 s2
s2 = pd.Series(quantities,index=fruits)
#4.印出 n1 
print(f'{n1=}')
print('='*10)
#5.印出 s1 
print('s1=',s1,sep='\n')
print('='*30)
#6.印出 s1 的 index
print(s1.index)
print('='*30)
#7.印出 s1 的 values
print(s1.values)
print('='*30)
#8.印出 s2 
print('s2=',s2,sep='\n')
print('='*30)
#9.印出 s2 的 index
print(s2.index)
print('='*30)
#10.印出 s2 的 values
print(s2.values)

print('='*30)
#11.印出 s2 的 第二筆資料的值
print(f's2 的第二筆資料取值：{s2["橘子"]}')
print('='*30)
