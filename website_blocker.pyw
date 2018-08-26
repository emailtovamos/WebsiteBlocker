import time
from datetime import datetime as dt

hosts_temp=r"C:\Users\satya\python\Application3\hosts"
#hosts_temp="hosts"

hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
hosts_temp=hosts_path
redirect="127.0.0.1"
website_list=["www.bbc.com", "bbc.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,0) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23):
        print("Working Hours....")
        #with automatically takes care of closing and all. Don't have to worry about them!
        with open(hosts_temp,'r+') as file: #r+ means read and append. write function will just replace!
            content=file.read()
            for website in website_list:
                if website in content:
                    pass #if pass gets executed then else statement will not be executed
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hosts_temp,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

        print("Fun hours...")
    time.sleep(5)
