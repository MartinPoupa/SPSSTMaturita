# 15. Síťové technologie


## Historie 
Model OSI vznikal tehdy, kdy se data posílala po telefonních kanálech.


## Členění modelu OSI 

### Horizontální dělení
Dělení na systémy  
Dva typy
- koncové systémy   (PC)
- mezilehlé systémy [občas se mohou chovat jako koncové systémy] (switch, router)

### Vertikální dělení
Dělení na vrstvy


#### Větičky
7\. **Aplikační vrstva** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; --> &nbsp; Vzájemnou komunikaci aplikací.  
6\. **Prezentační vrstva** &nbsp; --> &nbsp; Správná prezentace dat na koncovém systému.  
5\. **Relační vrstva** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; --> &nbsp; Stará se o zahájení, průběh a ukončení jednotlivých relací.  
4\. **Transportní vrstva** &nbsp; --> &nbsp; Transport dat s předem definovanými vlastnostmi.  
3\. **Síťová vrstva** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; --> &nbsp; Zajišťuje přenos mezi libovolnými systémy, nejdůležitější.  
2\. **Linková vrstva** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; --> &nbsp; Spolehlivý přenos mezi sousedními systémy.  
1\. **Fyzická vrstva** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; --> &nbsp; Přenos jednotlivých bitů a synchronizace.

## Tok data modelem  

### Enkapsulace a dekapsulace
N = číslo vrstvy
```
N + 1|            |PDU|                 |
-----|------------|---|-----------------|
N    |       {|PCI|SDU|PCI|} = PDU      |
-----|--------|-----------|-------------|
N - 1|   {|PCI|    SDU    |PCI|} = PDU  |
```
