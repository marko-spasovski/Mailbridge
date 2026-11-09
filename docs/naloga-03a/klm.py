#!/usr/bin/env python3
"""KLM napoved in primerjava z meritvami za nalogo 03a (MailBridge).

Zagon: python3 docs/naloga-03a/klm.py
Izpis je prilepljen v report.md. Ko dopolnite results-template.csv, skripto
zaženite znova in posodobite razdelek »Dopolniti po zbiranju podatkov«.
"""

import csv
from pathlib import Path

# Konstante (Card, Moran in Newell 1980; povprečen tipkar)
P = 1100  # Point: premik miške do cilja
C = 230   # Click: klik gumba miške
K = 280   # Keystroke: pritisk tipke
M = 1350  # Mental: miselna priprava (samo v razširjeni napovedi)

TO = "aplazl55@gmail.com"
SUBJECT = "Test"
BODY = "Pozdrav"
NAME = "Test"

# (korak, opis, P, C, K) ; vsaka vrstica je en logični korak (za M)
TASK1 = [
    ("1", "Klik na gumb »+« (Add an account) v stranski vrstici", 1, 1, 0),
    ("2", "Klik na »Gmail« v meniju", 1, 1, 0),
    ("3", "Google: klik na svoj račun (izbirnik računov)", 1, 1, 0),
    ("4", "Google: »Continue« na opozorilu o nepreverjeni aplikaciji", 1, 1, 0),
    ("5", "Google: potrditveno polje »Select all« (dovoljenja)", 1, 1, 0),
    ("6", "Google: »Continue« na zaslonu z dovoljenji", 1, 1, 0),
    ("7", "Klik na »New mail«", 1, 1, 0),
    ("8", f"Vnos prejemnika v polje To (fokus je že tam): »{TO}«", 0, 0, len(TO)),
    ("9", "Klik v polje Subject", 1, 1, 0),
    ("10", f"Vnos zadeve: »{SUBJECT}«", 0, 0, len(SUBJECT)),
    ("11", "Klik v polje za besedilo sporočila", 1, 1, 0),
    ("12", f"Vnos besedila: »{BODY}«", 0, 0, len(BODY)),
    ("13", "Klik na »Send«", 1, 1, 0),
]
# Logični koraki za M: tipkanje v polje šteje skupaj s klikom v to polje.
TASK1_MENTAL = 11

TASK2 = [
    ("1", "Klik na ikono zobnika (Settings) v zgornji vrstici", 1, 1, 0),
    ("2", "Klik v polje »Display name«", 1, 1, 0),
    ("3", "Ctrl+A (izbor obstoječega imena)", 0, 0, 2),
    ("4", f"Vnos imena: »{NAME}«", 0, 0, len(NAME)),
    ("5", "Klik na »Save«", 1, 1, 0),
]
TASK2_MENTAL = 4  # gumb Settings, polje, zamenjava imena (Ctrl+A + vnos), Save


def znaki(n):
    # Slovenska dvojina in množina: 1 znak, 2 znaka, 3–4 znaki, 5+ znakov
    r = n % 100
    return "znak" if r == 1 else "znaka" if r == 2 else "znaki" if r in (3, 4) else "znakov"


def table(name, steps, mental):
    print(f"### {name}\n")
    print("| Korak | Operacija | P | C | K | Čas (ms) |")
    print("|---|---|---:|---:|---:|---:|")
    tp = tc = tk = 0
    for step, text, p, c, k in steps:
        ms = p * P + c * C + k * K
        tp, tc, tk = tp + p, tc + c, tk + k
        print(f"| {step} | {text} | {p} | {c} | {k} | {ms} |")
    base = tp * P + tc * C + tk * K
    print(f"| **Skupaj** | | **{tp}** | **{tc}** | **{tk}** | **{base}** |\n")
    print(f"- Osnovni KLM (P, C, K): {tp} × {P} + {tc} × {C} + {tk} × {K} = **{base} ms = {base / 1000:.2f} s** (uradna napoved)")
    ext = base + mental * M
    print(f"- Razširjeno z {mental} × M ({M} ms): {base} + {mental * M} = {ext} ms = {ext / 1000:.2f} s\n")
    return base, ext


print("## Število znakov\n")
for label, s in [("To", TO), ("Subject", SUBJECT), ("Besedilo", BODY), ("Display name", NAME)]:
    print(f"- {label}: »{s}« = {len(s)} {znaki(len(s))}")
print("- Ctrl+A = 2 pritiska tipk (Ctrl in A)\n")

pred = {}
pred["1"] = table("Naloga 1: povezava Gmail in pošiljanje sporočila", TASK1, TASK1_MENTAL)
pred["2"] = table("Naloga 2: sprememba prikaznega imena v »Test«", TASK2, TASK2_MENTAL)

print("## Napoved in meritve\n")
print("| Udeleženec | Naloga | Izmerjeno (s) | KLM (s) | Razlika (s) | Razlika (%) | KLM+M (s) | Razlika do KLM+M (%) |")
print("|---|---|---:|---:|---:|---:|---:|---:|")
rows = list(csv.DictReader(open(Path(__file__).with_name("results-template.csv"), encoding="utf-8")))
measured = {"1": [], "2": []}
for r in rows:
    if not r["time_s"].strip() or r["time_s"].strip().upper() == "TODO":
        print(f"| {r['participant']} | {r['task']} | TODO | | | | | |")
        continue
    t = float(r["time_s"])
    if r["success"].strip().lower() == "da":
        measured[r["task"]].append(t)
    base, ext = (x / 1000 for x in pred[r["task"]])
    print(f"| {r['participant']} | {r['task']} | {t:.2f} | {base:.2f} | {t - base:+.2f} | {(t - base) / base * 100:+.1f} % | {ext:.2f} | {(t - ext) / ext * 100:+.1f} % |")

print("\n## Povprečja uspešnih izvedb\n")
for task, values in measured.items():
    if values:
        avg = sum(values) / len(values)
        print(f"- Naloga {task}: n = {len(values)}, povprečje = {avg:.2f} s")
    else:
        print(f"- Naloga {task}: še ni podatkov")
