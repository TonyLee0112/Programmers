주소 : https://school.programmers.co.kr/learn/courses/30/lessons/169199  
def solution(board):
    answer = -1
    length, width = len(board), len(board[0])
    a = -1
    b = -1
    for i in range(length) :
        for j in range(width) :
            if board[i][j] == "R" :
                a,b = j, i

    score = 0
    dir = -1
    q = [[a,b,score,dir]]
    print("initial q : {}".format(q))
    # score = 이때까지 움직인 횟수, dir = 앞으로 움직일 방향
    direction = [(0,-1),(0,1),(-1,0),(1,0)] # 상하좌우 순
    Exit = True

    while len(q) > 0 and Exit :
        temp = q.pop(0)
        print("{} popped".format(temp))
        x,y = temp[0],temp[1]
        s = temp[2]
        if (0 <= x < width) and (0 <= y < length) :
            if dir == -1 :
                q.append([x, y, s, 0])
                q.append([x, y, s, 1])
                q.append([x, y, s, 2])
                q.append([x, y, s, 3])
            else :
                nextX = x + direction[dir][0]
                nextY = y + direction[dir][1]
                if dir == 0 : # 위로 이동
                    if nextY >= 0 :
                        if board[nextY][nextX] == "D" :
                            if board[y][x] == "G" :
                                answer = s+1
                                Exit = False
                            else :
                                q.append([nextX, nextY, s+1, 2])
                                q.append([nextX, nextY, s+1, 3])
                        else :
                            q.append([nextX, nextY, s, 0])
                    else :
                        q.append([x,y, s + 1, 2])
                        q.append([x,y, s + 1, 3])
                if dir == 1 : # 아래로 이동
                    if nextY < length :
                        if board[nextY][nextX] == "D" :
                            if board[y][x] == "G" :
                                answer = s+1
                                Exit = False
                            else :
                                q.append([nextX, nextY, s+1, 2])
                                q.append([nextX, nextY, s+1, 3])
                        else :
                            q.append([nextX, nextY, s, 1])
                    else :
                        q.append([x, y, s + 1, 2])
                        q.append([x, y, s + 1, 3])
                if dir == 2 : # 좌로 이동
                    if nextX >= 0 :
                        if board[nextY][nextX] == "D" :
                            if board[y][x] == "G" :
                                answer = s+1
                                Exit = False
                            else :
                                q.append([nextX, nextY, s+1, 0])
                                q.append([nextX, nextY, s+1, 1])
                        else :
                            q.append([nextX, nextY, s, 2])
                    else :
                        q.append([x, y, s + 1, 0])
                        q.append([x, y, s + 1, 1])
                if dir == 3 : # 우로 이동
                    if nextY < width :
                        if board[nextY][nextX] == "D" :
                            if board[y][x] == "G" :
                                answer = s+1
                                Exit = False
                            else :
                                q.append([nextX, nextY, s+1, 0])
                                q.append([nextX, nextY, s+1, 1])
                        else :
                            q.append([nextX, nextY, s, 3])
                    else :
                        q.append([x, y, s + 1, 0])
                        q.append([x, y, s + 1, 1])
    return answer

INPUT = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
print(solution(INPUT))
