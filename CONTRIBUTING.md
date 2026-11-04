# Come contribuire

Grazie per voler arricchire la mappa. Bastano tre regole.

1. **Ogni dato ha una fonte pubblica.** Un link a un sito istituzionale, a un registro (RUNTS, CONI, Camera di commercio), a un atto o a un articolo di stampa.
2. **Solo dati in ruolo.** Per i referenti indica nome e ruolo come compaiono sulla fonte (presidente, dirigente, sindaco…). Email solo istituzionali o dell'ente. Mai numeri di cellulare personali, indirizzi di casa o informazioni sulla vita privata.
3. **Un ente per riga.** Gruppi di piccole realtà simili (per esempio le società sportive di un comune) possono stare in una riga sola.

## Proporre un ente senza toccare i file

Usa il pulsante *Proponi un ente* sulla mappa oppure apri una [nuova segnalazione](../../issues/new/choose). Chi cura il progetto la controlla e la aggiunge ai dati.

## Modificare `data/stakeholder.csv`

Puoi farlo dal browser: apri il file su GitHub, clicca sulla matita, aggiungi la riga e proponi la modifica (pull request). Il controllo automatico verifica che il file sia leggibile.

| Colonna | Cosa scrivere |
|---|---|
| `id` | Nuovo codice progressivo: `S` + tre cifre dopo l'ultimo esistente (es. `S185`) |
| `nome` | Nome ufficiale dell'ente |
| `categoria` | Numero e nome, es. `8. Terzo settore e associazioni culturali` (vedi elenco sotto) |
| `comune` | Uno o più dei 10 comuni, oppure `Regione`, `Area`, `Nazionale` |
| `descrizione` | Cosa fa, in una o due frasi |
| `rilevanza` | `Alta`, `Media` o `Bassa` per il coinvolgimento dei giovani e la gestione delle opere |
| `ruolo_nel_progetto` | Es. `Gatekeeper`, `Partner`, `Possibile gestore`, `Decisore`, `Fonte dati` |
| `opere_collegate` | Numeri delle opere (da `data/opere.csv`) separati da virgola, oppure vuoto |
| `contatti` | Sito, email o PEC dell'ente |
| `fonti` | Uno o più link separati da ` ; ` |
| `verifica` | `Verificato` o `Da verificare` |
| `referente`, `ruolo_referente` | Nome e ruolo pubblico, oppure `Da individuare` |
| `linkedin` | Pagina LinkedIn dell'ente o profilo pubblico professionale del referente |
| `email` | Email istituzionale o dell'ente |
| `fonte_referente` | Link alla fonte del nominativo |

### Categorie

1 Enti locali · 2 Governance d'area e sviluppo locale · 3 Regione Basilicata ed enti regionali · 4 Livello nazionale ed europeo · 5 Scuola e formazione · 6 Welfare e sanità · 7 Chiesa e realtà ecclesiali · 8 Terzo settore e associazioni culturali · 9 Sport e outdoor · 10 Patrimonio, cultura e ambiente · 11 Economia, lavoro e innovazione · 12 Università e ricerca

## Revisione

Chi cura il progetto controlla fonti e dati personali prima di unire una modifica. Le richieste di rimozione di dati personali hanno la precedenza su tutto il resto.
