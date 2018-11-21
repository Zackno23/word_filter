class WordFilter:
    def __init__(self,filter1):
        self.search = filter1

    def detect(self, sentence, censored):
        if self.search in sentence:
            sentence = sentence.replace('アーセナル', censored)
        return sentence

my_filter = WordFilter("アーセナル")
print(my_filter.detect('昨日のアーセナルの試合は熱かった', 'ピー'))
print(my_filter.detect('昨日のリバプールの試合は熱かった', 'ピー'))
