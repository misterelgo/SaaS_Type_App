#!/usr/bin/python3
import getpass
import sys
import docker
import os
client = docker.from_env()

if len (sys.argv) == 3:
    my_dockerfile = open("Dockerfile", "w")
    link = sys.argv[1]
    my_dockerfile.write(
                    "\nFROM ubuntu:latest"
                    "\nMAINTAINER Gora DIEYE <misterelgo@gmail.com>\n"
                    "\nENV TZ=Europe/Paris\n"
                    "\nRUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone\n"
                    "\nRUN apt-get update\n"
                    "\nRUN apt-get -y upgrade\n"
                    "\nRUN apt-get install -y git\n"
                    "\nRUN apt-get -y install apache2\n"
                    "\nRUN mkdir /var/www/html/app\n"                           
                    "\nRUN git clone "+link +" /var/www/html/app\n"
                    "\nENV APACHE_RUN_USER www-data\n"
                    "\nENV APACHE_RUN_GROUP www-data\n"
                    "\nENV APACHE_LOG_DIR /var/log/apache2\n"
                    "\nENV APACHE_LOCK_DIR /var/lock/apache2\n"
                    "\nENV APACHE_PID_FILE /var/run/apache2.pid\n"
                    "\nEXPOSE 80\n"
                    "\nCMD /usr/sbin/apache2ctl -D FOREGROUND")
    my_dockerfile.close()
    name = sys.argv[2]
    print("Start Building your docker image...")
    client.images.build(path = "./",tag = name)
    print("Image creation checking: "+name)
    print(client.images.get(name))
    if name:
    	print("deployed successfully!")

    os.system("docker login --username=misterelgo --password=rokhayalo")
    os.system("docker push "+name)

    """login = raw_input("Docker Hub id: ")
    password= getpass.getpass("Your password please: ")
    #print(password)
    print("start pushing your docker image to docker hub")
    client.login(username= login, password= password)"""
    for line in client.images.push(name, stream=True, decode=True):
    	print(line)
 
else:
	print ("Argument Error! Retry Please")

# python SaaS.py https://github.com/misterelgo/PHP-MySQL-CRUD-Web-Application.git misterelgo/saas