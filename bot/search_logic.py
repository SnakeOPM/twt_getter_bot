from snscrape.modules import twitter as twt

class Searcher():
    def searcher_decorator(func):
        def searcher_unit(self, *args, **kwargs):
            update_this = func(self.username)
            sns = twt.TwitterSearchScraper(update_this)
            for i, item in enumerate(sns.get_items()):
                self.result['username'].append(item.username)
                self.result['content'].append(item.content)
                self.result['full'].append(item.media)
                if i == 10:
                    break
            return self.result
        return searcher_unit