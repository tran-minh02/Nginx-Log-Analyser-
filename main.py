from collections import defaultdict
import time 
import itertools
ip = defaultdict(int)
path = defaultdict(int)
status_code = defaultdict(int)
user_agent = defaultdict(int)

def count(input_log):
    ip[lst[0]] += 1
    path[lst[1]] += 1
    status_code[lst[2]] += 1
    user_agent[lst[3]] += 1
    
def sort_dict(dict):
    return dict(sorted(dict.items(), key=lambda item: item[1], reverse=True))

def output(dic):
    for x in dict(itertools.islice(dic.items(), 5)):
        print(f"{x} - {dic[x]} requests")
        
with open("sample-nginx-log.txt", "r") as f:
    while True:
        try:
            input_line = f.readline().strip().split(" ")
            lst = [input_line[0],input_line[6],input_line[8]," ".join(input_line[11:])]
            count(lst)
        except IndexError as e : 
            # time.sleep(60)
            # continue
            break
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
    