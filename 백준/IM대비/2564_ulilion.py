width, height = map(int, input().split())
N =int(input())

position = []
for i in range(N + 1):
    position.append(list(map(int, input().split())))

security = position[-1][0]      # 경비원 동서남북 위치
street = 0                      # 최단거리 합
# 1 = 북, 2 = 남, 3 = 서, 4 = 동
for i in range(N):
    store = position[i][0]      # 가게의 동서남북 위치

    if security == store:       # 둘 다 같은 선상에 있으면
        street += abs(position[i][1] - position[-1][1]) # 절댓값 차이

    elif security == 1:         # 경비가 북에 있고
        if store == 2:          # 가게가 남에 있으면
            if (position[-1][1] + position[i][1]) <= (width - position[-1][1]) + (width - position[i][1]):
                street += height + (position[-1][1] + position[i][1])
            else:
                street += height + (width - position[-1][1]) + (width - position[i][1])
        elif store == 3:        # 가게가 서에 있으면
            street += position[i][1] + position[-1][1]
        elif store == 4:        # 가게가 동에 있으면
            street += position[i][1] + (width - position[-1][1])

    elif security == 2:         # 경비가 남에 있고
        if store == 1:          # 가게가 북에 있으면
            if (position[-1][1] + position[i][1]) <= (width - position[-1][1]) + (width - position[i][1]):
                street += height + (position[-1][1] + position[i][1])
            else:
                street += height + (width - position[-1][1]) + (width - position[i][1])
        elif store == 3:        # 가게가 서에 있으면
            street += height - position[i][1] + position[-1][1]
        elif store == 4:        # 가게가 동에 있으면
            street += (height - position[i][1]) + (width - position[-1][1])
            
    elif security == 3:         # 경비가 서에 있고
        if store == 1:          # 가게가 북에 있으면
            street += position[i][1] + position[-1][1]
        elif store == 2:        # 가게가 남에 있으면
            street += position[i][1] + (height - position[-1][1])
        elif store == 4:        # 가게가 동에 있으면
            if (position[-1][1] + position[i][1]) <= (height - position[-1][1]) + (height - position[i][1]):
                street += width + (position[-1][1] + position[i][1])
            else:
                street += width + (height - position[-1][1]) + (height - position[i][1])
          
    elif security == 4:         # 경비가 동에 있고
        if store == 1:          # 가게가 북에 있으면
            street += position[-1][1] + (height - position[i][1])
        elif store == 2:        # 가게가 남에 있으면
            street += (height - position[-1][1]) + (width - position[i][1])
        elif store == 3:        # 가게가 서에 있으면
            if (position[-1][1] + position[i][1]) <= (height - position[-1][1]) + (height - position[i][1]):
                street += width + (position[-1][1] + position[i][1])
            else:
                street += width + (height - position[-1][1]) + (height - position[i][1])
print(street)