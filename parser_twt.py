from snscrape.modules import twitter as twt
from collections import defaultdict


class Find_info():
    def __init__(self, username):
        self.username = username


    def find_by_hash(self):
        sns = twt.TwitterSearchScraper(self.username)
        self.result = defaultdict(list)
        for i, item in enumerate(sns.get_items()):
            self.result['username'].append(item.username)
            self.result['content'].append(item.content)
            self.result['full'].append(item.media)
            if i == 10:
                break
        return self.result

    
