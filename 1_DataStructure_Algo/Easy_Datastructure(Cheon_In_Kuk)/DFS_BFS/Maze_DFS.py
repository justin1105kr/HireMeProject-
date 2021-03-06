# ############################
# Basic Idea : 현재의 경로가 막혔을 경우 다시 선택할 수 있는 다른 경로들을 저장함
#              가장 최근의 갈림길로 돌아가 다른 곳을 찾음
# 1) DFS(스택) : 하나의 경로를 선해 끝까지 가고 막히면 새로운 경로 찾음
# 2) BFS(큐)  : 인접한 위치들 방문 후, 방문한 위치들에 인접한 위치들을 순서대로 찾음.
#          가까운 위치부터 찾
################################

# BFS 가정
# 시작 : 첫 위치 스택 삽입
# Step1 : 스택이 공백이 아닐 경우
#         - 위치를 끄냄 ( 현재위치 )
#         - 스택이 공백일 경우, 미로에 출구가 없믄 것
#         - 방문했다는 위치 등록
# Step2 : 현재 위치가 출구일 경우 탈락
#         - 아닐 경우, 상하좌우 이웃방 확인 후 벽이 아닐 경우 스택에 삽입

from Stack import Stack

def isValidPos(x,y, map):
    if map[x][y] == '0'  or map[x][y] == 'x':
        return True
    return False

    # if x < 0 or y < 0 or x >= len(map) or y >= len(map[0]) :
    #     return False
    # elif map[x][y] == '0' or map[x][y] == 'x' :
    #     return True

def DFS(start_coordinate, end_coordinate, map):
    s = Stack()
    s.push(start_coordinate)
    steps = 0

    while not s.isEmpty():
        here = s.pop()
        (x,y)=here

        if here == end_coordinate :
            return True
        else :
            map[x][y] = '.' # 방문 표시
            # 우좌하상 -> 상하좌우 순으로 꺼내서 확인
            # 꺼냈을 경우 가능한 경로가 있다면 일단 집어넣고 따라감
            if isValidPos(x, y + 1, map):
                s.push( (x, y + 1) )
            if isValidPos(x, y - 1, map):
                s.push( (x, y - 1) )
            if isValidPos(x + 1, y, map):
                s.push( (x + 1, y) )
            if isValidPos(x - 1, y, map):
                s.push( (x - 1, y) )

            steps += 1

        for i in range(len(map[0])):
            for j in range(len(map)):
                print(map[i][j], end = ' ')
            print()

        print('status : ', s.stack)
        print('steps : ', steps)
        print()
    return False # While 문에서 True 반환 못한 경우 탐색 실패


if __name__ == '__main__' :

    map = [ [ '1', '1', '1', '1', '1', '1'],
            [ 'e', '0', '0', '0', '0', '1'],
            [ '1', '0', '1', '0', '1', '1'],
            [ '1', '1', '1', '0', '0', 'x'],
            [ '1', '1', '1', '0', '1', '1'],
            [ '1', '1', '1', '1', '1', '1'],]

    result = DFS((1,0), (3,5), map)

    if result :
        print('미로 탐색 성공')
    else :
        print('미로 탐색 실패')


