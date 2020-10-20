import serial  # 引用pySerial模組

COM_PORT = 'COM9'  # 指定通訊埠名稱
BAUD_RATES = 115200  # 設定傳輸速率
ser = serial.Serial(COM_PORT, BAUD_RATES)  # 初始化序列通訊埠

try:
    while True:
        while ser.in_waiting:  # 若收到序列資料…
            data = ser.readline().decode()  # 讀取一行
            #print(type(data))
            #print(ord(data))
            print(data)
            print(type(data))
            print('a')
            print(type('a'))
            if(data == data):
                print('do')
            #print('接收到的原始資料：', data_raw)
            #print('接收到的資料：', type(data))
            #print(int(data))

except KeyboardInterrupt:
    ser.close()  # 清除序列通訊物件
    print('再見！')