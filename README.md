# ntp-server

用Python + NTP + Crondtab 實作的時間校正docekr模組<br>

功能 :
------
* 指定NTP server 
* 每10分鐘校正時間 , 校正的NTP server為上面變數所設定
* 參數設定集群IP , 可檢查整個集群的時間顯示在Log上
* BIOS的硬體時間可選擇要不要一起校正

運行:
------
進入docker-compose的資料夾

    docker-compose -f docker-compose.yml up -d
    
