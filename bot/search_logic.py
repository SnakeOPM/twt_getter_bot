from snscrape.modules import twitter as twt
from collections import defaultdict
import re


class _fill_res():
    def __init__(self, search_result) -> None:
        self.search_result = search_result
        self.result = defaultdict(list)

    def fill_resulting(self):
        for i, item in enumerate(self.search_result.get_items()):  #sns.get_items()
            self.result['username'].append(item.username)
            self.result['content'].append(item.content)
            self.result['full'].append(item.media)
            if i == 10:
                break
        return self.result
                 


class Searcher():
    def searcher_decorator(func):
        def searcher_unit(self, *args, **kwargs):
            update_this = func(self.username)
            update_this = re.findall("'(.*?)'", update_this)
            update_this = "".join(update_this)
            sns = twt.TwitterHashtagScraper(update_this)
            self.result = _fill_res(sns).fill_resulting()
            return self.result
        return searcher_unit
    
    def searcher_decorator_for_users(func):
        def sercher_user(self, *args, **kwargs):
            update_this = func(self.username)
            update_this = re.findall("'(.*?)'", update_this)
            update_this = "".join(update_this)
            sns = twt.TwitterUserScraper(update_this)
            self.result = _fill_res(sns).fill_resulting()
            return self.result
        return sercher_user