import matplotlib.pyplot as plt
import pandas as pd
## 利用 pyplot 繪製圖表

## 設定中文字型為 微軟正黑
plt.rcParams['font.sans-serif']=['Microsoft JhengHei','sans-serif']
## fig 是整張圖 ax 是繪圖區 figsize=(寬,高)
fig,ax=plt.subplots(figsize=(8,5))
#利用 bar 方法設定 x標籤與y值
ax.bar(['card','atm','code','wallet'],[10200,5100,2100,3100])
#設定圖表標題為 '各付款方式訂單數' 字型大小為 14
ax.set_title('各付款方式訂單數',fontsize=14)
#設定 x 軸標籤為 付款方式
ax.set_xlabel('付款方式')
#設定 y 軸標籤為 訂單數
ax.set_ylabel('訂單數')

#為資料加上資料標籤


#自動調整邊距,避免標籤被截掉

#儲存圖表名稱為payment.png


#顯示圖表
plt.show()
