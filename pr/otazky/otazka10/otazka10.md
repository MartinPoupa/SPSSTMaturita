# 10. Pozemské spoje bod-bod

Spoj bod-bod je obousměrné bezdrátové propojení dvou bodů úzkým paprskem.
Provozují se na frekvencích od 100 MHz do 300 GHz, jak v licenčních, tak i v bezlicenčních pásmech. 

Tyto spoje se často používají na propojení vzdálených stanic, které jsou mimo infrastrukturu.

<img src="picture/bodbod.png" alt="drawing" width="500"/><br>

## Modulace
  - 2, 4-PSK
  - 256, 512, 1024-QAM 


## Výkonová bilance

![](https://latex.codecogs.com/svg.latex?\Large&space;P_P=P_V+G_V+G_P-L_S-L_N-L_{FSL})

![](https://latex.codecogs.com/svg.latex?\Large&space;P_V) výkon vysílače [dBm]

![](https://latex.codecogs.com/svg.latex?\Large&space;G_V) zisk vysílací antény [dBi]

![](https://latex.codecogs.com/svg.latex?\Large&space;G_P) zisk přijímací antény [dBi]

![](https://latex.codecogs.com/svg.latex?\Large&space;L_S) celkové stálé ztráty [dB]

![](https://latex.codecogs.com/svg.latex?\Large&space;L_N) celkové náhodné ztráty [dB]

![](https://latex.codecogs.com/svg.latex?\Large&space;L_{FSL})ztráty volným prostorem (Free Space Loss)

### Fresnelova zóna
Prostor, ve kterém se šíří 60 % energie vysílané mezi body v **první** Fresnelově zóně.

Vypadá jako párek.

![](https://latex.codecogs.com/svg.latex?\Large&space;b_1[m]=17,32({\frac{d_1d_2}{fd}})^{\frac{1}{2}}) 

<img src="picture/frenel.png" alt="drawing" width="400"/><br>

### Útlum
#### Šířením volným prostorem 
  Tento útlum záleží na frekvenci a vzdálenosti. Vychází z Maxwellových rovnic.
  
  ![](https://latex.codecogs.com/svg.latex?\Large&space;L_{FSL}[db]=92.4+20log(d[km])+20log(f[Ghz]))
#### Hydrometeory
  Je útlum způsobený počasím - silný déšt, mlha a sněžení.

  Tento útlum se odvíjí od podnebí, ve kterém se nachází spoj.

#### Rychlý únik
  Vícevidové šíření. Signály jsou posunuté díky odrazům a nelinearitě atmosféry.
