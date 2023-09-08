#ランダムな整数を利用するために、randomモジュールをインポート
import random

# 変数numに0～10までのランダムな整数を代入する
var = random.randint(0, 10)

print(var)

if var % 3 == 0:
  print("Fizz")
elif var % 5 == 0:
  print("Buzz")
else:
  print(var)
