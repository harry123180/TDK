import threading
import time
import serial

# 子執行緒，也就是你第二個需要執行的程式
def two_job():
	print('thread %s is running...' % threading.current_thread().name)
	for i in range(5):
		print("我是第二個程式：", i)
		time.sleep(0.5)
# 設定子執行緒
t = threading.Thread(target = two_job)
# 執行他
t.start()
print('thread %s is running...' % threading.current_thread().name)
# 這邊開始寫你主要程式碼的工作
for i in range(2):
	print("我是主要程式碼", i)
	time.sleep(1)
t.join()
print('thread %s is running...' % threading.current_thread().name)
print("Done.")