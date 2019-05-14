import requests


class News:

    def __init__(self, sources, config=None):
        self.sources = sources
        self.config = config

    def set_sources(self, sources):
        self.sources = sources

    def get_top_url(self):
        base_link = "https://newsapi.org/v2/"
        source_request = "sources=" + ",".join(self.sources[0:len(self.sources)]) + "&"
        top_link = "%stop-headlines?%sapiKey=%s" % (base_link, source_request, self.config["NEWS"]["API_KEY"])

        return top_link

    def get_response(self, url):
        return requests.get(url)

    def get_articles(self, response):
        json_t = response.json()
        articles = []
        for article in json_t["articles"]:
            art_item = (article["source"]["name"], article["title"], article["description"])
            articles.append(art_item)

        return articles