def moving(x,y,dir,board,score) : # 한 칸이라도 이동가능할 때 사용
    # 한 번 미끄러져 이동하기 -> 이동 후 좌표와 점수를 list로 반환함.
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    width = len(board[0])
    length = len(board)
    return_list = [x,y,score]

    while True : # 이동 후 판단
        x += dx[dir]
        y += dy[dir]
        if (0 <= x < width) and (0 <= y < length) :
            if board[y][x] == "D" : # 장애물에 닿기
                score += 1
                # 이전 위치 반환
                x -= dx[dir]
                y -= dy[dir]
                return_list = [x, y, score]
                return return_list
        else : # 경계에 닿음
            score += 1
            # 이전 위치 반환
            x -= dx[dir]
            y -= dy[dir]
            return_list = [x, y, score]
            return return_list
def movable(x,y,board):
    width = len(board[0])
    length = len(board)
    if (0 <= x < width) and (0 <= y < length) :
        if board[y][x] == "D" :
            return False
        else :
            return True
    else :
        return False
def solution(board) :
    width = len(board[0])
    length = len(board)

    i = 0
    j = 0
    while board[j][i] != "R" : # R 위치 찾기 (i,j)
        if i < width - 1 :
            i += 1
        elif i == width - 1 :
            j += 1
            i = 0

    q = [[i,j,0,-1]] # [x,y,score,dir]
    # recursion_limit 을 안 걸면 안 끝나서 visited 만
    visited = [[[0 for _ in range(4)] for _ in range(width)] for _ in range(length)]
    # board 의 각 점에 대하여 길이 4인 list 추가 : 같은 점에서 이동했던 방향으로 이동하는 경우 제거
    while q :
        temp = q.pop(0)
        x, y, score, dir = temp[0], temp[1], temp[2], temp[3]

        # 이동할 방향 설정
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        if dir == -1 : # 시작지점
            for Dir in range(4) :
                X = x + dx[Dir]
                Y = y + dy[Dir]
                if movable(X,Y,board) == True :
                    q.append([x,y,score,Dir])
        else : # 이동할 방향이 주어졌을 때
            X = x + dx[dir]
            Y = y + dy[dir]
            if visited[y][x][dir] == 0 : # 그 점으로 이동하기 전에 판단
                # 이동
                if movable(X,Y,board) == True :
                    newX, newY, newScore = moving(x,y,dir,board,score)
                    visited[y][x][dir] = 1
                    if board[newY][newX] == "G" :
                        return newScore
                    #이동한 지점 기준으로 다음 지점들 append
                    if dir == 0 or dir == 1 :
                        for i in range(2,4) :
                            nextX = newX + dx[i]
                            nextY = newY + dy[i]
                            if movable(nextX,nextY,board) == True :
                                q.append([newX,newY,newScore,i])
                    elif dir == 2 or dir == 3 :
                        for i in range(0,2) :
                            nextX = newX + dx[i]
                            nextY = newY + dy[i]
                            if movable(nextX,nextY,board) == True :
                                q.append([newX,newY,newScore,i])
    return -1
