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
- Zprava která se hodí k určitému přenosu
- Přechod z jednoho signálu na druhý :
- Změna abecedy
- Změna fyzikální podstaty
- Změna kódování

### Redundance
- Poměr užitečných informací vůči neužitečným
  - \- Zabírá místo			
  - \- Zvyšuje cenu
  - \+ Zvyšuje odolnost proti chybám
  
## Model telekomunikačního řetězce
co se zprávou musíme udělat, než ji pošleme po kanálu


### Kanál
spojuje dvě místa
přenáší signál
drát, trubka, vzduch, optické vlákno…
výhoda : spojuje dva body
nevýhody : je drahý, dělá chyby, neumí přenést vše, omezená kapacita
### Kodér zdroje 
(komprese)
- má za úkol signál zkrátit (snižuje redundanci)
- zrychluje a zlevňuje komunikaci
- př. .zip, .rar, MPEG (.mpg, .mp3, .mp4)
### Kodér kanálu
- má za úkol signál přizpůsobit parametrům kanálu tak aby dobře prošel
- Zajištuje aby signál prošel nezměnění kanálem
- př. RS-232, I²C, Ethernet II
### Mnohonásobný přenos kanálem
- xDM	(Division Multiplex)
- xDMA	(Division Multiple Access)
  - SDMA	(Space Division Multiple Access)
    - Rozdělím prostor na různé oblasti
  - FDMA	(Frequency Division Multiple Access)
    - Rozdělení spektra na části (kanály)
  - WDMA	(Wave lenght Division Multiple Access)
    - Rozdělení spektra na části (kanály)
  - TDMA	(Time Division Multiple Access)
    - Nejpoužívanější
  - CDMA	(Code Division Multiple Access)
    - Pomocí kódování správy

## Komprese

### Ztrátová komprese
- nahradí nejméně potřebná data podobnými daty, která už jsou ve zprávě obsazena, ale ve větší váze -> ztratí část informace
- obrázek = snížení počtu barev, hudba = snížení vzorkovací frekvence
- příklad:
  - .jpg
  - .mp3
  
### Bezeztrátová komprese
- místo, aby věci opakovala, tak je jen popíše
- neztratí data, pouze je upraví, aby byla kratš
- příklad:
  - .zip
  - .rar

### MPEG 
DVB2 	MPEG2
DVB 	MPEG2

Stream -> 	gop(12 frejmů)
		typy 
		I - obrázek  .jpg
		P - předvídání
		B - bidirectional 

I fream - .jpg

Makro blok = 2x2 blok
Blok = 8x8 pixel
