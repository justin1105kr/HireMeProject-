# map
# map(함수, 리스트/튜플)
# 원본 리스트 변경않고 함수 이용하여 맵 객체 생성
# 맵 객체는 변수 여러 개에 저장 가능
########################################

###########################################
# (1) map 객체기 이용하여 새로운 리스트 생성하기  ##
##########################################
# list(map(함수, 리스트))
# tuple(map(함수, 튜플))
#
# 아래 의 두 식은 같음
# >>> a = [1.2, 2.5, 3.7, 4.6]
# >>> for i in range(len(a)):
# ...     a[i] = int(a[i])
#
# >>> a = list(map(int, a))기


###########################################
# (2) map 객체 이용하여 여러 변수에 값 저장하기  ##
#########################################
# x = input().split()     # 맵 객체는 변수 여러 개에 저장할 수 있음
# input().split()의 결과는 문자열 리스트
# # m = map(int, x)        # 리스트의 요소를 int로 변환, 결과는 맵 객체
# # a, b = m


##############################
# 32.2.2 map에 여러 객체 넣기  ##
###########################################
# map(함수, 반복 가능 객체1, 시퀀스 객체2....)
a = [1,2,3,4,5]
b = [10,20,30,40,50]
map_a_b = map((lambda a, b : a*b), a, b)
list_a_b = list(map_a_b)
print(list_a_b)


####################################
# 32.2.3 filter(함수, 반복 가능 객체) ##
###########################################
# 함수의 반환값이 True인 경우의 값으로 새로운 리스트 생성
def f(x) :
    return x > 5 and x < 10
a = [1,2,3,4,5,6,7,8,9]
print(list(filter(f,a)))
print( list( filter((lambda x : x > 5 and x < 10), a) ) )


#####################################
# 32.2.4 reduce(함수, 반복 가능 객체)  ##
###########################################
# 반복 가능 객체를 함수처리 후 누적 덧셈 후 반환
from functools import reduce
a = [1,2,3,4,5,6,7,8,9]
reduced_a = reduce((lambda x,y : x+y), a)
print(reduced_a)