import requests
import socket
import os
import json
import subprocess
import psutil
import time
import logging

logging.basicConfig(
    level=logging.INFO,  # 设置日志级别
    format="%(asctime)s - %(levelname)s - %(message)s",  # 设置日志格式
    datefmt="%Y-%m-%d %H:%M:%S"  # 设置时间格式
)

def none_palyer():
    url = "http://localhost:8212/v1/api/players"
    payload={}
    headers = {
    'Accept': 'application/json',
    'Authorization': 'Basic QWRtaW46Um9idXN0MTIzNA=='
    }
    resp=requests.request("GET", url, headers=headers, data=payload)
    return resp.json()['players']
    
def shut_down():
    url = "http://localhost:8212/v1/api/shutdown"
    payload = json.dumps({
    "waittime": 5,
    "message": ""
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic QWRtaW46Um9idXN0MTIzNA=='
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.status_code

def wait_recv():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", 8211))
    sock.recvfrom(1024)
    sock.close()


def lauch_pal():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_program = os.path.join(script_dir, "PalServer.exe")
    subprocess.Popen(target_program, shell=True)  


running=False
while True:
    if running:
        count=0
        while count<10:
            if len(none_palyer())==0:
                count+=1
            else:
                count=0
            time.sleep(60)
        logging.info("检测到服务器无玩家，即将关闭服务器")
        shut_down()
        logging.info("服务器已关闭")
        running=False
    else:
        logging.info("监听连接中")
        wait_recv()
        logging.info("收到连接请求，正在启动服务器")
        lauch_pal()
        logging.info("服务器已启动")
        running=True
    time.sleep(10)
