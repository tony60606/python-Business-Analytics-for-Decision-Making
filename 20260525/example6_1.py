from common import factor
import pandas as pd
facts=factor()
##利用groupby
facts['order_week'] = facts['order_date'].dt.to_period('W')
df=facts.groupby('order_week',as_index=False).agg(
    revenue = ('line_revenue','sum'),
    orders = ('order_id','count')
    ).assign(aov=lambda x : (x['revenue']/x['orders'])).round(2)
df.to_csv('temp1.csv')
print('='*50)
##利用pivot_table
df2 = facts.pivot_table(
    values = 'line_revenue',
    index = 'order_week' ,
    aggfunc = ['sum','count','mean'],
).round(2)
df2.columns=['revenue','orders','aov']
df2.to_csv('temp2.csv')