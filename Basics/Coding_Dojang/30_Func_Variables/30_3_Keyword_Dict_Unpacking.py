###################################
# 30_3_1 키워드 인수와 딕셔너리 언패킹  ##
###########################################################
# - 딕셔너리 언패킹 사용 시
#   => 매개변수의 이름 및 키 이름이 값아야함
#   => 매개변수 개수와 딕셔너리의 키 갯수 같아야 함
###########################################################
def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')

personal_info(*x) # 키 출력 => 이름 : name, 나이 : age, 주소 : address
personal_info(**x) # 값 출력 => 이름 : 홍길동, 나이 : 30, 주소 : 서울시 용산구 이촌동

##############################################
# 30_3_2 키워드 인수를 사용하는 가변 인수 함수 만들기 ##
###########################################################
# - 함수를 만들 때 괄호 안에 **kwargs와 같이 매개변수 앞에 **를 붙입니다.
# - 키워드 가변 인수의 매개변수는 kwargs 를 관례적으로 사용
# def 함수이름(**매개변수)
#     코드
###########################################################
def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')
personal_info(name='홍길동')
x = {'name', 홍길동}
personal_info(**x) # 언패킹하여 호출 가능

################################################
# 30_3_3 **kwargs를 사용한 가변 인수 함수 사용 방법  ##
###########################################################
# - 함수 안에서 "특정 키가 있는 지 확인" 후 해당 기능 만듬
def personal_info(**kwargs):
    if 'name' in kwargs:    # in으로 딕셔너리 안에 특정 키가 있는지 확인
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:
        print('나이: ', kwargs['age'])
    if 'address' in kwargs:
        print('주소: ', kwargs['address'])


##################################################
# 참고 | 고정 인수와 가변 인수(키워드 인수)를 함께 사용하기  ##
###########################################################
# 고정 인수와 가변 인수(키워드 인수)를 함께 사용할 때는 다음과 같이
# 고정 매개변수를 먼저 지정하고, 그 다음 매개변수에 **를 붙여주면 됩니다.
def personal_info(name, **kwargs):
    print(name)
    print(kwargs)

##########################################
# 참고 | 위치 인수와 키워드 인수를 함께 사용하기  ##
###########################################################
# - 고정 매개 변수, 가변 위치 변수, 가변 키워드 인수 순으로 매개변수 지정해야함
# def func(고정매개변수, *args, **kwargs)
#
# 함수에서 위치 인수를 받는 *args와 키워드 인수를 받는 **kwargs를 함께 사용할 수도 있습니다.
# 다음과 같이 함수의 매개변수를 *args, **kwargs로 지정하면 위치 인수와 키워드 인수를 함께 사용합니다.
def custom_print(*args, **kwargs):
    print(*args, **kwargs)

custom_print(1, 2, 3, sep=':', end='')
