###########################################
# 27.2.1 반복으문으로 여러 줄을 파일에 쓰기      ##
##########################################
# 개행문자 사용
print('27.2.1')
with open('hello.txt', 'w') as file :
    for i in range(3) :
        file.write('Hello, World! {0}\n'.format(i))


############################################
# 27.2.2 리스트에 들어있는 문자열을 파일에 쓰기    ##
# 객체.writelines(문자열)                  ##
#########################################
print('27.2.2')
lines = ['안녕하세요\n', '파이썬\n', '코딩 도장\n']
with open('hello.txt', 'w') as file :
    file.writelines(lines)


#############################################
# 27.2.3 파일 내용 한 줄씩 리스트로 가져오기       ##
# 객체.readlines()                        ##
# 한 줄씩 리스트 형태로 가져옴                ##
########################################
print('27.2.3')
with open('hello.txt', 'r') as file :
    lines = file.readlines() # 리스트에 한줄씩 저장됨
    print(lines)


#############################################
# 27.2.4 파일의 내용을 한 줄씩 읽기             ##
# 변수 = 파일객체.realine()                 ##
# 한 줄씩 순차대로 가져옴                    ##
########################################
# line != ''와 같이 빈 문자열이 아닐 때까지 계속 읽어옴
print('27.2.4')
with open('hello.txt', 'r') as file :
    line = None # 변수 line을 None으로 초기화
    while line != '' :
        line = file.readline()
        print(line.strip('\n'))


#############################################
# 27.2.5 for 반복문으로 파일의 내용 줄 단위로 읽기 ##
###########################################
print('********************************')
with open('hello.txt', 'r') as file :
    for line in file :
        print(line.strip('\n'))
    # for에 파일 객체 지정 시, 파일의 내용을 한 줄씩 읽어서 변수에 저장
print('********************************')


################################
# 참고자료 | 파일 객체는 이터레이터  ##
##############################
# 파일 객체는 이터레이터, 따라서 변수 여러개에 저장하는 언패킹도 가능
# "언패킹(Unpacking) : 변수 여러개에 저장
file = open('hello.txt', 'r')
a, b, c = file
print(a,b,c)






