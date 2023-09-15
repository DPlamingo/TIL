import requests
# Python 으로 AIP에 요청 보내기
API_KEY = 'ttbtjqmone1205001'
params = {
    'ttbkey': API_KEY,
    'Query' : 'Aladin',
    'QueryType': 'ItemNewAll',
    'MaxResults':10,
    'start':1,
    'SearchTarget':'Book',
    'output':'js',
    'Version':'20131101',

}
URL = "http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey=ttbtjqmone1205001&QueryType=ItemNewAll&MaxResults=10&start=1&SearchTarget=Book&output=js&Version=20131101"

# url/?key=value&key=value
# requests.get(URL, params)
response = requests.get(URL, params=params)
data = response.json()
print(data['item'])
for item in data['item']:
    print(item['isbn'])
    print(item['title'])
    print(item['pubDate'])