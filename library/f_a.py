# abs()は絶対値を返す関数。引数が複素数の場合は原点からの距離が返される
ab-value = abs(-111)
# => 111

# all()は引数の全ての要素がTrue、もしくは引数が空の場合にTrueを返す
# all()を使わない場合は以下のようになる

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

# any()は引数のいずれかの値がTrueならTrueを返す。以下と等価

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

# ascii()はASCII文字列を返す関数。ASCIIではない文字列が渡された場合は\xや\uでエスケープされて返される
var = ascii("Hello") # => "Hello"
var = ascii('ãäëÿ')  # => "'\\xe3\\xe4\\xeb\\xff'"