import pandas as pd
from common import factor
import numpy as np
facts=factor()
customers=pd.read_csv('data/raw/customers.csv')
facts=facts.merge(customers,on='customer_id',how='left')
## 管道*客群的平均客價交叉表
cross=facts.pivot_table(
     values = 'line_revenue' ,
     index = 'acquisition_channel' ,
     columns = 'segment',
     aggfunc = 'mean',
     margins = True

).round(0)
print(cross)