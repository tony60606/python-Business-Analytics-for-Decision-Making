#讀入相關資料表 --begin
import pandas as pd
orders=pd.read_csv("data/raw/orders.csv")
order_items=pd.read_csv("data/raw/order_items.csv")
sessions=pd.read_csv("data/raw/sessions.csv")
events=pd.read_csv("data/raw/events.csv")
print(type(orders))
#讀入相關資料表 --end

#計算revenue --begin
#合併資料表
df_merged = pd.merge(order_items,orders,on="order_id",how="left")
#只查看已完成訂單
df_completed = df_merged[df_merged["status"]=="completed"].copy()
#將dataframe轉CSV
df_completed.to_csv("temp1.csv")
#新增一個recode_revenue欄位,用來計算每筆紀錄金額
df_completed['recode_revenue']=df_completed['quantity']*df_completed["unit_price"]*(1-df_completed['discount_rate'])
df_completed.to_csv('temp2.csv')
total_revenue=df_completed['recode_revenue'].sum()
print(total_revenue)
#計算revenue --end