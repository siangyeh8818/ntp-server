#!/bin/bash
#sed -i s"/<SPECIFY-NTP>/$SPECIFY_NTP_SERVER/g" /etc/ntp.conf 
#/usr/sbin/ntpd -p /var/run/ntpd.pid
env | grep NTP_CLUSTER_IP_LIST >> env.txt
env | grep NTP_NODE_USER >> env.txt
env | grep NTP_NODE_PASSWORD >> env.txt
env | grep SPECIFY_NTP_SERVER >> env.txt
crond
touch /var/log/cron.log
tail -f /var/log/cron.log -n 1
#python main.py
