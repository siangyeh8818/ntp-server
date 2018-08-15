#coding:utf-8
import os
import commands

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
    jmx_content=f_jmx.readline()

f_jmx.close()
env_object = os.environ
#list = env_object.get('NTP_CLUSTER_IP_LIST')
#env_password = env_object.get('NTP_NODE_PASSWORD')
#env_user = env_object.get('NTP_NODE_USER')
#print list
#print list.split(",")[0]
#print list.split(",")[1]
#print list.split(",")[2]
cluster_number=list.count(",")+1
print "-----------Starting to checking cluster node time----------------"
print "Node number : "+ str(list.count(",")+1)
os.system("rm -rf hosts-list")
os.system("rm -rf /root/.ssh/known_hosts")
os.system("rm -rf init-ssh.sh")
os.system("rm -rf init-ssh2.sh")
os.system("rm -rf result.txt")
for item in range(0,cluster_number,1):
#    print item
    os.system("echo sshpass -p " + env_password + " ssh -o StrictHostKeyChecking=no " + env_user + "@" + list.split(",")[item] + " date >> init-ssh.sh" )
    os.system("echo sshpass -p " + env_password + " ssh -o StrictHostKeyChecking=no " + env_user + "@" + list.split(",")[item] + " ls -l /etc/localtime >> init-ssh2.sh" )
    os.system("echo sshpass -p " + env_password + " ssh -o StrictHostKeyChecking=no " + env_user + "@" + list.split(",")[item] + " 'ls -l /etc/localtime >> result.txt' >> init-ssh2.sh" )
    os.system("echo " + list.split(",")[item] + " ansible_connection=ssh ansible_ssh_pass="+ env_password + " ansible_ssh_user=" + env_user + " >>hosts-list")

os.system("chmod +x init-ssh.sh")
os.system("./init-ssh.sh")
os.system("chmod +x init-ssh2.sh")
os.system("./init-ssh2.sh")

result_file="/ntp-ansible/result.txt"
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

#line = commands.getstatusoutput("ansible all -i hosts-list -m command -a 'ls -l /etc/localtime'")
#print line[1]
    
print "-----------Ending to checking cluster node time----------------"
