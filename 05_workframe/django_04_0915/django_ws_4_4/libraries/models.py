from django.db import models
import requests

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    title = models.TextField()
    # yyyy-mm-dd
    pub_date = models.DateField()

    @classmethod
    def insert_data(cls):
        API_KEY = 'ttbtjqmone1205001'
        params = {
    'ttbkey': API_KEY,
    # 'Query' : 'Aladin',
    'QueryType': 'ItemNewAll',
    'MaxResults':10,
    'start':1,
    'SearchTarget':'Book',
    'output':'js',
    'Version':'20131101',

}
        URL = "http://www.aladin.co.kr/ttb/api/ItemList.aspx"

# url/?key=value&key=value
# requests.get(URL, params)
        response = requests.get(URL, params=params)
        data = response.json()
        # print(data['item'])
        for item in data['item']:
            # isbn = item['isbn']
            # print(item['isbn'])
            # print(item['title'])
            # print(item['pubDate'])
            params = {
                'isbn' : item['isbn'],
                'title' : item['title'],
                'pubDate' : item['pubDate'],
                        }
            book = cls(**params)
            book.save()