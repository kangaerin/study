print("a" + "b")
print("a", "b")

## 방법 1
print("나는 %d살 입니다." % 20)
# d 는 정수를 의미

print("나는 %s를 좋아해요." % "파이썬")
# s는 문자열을 의미

print("Apple은 %c로 시작해요." % "A")
# c는 한 글자를 의미

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))
# 두 가지를 이용할떄는 () 안에 넣기


## 방법2
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

## 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))

## 방법 4 (v 3.6이상)
age = 24
color = "노란"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
