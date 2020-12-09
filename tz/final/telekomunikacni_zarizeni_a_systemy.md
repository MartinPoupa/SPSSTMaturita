# 1. Telefonní přístroj – princip, druhy
# 2. Pobočková technika
# 3. Digitalizace telefonního signálu
# 4. Digitální spojování – články T a S
# 5. Signalizace ve spojovacích sítích
# 6. Přípojky ISDN
# 7. Přenosové systémy PCM, PDH a SDH
# 8. Legislativní podmínky provozu bezdrátových spojů
# 9. Komponenty bezdrátových systémů
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
 
 
# 11. Architektura mobilních sítí (GSM, GPRS, LTE)
# 12. Družicové systémy
# 13. Zdrojové kódování systému DVB
# 14. DVB–S, C kanálové kódování
# 15. DVB–T kanálové kódování
# 16. DAB/DAB+
# 17. Zdroje světla pro telekomunikační systémy
# 18. Detektory světla pro telekomunikační systémy
# 19. Optické systémy WDM
# 20. Modulační techniky a protokoly optických sítí
# 21. Páteřní optické sítě
# 22. Přístupové optické sítě – druhy a principy funkce
všechno krom páteřní sítě 

## PON
pasive optical network

### P2P
komunikace bod bod

      
    provider <------------> user


### P2MP
komunikace bod moc bodů

                  TDM              / <--> user
    provider <------------> splitter <--> user
                                   \ <--> user
# 23. Komponenty pro optické přístupové sítě

## Vlákna

## Sváry

## Konektory

Konektor na spojování optických vláken tvoří keramická ferule, v které je uchyceno skleněné vlákno. Ferule je uchycena do plastového pouzdra které zajištuje rovnání ferule vůči feruli na druhé straně.

### PC ferule

Konektor s označením **PC**  je většinou <span style="color:blue">**modrý**</span> ale může mít jakoukoli barvu.
Ferule je plochá.

<img src="picture/PC_ferule.png" alt="drawing" width="250"/><br>
<br>

### APC ferule
Konektor s označením **APC** je vždy <span style="color:green">**zelený**</span> a takřka nikdy nemá jinou barvu.
Ferule je zkosená, aby deflektovala odražené světlo.  
<span style="color:red">**!!!**</span>
<span style="color:green">**Zelený**</span>
konektor se smí zapojovat jen do
<span style="color:green">**zeleného**</span>
konektoru, jinak se zničí
<span style="color:red">**!!!**</span>

<img src="picture/APC_ferule.png" alt="drawing" width="250"/><br>
<br>

### Typy konektorů
#### SC konektor
**SC** konektor je nepoužívanějším tipem konektoru.
<img src="picture/SC_konektor.png" alt="drawing" width="350"/>
<br>
<br>
<br>

#### LC konektor
**LC** konektor se většinou používá na zásuvních kartách v routrech a switčích.  
<img src="picture/LC_konektor.png" alt="drawing" width="350"/>
<br>
<br>
<br>

#### E2000 konektor   
**E2000** konektor se využívá na dálkovích trasách díki jeho vysoké spolehlivosti.   
<img src="picture/E2000_konektor.png" alt="drawing" width="350"/><br>

## Spojky
# 24. Optika v datových centrech
# 25. Sítě NGA a NGN
