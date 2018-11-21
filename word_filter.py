class WordFilter:
    def __init__(self,filter1):
        self.search = filter1

    def detect(self, sentence, censored):
        for i in range(0, len(self.search)):
            if self.search[i] in sentence:
                sentence = sentence.replace(self.search[i], censored)
        return sentence


print("NGワードを設定してください")
print("NGワードを入力し終わったら、半角でeを入力してください")
censored = input('伏せ字を設定してください：')
fil = []


def ng_word_list(filter_list):  # NGワードの設定
    counter = 1
    while True:
        global fil
        ng_word = input('NGワード：' + str(counter) + ':')
        if ng_word == 'e':
            break
        filter_list.append(ng_word)
        counter += 1
        fil = filter_list
    return filter_list


#repeat == yである限り、フィルタリングを繰り返せる。
repeat = "y"
while repeat.lower() == 'y':
    my_filter = WordFilter(ng_word_list(fil))
    # fil = ng_word_list(fil)
    while True:
        print(my_filter.detect('昨日のアーセナルの試合は熱かった', censored))
        print(my_filter.detect('昨日のリバプールの試合は熱かった', censored))
        repeat = input('フィルタリングをし直しますか?(y/n)')
        if repeat.lower() == 'n':
            break
        else:
            while True:
                for i in range(0, len(fil)):
                    print(i + 1, fil[i], '', end="")
                change_NG_Number = int(input('どのNGワードを変更しますか?'))
                if change_NG_Number < 1 or change_NG_Number > len(fil):
                    print("正しい数値を入力してください")
                    continue

                change_NG_Word = input('新しいNGワード')
                fil[change_NG_Number - 1] = change_NG_Word
                break
            continue
