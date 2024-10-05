# 두 정수를 입력받기
num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))

# 덧셈, 뺄셈, 곱셈, 나눗셈 연산
sum_result = num1 + num2
diff_result = num1 - num2
mul_result = num1 * num2

# 나눗셈 처리
if num2 != 0:
    div_result = num1 / num2
else:
    div_result = "정의되지 않음"

# 결과 출력
#다른내용 추가
print(f"두 수의 나머지: {num2%num1}")
print(f"두 수의 합: {sum_result}")
print(f"두 수의 차: {diff_result}")
print(f"두 수의 곱: {mul_result}")
print(f"두 수의 나눗셈: {div_result}")