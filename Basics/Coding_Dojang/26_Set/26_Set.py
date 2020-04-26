####################
# 26.1 세트 만들기  ##
################################################################################
# 세트는 { }(중괄호) 안에 값을 저장하며 각 값은 ,(콤마)로 구분해줍니다.
#
# 세트 = {값1, 값2, 값3}
# 간단하게 과일이 들어있는 세트를 만들어보겠습니다.
#
# >>> fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
# >>> fruits
# {'pineapple', 'orange', 'grape', 'strawberry', 'cherry'}
#
# 그리고 set(range(5))와 같이 숫자를 만들어내는 range를 사용하면 0부터 4까지 숫자를 가진 세트를 만들 수 있습니다.
# 단, 세트가 { }를 사용한다고 해서 c = {}와 같이 만들면 빈 딕셔너리가 만들어지므로 주의해야 합니다.
################################################################################


#######################################
# 26.1.1  세트에 특정 값이 있는지 확인하기  ##
################################################################################
# 그럼 세트에 특정 값이 있는지 확인하려며 어떻게 해야 할까요? 지금까지 리스트, 튜플, 딕셔너리에 사용했던 in 연산자를 사용하면 됩니다.
#
# 값 in 세트
# >>> fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
# >>> 'orange' in fruits
# True
# >>> 'peach' in fruits
# False
################################################################################


####################
# 참고 | 프로즌 세트 ##
################################################################################
# 파이썬은 내용을 변경할 수 없는 세트도 제공합니다.
# 프로즌세트 = frozenset(반복가능한객체)
# >>> a = frozenset(range(10))
# >>> a
# frozenset({0, 1, 2, 3, 4, 5, 6
################################################################################


####################################
# 26.2.4  세트가 겹치지 않는지 확인하기  ##
################################################################################
# disjoint는 현재 세트가 다른 세트와 겹치지 않는지 확인합니다. 겹치는 요소가 없으면 True, 있으면 False입니다.
# 현재세트.isdisjoint(다른세트)
# >>> a = {1, 2, 3, 4}
# >>> a.isdisjoint({5, 6, 7, 8})       # 겹치는 요소가 없음
# True
# >>> a.isdisjoint({3, 4, 5, 6})    # a와 3, 4가 겹침
# False
################################################################################


##############################
# 26.3.1  세트에 요소 추가하기  ##
################################################################################
# add(요소)는 세트에 요소를 추가합니다.
#
# >>> a = {1, 2, 3, 4}
# >>> a.add(5)
#
# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*
# 26.3.2  세트에서 특정 요소를 삭제하기
# remove(요소)는 세트에서 특정 요소를 삭제하고 요소가 없으면 에러를 발생시킵니다.
#
# >>> a.remove(3)
# >>> a
# {1, 2, 4, 5}
#
# discard(요소)는 세트에서 특정 요소를 삭제하고 요소가 없으면 그냥 넘어갑니다.
# 다음은 세트 a에 2가 있으므로 2를 삭제하고, 3은 없으므로 그냥 넘어갑니다.
#
# >>> a.discard(2)
# >>> a
# {1, 4, 5}
#
# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*
# 26.3.3  세트에서 임의의 요소 삭제하기
# pop()은 세트에서 임의의 요소를 삭제하고 해당 요소를 반환합니다. 만약 요소가 없으면 에러를 발생시킵니다.
#
# >>> a = {1, 2, 3, 4}
# >>> a.pop()
# 1
#
# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*
# 26.3.4  세트의 모든 요소를 삭제하기
# clear()는 세트에서 모든 요소를 삭제합니다.
#
# >>> a.clear()
# >>> a
#
# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*
# 26.3.5  세트의 요소 개수 구하기
# 지금까지 리스트, 튜플, 문자열, range, 딕셔너리의 요소 개수를 구할 때 len 함수를 사용했죠?
#
# 마찬가지로 len(세트)는 세트의 요소 개수(길이)를 구합니다.
#
# >>> a = {1, 2, 3, 4}
# >>> len(a)
# 4
################################################################################


#########################
# 26.2 집합 연산 사용하기  ##
################################################################################
# | 연산자는 합집합(union)을 구하며 OR 연산자 |를 사용합니다.
# set.union 메서드와 동작이 같습니다.
# 다음은 세트 {1, 2, 3, 4}와 {3, 4, 5, 6}을 모두 포함하므로 {1, 2, 3, 4, 5, 6}이 나옵니다.
#
# 세트1 | 세트2
# set.union(세트1, 세트2)
# >>> a = {1, 2, 3, 4}
# >>> b = {3, 4, 5, 6}
# >>> a | b
# {1, 2, 3, 4, 5, 6}
# >>> set.union(a, b)
# {1, 2, 3, 4, 5, 6}
#
# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*
# & 연산자는 교집합(intersection)을 구하며 AND 연산자 &를 사용합니다.
# set.intersection 메서드와 동작이 같습니다.
# 다음은 세트 {1, 2, 3, 4}와 {3, 4, 5, 6} 중에서 겹치는 부분을 구하므로 {3, 4}가 나옵니다.
#
# 세트1 & 세트2
# set.intersection(세트1, 세트2)
# >>> a & b
# {3, 4}
# >>> set.intersection(a, b)
# {3, 4}
#
# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*
# - 연산자는 차집합(difference)을 구하며 뺄셈 연산자 -를 사용합니다.
# set.difference 메서드와 동작이 같습니다.
# 다음은 {1, 2, 3, 4}에서 {3, 4, 5, 6}과 겹치는 3과 4를 뺐으므로 {1, 2}가 나옵니다.
#
# 세트1 - 세트2
# set.difference(세트1, 세트2)
# >>> a - b
# {1, 2}
# >>> set.difference(a, b)
# {1, 2}
#
# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*
# ^ 연산자는 대칭차집합(symmetric difference)을 구하며 XOR 연산자 ^를 사용합니다.
# set.symmetric_difference 메서드와 동작이 같습니다.
# 대칭차집합은 XOR 연산자의 특성을 그대로 따르는데 XOR은 서로 다르면 참입니다.
# 따라서 집합에서는 두 집합 중 겹치지 않는 요소만 포함합니다.
# 다음은 세트 {1, 2, 3, 4}와 {3, 4, 5, 6} 중에서 같은 값 3과 4를 제외한 다른 모든 요소를 구하므로 {1, 2, 5, 6}이 나옵니다.
#
# 세트1 ^ 세트2
# set.symmetric_difference(세트1, 세트2)
# >>> a ^ b
# {1, 2, 5, 6}
# >>> set.symmetric_difference(a, b)
# {1, 2, 5, 6}
#
# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*
# 26.2.2  부분 집합과 상위집합 확인하기
# 세트는 부분집합, 진부분집합, 상위집합, 진상위집합과 같이 속하는 관계를 표현할 수도 있습니다.
#
# <=은 현재 세트가 다른 세트의 부분집합(subset)인지 확인하며
# issubset 메서드와 같습니다.
#
# 현재세트 <= 다른세트
# 현재세트.issubset(다른세트)
# >>> a = {1, 2, 3, 4}
# >>> a <= {1, 2, 3, 4}
# True
#
# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*
# <은 현재 세트가 다른 세트의 진부분집합(proper subset)인지 확인하며 메서드는 없습니다.
# 다음은 세트 {1, 2, 3, 4}가 {1, 2, 3, 4, 5}의 진부분집합이므로 참입니다.
# 즉, 부분집합이지만 같지는 않을 때 참입니다.
#
# 현재세트 < 다른세트
# >>> a = {1, 2, 3, 4}
# >>> a < {1, 2, 3, 4, 5}
# True
#
# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*
# >=은 현재 세트가 다른 세트의 상위집합(superset)인지 확인하며
# issuperset 메서드와 같습니다.
#
# 현재세트 >= 다른세트
# 현재세트.issuperset(다른세트)
# >>> a = {1, 2, 3, 4}
# >>> a >= {1, 2, 3, 4}
# True
# >>> a.issuperset({1, 2, 3, 4})
# True
#
# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*
# >은 현재 세트가 다른 세트의 진상위집합(proper superset)인지 확인하며 메서드는 없습니다.
#
# 현재세트 > 다른세트
# >>> a = {1, 2, 3, 4}
# >>> a > {1, 2, 3}
# True
#
################################################################################


## 연습문제 ##
# 26.8 연습문제: 공배수 구하기
# 다음 소스 코드를 완성하여 1부터 100까지 숫자 중 3과 5의 공배수를 세트 형태로 출력되게 만드세요.
a = { i for i in range(1,100) if i % 3 == 0}
b = { i for i in range(1,100) if i % 5 == 0}
print(a & b)

# 표준 입력으로 양의 정수 두 개가 입력됩니다.
# 다음 소스 코드를 완성하여 두 숫자의 공약수를 세트 형태로 구하도록 만드세요.
# 단, 최종 결과는 공약수의 합으로 판단합니다.
num1, num2 = map(int, input().split())
a = { i for i in range(1, num1+1) if num1 % i == 0 }
b = { i for i in range(1, num2+1) if num2 % i == 0 }
divisor = a & b
result = 0

if type(divisor) == set :
    result = sum(divisor)

print(result)
