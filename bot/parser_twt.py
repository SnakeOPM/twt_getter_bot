from collections import defaultdict
from search_logic import Searcher as find_dec


class Find_info():
    def __init__(self, username):
        self.username = username
        self.result = defaultdict(list)
                
    @find_dec.searcher_decorator
    def find_by_hash(*sns):
        return f'{sns}'
    

    @find_dec.searcher_decorator_for_users
    def find_user(*sns):
        return f'{sns}'
    
