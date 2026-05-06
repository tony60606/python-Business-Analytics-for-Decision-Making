import numpy as np
#1.建立一維陣列
# arr1=np.array([1,3,5,7,9])
# #2.建立二維陣列,含int ,float ,str
# arr2=np.array([[1,2,3],
#                [1.1,1.2,1.3],
#                ['11','12','13']])
# #3.印出一維陣列內容,形狀,資料型態
# print(f'{arr1=}')
# print(f'{arr1.shape=}')
# print(f'{arr1.dtype=}')
# print("="*30)
# #4.印出二維陣列內容,形狀,資料型態
# print(f'{arr2=}')
# print(f'{arr2.shape=}')
# print(f'{arr2.dtype=}')

# #5.向量化運算,對每個元素同時操作,將陣列1*2+1
# print(arr1*2+1)
#廣播,不同形狀的陣列自動對齊
#6.宣告 price為ndarry,內容為100,200,300
# price = np.array([100,200,300])
# #7.宣告 discount=0.1 #純量會自動擴展為[0.1,0.1,0.1]
# discount = 0.1
# #8.宣告final為 price*(1-discount)
# final = price * (1-discount)
# #9.印出final內容
# print(f'{final=}')
#常用統計函式
data=np.array([120,350,280,95,410])
#10.印出平均值
print(f'平均值：{np.mean(data)}')
#11.印出中位數
print(f'中位數：{np.median(data)}')
#12.印出標準差
print(f'標準差：{np.std(data):.2f}')
#13.印出總和
print(f'總和：{np.sum(data)}')
#14.印出最大值
print(f'最大值：{np.max(data)}')
#15.印出最小值
print(f'最小值：{np.min(data)}')

#布林索引
#16.印出大於200元素
print(f'大於200的元素：{data[data>200]}')
#17.計算大於200的元素總和為
print(f'總和：{data[data>200].sum()}')

#18.計算大於200的元素數目為
print(f'有幾個：{(data>200).sum()}')
#19.將大於200的元素,值改為0
data[data>=200]=0
print(f'大於200的元素改0:{data}')
