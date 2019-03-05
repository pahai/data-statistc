import json
import numpy as np
#~ #获取时间数据组
with open(r'C:\Users\Administrator\Desktop\time.txt','r') as f:
	time_list = []
	for i in f.readlines():
		i = i.strip('\n')
		time_list.append(str(i))
	f.close()

#获取链上资产总量	
with open(r'C:\Users\Administrator\Desktop\total_value.txt','r') as f:
	total_value = []
	for i in f.readlines():
		i = i.strip('\n')
		total_value.append(float(i))
	f.close()
	
#获取各币种总市值
with open(r'C:\Users\Administrator\Desktop\asset_list.txt','r') as f:
	asset_list = []
	for i in f.readlines():
		i = eval(i.strip('\n'))
		asset_list.append(i)
	f.close()

#获取各币种价格
with open(r'C:\Users\Administrator\Desktop\price_list.txt','r') as f:
	price = []
	price_list=[]
	for i in f.readlines():
		i = i.strip('\n')
		price_list.append(eval(i))
	for i in price_list:
		a = list(map(float,i))
		price.append(a)
	f.close()
	
#获取各币种数量
with open(r'C:\Users\Administrator\Desktop\num_list.txt','r') as f:
	num =[]
	num_list=[]
	for i in f.readlines():
		i = i.strip('\n')
		num.append(eval(i))
	for i in num:
		b = list(map(float,i))
		num_list.append(b)
	f.close() 

#计算近期币数量变化幅度
now = np.array(num_list[-1])
last_oneday = np.array(num_list[-24])
last_oneweek = np.array(num_list[-168])	
day_change = list(100*(now - last_oneday)/last_oneday)
week_change = list(100*(now - last_oneweek)/last_oneweek)
btc_price=[]
hc_price=[]
for i in price:
	btc_price.append(i[0])
	hc_price.append(i[4]*2000)	
	
#整理各币种市值列表	
btc = []
elf = []
pax = []
eth = []
hc = []
ltc = []
usdt = []

for i in asset_list:
	btc.append(i[0])
	elf.append(i[1])
	pax.append(i[2])
	eth.append(i[3])
	hc.append(i[4])
	ltc.append(i[5])
	if len(i)>6:
		usdt.append(i[6])
	else:
		usdt.append(0)	

#
data = {
	"coins":["BTC","ELF","PAX","ETH","HC","LTC","USDT"],
	"day_change":day_change,
	"week_change":week_change,
	"btc_price":btc_price,
	"hc_price":hc_price,
	"time":time_list,
	"total_value":total_value,
	"asset_list":asset_list[-1],
	"btc":btc,
	"elf":elf,
	"pax":pax,
	"eth":eth,
	"hc":hc,
	"ltc":ltc,
	"usdt":usdt
}	

with open(r'C:\inetpub\wwwroot\data.json','w',encoding="utf-8") as j:
	json.dump(data,j)
