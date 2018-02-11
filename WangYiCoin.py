import requests
import json

cookies = {
    'NTES_YD_SESS': 'Your cookie info'
    '_gat': 'Your cookie info',
    'STAREIG': 'Your cookie info',
}

headers = {
    'Host': 'star.8.163.com',
    'Origin': 'https://star.8.163.com',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202star_client_1.0.0',
    'Referer': 'https://star.8.163.com/m',
    'Accept-Language': 'zh-cn',
    'X-Requested-With': 'XMLHttpRequest',
}

# 请求领取coin接口
def collectCoins(coinId):
	headers = {
	    'Host': 'star.8.163.com',
	    'Accept': 'application/json, text/plain, */*',
	    'X-Requested-With': 'XMLHttpRequest',
	    'Accept-Language': 'zh-cn',
	    'Cache-Control': 'max-age=0',
	    'Content-Type': 'application/json;charset=UTF-8',
	    'Origin': 'https://star.8.163.com',
	    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202star_client_1.0.0',
	    'Referer': 'https://star.8.163.com/m',
	}

	data = '{"id":%s}' %coinId
	response = requests.post('https://star.8.163.com/api/starUserCoin/collectUserCoin', headers=headers, cookies=cookies, data=data)
	print(response.text)
	print(data)


# 1、请求首页数据，检查是否有coin可以收集。有则将coin保存到列表容器
response = requests.post('https://star.8.163.com/api/home/index', headers=headers, cookies=cookies)
jsonData = json.loads(response.text)
collectCoinsList = jsonData['data']['collectCoins']
print(collectCoinsList)
if len(collectCoinsList) == 0:
	print('当前没有黑钻可以领取...')
else:
	# 2、检查coin列表容器是否有值，遍历请求领取coin接口
	for collectCoinsItem in collectCoinsList:
		print(collectCoinsItem)
		collectCoins(collectCoinsItem['id'])
