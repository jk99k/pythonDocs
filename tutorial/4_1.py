x = int(input("Please enter an integer "))
if x < 0:
    x = x*(-1)
    print("値が負だったので正にしました\n")
    print(x)
elif x == 0:
    print("ゼロです\n")
    print(x)
else:
    print("正の数です\n")
    print(x)

# ターミナルで $ python 4_1.py と実行すると上の処理が実行される
# 変数xをinputで与えている