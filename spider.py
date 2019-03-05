import re
from pyquery import PyQuery as pq
import requests
import time
url = "http://explorer.hx.cash/hx-browser/getStatis"
cmt_url = 'https://coinmarketcap.com/currencies/aelf/'
api = 'http://api.zb.cn/data/v1/allTicker'
binance_api = 'https://api.binance.com/api/v3/ticker/price?symbol=ELFBTC'
headers = {
            'User-Agent':'Mozilla/5.0(Macintosh;Intel Mac OS X 10_13_3)AppleWebKit/537.36(KHTM,like Gecko) Chrome/65.0.3325.162 Safari/537.36'
        }
parms = {'Accept':'application'}

#获取hx区块浏览器信息
response = requests.post(url, headers=headers,json=parms)
a = response.json()
cross_asset = a.get('data').get('crossAsset')
reward = a.get('data').get('reward')

#zb交易所api，获取币价信息
price = requests.get(api,headers = headers).json()

#~ #binance api
#~ binance = requests.get(binance_api,headers = headers).json()
#~ elfbtc = float(binance['price'])

#获取cmt价格
elf_text = requests.get(cmt_url,headers = headers).text
doc = pq(elf_text)
elfusd = float(doc('.h2.text-semi-bold.details-panel-item--price__value').text())

usdt_price = price.get('usdtqc').get('last')
btc_price = price.get('btcqc').get('last')
elf_price = str(elfusd * float(usdt_price))
pax_price = price.get('paxqc').get('last')
eth_price = price.get('ethqc').get('last')
hc_price = price.get('hcqc').get('last')
ltc_price = price.get('ltcqc').get('last')

#获取本地时间
localtime = time.asctime(time.localtime(time.time()))



num_list = []#各币种质押数量
price_list = [btc_price,elf_price,pax_price,eth_price,hc_price,ltc_price，usdt_price]#各币种现价列表
b = cross_asset.split()
for i in b:
	if b.index(i) % 2 == 0:
		num_list.append(i)
		
asset_list = [float(a)*float(b) for a,b in zip(num_list,price_list)]	#各币种市值列表

total_value = sum(asset_list)


#~ with open(r'C:\Users\Pahai\Desktop\price_list.txt','a',encoding = 'utf-8') as f:
	#~ f.write(str(price_list))
	#~ f.write('\n')
	#~ f.close()
#~ with open(r'C:\Users\Pahai\Desktop\asset_list.txt','a',encoding = 'utf-8') as f:
	#~ f.write(str(asset_list))
	#~ f.write('\n')
	#~ f.close()
#~ with open(r'C:\Users\Pahai\Desktop\total_value.txt','a',encoding = 'utf-8') as f:
	#~ f.write(str(total_value))
	#~ f.write('\n')
	#~ f.close()
#~ with open(r'C:\Users\Pahai\Desktop\time.txt','a',encoding = 'utf-8') as f:
	#~ f.write(localtime)
	#~ f.write('\n')
	#~ f.close()
	

	
print('质押情况：')
print(cross_asset)
print('当前币价：')
print(price_list)
print('市值：')
print(asset_list)
print('hx链上资产：'+str(total_value/100000000) + '亿元')
