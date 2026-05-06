import pandas as pd
import time
df=pd.read_csv("data/raw/order_items.csv")

#1.利用for loop計算--begin
#啟動計時器
start_time = time.perf_counter()
revenues = []
for i in range(len(df)) :
    rev = df.iloc[i]['quantity']*df.iloc[i]['unit_price']*(1-df.iloc[i]['discount_rate'])
    revenues.append(rev)
print(f"總金額:{sum(revenues):.2f}")
#關閉計時器
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"迴圈方式共花費時間:{elapsed_time:.4f}秒")
#1.利用for loop計算--end
print("*"*20)
#2.利用dataframe向量化處理方式--begin
start_time1 = time.perf_counter()
df['record_total'] = df['quantity']*df['unit_price']*(1-df['discount_rate'])
print(f'總金額：{df["record_total"].sum():.2f}')
end_time1 = time.perf_counter()
elapsed_time1 = end_time1 - start_time1
print(f"迴圈方式共花費時間:{elapsed_time1:.4f}秒")
#2.利用dataframe向量化處理方式--end