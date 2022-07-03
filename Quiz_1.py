

# 사이트 별 비밀번호 작성 프로그램 생성

#예 : http://naver.com
# 규칙1) http:// 부분은 제외 > naver.com
# 규칙2) 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3) 남은 글자중 처음 세자리 + 글자 개수 + 글자내 'e' 개수 + "!"로 구성

# 예) 생성된 비밀번호 : nav51!

url = "http://naver.com"

url_1 = url.replace("http://", "") # 규칙1
print(url_1)

url_2 = url_1[:url_1.index(".")] # 규칙2 [0:5] -> 0, 1, 2, 3, 4
print(url_2)

url_3 = url_2[:3] + str(len(url_2)) + str(url_2.count("e")) + "!"
print(url_3)
print("{0}의 비밀번호는 {1}입니다.".format(url, url_3))