# 10. Přijímače – superhet a SDR

## superhet


## SDR

převedu signál na na niší frekvenci pomocí superhetu 


### DDC

**ant.**  <span style="color:red">--></span> **BPF** <span style="color:red">--></span> **ADC** <span style="color:green">--></span> **DDC** <span style="color:green">--></span> **CPU** <span style="color:green">--></span> **signal**

- BPF - filtr pro základní pásmo
- ADC - A/D převodník
- DDC - digitální směšovač (snižuje nosnou, posunuje ji o 90° a snižuje vzorkovací frekvenci)
- CPU - signáloví procesor


<img src="picture/dcc.png" alt="drawing" width="300"/><br>
**DCC**


### QSD

**ant.**  <span style="color:red">--></span> **BPF**  <span style="color:red">--></span> **QSD**  <span style="color:red">--></span> **ADC** <span style="color:green">--></span> **CPU** <span style="color:green">--></span> **signal**

- BPF - filtr pro základní pásmo
- QSD - analogoví směšovač (snižuje nosnou, posunuje ji o 90° a snižuje vzorkovací frekvenci)
- ADC - A/D převodník
- CPU - signáloví procesor
 
 
