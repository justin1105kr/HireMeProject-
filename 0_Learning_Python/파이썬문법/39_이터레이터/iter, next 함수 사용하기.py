# 반복을 끝낼값 : sentinel, 한국어로는 감시병이라는 의미.
# 반복이 끝날 때까지 값을 감시함

################################
# 39.4 iter, next 함수 활용하기  ##
##############################################################
# 파이썬 내장함수 iter, next
# iter(객체)는 객체의 __iter__ 메소드 호출
# next(객체)는 객체의 __next__ 메소드 호출

it = iter(range(3))
next(it) # 0
next(it) # 1
next(it) # 2


#######################################################
# 39.4.1 iter(객체), iter(객체, 반복을 끝낼 값=sentinel ) ##
# 반복을 끝낼 값이 나올 경우, StopIteration               ##
##############################################################

import random
it = iter(lambda : random.randint(0,5), 2)
# 0~5의 무작위 수 생성, 2 나올 경우 StopIteration 에러 발생, 종료

for i in iter(lambda : random.randint(0,5), 2) :
    print(i, end=' ')

##########################################################
# 39.4.3 next(객체), next(객체, 기본값)                    ##
# 반복이 끝나더라도 StopIteration이 발생하지 않고 기본값 출력     ##
##############################################################
it = iter(range(3))
next(it, 10) #0
next(it, 10) #1
next(it, 10) #2
next(it, 10) #10
next(it, 10) #10
