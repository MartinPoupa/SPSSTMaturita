# 10. Pozemské spoje bod-bod

Spoj bod-bod je obousměrné bezdrátové propojení dvou bobů úzkým paprskem.
provozují se na frekvencích od 100 MHz do 300 GHz, jak v licenčních tak i v bez licenčních pásmech. 

Tyto spoje se často používají na propojení váleních stanic které jsou mimo infrastrukturu.

<img src="picture/bodbod.png" alt="drawing" width="500"/><br>

## Modulace
  - 2, 4-PSK
  - 256, 512, 1024-QAM 


## Výkonová bilance

![](https://latex.codecogs.com/svg.latex?\Large&space;P_P=P_V+G_V+G_P-L_S-L_N-L_{FSL})

![](https://latex.codecogs.com/svg.latex?\Large&space;P_V) výkon vysílače [dBm]

![](https://latex.codecogs.com/svg.latex?\Large&space;G_V) zisk vysílací antény [dBi]

![](https://latex.codecogs.com/svg.latex?\Large&space;G_P) zisk vysílací antény [dBi]

![](https://latex.codecogs.com/svg.latex?\Large&space;L_S) celkové stálé ztráty [dB]

![](https://latex.codecogs.com/svg.latex?\Large&space;L_N) celkové náhodné ztráty [dB]

![](https://latex.codecogs.com/svg.latex?\Large&space;L_{FSL})ztráty volným prostorem (Free Space Loss)

### Frenelova zóna
Prostor v kterém se šíří většina energie vysílání mezi body.

Vypadá jako párek.

![](https://latex.codecogs.com/svg.latex?\Large&space;b_1[m]=17,32({\frac{d_1d_2}{fd}})^{\frac{1}{2}}) 

<img src="picture/frenel.png" alt="drawing" width="400"/><br>

### Útlum
#### Šířením volným prostorem 
  Tento utlum záleží na frekvenci a vzdáleností vychází z Maksfelových rovnic.
  
  ![](https://latex.codecogs.com/svg.latex?\Large&space;L_{FSL}[db]=92.4+20log(d[km])+20log(f[Ghz]))
#### Hydrometeory
  je útlum způsobený počasím silný déšt, mlha a sněžení.

  tento útlum se odvíjí od podnebí v kterém se nachází spoj.

#### Rychlí únik
  Více vidové šíření. Signály jsou posunuté díky odrazům a nelinearitě atmosféry.
