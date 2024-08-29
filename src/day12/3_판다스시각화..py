# p.124
from idlelib.iomenu import encoding

import matplotlib.pyplot as plt
import pandas as pd

day= [2015,2016,2017,2018,2019,2020]
data = [[500,450,520,610],
        [690,700,820,900],
        [1100,1030,1200,1380],
        [1500,1650,1700,1850],
        [1990,2020,2300,2420],
        [1020,1600,2200,2550]]


dt_tbl = pd.DataFrame(data, index=day ,columns=['1분기','2분기','3분기','4분기'])
dt_tbl.to_csv("dbtbl.csv", encoding='utf-8', mode='w', index=True)

# print(dt_tbl)

x = range(0, len(data[1]))

for i in data :
    plt.plot(x,i)

plt.title('2015~2020 Quarterly sales')
plt.xlabel('Quarterly')
plt.ylabel('sales')

xLabel = ['first','second','third','fourth']
plt.xticks(x, xLabel, fontsize=10)

yLabel = ['500','1000','1500','2000','2500']


plt.legend(['2015','2016','2017','2018','2019','2020'])
# plt.show()