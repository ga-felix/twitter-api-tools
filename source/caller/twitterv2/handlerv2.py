from time import sleep


class Case:
    
    def __init__(self, code: int):
        self.code = code
        
    def is_case(self, code: int):
        if self.code == code:
            self.do()
        
    def do(self):
        pass
        
def LimitReachedCase(Case):
    
    def do(self):
        
    

class TwitterLimitHandler:
    
    def __init__(self, cases: list):
        self.cases = cases
    
    def handle(self, exception: Exception):
        