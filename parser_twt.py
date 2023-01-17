from snscrape.modules import twitter as twt
from collections import defaultdict


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


class Find_info():
    def __init__(self, username):
        self.username = username
        self.result = defaultdict(list)

                
    @searcher_decorator
    def find_by_hash(*sns):
        return f'#{sns}'
    

    @searcher_decorator
    def find_user(*sns):
        return f'@{sns}'
    


# dind = Find_info('snaleart')
# sda = dind.find_by_hash()
# print(dind.result['username'][0])
