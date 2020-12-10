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

## Superhet


## SDR

převedu signál na na nižší frekvenci pomocí superhetu 


### DDC

**ant.**
<font color="red">--></font>
**BPF** 
<font color="red">--></font> 
**ADC** 
<font color="green">--></font> 
**DDC** 
<font color="green">--></font>
**CPU** 
<font color="green">--></font> 
**signal**

- BPF - filtr pro základní pásmo
- ADC - A/D převodník
- DDC - digitální směšovač (snižuje frekvenci nosné, posunuje ji o 90° a snižuje vzorkovací frekvenci)
- CPU - signálový procesor

**DCC**  
<img src="picture/dcc.png" alt="drawing" width="300"/><br>



### QSD

**ant.**
<font color="red">--></font> 
**BPF** 
<font color="red">--></font> 
**QSD** 
<font color="red">--></font> 
**ADC** 
<font color="green">--></font> 
**CPU** 
<font color="green">--></font> 
**signal**



- BPF - filtr pro základní pásmo
- QSD - analogový směšovač (snižuje frekvenci nosné, posunuje ji o 90° a snižuje vzorkovací frekvenci)
- ADC - A/D převodník
- CPU - signálový procesor
 
 
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
Všechno kromě páteřní sítě 

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
### Sváry
<img src="picture/svar.png" alt="drawing" width="500"/><br>
<br>

### svářečka
<img src="picture/svarecka.jpeg" alt="drawing" width="350"/><br>
<br>

### svařování
1. na vlákno nasadíme ochranu sváru.  
<img src="picture/svarovani-step1.png" alt="drawing" width="200"/><br>
<br>
2. pomocí kleští sundáme primární ochranu.   
<img src="picture/svarovani-step2.png" alt="drawing" width="200"/><br>
<br>
3. očistíme hadříkem namočením do izopropil alkoholu.  
<img src="picture/svarovani-step3.png" alt="drawing" width="200"/><br>
<br>
4. ulomíme konec vlákna na lámačce.  
<img src="picture/svarovani-step4.png" alt="drawing" width="200"/><br>
<br>
5. vlákna upneme do svářečky, po zaklapnutí se automaticky svaří.  
<img src="picture/svarovani-step5.png" alt="drawing" width="200"/><br>
<br>
6. na svár nasadíme ochranu a zapečeme.  
<img src="picture/svarovani-step6.png" alt="drawing" width="200"/><br>
<br>
7. opatrně zatáhneme za čerství svár pokud se neroztrhne je v pořádku.  
<img src="picture/svarovani-step7.png" alt="drawing" width="200"/><br>
<br>

## Konektory

Konektor na spojování optických vláken tvoří keramická ferule, ve které je uchyceno skleněné vlákno. Ferule je uchycena do plastového pouzdra, které zajištuje rovnání ferule vůči feruli na druhé straně.

### PC ferule

Konektor s označením **PC**  je většinou <font color="blue">**modrý**</font>, ale může mít i jinou jakoukoli barvu.
Ferule je plochá.

<img src="picture/PC_ferule.png" alt="drawing" width="250"/><br>
<br>

### APC ferule
Konektor s označením **APC** je vždy <font color="green">**zelený**</font> a takřka nikdy nemá jinou barvu.
Ferule je zkosená, aby deflektovala odražené světlo.  
<font color="red">**!!!**</font>
<font color="green">**Zelený**</font>
konektor se smí zapojovat jen do
<font color="green">**zeleného**</font>
konektoru, jinak se zničí
<span style="color:red">**!!!**</font>

<img src="picture/APC_ferule.png" alt="drawing" width="250"/><br>
<br>

### Typy konektorů
#### SC konektor
**SC** konektor je nepoužívanějším typem konektoru.  
<img src="picture/SC_konektor.png" alt="drawing" width="350"/>
<br>
<br>
<br>

#### LC konektor
**LC** konektor se většinou používá na zásuvných kartách v routrech a switčích.  
<img src="picture/LC_konektor.png" alt="drawing" width="350"/>
<br>
<br>
<br>

#### E2000 konektor   
**E2000** konektor se využívá na dálkových trasách díky jeho vysoké spolehlivosti.   
<img src="picture/E2000_konektor.png" alt="drawing" width="350"/><br>

## Spojky
# 24. Optika v datových centrech
# 25. Sítě NGA a NGN
