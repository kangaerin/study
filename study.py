python = "Python is Amazing"

print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")  # 몇번째에 위치에 있는지
print(index)  # git에 들어가는지 확인

index = python.index("n", index + 1)
print(index)

print(python.find("Java"))  # 없는 글자를 넣으면 -가 나오게 됨.

#print(python.index("Java")) # 파이썬문장 에서는 자바가 없기때문에 에러가 발생한다.
# find를 쓸 경우에는 오류로 멈추지 않고 계속 진행됨.
print("hi")

print(python.count("n"))