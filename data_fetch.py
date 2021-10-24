import requests

API_KEY = 'ed25392973ee4646a4426a126139f7eb'

def get_top_headlines(category=None):
	url = 'https://newsapi.org/v2/top-headlines'
	if category:
		p = {
			'country': 'in',
			'apiKey' : API_KEY,
			'category': category
		}
	else:
		p = {
			'country': 'in',
			'apiKey' : API_KEY
		}

	responce = requests.get(url, params=p)
	data = responce.json()
	articles = data["articles"]
	return articles

def get_everything(search_keyword = None):
	if not search_keyword:
		return get_top_headlines()

	url = 'https://newsapi.org/v2/everything'
	p = {
		'apiKey' : API_KEY,
		'q': search_keyword
	}

	responce = requests.get(url, params=p)
	data = responce.json()
	articles = data["articles"]
	return articles