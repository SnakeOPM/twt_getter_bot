from collections import defaultdict
from search_logic import Searcher as find_dec


class Find_info():
    def __init__(self, username):
        self.username = username
        self.result = defaultdict(list)
                
    @find_dec.searcher_decorator
    def find_by_hash(*sns):
        return f'#{sns}'
    

    @find_dec.searcher_decorator
    def find_user(*sns):
        return f'@{sns}'
    


dind = Find_info('NyanNyanners')
sda = dind.find_user()
print(dind.result['username'][0],  dind.result['content'][0], dind.result['username'][1], dind.result['content'][1])

