# 인사를 하고 이름을 묻는 프로그램.
print("안녕하세요 저는 파이썬입니다.")
print("당신은 누굽니까?")
your_name = input()

print(your_name + "님 반갑습니다.")
print("올해 몇살이십니까?")
age = input()

print(str(2019 - int(age) + 1) + "년생이시군요.")
