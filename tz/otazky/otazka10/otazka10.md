# 10. Přijímače – superhet a SDR

## Superhet

```
                 ^
                /
    ant. --> filtr --> směšovač --> filtr --> zesilovač --> detektor --> nz. frekvence
              /           ^  
                          |/
                         ozs 
                         /
                         
                         
                         
```                    




## SDR 

Převedu signál na na nižší frekvenci pomocí superhetu 

### Přijímač

#### DDC

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



#### QSD

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
 
 
### Vysílač

                      I | \
                   / -> |  >
                  /     | /
        cpu => D/A   
                  \   Q |
                   \ -> |
                        |
