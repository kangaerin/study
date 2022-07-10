# 집합(set)
# 중복 안됨, 순서 없음

my_set = {1, 2, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}

python = set(["유재석", "박명수"])

# 교집합 출력
print(java & python)
print(java.intersection(python))

# 합집합 출력
print(java | python)
print(java.union(python))

# 차집합 출력
print(f' 차집합 : {java - python}')
print(java.difference(python))

# python 추가
python.add("김태호")
print(f' 추가 : {python}')

# java 제거
java.remove("김태호")
print(f' 제거 : {java}')