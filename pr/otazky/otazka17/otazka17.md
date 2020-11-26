# 17. TCP/IP protocol stack


## Vrstvový model TCP/IP
|ČÍSLO|VRSTVA|JEDNOTKA DAT|PROTOKOLI|POPIS|
|---|---|---|---|---|
|7\.|**Aplikační vrstva**|data|HTTP, FTP, SSH, MQTT|komunikace aplikací|
|4\.|**Transportní vrstva**|segment|TCP, UDP|spojuje příjemce s odesílatelem|
|3\.|**Síťová vrstva**|paket|IP4/IP6, ICMP, IGMP|stará se o správný přenos po síti a spojuje uzly| 
|2\.|**Linková vrstva**|rámec|Ethernet, ARP|vrstva starající se o navázání správný a přenos na mediu|
|1\.|**Fyzická vrstva**|bity|UTP kabel, Optické vlákno, WIFI|spojení mezi dvěma body|


### Navazování spojení HTTP
|n.|protokol|odesílatel|příjemce|zprava|odpověď|
|---|---|---|---|---|---|
|1. | ARP | Apple_d1:12:b1    |Broadcast     |Who has 192.168.1.1 Tell 192.168.1.180| |
|2. | ARP | Routerbo_24:dd:ae |Apple_d1:12:b1|192.168.1.254 is at 64:d1:54:24:dd:ae|2.|
|3. | DNS | 192.168.1.180     |192.168.1.51  |Standard query 0xea2a A korona.panska.cz| | 
|4. | DNS | 192.168.1.51      |192.168.1.180 |Standard query response 0xea2a A korona.panska.cz A 217.195.162.33|3.|  
|5. | ARP | Apple_d1:12:b1    |Broadcast     |Who has 192.168.1.254 Tell 192.168.1.180| |
|6. | ARP | Routerbo_24:dd:ae |Apple_d1:12:b1|192.168.1.254 is at 64:d1:54:24:dd:ae|5.| 
|7. | TCP | 217.195.162.33    |217.195.162.33|64986 -> 80 [SYN]| |
|8. | TCP | 217.195.162.33    |192.168.1.180 |80 -> 64986 [SYN, ACK]|5.|
|9. | TCP | 92.168.1.180      |217.195.162.33|64986 -> 80 [ACK]|6.|
|10. | HTTP| 192.168.1.180     |217.195.162.33|GET / HTTP/1.1| |
|11. | TCP | 217.195.162.33    |192.168.1.180 |80 -> 64986 [ACK]|8.|
|12.| HTTP| 217.195.162.33    |192.168.1.180 |HTTP/1.1 200 OK (text/html)|8.|
|13.| TCP | 192.168.1.180     |217.195.162.33|64986 → 80 [ACK]|10.|
