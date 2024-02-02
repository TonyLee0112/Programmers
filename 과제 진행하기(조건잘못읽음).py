from collections import deque
def solution(plans):
    answer = []
    for assign in plans:
        t = get_time(assign[1])
        assign[1] = t
        assign[2] = int(assign[2])
        assign.append(assign[0])
        assign.pop(0)
        # assign 순서 변경 : [시작 시간,걸리는 시간,이름]

    plans.sort()

    q = deque(plans)
    print("initial q : {}".format(q))
    print("\n")
    while q:
        # q[i] = [시작 시간,걸리는 시간,이름]
        start = q[0][0]
        end = start + q[0][1]
        if len(q) > 1 :
            next_start = q[1][0]
            if next_start < end:
                q[0][1] -= next_start - start  # 경과 시간을 걸리는 시간에서 빼주고 뒤로 보냄
                temp = q.popleft()
                print("{} popped from q".format(temp))
                print("current q : {}".format(q))
                cnt = 1
                while cnt < len(q) : # 뒤의 어느 부분으로 보낼 것인가
                    if q[cnt-1][0]+ q[cnt-1][1] < q[cnt][0] :
                        temp[0] = q[cnt-1][0]+ q[cnt-1][1]
                        q.insert(cnt,temp)
                        print("{} added at {}th index".format(temp,cnt))
                        print("current q : {}".format(q))
                        break
                    else :
                        cnt += 1
                if cnt == len(q) :
                    last_index = len(q)-1
                    temp[0] = q[last_index][0]+q[last_index][1]
                    q.append(temp)
                    print("{} added at {}th index".format(temp, cnt))
                    print("current q : {}".format(q))
            else:
                finish = q.popleft()
                answer.append(finish[2])
                print("{} is finished at {}".format(finish[2],finish[0]+finish[1]))
        else :
            finish = q.popleft()
            answer.append(finish[2])
            print("{} is finished at {}".format(finish[2], finish[0] + finish[1]))

        print("\n")
    return answer


def get_time(time_str):
    time_h, time_sec = map(int, time_str.split(':'))
    t = time_h * 60 + time_sec
    return t

p = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]

sol = solution(p)

ans = ["science", "history", "computer", "music"]

if sol == ans :
    print("congratulations")
else :
    print("do it again")
    print("sol : {}".format(sol))
    print("ans : {}".format(ans))
