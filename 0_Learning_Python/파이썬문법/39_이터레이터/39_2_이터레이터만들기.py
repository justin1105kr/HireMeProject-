##########################
# 39.2 이터레이터 만들기    ##
# ** 이터레이터는 언패킹이 가능 **
##############################################################
# __iter__ 와 __next__ 메소드를 이용하여
# range()와 같이 동작하는 이터레이터 생성하기
# ###################################
# class 이터레이터이름:                 #
#     def __iter__(self):           #
#         코드                       #
#                                   #
#     def __next__(self):           #
#         코드                       #
##############################################################

class Counter: # Range와 같은 동장을 하는 클래스
    def __init__(self, stop):
        self.current = 0        # 현재 숫자 유지, 0부터 지정된 숫자 직전까지 반복
        self.stop = stop        # 반복을 끝낼 숫자

    def __iter__(self):
        return self             # 현재 인스턴스를 반환

    def __next__(self):
        if self.current < self.stop:  # 현재 숫자가 반복을 끝낼 숫자보다 작을 때
            r = self.current          # 반환할 숫자를 변수에 저장
            self.current += 1         # 현재 숫자를 1 증가시킴
            return r                  # 숫자를 반환
        else:                         # 현재 숫자가 반복을 끝낼 숫자보다 크거나 같을 때
            raise StopIteration       # 예외 발생


for i in Counter(3) :
    print(i)

c = Counter(3)
print(c.__iter__().__next__())
print(c.__iter__().__next__())
print(c.__iter__().__next__()) # 같은 값 출력
# print(c.__iter__().__next__()) # StopIeration


############################
# 39.3 이터레이터 언패킹      ##
# 이터레이터는 언패킹이 가능함  ##
# map도 이터레이터의 일종    ##
##############################################################
print('언패킹')
a, b, c = Counter(3)
print(a,b,c)

################################
# 참고 | 반환값을 _에 저장하는 이유  ##
###############################
# 반환값을 언패킹했을 때 _에 할당하는 것은
# 특정 순서의 반환값 사용하지 않고 무시하겠다는 관례적 표현입니다.
# 예를 들어 다음과 같은 코드는 언패킹 했을 때 두 번째 변수는 사용하지 않겠다는 뜻입니다.
a, _, c, d =  range(4)
print(a, c, d)