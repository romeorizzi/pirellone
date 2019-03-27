# Luci al Pirellone 

##### (Selezioni nazionali oii 2005 - Milano)
  
Il Pirellone è un noto grattacielo di Milano, in cui le
finestre sono disposte ordinatamente su M righe (piani) e
N colonne. Le righe sono numerate da 0 a M-1 (dall'alto in basso)
e le colonne da 0 a N-1 (da sinistra a destra).

Non tutti i dipendenti spengono la luce dei loro uffici, la sera prima
di uscire. Quindi alcune finestre rimangono illuminate e tocca al
custode provvedere a spegnerle.

Il custode non può entrare nei singoli uffici ma dispone di M+N interruttori speciali, con un funzionamento particolare.
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

### Funzioni

Per risolvere il problema, dovrai implementare le seguenti due funzioni.

#### `is_solvable(M, N, P[][])`

Questa funzione riceve in input una matrice `P` di `M` righe ed `N` colonne, dove ogni cella è uno `1` oppure un `0` a seconda se la luce di quella finestra sia originariamente accesa oppure spenta. La funzione dovrà restituire `1` nel caso il Pirellone assegnatole sia risolvibile, `0` altrimenti. 


#### `solve(M, N, P[][], switch_row(row), switch_col(col))`

Questa procedura computa e comunica al custode una sequenza di azioni utili allo spegnimento del Pirellone.
I grattacieli passati a questa funzione ammettono sempre una soluzione.
Analogamente a prima, `M` ed `N` indicano la dimensione del grattacielo, mentre `P` descrive la situazione iniziale di ciascuna finestra.
Per comunicare al custode le azioni da effettuare, devi avvalerti delle procedure di callback `switch_row(row)` e `switch_col(col)`,
che suggeriscono di agire sull'interruttore, rispettivamente di riga e di colonna, indicato.

Il tuo obbiettivo è chiamare queste funzioni per spegnere tutte le luci del Pirellone. Tuttavia queste funzioni non agiscono sulla copia del palazzo che ti è stata passata in locale col parametro `P`, ma comunicano meramente il tuo piano di spegnimento al custode, solo lui potrà agire sugli interruttori. Se vuoi puoi provvedere tu ad aggiornare il contenuto di `P`, la tua copia locale del palazzo, corrispondentemente ad ogni chiamata alle procedure di callback. Se vorrai optare per questa possibilità, ti suggeriamo allora di wrappare le chiamate alle due callback entro due funzioni che provvedano anche all'aggiornamento di `P`.    

**NB**: sebbene ti venga chiesto di implementare le funzioni in un singolo file, fra la valutazione di un goal e l'altro il
processo viene interrotto. Non funzionerà in sostanza definire variabili globali per condividere dati fra le 
due funzioni `is_solvable` e `solve` che sei chiamato ad implementare. 


### Goals 

Questo problema prevede i seguenti goal, obbiettivi che dovrai raggiungere:

- `decision_exponential`: decidere se il Pirellone sia spegnibile o meno, con M,N <= 10
- `solve_exponential`: qualora esista, dara una sequenza di mosse che spenga l'intero Pirellone, con M,N <= 10
- `decision_quadratic` e `solve_exponential`: rispettivamente come i primi due, ma con M,N <= 100
