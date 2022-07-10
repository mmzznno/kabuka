from pandas_datareader.stooq import StooqDailyReader
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

#株価取得範囲を設定
start = datetime(2021, 4, 1)
end = datetime(2022, 6, 1)
#銘柄を入力(日経・エイピアG)
stock = ['^NKX','4180.JP']
#株価取得
df = StooqDailyReader(stock, start=start, end=end)
df_stock = df.read()['Close']
#相関係数
df_stock.corr()
#print((df_stock.corr()['^NKX']))
df_c = (df_stock.corr()['^NKX'])
print(df_c)
#棒グラフppy
df_c.plot(kind="bar", figsize=(12,5))

plt.title('Graph',fontsize=18)
#plt.axes().set_axisbelow(True)
#調査予定　棒が消える

plt.grid(True)
plt.savefig("corr_graph1.png")
plt.show()
#ヒートマップ
sns_plot = sns.heatmap(df_stock.corr())
figure = sns_plot.get_figure()
figure.savefig("corr_graph2.png")