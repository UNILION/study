import socket
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'SEOUL01_PYTHON'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901

TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [ [0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127] ]

class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: ' + HOST + ':' + str(PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: ' + HOST + ':' + str(PORT))
        send_data = '9901/' + NICKNAME
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play.\n--------------------')
    def request(self):
        self.sock.send('9902/9902'.encode())
        print('Received Data has been currupted, Resend Requested.')
    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: ' + recv_data)
        return recv_data
    def send(self, angle, power):
        merged_data = '%d/%d' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: ' + merged_data)
    def close(self):
        self.sock.close()
        print('Connection Closed.\n--------------------')

class GameData:
    def __init__(self):
        self.order = 0
        self.reset()
    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]
    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = int(float(split_data[idx]))
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)

    def arrange(self):
        self.order = self.balls[0][1]
        print('\n* You will be the %s player. *\n' %
              ('first' if self.order == 1 else 'second'))

    def show(self):
        print('=== Arrays ===')
        for i in range(NUMBER_OF_BALLS):
            print('Ball%d: %d, %d' % (i, self.balls[i][0], self.balls[i][1]))
        print()

def play(conn, gameData):
    import math

    r = 5.73 / 2
    white = gameData.balls[0]
    arrival = HOLES[0]
    # gameball[0] => 흰색 공
    # gameball[1] => 목적 공
    # 목적구 정하기
    if gameData.order == 1:  # 선공
        ball_list = [gameData.balls[1], gameData.balls[3], gameData.balls[5]]
        print("111")
        print(ball_list)
    else:  # 후공
        ball_list = [gameData.balls[2], gameData.balls[4], gameData.balls[5]]
        print("222")
        print(ball_list)
    real_min = 300  # 홀과 목적구의 최소 값
    purposes = ball_list[0]  # 최종 목적구
    arrivals = HOLES[0]  # 최종 홀
    flag = 0
    for j in range(3):
        if (ball_list[j][0] == 0) and (ball_list[j][1] == 0):  # 만약 이미 들어간 홀이면
            flag += 1
            continue

        if (j == 2) and (flag != 2):  # 만약 둘 다 없으면 검은공을 목적구로 설정
            continue

        purpose = ball_list[j]  # 현재 목적구
        # 홀 위치 정하기

        if purpose[0] <= 127:
            holes_list = [HOLES[0], HOLES[1], HOLES[3], HOLES[4]]
        else:
            holes_list = [HOLES[1], HOLES[2], HOLES[4], HOLES[5]]

        min = 300  # (254^2 + 127^2)^(0.5) = 284
        for i in range(4):
            if (white[0] <= purpose[0]) and (white[1] <= purpose[1]):  # 수구 기준 목적구가 1사분면
                arrival = holes_list[3]  # 홀의 위치
                if ((holes_list[3][0] - purpose[0]) ** 2 + (holes_list[3][1] - purpose[1]) ** 2) ** (0.5) < min:
                    min = ((holes_list[3][0] - purpose[0]) ** 2 + (holes_list[3][1] - purpose[1]) ** 2) ** (0.5)

            elif (white[0] >= purpose[0]) and (white[1] <= purpose[1]):  # 2사분면
                arrival = holes_list[2]  # 홀의 위치
                if ((holes_list[2][0] - purpose[0]) ** 2 + (holes_list[2][1] - purpose[1]) ** 2) ** (0.5) < min:
                    min = ((holes_list[2][0] - purpose[0]) ** 2 + (holes_list[2][1] - purpose[1]) ** 2) ** (0.5)

            elif (white[0] >= purpose[0]) and (white[1] >= purpose[1]):  # 3사분면
                arrival = holes_list[0]  # 홀의 위치
                if ((holes_list[0][0] - purpose[0]) ** 2 + (holes_list[0][1] - purpose[1]) ** 2) ** (0.5) < min:
                    min = ((holes_list[0][0] - purpose[0]) ** 2 + (holes_list[0][1] - purpose[1]) ** 2) ** (0.5)

            elif (white[0] <= purpose[0]) and (white[1] >= purpose[1]):  # 4사분면
                arrival = holes_list[1]  # 홀의 위치
                if ((holes_list[1][0] - purpose[0]) ** 2 + (holes_list[1][1] - purpose[1]) ** 2) ** (0.5) < min:
                    min = ((holes_list[1][0] - purpose[0]) ** 2 + (holes_list[1][1] - purpose[1]) ** 2) ** (0.5)

        if min < real_min:  # 홀과 가장 가까운 목적구 찾기
            real_min = min  # 홀과 목적구의 최소 거리
            purposes = purpose  # 최종 목적구를 현재 목적구로 정함
            arrivals = arrival  # 최종 홀을 현재 목적구랑 가까운 홀로 정함

    print("real_min : {} ".format(real_min))
    print("white: {}".format(white))
    print("purposes : {} ".format(purposes))
    print("arrivals : {} ".format(arrivals))
    # 홀 위치 - 목적구 위치 대각선 길이
    b = ((arrivals[0] - purposes[0]) ** 2 + (arrivals[1] - purposes[1]) ** 2) ** (0.5)

    # 홀과 목적구의 y 값의 차이 / 대각선의 길이에 arccos 적용으로 세타 구하기
    theta = math.acos((arrivals[1] - purposes[1]) / b)  # 라디안

    # (대각선 길이 + 2r)에  cos  세타를 곱하면 옮길 목적구 까지의 y 수정값 알 수 있음
    # cos 세타 적용해서 나온 y값을 목적구에서 빼거나 더해줌
    new_y = (b + 2 * r) * math.cos(theta)  # (arrivals[1] - purposes[1]) / b 그대로
    # 홀의 y좌표에서 위의 값을 뺀 것이 새로운 목적구 값
    print("first_new_y : {}".format(new_y))
    new_y = arrivals[1] - new_y
    print("second_new_y : {}".format(new_y))

    # 그 다음은 sin을 이용해서 x 수정값 알 수 있음
    # sin세타 적용해서 나온 x값을 목적구에서 더해거나 빼줌
    new_x = (b + 2 * r) * math.sin(theta)  # 무조건 양수, 오른쪽이면 홀에서 더해주고 왼쪽은 빼줄 필요 있음
    if arrivals[0] < purposes[0]:       # 목적구가 홀보다 오른쪽
        new_x = arrivals[0] + new_x
    else:
        new_x = arrivals[0] - new_x

    purposes = [new_x, new_y]

    angle = (90 - 180 / math.pi * math.atan2(new_y, new_x))
    power = 50  # 홀까지 가는데 최소 힘, 너무 쎄면 공이 튕겨 나올지도
    conn.send(angle, power)

def main():
    conn = Conn()
    gameData = GameData()
    print(gameData.balls)
    print(gameData.reset())
    print(gameData.show())
    print(gameData.read(conn))
    while True:
        gameData.read(conn)
        gameData.show()
        if gameData.balls[0][0] == 9909:
            break
        play(conn, gameData)
    conn.close()
    print('Connection Closed')

if __name__ == '__main__':
    main()
