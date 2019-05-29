# 単語の一部分を組み合わせてコラするやつ

## 使い方

```
usage: Usage: python word_collage_maker.py WORD_LIST_FILE TEXT [WORD_COUNT]

positional arguments:
  WORD_LIST_FILE        UTF-8、1行につき1単語
  TEXT                  コラしたい文字列

optional arguments:
  -h, --help            show this help message and exit
  -WORD_COUNT WORD_COUNT
```

## 使用例

```
>python word_collage_maker.py ghibli_list.txt 天空山田返し
単語リストを読み込み...
辞書データを生成...
探索……
【天空】：
　天空の城ラピュタ
【山田】：
　ホーホケキョ となりの山田くん
【返し】：
　猫の恩返し

>python word_collage_maker.py ghibli_list.txt 耳をすませば山田くんの紅がきこえる
単語リストを読み込み...
辞書データを生成...
探索……
【耳をすませば】：
　耳をすませば
【山田くん】：
　ホーホケキョ となりの山田くん
【の】：
　風の谷のナウシカ
【紅】：
　紅の豚
【がきこえる】：
　海がきこえる
```

## 注意点

- 当ツールは[MIT License](https://www.catch.jp/oss-license/2018/11/14/use_mit_license/)です
- WORD_LIST_FILEを変えれば任意の単語リストから生成できます
