# ntp-server

用Python + NTP + Crondtab 實作的時間校正docekr模組<br>

功能 :
------
* 指定NTP server 
* 每10分鐘校正時間 , 校正的NTP server為上面變數所設定
* 參數設定集群IP , 可檢查整個集群的時間顯示在Log上
* BIOS的硬體時間可選擇要不要一起校正

參數:
------
* NTP_CLUSTER_IP_LIST=集群每台節點的IP,以逗號分割
* NTP_NODE_USER=節點的登入用戶
* NTP_NODE_PASSWORD=節點的登入密碼
* SPECIFY_NTP_SERVER=指定要連的NTP server
* BIOS_TIME_CORRETCION=是否一起校正硬體BIOS時間 , 若要設為True ,不要設為False

運行:
------
進入docker-compose的資料夾

    docker-compose -f docker-compose.yml up -d
    
