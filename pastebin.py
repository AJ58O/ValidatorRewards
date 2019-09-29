import requests

class Pastebin:
	def __init__(self, token):
		self.token = token
		self.base_url = "https://pastebin.com/api/api_post.php"

	def paste(self, message):
		url = self.base_url
		payload = {
			"api_dev_key":self.token,
			"api_option":"paste",
			"api_paste_code":message
		}
		r = requests.post(url=url, data=payload)
		return r.content