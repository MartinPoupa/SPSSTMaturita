# 18. Linková vrstva a ethernet

## Ethernet
- Síťová technologie (LAN)
- Nejrozšířenější síťová technologie
- Zabírá první a druhou vrstvu OSI
### Ethernet I
- Topologie: BUS (sběrnice)
- Richlost: 10Mbps
- Kabel: Koaxiální kabel s impedancí 50 Ω (max 500 m kabelu)
- Vznikl v letech  1972–1975 v laboratořích PARC firmy Xerox
### Ethernet II
- Topologie: Star
- Richlost: 100 Mbps, 1 Gbps, 10 Gbps
- Kabel: UTP kabel (CAT 5, CAT 5e, CAT 6 a CAT 7) (max 100 m kabelu)

## tipi zpráv
### unicast
### multicast
### broadcast



## Linková vrstva
### MAC adresa
Ethernetová MAC adresa se skládá ze 48 bitů nař. (01:23:45:67:89:ab)
MAC adresa se nemění a je svázaná s konkrétní síťovou kartou

### Rámec

- Ethernet II Rámec:
  | cílová mac adresa | zdrojová mac adresa |EtherType|data          |CRC          |  
  |:-----------------:|:-------------------:|:-------:|:------------:|:-----------:|  
  | 80 00 20 7A 3F 3E | 80 00 20 20 3A AE   | 08 00   | payload      | 00 20 20 3A | 
  | 6 bytů            | 6 bytů              |2 bytů   |46 - 1500 bytů|4 bytů       |  
  
## ARP protokol
