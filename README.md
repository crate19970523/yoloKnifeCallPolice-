辨識刀子的方法:
1.在下面網址下載yolo.h5  
https://drive.google.com/open?id=1Ac0d6wx8_Ud_Do5qPKLm8IN5F1c6NyRV  
2.將下載下來的檔案放在model_data裡  
3.執行main.py檔案  
P.S. yolo.py用在辨識的部分、transmissionServer.py檔是SARVER
  ****
訓練方法:  
1.先將要訓練的照片放在VOCdevkit\VOC2007\JPEGImages  
2.利用labelImg將照片上標籤XML檔放在VOCdevkit\VOC2007\Annotations  
註:labelImg可參考https://tw.openrobot.club/article/index?sn=10976 (非我做的網站)  
3.執行VOCdevkit\VOC2007裡的make_main_txt.py  
4.執行voc_annotation.py  
5.在命令提示字元輸入python convert.py -w yolov3.cfg yolov3.weights model_data/yolo_weights.h5  
6.執行train.py  
  ****
辨識開始方式:  
1.修改model_data資料夾中的my_classes將自己用到的名稱打在裡面，一行一個  
2.修改yolo.py檔中的model_path改成logs/000/trained_weights_final.h5  
3.修改yolo.py檔中的classes_path改成model_data/my_classes.txt  
4.修改yolo.py檔中第220行的path = 'imgtest/LTU.jpg'改成要辨識的圖片的位置  
5.修改yolo.py檔中的229行的if(anser=='knife'):判斷式將knife改成要判斷的東西名稱  
6.第五點的判斷式的下面修改成判斷後要做的事情  
  ****
注意:目前該方法辨識率較低目前正在嘗試新的方法