# bin()は整数を引数に取り、"0b"を先頭にした
# 二進数文字列に変換する。
bin(2) # => "0b10"
bin(-10) # => "-0b1010"



# breakpoint() が実行されるとデバッガに移行する。
# 引数を sys.breakpointhook() に渡す。
# 環境変数 PYTHONBREAKPOINT の値が 0 だとデバッガは起動しない。

# bool　クラスはPythonの標準の真偽値のための組み込みデータ型
bl = True
bl = False
type(bl) # => <class 'bool'>