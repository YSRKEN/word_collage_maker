from argparse import ArgumentParser
from typing import Tuple, List, Dict, Set


def parse_arg() -> Tuple[str, str, int]:
    """コマンドライン引数をパースする

    Returns
    -------
        単語リストのファイル名、入力文字列
    """
    usage = f'Usage: python {__file__} WORD_LIST_FILE TEXT [WORD_COUNT]'
    arg_parser = ArgumentParser(usage=usage)
    arg_parser.add_argument('WORD_LIST_FILE', type=str, help='UTF-8、1行につき1単語')
    arg_parser.add_argument('TEXT', type=str, help='コラしたい文字列')
    arg_parser.add_argument('-WORD_COUNT', type=int, default=5, help='候補を表示する最大個数')
    args = arg_parser.parse_args()
    return args.WORD_LIST_FILE, args.TEXT, args.WORD_COUNT


def create_word_dic(word_list: List[str]) -> Dict[int, Dict[str, Set[int]]]:
    """単語リストから、検索しやすい辞書を作成する

    Parameters
    ----------
    word_list: List[str]
        単語リスト

    Returns
    -------
        word_dic[部分文字列の長さ][部分文字列]={対象となる文字列のインデックス}
    """

    word_dic: Dict[int, Dict[str, Set[int]]] = {}
    for index, word in enumerate(word_list):
        # index……対象となる文字列のword_listに対するインデックス
        # word……対象となる文字列
        # p……文字列を切り取る際の始点
        # q……文字列を切り取る際の終点
        word_len = len(word)
        p_range = range(0, word_len)
        for p in p_range:
            q_range = range(p + 1, word_len + 1)
            for q in q_range:
                # 文字列を切り取る
                slice_word = word[p:q]
                slice_len = q - p

                # 切り取った文字列が登録済みでないかを確認する
                if slice_len not in word_dic:
                    word_dic[slice_len] = {}
                if slice_word not in word_dic[slice_len]:
                    word_dic[slice_len][slice_word] = set()

                # 登録
                word_dic[slice_len][slice_word].add(index)
    return word_dic


def search_word(text: str, word_list: List[str], word_dic: Dict[int, Dict[str, Set[int]]], word_count: int):
    """文字コラ用の候補を検索する

    Parameters
    ----------
    text: str
        対象の文字列
    word_list: List[str]
        単語リスト
    word_dic: Dict[int, Dict[str, Set[int]]]
        word_dic[部分文字列の長さ][部分文字列]={対象となる文字列のインデックス}
    word_count: int
        候補を表示する最大数
    """

    # p……文字列を切り取る際の始点
    # q……文字列を切り取る際の終点
    text_len = len(text)
    p = 0
    while p < text_len:
        q_range = range(text_len, p, -1)
        flg = False
        for q in q_range:
            # 文字列を切り取る
            slice_text = text[p:q]
            slice_len = q - p

            # 切り取った文字列がヒットするかを判定する
            if slice_len not in word_dic:
                continue
            if slice_text not in word_dic[slice_len]:
                continue

            # ヒットしたので単語一覧を表示する
            print(f'【{slice_text}】：')
            for index in list(word_dic[slice_len][slice_text])[0:word_count]:
                print(f'　{word_list[index]}')
            p += slice_len
            flg = True
            break
        if not flg:
            print('エラー：適合する単語が見つかりません')
            break


def main():
    word_list_file, text, word_count = parse_arg()

    print('単語リストを読み込み...')
    word_list = []
    for line in open(word_list_file, 'r', encoding='UTF-8'):
        word_list.append(line.rstrip('\r\n'))

    print('辞書データを生成...')
    word_dic = create_word_dic(word_list)

    print('探索……')
    search_word(text, word_list, word_dic, word_count)


if __name__ == '__main__':
    main()
