class WordFilter:
    def __init__(self,filter1):
        self.search = filter1

    def detect(self, sentence):
        if self.search in sentence:
            return True
        else:
            return False
        return result


my_filter = WordFilter("アーセナル")
print(my_filter.detect('昨日のアーセナルの試合は熱かった'))
print(my_filter.detect('昨日のリバプールの試合は熱かった'))