#coding:utf-8
import os
import time
import commands

print "-----------Starting to checking cluster node time----------------"
def identifyFileExist(filepath):
    if not os.path.exists(filepath):
        print filepath,'does not exists , stop testing........'
        exit(1)

env_load_file="/ntp-ansible/env.txt"
identifyFileExist(env_load_file)
f_jmx = open("%s"%env_load_file)
jmx_content=f_jmx.readline()
while jmx_content:
    if not jmx_content.find("NTP_CLUSTER_IP_LIST")==-1:
        list=jmx_content.split("=")[1]
        list=list.strip('\n')
    if not jmx_content.find("NTP_NODE_PASSWORD")==-1: 
        env_password=jmx_content.split("=")[1]
        env_password=env_password.strip('\n')
    if not jmx_content.find("NTP_NODE_USER")==-1:
        env_user=jmx_content.split("=")[1]
        env_user=env_user.strip('\n') 
    if not jmx_content.find("SPECIFY_NTP_SERVER")==-1:
        env_ntpserver=jmx_content.split("=")[1]
        env_ntpserver=jmx_content.split("=")[1]
    jmx_content=f_jmx.readline()

f_jmx.close()
os.system("/usr/sbin/ntpdate  -s " +env_ntpserver)
env_object = os.environ
#list = env_object.get('NTP_CLUSTER_IP_LIST')
#env_password = env_object.get('NTP_NODE_PASSWORD')
#env_user = env_object.get('NTP_NODE_USER')
cluster_number=list.count(",")+1
time.sleep(1)
print "Node number : "+ str(list.count(",")+1)
time.sleep(1)
os.system("rm -rf hosts-list")
os.system("rm -rf /root/.ssh/known_hosts")
os.system("rm -rf init-ssh.sh")
os.system("rm -rf init-ssh2.sh")
os.system("rm -rf result.txt")
time.sleep(2)
for item in range(0,cluster_number,1):
#    print item
    os.system("echo sshpass -p " + env_password + " ssh -o StrictHostKeyChecking=no " + env_user + "@" + list.split(",")[item] + " date >> init-ssh.sh" )
    os.system("echo sshpass -p " + env_password + " ssh -o StrictHostKeyChecking=no " + env_user + "@" + list.split(",")[item] + " ls -l /etc/localtime >> init-ssh2.sh" )
    os.system("echo sshpass -p " + env_password + " ssh -o StrictHostKeyChecking=no " + env_user + "@" + list.split(",")[item] + " 'ls -l /etc/localtime >> result.txt' >> init-ssh2.sh" )
    os.system("echo " + list.split(",")[item] + " ansible_connection=ssh ansible_ssh_pass="+ env_password + " ansible_ssh_user=" + env_user + " >>hosts-list")

result_file="/ntp-ansible/result.txt"
time.sleep(1)
os.system("touch "+result_file)
time.sleep(1)
os.system("chmod +x init-ssh.sh")
time.sleep(1)
os.system("./init-ssh.sh")
time.sleep(2)
os.system("chmod +x init-ssh2.sh")
time.sleep(1)
os.system("./init-ssh2.sh")
time.sleep(2)
f_result = open(result_file)
result_content=f_result.readline()
while result_content:
   contentdata = result_content.split("->")
#   os.system("sshpass -p " + env_password + " ssh -o StrictHostKeyChecking=no " + env_user + "@" + list.split(",")[item] + "ls  " + contentdata[1].strip('\n'))
   line=commands.getstatusoutput("sshpass -p " + env_password + " ssh -o StrictHostKeyChecking=no " + env_user + "@" + list.split(",")[item] + " ls  " + contentdata[1].strip('\n')) 
   if  line[1].find("No such file")==-1:
       print line[1] + " is existing , checking status : SUCCESS"
   else:
       print line[1] + " is lossing , checking status : Failed"
   result_content=f_result.readline()
f_result.close()

time.sleep(2) 
print "-----------Ending to checking cluster node time----------------"
