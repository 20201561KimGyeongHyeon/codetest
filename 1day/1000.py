# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
A, B = input().split()
x = int(A)
y = int(B)
print(x+y)

# split() : 문자열을 공백이나 다른 문자로 분리해서 리스트를 반환, 공백기준으로 앞 뒤 나눔
# 2번째 방법으로 map함수가 있음
# a,b = map(int, input().split())
# print(a+b)
# 리스트 하나하나를 함수명에 대입