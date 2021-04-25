# 5. Signalizace ve spojovacích sítích

**Signalizace** (v telefonních sítích) je proces k sestavení a ukončení telefonního hovoru

Typy signalazice 
CAS - stejný kanál jako hovor
CCS - zvlášsní kanál

## Stavy Signalizace

1. klid - klid
2. obsazení (vyzvedneme telefon)
3. volba (natutáme číslo)
4. vyzvánění
5. hovor - klid
6. ukončení hovoru




## Přenašeč tipu U
typ CAS
analogová Signalizace
### Stavy 
klid - 48V, 0A <br> 
obsazení - stejnosměrný proud pokles V, teče 2OmA<br> 
volba - tónová nebo pulzní(pulzi 100 ms)<br> 
vyzvánění - střídavé napětí 50Hz/25Hz 75V<br> 
vyzvednutí - stejnosměrný proud pokles V, teče 2OmA<br>  
ukončení hovoru - 48V, 0A

## Signalizace DSS1 
typ CAS <br> 
digitální signalizace<br> 
DSS1 používá se na ISDN rozhraní.
### ISDN
zdroj
http://www.elearn.vsb.cz/archivcd/FEI/ISDN/isdn_text.pdf
#### Vrstvy 
1. fyzická - AMI
2. linková - HDLC
3. síťová - DSS1

### Stavba packetu

Protocol discriminator

### Stavy 
<img src="picture/DSS1.png" alt="drawing" width="300"/><br>


## Signalizace SS7
typ CCS
digitální Signalizace

### Dělení sítí
- NAT 0 - provider
- NAT 1 - stát
- INAT 0 - mezistátní (evropa, usa)
- INAT 1 - mezikontinettální (země)

### Typy ústředen
- SP
- STP 

zdroj
http://ozeas.sdb.cz/panska/3A/TS/vyuka/SS7/adoc.pub_signalizani-system-ss7.pdf


kubalík 


co to je, k čemu to slouží 

základní stavy signalizace ( klid, obsazení, volba, závěr, ......) 

přenašeč typu U 

signalizace DSS1 

signalizace SS7  

porovnání s modelem OSI 

popis signalizační sítě, úrovně, SP, STP  

MTP, TUP, ISUP, SCCP  vrstvi

popis průběhu signalizace při spojení účastníků   
