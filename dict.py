cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5] # 에러발생
print(cabinet.get(5))  # None 출력되며 에러 발생하지 않음
print(cabinet.get(5, "사용가능"))  # 가져올 수 있으면 5, 아니면 사용가능을 가져온다.
print("hi")

#  사진 자료형에 어떤 값이 있는지 확인
print(3 in cabinet)  # 값이 존재한다면 true, 아니면 false
print(5 in cabinet)

cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 값 할당
print(cabinet)
cabinet["C-20"] = "조세호"
print(cabinet)
cabinet["A-3"] = "김종국"
print(cabinet)  # 값이 갱신된다.

# 값 제거
del cabinet["A-3"]
print(cabinet)

# 키만 출력
print(cabinet.keys())
# 값만 출력
print(cabinet.values())
# 둘다 출력
print(cabinet.items())

# 사전 제거
cabinet.clear()
print(cabinet)