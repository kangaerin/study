# 리스트 []

# 지하철 칸 변로 10, 20, 30명

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)


subway = ["유재석", "조세호", "박명수"]
print(subway)


# 조세호씨가 몇번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 다음 정류장에 하하씨가 추가로 탐.
subway.append("하하") # 맨 뒤에 붙음
print(subway)

# 유재석과 조세호 사이에 정형돈 넣기
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람들을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# 같은 사람의 이름이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [2, 5, 1, 4, 3]
num_list.sort()
print(num_list)

# 순서 뒤집기

num_list.reverse()
print(num_list)


# 리스트 안의 내용을 모두 지우고 싶을때
num_list.clear()
print(num_list)

# 다양한 자료형과 함께 사용할 수 있다.
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list = [2, 5, 1, 4, 3]
num_list.sort()
num_list.extend(mix_list)
print(num_list)