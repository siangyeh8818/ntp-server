FROM siangyeh8818/python-base-environment:3.6

RUN yum -y install ntp net-tools ansible openssh* crontabs.noarch
RUN mkdir -p /ntp-ansible
WORKDIR /ntp-ansible 
COPY hosts-list /ntp-ansible 
#COPY run-ans.sh /ntp-ansible
#RUN chmod +x run-ans.sh
COPY inspect-ntp.py /ntp-ansible
RUN chmod +x /ntp-ansible/inspect-ntp.py
COPY crondfile /etc/cron.d/
RUN chmod 0644 /etc/cron.d/crondfile
COPY ntp.conf /etc/
COPY docker-entrypoint.sh /ntp-ansible
#COPY cron_job.sh /ntp-ansible
#RUN chmod +x /ntp-ansible/cron_job.sh
RUN chmod +x /ntp-ansible/inspect-ntp.py
COPY main.py /ntp-ansible
CMD ["bash","/ntp-ansible/docker-entrypoint.sh"]
