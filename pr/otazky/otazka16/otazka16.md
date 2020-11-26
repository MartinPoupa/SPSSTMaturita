# 16. Referenční model OSI
## ISO/OSI
Referenční model **ISO/OSI** (Open Standart for Interconnection) se používá jako názorný příklad řešení komunikace v počítačových a telekomunikačních sítích pomocí vrstevnatého modelu, kde jsou jednotlivé vrstvy nezávislé a snadno nahraditelné.

### Pravidla OSI modelu
- Žádnou vrstvu nesmím vynechat
- Vrstvu mohu rozdělit do podvrstev

## Model OSI

|ČÍSLO|VRSTVA|JEDNOTKA DAT|POPIS|
|---|---|---|---|
|7\.|**Aplikační vrstva**|data|komunikace aplikací|
|6\.|**Prezentační vrstva**|data|má na starosti kódování zprávy
|5\.|**Relační vrstva**|data|má na starosti navázání, udržení a ukončení spojení|
|4\.|**Transportní vrstva**|segment|spojuje příjemce s odesílatelem|
|3\.|**Síťová vrstva**|paket|stará se o správný přenos po síti a spojuje uzly|
|2\.|**Linková vrstva**|rámec|vrstva starající se o bezchybný přenos na médiu|
|1\.|**Fyzická vrstva**|bity|spojení mezi dvěma body|

## Vrstvy od Šerýcha (Větičky) 

7\. **Aplikační vrstva** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; --> &nbsp; Vzájemnou komunikaci aplikací.  
6\. **Prezentační vrstva** &nbsp; --> &nbsp; Správná prezentace dat na koncovém systému.  
5\. **Relační vrstva** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; --> &nbsp; Stará se o zahájení, průběh a ukončení jednotlivých relací.  
4\. **Transportní vrstva** &nbsp; --> &nbsp; Transport dat s předem definovanými vlastnostmi.  
3\. **Síťová vrstva** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; --> &nbsp; Zajišťuje přenos mezi libovolnými systémy, nejdůležitější.  
2\. **Linková vrstva** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; --> &nbsp; Spolehlivý přenos mezi sousedními systémy.  
1\. **Fyzická vrstva** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; --> &nbsp; Přenos jednotlivých bitů a synchronizace.
