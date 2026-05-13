import pandas as pd
from common import factor
facts=factor()
#針對payment_type欄位分群,不產生索引欄,統計下列資訊
# (訂單數=order_id,計數),(不重覆顧客數=customer_id,累計不重覆),(總營收=line_revenue,加總)
by_payment_users=facts.groupby('payment_type',as_index=False).agg(訂單數=('order_id','count'),不重複顧客數=('customer_id','nunique'),總營收=('line_revenue','sum'))
##輸出為temp2.csv
by_payment_users.sort_values('總營收',ascending=False)
by_payment_users.to_csv('temp2.csv',)