# 大雑把なPythonの紹介というページ
# 簡単な変数の扱いについて触れている

#　変数の宣言
spam = 1 

# クオーテーションで囲むとコメントアウトはされない
text = "#This is not a comment."

# 変数アノテーションによって変数の型を宣言する
answer: int
answer = 2 + 2

# While構文の実行(フィボナッチ数列の出力)
#　フィボナッチ数列の漸化式 F(n+2) = F(n+1) + F(n)
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b
# => 0 1 1 2 3 5 8

# while構文の定型文
# while <変数> "<" or "<=" 定数:
#    処理()

# 3 ** 3 は「　3の３乗　」を意味する。
num: int
num = 3 ** 3 # => 27
# -3の３乗とはならない。マイナスより累乗の方が先に計算されるため
# -(3の３乗)、つまり-27となる。
num = -3 ** 3 # => -27
