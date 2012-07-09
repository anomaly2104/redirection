import webapp2
import random
import config

class DitributeTrafficAPI(webapp2.RequestHandler):
    def get(self):
		seq = [x for x in config.URLS for y in range(config.URLS[x])]
		selected_url = random.choice(seq)
		self.redirect(selected_url)
