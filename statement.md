Luci al Pirellone (Selezioni nazionali oii 2005 - Milano)
  
Il Pirellone è un noto grattacielo di Milano, in cui le
finestre sono disposte ordinatamente su M righe (piani) e
N colonne. Le righe sono numerate da 1 a M (dall'alto in basso)
e le colonne da 1 a N (da sinistra a destra).

Non tutti i dipendenti spengono la luce dei loro uffici, la sera prima
di uscire. Quindi alcune finestre rimangono illuminate e tocca al
custode provvedere a spegnerle.

Il custode non può entrare nei singoli uffici ma dispono di M+N interruttori speciali, con un funzionamento particolare.
Ci sono M interruttori di riga e N interruttori di colonna.
Quando il custode agisce sull'i-esimo interruttore di riga, tutte le luci accese
dell'i-esima riga si spengono ma, allo stesso tempo, quelle
spente si accendono! Analogamente alle righe, un interruttore di
colonna spegne le luci accese di quella colonna e accende quelle
spente.

Aiuta il custode a decidere quali degli M+N interruttori azionare al fine di spegnere tutte le luci delle finestre del Pirellone.
Data la configurazione iniziale di luci, il custode deve verificare se sia possibile spegnere le luci con gli interruttori
speciali e, in tal caso, deve specificare anche su quali interruttori
agire. Altrimenti, segnala la situazione di impossibilità.

Goal 1: decidere se il Pirellone sia spegnibile o meno, con M,N <= 10
Goal 2: qualora esista, dara una sequenza di mosse che spenga l'intero Pirellone, con M,N <= 10
Goal 3 e 4: come 1 e 2, ma con M,N <= 100
Goal 5 e 6: come 3 e 4, ma ora hai a disposizione solo O(M+N) memoria interna per condurre le operazioni
Goal 7 e 8: come 3 e 4, ma ora hai a disposizione solo O(1) memoria interna per condurre le operazioni, e la funzione che interroga lo stato di una cella può essere invocata la più una volta per cella.
Goal 9: come 8, ma devi essere superveloce ed interogare un minimo numero di celle. Tuttavia puoi ora assumere che il Pirellone sia spegnibile. 

