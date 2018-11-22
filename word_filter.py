class WordFilter:
    def __init__(self, ng_list):
        self.ng_list = ng_list

    def detect(self, sentence, censored):
        for i in range(len(self.ng_list)):
            if self.ng_list[i] in sentence:
                sentence = sentence.replace(self.ng_list[i], censored)
        return sentence


print("NGワードを設定してください")
print("NGワードを入力し終わったら、半角でeを入力してください")
censored = input('伏せ字を設定してください：')
fil = []

while True:
    ng_word = input("NGワード" + str(len(fil) + 1) + ':')
    if ng_word == 'e':
        break
    fil.append(ng_word)

# repeat == yである限り、フィルタリングを繰り返せる。
repeat = "y"
while repeat.lower() == 'y':
    my_filter = WordFilter(fil)
    while True:
        print(my_filter.detect('昨日のアーセナルの試合は熱かった', censored))
        print(my_filter.detect('昨日のリバプールの試合は熱かった', censored))
        repeat = input('フィルタリングをし直しますか?(y/n)')
        if repeat.lower() == 'n':
            break
        else:
            while True:
                # NGワードリストの更新
                print('NGワードリスト', end='')
                for i in range(len(fil)):
                    print(i + 1, fil[i], '', end="")
                change_NG_Number = input('\nどのNGワードを変更しますか?'
                                         '\n＋を入力すると、新しいNGワードを追加できます。')
                if change_NG_Number == '+':
                    fil.append(input('追加するワード'))
                    print('NGワードリストに', fil[-1], 'を追加しました。')
                    break
                if not int(change_NG_Number) >= 1 and int(change_NG_Number) <= len(fil):
                    print("正しい数値を入力してください")
                    continue

                change_NG_Word = input('新しいNGワードを設定してください。'
                                       '\n何も入力せずにエンターを押すと、そのワードがリストから削除されます。'
                                       '\n新しいNGワード:')
                if len(change_NG_Word) == 0:
                    print(fil[int(change_NG_Number) - 1], 'はリストから削除されました')
                    del fil[int(change_NG_Number) - 1]
                    break

                fil[int(change_NG_Number) - 1] = change_NG_Word
                break
            continue
