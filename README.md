# Costellazione Marmo Platano

Mappa aperta degli attori dell'**Area Interna Marmo Platano** (Basilicata): enti locali, scuole, terzo settore, sport, cultura, economia e istituzioni, con le 28 opere della strategia d'area *Futuro Dentro* (2021-2027).

I dieci comuni (Bella, Balvano, Baragiano, Castelgrande, Muro Lucano, Pescopagano, Rapone, Ruoti, Ruvo del Monte, San Fele) sono disposti secondo le coordinate reali. Ogni punto è un ente. Cliccandolo si aprono referente, contatti istituzionali, opere collegate e fonti.

Il progetto nasce dal lavoro dell'Osservatorio sulle Culture e le Politiche Giovanili (OCPG) dell'Università di Salerno nel progetto *Inserimento di risorse umane e task force specialistiche* (PN Capacità per la Coesione 2021-2027). È aperto: chiunque conosca il territorio può proporre enti mancanti o correggere quelli presenti.

**Mappa online:** https://angylla.github.io/costellazione-marmo-platano/

## Cosa contiene

| File | Contenuto |
|---|---|
| `data/stakeholder.csv` | Gli enti: categoria, comune, descrizione, rilevanza, ruolo nel progetto, opere collegate, contatti, fonti, referente |
| `data/opere.csv` | Le 28 operazioni della strategia *Futuro Dentro* (DGR 348/2026) |
| `data/comuni.csv` | Sindaci, popolazione, classe SNAI, ambito sociale, diocesi, scuole |
| `data/aree.csv` | Le 7 aree interne SNAI e le 2 aree urbane, con i comuni e le coordinate (la composizione e le scuole sono incorporate nella pagina) |
| `data/terziario.csv` | Università, AFAM, ITS e istituti superiori di formazione in Basilicata |
| `src/template.html` | La pagina della mappa (HTML, CSS e JavaScript, usa D3) |
| `tools/build.py` | Unisce dati e pagina in `dist/index.html` |

Le categorie degli enti sono numerate da 1 a 12 (vedi `CONTRIBUTING.md`).

## Come contribuire

Ci sono tre modi, dal più semplice al più tecnico.

1. **Dalla mappa:** il pulsante *Proponi un ente* (o *Segnala una correzione* nella scheda di un ente) apre un modulo già compilato su GitHub.
2. **Da GitHub:** apri una [nuova segnalazione](../../issues/new/choose) e scegli *Nuovo ente*, *Correzione* o *Rimozione / rettifica*.
3. **Modificando i dati:** cambia `data/stakeholder.csv` direttamente dall'interfaccia web di GitHub e apri una pull request.

Ogni proposta viene controllata da chi cura il progetto prima di essere pubblicata. Le regole sono in [CONTRIBUTING.md](CONTRIBUTING.md).

## Pubblicare la mappa (per chi cura il progetto)

1. Crea un repository pubblico su GitHub chiamato `costellazione-marmo-platano` e carica il contenuto di questa cartella.
2. In **Settings → Pages**, alla voce *Source* scegli **GitHub Actions**.
3. Ogni modifica a `data/` o `src/` ricostruisce e pubblica la mappa da sola (workflow `.github/workflows/pages.yml`). Il pulsante *Proponi un ente* si collega automaticamente al repository.
4. In **Settings → General → Features** lascia attive le *Issues*. Le etichette `nuovo`, `correzione` e `rimozione` vengono applicate dai moduli.

Per provarla sul tuo computer:

```bash
python3 tools/build.py --repo nome-utente/costellazione-marmo-platano
# poi apri dist/index.html nel browser
```

## Licenze

- **Codice** (`src/`, `tools/`, `.github/`): [MIT](LICENSE).
- **Dati** (`data/`): [Creative Commons Attribuzione 4.0 (CC BY 4.0)](LICENSE-DATA). Puoi riusarli citando: *Costellazione Marmo Platano, OCPG – Università di Salerno*.

## Dati personali

I nominativi dei referenti provengono da fonti pubbliche (siti istituzionali, registri, stampa) e sono riportati solo nel loro ruolo. Per chiedere la rettifica o la rimozione di un dato personale leggi [PRIVACY.md](PRIVACY.md).

## Fonti principali

Strategia d'area *Futuro Dentro* e 28 schede intervento; Regione Basilicata (PR FESR FSE+ 2021-27); Dipartimento per le politiche di coesione; anagrafe scuole del Ministero dell'Istruzione e del Merito (a.s. 2026/27); Registro unico nazionale del Terzo settore tramite Italia non profit; siti istituzionali dei Comuni; stampa locale. Ogni ente riporta le sue fonti specifiche. Ultimo controllo dei link: 19 ottobre 2026.
