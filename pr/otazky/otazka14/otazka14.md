# 14. Model telekomunikačního řetězce
## Teorie informace
    Informace -> Zpráva -> Signál
### Informace
- je nehmotná
- můžu určit její množství
- informaci dokážu přenášet (v prostoru x, y, z, t)
- maximální rychlost C (ve vakuu), přenáším informaci v čase a prostoru
- užitečné (informace jen o změně)
- nadbytečné (redundantní), (o ustáleném stavu, opakující se)
### Zpráva
- zhmotněná informace (třeba si něco zapíšu do sešitu)
- fyzikální podstata (akustické vlnění, el. proud, chemické vazby, optika…)
- abeceda :                   
  - diskrétní = digitálně skrz A/D převodník
  - spojitá = mluvení do mikrofonu
- kódování (gramatika, pravidla)
### Signál 
- zpráva, která se hodí k určitému přenosu
- přechod z jednoho signálu na druhý :
- změna abecedy
- změna fyzikální podstaty
- změna kódování
### Redundance
- Poměr užitečných informací vůči neužitečným
  - \- Zabírá místo			
  - \- Zvyšuje cenu
  - \+ Zvyšuje odolnost proti chybám
  
  
## Model telekomunikačního řetězce
co se zprávou musíme udělat, než ji pošleme po kanálu

    zdroj --> kodér zdroje --> kodér kanálu --> Kanál --> dekodér kanálu --> dekodér zdroje --> příjemce

### Kanál
- spojuje dvě místa
- přenáší signál
- drát, trubka, vzduch, optické vlákno…
- výhoda : spojuje dva body
- nevýhody : je drahý, dělá chyby, neumí přenést vše, omezená kapacita
### Kodér zdroje 
(komprese)
- má za úkol signál zkrátit (snižuje redundanci)
- zrychluje a zlevňuje komunikaci
- př. .zip, .rar, MPEG (.mpg, .mp3, .mp4)
### Kodér kanálu
- má za úkol signál přizpůsobit parametrům kanálu tak, aby dobře prošel
- zajištuje, aby signál prošel nezměněný kanálem
- př. RS-232, I²C, Ethernet II
### Mnohonásobný přenos kanálem
- **xDM**	(Division Multiplex)
- **xDMA**	(Division Multiple Access)
  - **SDMA**	(Space Division Multiple Access)
    - Rozdělení prostoru na různé oblasti
  - **FDMA**	(Frequency Division Multiple Access)
    - Rozdělení spektra na části (kanály)
  - **WDMA**	(Wave lenght Division Multiple Access)
    - Rozdělení spektra na části (kanály)
  - **TDMA**	(Time Division Multiple Access)
    - Nejpoužívanější
  - **CDMA**	(Code Division Multiple Access)
    - Pomocí kódování zprávy
    
    
## Komprese
### Ztrátová komprese
- nahradí nejméně potřebná data podobnými daty, která už jsou ve zprávě obsažena, ale ve větší váze -> ztratí část informace
- obrázek = snížení počtu barev, hudba = snížení vzorkovací frekvence
- příklad:
  - **jpg**
  - **mp3**
  
### Bezeztrátová komprese
- místo, aby věci opakovala, tak je jen popíše
- neztratí data, pouze je upraví, aby byla kratší
- příklad:
  - **rle**
  - **zip**
  - **rar**
  
### RLE
**RLE** je bezeztrátová komprese a má široké využití.  
Komprimuje tak, že kóduje posloupnosti stejných hodnot do dvojic (délka posloupnosti, hodnota). 

    AAAACDDCBBBBBCDABBDBCCCC --RLE--> 4AC2DC5BCDA2BDB4C

### JPEG
**JPEG** je ztrátová komprese používaná na obrázky.  

- Postup komprimace: 
  1. obrázek převedu do **YCbCr**
  2. Snížení přesnosti informací o barvě (blok: barva 16x16, jas 8x8)
  3. Složky obrázku jsou následně rozděleny do bloků a na každém bloku je provedena diskrétní transformace
  4. Provede se kvantizace (zde dochází k ztrátové kompresi)
  5. Zkomprimuje se pomocí bezeztrátové komprese **RLE** a použije se **Hufffmanovo kódování**
  
  

### MPEG 
MPEG je *Moving Picture Experts Group* komprese pro video a audio.  
- druh: 
  - **MPEG4** (video, DVB2)
  - **MPEG3** (nepoužívá se, byla zrušena)
  - **MPEG2** (DVD, DVB)
  - **MPEG1** (zvuk ,CD)
  
#### MPEG2
- Postup komprimace: 
  1. Stream se rozdělí do group, ty obsahují 12 frejmů  
  typy frejmů:
    - **I** - obrázek  .jpg
    - **P** - předvídání
    - **B** - bidirectional 
  2. frejmům se přisadí tip  
  v pořadí:
          I B B P B B P B B P B B
    
  
  
  
  
  
