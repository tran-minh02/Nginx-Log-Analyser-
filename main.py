from collections import defaultdict
import time 
import itertools
from tabulate import tabulate
import os , sys
import subprocess 

ip = defaultdict(int)
path = defaultdict(int)
status_code = defaultdict(int)
user_agent = defaultdict(int)
log_file_path = r"/var/log/nginx/access.log"

def check_file_part(log_part):
    if os.path.exists(log_part):
        return log_part
    else: 
        log_part = r"sample-nginx-log.txt"
        print("Đây là kết quả mẫu đến từ input của Roadmap.sh")
        return log_part

def check_nginx_service():       
    output = os.popen("systemctl is-active nginx").read().strip()
    if output == "active":
        pass
    else:
        print("Hệ thống không chạy máy chủ Nginx")
        # sys.exit()
    
def count(input_log):
    ip[input_log[0]] += 1
    path[input_log[1]] += 1
    status_code[input_log[2]] += 1
    user_agent[input_log[3]] += 1

def output(dic):
    header = [1,2]
    result = tabulate(list(itertools.islice(dic.items(), 5)), tablefmt="fancy_grid")
    print(result)

def monitor_log():
    check_nginx_service()
    log_file = check_file_part(log_file_path)
    with open(log_file, "r") as f:
        try: 
            while True:
                input_line = f.readline().strip().split(" ")
                lst = [input_line[0],input_line[6],input_line[8]," ".join(input_line[11:])]
                count(lst)
        except Exception as e :
            pass
    print('-------------------------------------------------')
    print("Top 5 IP addresses with the most requests:")
    output(ip)
    print('-------------------------------------------------')
    print("Top 5 most requested paths:")
    output(path)
    print('-------------------------------------------------')
    print("Top 5 response status codes:")
    output(status_code)
    print('-------------------------------------------------')
    print("Top 5 IP addresses with the most requests:")
    output(user_agent)
    print('-------------------------------------------------')
    
if __name__ == "__main__":
    monitor_log()