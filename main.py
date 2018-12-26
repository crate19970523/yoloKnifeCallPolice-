import threading
import time
from yolo import firstRun as yoloSet
from yolo import decectMydata
from transmissionServer import transmission
import os
import GUI
def main():
    transmissionThread = threading.Thread(target = transmission)#建立傳輸伺服端執行緒
    transmissionThread.start()#傳輸伺服端執行緒開始
    yoloSet()#yolo初始化yolo設定
    print("初始化完成")
    while True:
        if os.path.isfile('imgtest/ltuschool.jpg'):
            anser=decectMydata()#開始辨識
            if(anser=="knife"):
               GUI.ui()
            print("辨識完成")
            if os.path.isfile('./imgtest/ltuschool.jpg'):
                os.remove('./imgtest/ltuschool.jpg')
if __name__ == '__main__':
    main()