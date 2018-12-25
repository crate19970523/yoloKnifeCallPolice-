import threading
import time
from yolo import firstRun as yoloSet
from yolo import decectMydata
from transmissionServer import transmission
import os
def main():
        transmissionThread = threading.Thread(target = transmission)#建立傳輸伺服端執行緒
        transmissionThread.start()#傳輸伺服端執行緒開始
        yoloSet()#yolo初始化yolo設定
        while True:
        	if os.path.isfile('./imgtest/ltuschool.jpg'):
        		decectMydata()#開始辨識
        		if os.path.isfile('./imgtest/ltuschool.jpg'):
        			os.remove('./imgtest/ltuschool.jpg')
if __name__ == '__main__':
    main()