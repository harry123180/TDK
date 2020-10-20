import socket
import os
from _thread import *
##########################################TCP 端口 IP設定
ServerSocket = socket.socket()
host = '25.16.249.17'
port = 1233
ThreadCount = 0
#########################################伺服器全域變數宣告
pls1 = 0
pls2 = 0
id = 0
id_rq = 0
vision_result_1 = 0
vision_result_2 = 0
mission_id = 0
mov_cmd = 0
mov_dis = 0
mov_spd =0
############################################開始連線
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)
############################################訊息接收 更新數據
def block_number(number):
    global pls1 ,pls2 ,id ,id_rq,vision_result_1,vision_result_2,mission_id
    block_num = int(number[0])
    rply = 'tt'
    if (block_num == 0):
        print(number)
        mov_cmd = number[1]
        mov_spd = number[2]
        mov_dis = number[3]
        rply = '1' + str(' ') + str(pls1) + str(' ') + str(pls2)
        print(mov_cmd,mov_spd,mov_dis)
        # 第0號 來自筆電 資料格式: '區塊號 ,運動指令 ,運動速度,運動距離
        # mov_cmd 運動指令 0 = 停 ;1 = 前 ;2 = 左 ; 3 = 右 ; 4 = 後
        # mov_spd #速度設定
        # mov_dis 移動距離/角度設定

    elif (block_num == 1 and len(number) == 3):

        # 第1號 來自外部輸入區塊 資料格式 '區塊號 , 外部輸入指令類型 '
        # 回復: '收到(bool),執行結果(bool)'
        pls1 = number[1]
        pls2 = number[2]
        print(pls1, pls2)
        rply = '2'
    elif (block_num == 2):
        # 第二號 來自控制運動區塊 資料格式 '區塊號 ,有無執行中任務(bool) , x , y , theta , 視覺辨識需求號 '
        #第二號 來自控制運動區塊 資料格式 '區塊號 ,有無執行中任務(bool)
        # 回復:'收到(bool) , 任務指令 , 視覺辨識結果 '
        # 詢問Arduino物件距離
        # 詢問Arduino陀螺儀轉角

        rply = '3'+str(' ')+str(mission_id)+str(' ')+str(vision_result_1)+str(' ')+str(vision_result_2)
    elif (block_num == 3):
        # 第三號 來自視覺辨識區塊 資料格式 '區塊號 , 執行中的辨識號 ,辨識結果 ,'
        # 視覺辨識區塊 獨立控制攝影機
        # 辨識號0 : 不用辨識 回傳 0 , 0
        # 辨識號1 :擷取地上標線 回傳 標線斜率 標線距離
        # 辨識號2 :擷取左面牆線 回傳 車體偏角 距牆距離
        # 辨識號3 :擷取右面牆線 回傳 車體偏角 距牆距離
        # 辨識號4 :擷取正面物件 回傳 物件cx ,物件cy
        # 辨識號5 :擷取分類區位置 回傳 車體偏角
        # 回復:'收到,x,y,theta'
        id= number[1]
        rply = '4'
    elif (block_num == 4):
        # 第四號 來自路徑編輯區塊 資料格式 '區塊號 , 動作類型 , 動作距離 '
        # 回復:'收到(bool),x,y,theta'
        rply = '5'
    elif (block_num == 5):
        rply = '6'
    elif (block_num == 6):
        rply = '7'
    return rply


##############################################
def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server\n'))
    while True:
        data = str(connection.recv(2048), encoding='utf-8')
        sult = data.split(' ')
        # print(sult)
        reply = block_number(sult)

        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()


while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client,))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()
