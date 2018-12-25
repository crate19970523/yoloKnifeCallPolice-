#coding:utf-8
from flask import request, Flask
import time
import os
app = Flask(__name__)

@app.route("/", methods=['POST'])
def get_frame():
    start_time = time.time()
    upload_file = request.files['file']
    old_file_name = upload_file.filename
    if upload_file:
        file_path = os.path.join('./imgtest/', old_file_name)   #Server端的存放位置
        upload_file.save(file_path)
        print ("success")
        if not os.path.isfile('imgtest/ltuschool.jpg'):
        	print('有近來喔')
        	os.rename('./imgtest/ltu.jpg','./imgtest/ltuschool.jpg')
        print('file saved to %s' % file_path)
        duration = time.time() - start_time
        print('duration:[%.0fms]' % (duration*1000))
        return 'success'
    else:
        return 'failed'
def transmission():
    app.run("192.168.43.179", port=5000)                #Server端的IP以及port

if __name__ == "__main__":
    transmission()