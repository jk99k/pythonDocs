from typing import List


words: List(str) = ["cat", "window", "defenestrate"]
for w in words:
    print(w, len(w))

# for構文。

# len()はPythonの組み込み関数で、文字列、タプル、リスト、また辞書などのアイテム数を
# 返す関数。文字列の場合は文字数が返される。