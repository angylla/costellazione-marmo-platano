#!/usr/bin/env python3
"""Costruisce la mappa (dist/index.html) a partire dai CSV in data/.

Uso:  python3 tools/build.py [--repo nome-utente/nome-repo]
Il parametro --repo (o la variabile d'ambiente GITHUB_REPOSITORY) attiva
il pulsante "Proponi un ente", che apre un modulo su GitHub Issues.
Nessuna dipendenza esterna: solo la libreria standard di Python 3.8+.
"""
import csv, json, os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
AREA = ["Bella", "Balvano", "Baragiano", "Castelgrande", "Muro Lucano",
        "Pescopagano", "Rapone", "Ruoti", "Ruvo del Monte", "San Fele"]
CATEGORIE = {1: "Enti locali", 2: "Governance d'area e sviluppo locale", 3: "Regione Basilicata ed enti regionali",
             4: "Livello nazionale ed europeo", 5: "Scuola e formazione", 6: "Welfare e sanità",
             7: "Chiesa e realtà ecclesiali", 8: "Terzo settore e associazioni culturali", 9: "Sport e outdoor",
             10: "Patrimonio, cultura e ambiente", 11: "Economia, lavoro e innovazione", 12: "Università e ricerca"}


def rows(name):
    with open(DATA / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def num(s):
    try:
        return float(s)
    except (TypeError, ValueError):
        return 0


def categoria(v):
    m = re.match(r"\s*(\d+)", v or "")
    if m:
        return int(m.group(1))
    for k, n in CATEGORIE.items():
        if n.lower() == (v or "").strip().lower():
            return k
    raise ValueError(f"Categoria non riconosciuta: {v!r} (usa un numero da 1 a 12)")


def stakeholder():
    out, errors = [], []
    for i, r in enumerate(rows("stakeholder.csv"), start=2):
        try:
            c = categoria(r["categoria"])
        except ValueError as e:
            errors.append(f"stakeholder.csv riga {i}: {e}"); continue
        if not r["id"] or not r["nome"]:
            errors.append(f"stakeholder.csv riga {i}: id e nome sono obbligatori"); continue
        com = r["comune"]
        cs = [x for x in AREA if re.search(r"\b" + x + r"\b", com, re.I)]
        lv = None
        if not cs:
            cl = com.lower()
            lv = ("AREA" if any(k in cl for k in ["area", "10 comuni", "ambito", "7 comuni", "vari"])
                  else "NAZ" if any(k in cl for k in ["nazionale", "roma"]) else "REG")
        ops = [] if r["opere_collegate"].strip() == "tutte" else [int(x) for x in re.findall(r"\d+", r["opere_collegate"]) if 1 <= int(x) <= 28]
        parts = [p.strip() for p in re.split(r"\s;\s", r["fonti"]) if p.strip() and p.strip() != "-"]
        out.append(dict(id=r["id"], n=r["nome"], c=c, cn=CATEGORIE[c], com=com, d=r["descrizione"], r=r["rilevanza"] or "Media",
                        ro=r["ruolo_nel_progetto"], o=ops, ct="" if r["contatti"] in ("-", "") else r["contatti"],
                        f=[p for p in parts if p.startswith("http")], fn=[p for p in parts if not p.startswith("http")],
                        v=r["verifica"], cs=cs, lv=lv, rf=r["referente"], rr=r["ruolo_referente"], li=r["linkedin"],
                        em=r["email"], rs=r["fonte_referente"]))
    ids = [s["id"] for s in out]
    dup = {x for x in ids if ids.count(x) > 1}
    if dup:
        errors.append("id duplicati in stakeholder.csv: " + ", ".join(sorted(dup)))
    return out, errors


def main():
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    if "--repo" in sys.argv:
        repo = sys.argv[sys.argv.index("--repo") + 1]
    S, errors = stakeholder()
    if errors:
        print("Errori nei dati:\n  " + "\n  ".join(errors)); sys.exit(1)
    O = [dict(n=int(r["n"]), com=r["comune"], t=r["titolo"], e=num(r["importo_eur"]), u=r["ufficio_regionale"],
              a=r["ambito"], p=r["pertinenza"]) for r in rows("opere.csv")]
    C = [dict(n=r["comune"], s=r["sindaco"], l=r["lista"], ab=int(num(r["abitanti_2026"])), snai=r["classe_snai"],
              amb=r["ambito_sociale"], dio=r["diocesi"], sc=r["scuole"]) for r in rows("comuni.csv")]
    U = [dict(n=r["nome"], t=r["tipo"], sd=r["sede"], d=r["dettagli"], st=r["studenti"], w=r["sito"], f=r["fonte"],
              rf=r["referente"], rr=r["ruolo_referente"], li=r["linkedin"], em=r["email"], rs=r["fonte_referente"]) for r in rows("terziario.csv")]
    data = json.dumps(dict(S=S, O=O, C=C, U=U), ensure_ascii=False).replace("</", "<\\/")
    html = (ROOT / "src" / "template.html").read_text(encoding="utf-8")
    html = html.replace("__DATA__", data).replace("__REPO__", repo)
    (ROOT / "dist").mkdir(exist_ok=True)
    (ROOT / "dist" / "index.html").write_text(html, encoding="utf-8")
    (ROOT / "dist" / "costellazione.json").write_text(json.dumps(dict(S=S, O=O, C=C, U=U), ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"OK: {len(S)} enti, {len(O)} opere, {len(C)} comuni, {len(U)} istituzioni terziarie -> dist/index.html")


if __name__ == "__main__":
    main()
