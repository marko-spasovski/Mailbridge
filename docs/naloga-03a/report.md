# Naloga 03a: Čas izvedbe naloge (priprava na zbiranje podatkov)

**Predmet:** Vrednotenje uporabniške izkušnje, UM FERI
**Ekipa:** Marko Spasovski, Anže Plazl
**Aplikacija:** MailBridge – https://mailbridge-og1u.onrender.com/
**Rok oddaje:** torek, 10. 11. 2026, ob 17.00

MailBridge je spletni poštni odjemalec, ki v en nabiralnik združi račune Outlook in Gmail.

---

## 1. del: Primera uporabe

Pri obeh nalogah je udeleženec že prijavljen in začne na strani z nabiralnikom. Prijava in registracija nista del primera uporabe. Celotna navodila za udeleženca so v ločenih dokumentih `navodila-naloga-1.md` in `navodila-naloga-2.md`.

Koraki in oznake so preverjeni v izvorni kodi vmesnika (`public/js/core.js`, `mail.js`, `settings.js`, `public/*.html`) in na strežniku (`src/modules/accounts/accounts.routes.ts`, `src/integrations/gmail/provider.ts`). Vmesnik je v angleščini, zato so oznake gumbov navedene v izvirniku.

### 1.1 Naloga 1: Povezava računa Gmail in pošiljanje sporočila

**Navodilo za udeleženca:** »V MailBridge povežite svoj račun Gmail. Nato z njega pošljite sporočilo na naslov aplazl55@gmail.com z zadevo »Test« in besedilom »Pozdrav«.«

| Korak | Dejanje | Alternativa |
|---|---|---|
| 1 | Klik na »+« (»Add an account«) v razdelku »Accounts« v stranski vrstici | **1.a** »Settings« (zobnik) ali »Account menu« → »Profile and accounts« → »Mail accounts« → »Add Gmail«; **1.b** v praznem nabiralniku gumb »Connect Gmail« |
| 2 | Klik na »Gmail« v meniju | – |
| 3 | Google: izbira računa | **3.a** vnos e-naslova in gesla, če uporabnik ni prijavljen v Google |
| 4 | Google: »Continue« na opozorilu »Google hasn't verified this app« | – |
| 5 | Google: »Select all« in »Continue« na zaslonu z dovoljenji | **5.a** brez vseh dovoljenj za Gmail povezava ne uspe (»Allow every requested Gmail permission …«) → začetek znova |
| 6 | Vrnitev v MailBridge, obvestilo »Account connected. Syncing your mail…« | – |
| 7 | Klik na »New mail« (kurzor je v polju »To«, »From« je novi račun) | – |
| 8 | Vnos prejemnika | – |
| 9 | Klik v »Subject«, vnos »Test« | **9.a** premik s tipko Tab |
| 10 | Klik v polje za besedilo, vnos »Pozdrav« | **9.a** premik s tipko Tab |
| 11 | Klik na »Send« | **11.a** prazno polje → sporočilo »Add a recipient, a subject and a message.« |
| 12 | Obvestilo »Message sent.« – konec | – |

### 1.2 Naloga 2: Sprememba prikaznega imena v »Test«

**Navodilo za udeleženca:** »Svoje prikazno ime v profilu spremenite v »Test« in spremembo shranite.«

| Korak | Dejanje | Alternativa |
|---|---|---|
| 1 | Klik na zobnik (»Settings«) v zgornji vrstici | **1.a** »Account menu« (slika ali začetnice) → »Profile and accounts« |
| 2 | Klik v polje »Display name« (vnaprej izpolnjeno s trenutnim imenom) | – |
| 3 | Ctrl+A (označi obstoječe ime) | **3.a** brisanje s tipko Backspace |
| 4 | Vnos »Test« | – |
| 5 | Klik na »Save« | **5.a** Enter v polju |
| 6 | Obvestilo »Profile saved.« – konec | – |

### 1.3 Popravki prvotnih osnutkov

Pri preverjanju vmesnika v kodi smo popravili naslednje:

1. **Naloga 2, KLM:** prvotna tabela je mešala obe vstopni poti (zobnik in »Account menu« → »Profile and accounts«). Gumb z zobnikom vodi neposredno na `settings.html`, zato klik na »Profile and accounts« spada samo v alternativno pot 1.a. KLM zdaj šteje samo glavno pot.
2. **Naloga 2:** polje »Display name« je vnaprej izpolnjeno s trenutnim imenom (`value: user.displayName ?? ''`). Uporabnik mora staro ime najprej označiti (Ctrl+A) ali izbrisati, zato je ta korak dodan.
3. **Naloga 1:** v okno »New message« kurzor samodejno skoči v polje »To«, zato klik v to polje ni potreben.
4. **Naloga 1:** po vrnitvi z Googla je novi račun izbran in je samodejno nastavljen v polju »From«. Izbira pošiljatelja zato ni korak.
5. **Naloga 1:** dodani sta resnični alternativi 1.a (»Add Gmail« v nastavitvah) in 1.b (»Connect Gmail« v praznem nabiralniku).
6. **Naloga 1:** aplikacija od Googla zahteva `prompt=consent select_account`. Google zato vedno prikaže izbiro računa in zaslon z dovoljenji, tudi če je uporabnik prijavljen v en sam Google račun.
7. **Obe nalogi:** aplikacija nima bližnjic na tipkovnici za pisanje sporočila, nastavitve ali dodajanje računa (puščice delujejo samo v seznamu sporočil in menijih).

---

## 2. del: Metoda merjenja in analitika

### 2.1 Merjenje s štoparico

Čas merimo ročno s štoparico na mobilnem telefonu. Meritve izvedemo **med terminom vaj**, kot zahteva naloga pri uporabi štoparice.

- **Vloge:** en član ekipe meri čas in beleži opažanja, udeleženec izvaja nalogo. Izvajalec med nalogo ne pomaga.
- **Priprava:** udeleženec prebere navodilo in pove, da je pripravljen. Pred začetkom je odprta stran z nabiralnikom (`app.html`), na kateri je udeleženec že prijavljen.
- **Začetek:** štoparico sprožimo, ko izvajalec reče »Zdaj« in udeleženec prvič premakne miško.
- **Konec:** štoparico ustavimo, ko se prikaže potrditveno obvestilo: pri nalogi 1 »Message sent.«, pri nalogi 2 »Profile saved.«.
- **Uspeh:** naloga je uspešna, če se prikaže potrditveno obvestilo s pravilnimi podatki (pri nalogi 1 prejemnik aplazl55@gmail.com, zadeva »Test« in besedilo »Pozdrav«; pri nalogi 2 ime »Test«). Neuspešna je, če udeleženec odneha ali potrebuje pomoč.
- **Napaka:** vsak zgrešen ali nepotreben korak (npr. napačen meni, obvestilo o napaki, ponovni začetek povezave), ki ga izvajalec zabeleži.
- **Anonimnost:** rezultati se beležijo samo z oznakami P1–P4. Imena udeležencev niso povezana z rezultati.

### 2.2 Microsoft Clarity

Za zbiranje podatkov o sejah uporabljamo **Microsoft Clarity** (projekt `zb5jhevix7`, nastavljen **09. 11. 2026**).

Kaj smo naredili:

1. Dodali smo datoteko `public/js/analytics.js` s standardno kodo Clarity, ki naloži skripto `https://www.clarity.ms/tag/zb5jhevix7` in pripravi čakalno vrsto `window.clarity`.
2. Na vseh straneh (`index`, `register`, `forgot`, `reset`, `app`, `settings`) smo skripto vključili pred `core.js`.
3. **Razširili smo pravilnik CSP (Content-Security-Policy).** MailBridge ima strog CSP, ki blokira vrinjene (inline) skripte, zato standardne kode Clarity ni bilo mogoče prilepiti neposredno v HTML. Koda je zato v zunanji datoteki, v CSP pa smo dovolili samo domene Clarity:
   - `script-src`: `https://www.clarity.ms https://*.clarity.ms`
   - `img-src` in `connect-src`: `https://*.clarity.ms https://c.bing.com`

   `'unsafe-inline'` nismo dodali, čeprav ga primer v dokumentaciji Clarity vsebuje, ker bi z njim CSP izgubil zaščito pred vrinjenimi skriptami (XSS). Okvir za prikaz vsebine sporočil ima svoj ločen CSP, ki ostaja nespremenjen.

Clarity začne zbirati podatke šele, ko je sprememba objavljena na Renderju. Podatki se v nadzorni plošči Clarity prikažejo z zamikom do 2 ur. Podatkov iz Clarity v tem poročilu še ni.

### 2.3 Predloga za rezultate

Rezultati se vpisujejo v `results-template.csv`.

| Udeleženec | Naloga | Čas (s) | Uspeh | Napake | Opombe |
|---|---|---|---|---|---|
| P1 | 1 | | | | |
| P1 | 2 | | | | |
| P2 | 1 | | | | |
| … | … | | | | |

---

## 3. del: Napoved s KLM in primerjava

### 3.1 Metoda

Čas uspešne izvedbe napovemo z modelom KLM (Keystroke-Level Model). Upoštevamo samo glavno (uspešno) pot, brez alternativ. Konstante so za povprečnega tipkarja (Card, Moran in Newell 1980):

| Operator | Pomen | Čas |
|---|---|---|
| P (Point) | premik miške do cilja | 1.100 ms |
| C (Click) | klik gumba miške | 230 ms |
| K (Keystroke) | pritisk tipke | 280 ms |
| M (Mental) | miselna priprava (samo razširjena napoved) | 1.350 ms |

**Uradna napoved** je osnovni KLM z operatorji P, C in K. Razširjena napoved z enim operatorjem M na logični korak je dodana za primerjavo. Operatorja H (premik roke med miško in tipkovnico) in čakanja na sistem (R) ne upoštevamo. Velike črke in znak »@« štejemo kot en pritisk, ne kot dva (Shift + tipka).

Vse vrednosti so izračunane s skripto `klm.py` (zagon: `python3 docs/naloga-03a/klm.py`). Spodaj je njen nespremenjen izpis.

### 3.2 Izpis skripte

```text
## Število znakov

- To: »aplazl55@gmail.com« = 18 znakov
- Subject: »Test« = 4 znaki
- Besedilo: »Pozdrav« = 7 znakov
- Display name: »Test« = 4 znaki
- Ctrl+A = 2 pritiska tipk (Ctrl in A)
```

#### Naloga 1: povezava Gmail in pošiljanje sporočila

| Korak | Operacija | P | C | K | Čas (ms) |
|---|---|---:|---:|---:|---:|
| 1 | Klik na gumb »+« (Add an account) v stranski vrstici | 1 | 1 | 0 | 1330 |
| 2 | Klik na »Gmail« v meniju | 1 | 1 | 0 | 1330 |
| 3 | Google: klik na svoj račun (izbirnik računov) | 1 | 1 | 0 | 1330 |
| 4 | Google: »Continue« na opozorilu o nepreverjeni aplikaciji | 1 | 1 | 0 | 1330 |
| 5 | Google: potrditveno polje »Select all« (dovoljenja) | 1 | 1 | 0 | 1330 |
| 6 | Google: »Continue« na zaslonu z dovoljenji | 1 | 1 | 0 | 1330 |
| 7 | Klik na »New mail« | 1 | 1 | 0 | 1330 |
| 8 | Vnos prejemnika v polje To (fokus je že tam): »aplazl55@gmail.com« | 0 | 0 | 18 | 5040 |
| 9 | Klik v polje Subject | 1 | 1 | 0 | 1330 |
| 10 | Vnos zadeve: »Test« | 0 | 0 | 4 | 1120 |
| 11 | Klik v polje za besedilo sporočila | 1 | 1 | 0 | 1330 |
| 12 | Vnos besedila: »Pozdrav« | 0 | 0 | 7 | 1960 |
| 13 | Klik na »Send« | 1 | 1 | 0 | 1330 |
| **Skupaj** | | **10** | **10** | **29** | **21420** |

- Osnovni KLM (P, C, K): 10 × 1100 + 10 × 230 + 29 × 280 = **21420 ms = 21.42 s** (uradna napoved)
- Razširjeno z 11 × M (1350 ms): 21420 + 14850 = 36270 ms = 36.27 s

#### Naloga 2: sprememba prikaznega imena v »Test«

| Korak | Operacija | P | C | K | Čas (ms) |
|---|---|---:|---:|---:|---:|
| 1 | Klik na ikono zobnika (Settings) v zgornji vrstici | 1 | 1 | 0 | 1330 |
| 2 | Klik v polje »Display name« | 1 | 1 | 0 | 1330 |
| 3 | Ctrl+A (izbor obstoječega imena) | 0 | 0 | 2 | 560 |
| 4 | Vnos imena: »Test« | 0 | 0 | 4 | 1120 |
| 5 | Klik na »Save« | 1 | 1 | 0 | 1330 |
| **Skupaj** | | **3** | **3** | **6** | **5670** |

- Osnovni KLM (P, C, K): 3 × 1100 + 3 × 230 + 6 × 280 = **5670 ms = 5.67 s** (uradna napoved)
- Razširjeno z 4 × M (1350 ms): 5670 + 5400 = 11070 ms = 11.07 s

#### Napoved in meritve

| Udeleženec | Naloga | Izmerjeno (s) | KLM (s) | Razlika (s) | Razlika (%) | KLM+M (s) | Razlika do KLM+M (%) |
|---|---|---:|---:|---:|---:|---:|---:|
| P1 | 1 | 38.87 | 21.42 | +17.45 | +81.5 % | 36.27 | +7.2 % |
| P1 | 2 | 7.12 | 5.67 | +1.45 | +25.6 % | 11.07 | -35.7 % |
| P2 | 1 | TODO | | | | | |
| P2 | 2 | TODO | | | | | |
| P3 | 1 | TODO | | | | | |
| P3 | 2 | TODO | | | | | |
| P4 | 1 | TODO | | | | | |
| P4 | 2 | TODO | | | | | |

```text
## Povprečja uspešnih izvedb

- Naloga 1: n = 1, povprečje = 38.87 s
- Naloga 2: n = 1, povprečje = 7.12 s
```

*Opomba: skripta izpisuje decimalno piko. Povprečje pri n = 1 je samo meritev P1 in še ni povprečje skupine.*

### 3.3 Povzetek napovedi

| Naloga | Uradna napoved KLM | Razširjena (KLM + M) |
|---|---|---|
| 1 – Gmail in pošiljanje | **21,42 s** (21.420 ms) | 36,27 s (36.270 ms) |
| 2 – prikazno ime | **5,67 s** (5.670 ms) | 11,07 s (11.070 ms) |

### 3.4 Pilotni rezultati

| Udeleženec | Naloga | Čas (s) | Uspeh | Napake | Opombe |
|---|---|---|---|---|---|
| P1 | 1 | 38,87 | da | | pilotna izvedba |
| P1 | 2 | 7,12 | da | | pilotna izvedba |
| P2 | 1 | TODO | TODO | TODO | |
| P2 | 2 | TODO | TODO | TODO | |
| P3 | 1 | TODO | TODO | TODO | |
| P3 | 2 | TODO | TODO | TODO | |
| P4 | 1 | TODO | TODO | TODO | |
| P4 | 2 | TODO | TODO | TODO | |

### 3.5 Primerjava napovedi in meritve (P1)

| Naloga | KLM | Izmerjeno P1 | Razlika | Razlika (%) |
|---|---|---|---|---|
| 1 | 21,42 s | 38,87 s | +17,45 s | +81,5 % |
| 2 | 5,67 s | 7,12 s | +1,45 s | +25,6 % |

Pri obeh nalogah je izmerjeni čas daljši od uradne napovedi. Razlika je pri nalogi 1 bistveno večja. Možni razlogi:

1. **Miselne operacije.** Osnovni KLM ne vsebuje operatorja M (iskanje gumba, branje zaslona, odločanje). Z enim M na logični korak se napoved za nalogo 1 (36,27 s) od meritve razlikuje le še za +7,2 %.
2. **Nalaganje strani in hladni zagon Renderja.** Brezplačna storitev Render po neaktivnosti zaspi, zato prva zahteva traja dlje. KLM časa odziva sistema (R) ne vsebuje.
3. **Preusmeritve OAuth pri Googlu.** Naloga 1 vključuje tri preusmeritve (MailBridge → Google, Google → povratni naslov MailBridge, nato na stran z nabiralnikom) in nalaganje treh Googlovih zaslonov. Na te zaslone uporabnik čaka, branje opozorila o nepreverjeni aplikaciji pa traja dodatno.
4. **Branje navodil in podatkov.** Udeleženec med nalogo pogleda nazaj v navodila (npr. naslov prejemnika), kar KLM ne zajame.
5. **Poznavanje aplikacije.** P1 je član ekipe in aplikacijo pozna. Pri nalogi 2 je zato izmerjeni čas krajši od razširjene napovedi (7,12 s proti 11,07 s, −35,7 %): miselnih operacij je bilo očitno manj, kot jih predvideva en M na korak. Pri udeležencih, ki aplikacije ne poznajo (P3, P4), pričakujemo daljše čase.
6. **Ena meritev.** Pri n = 1 ne moremo sklepati o povprečju ali razpršenosti. Gre za pilotni podatek.

### 3.6 Dopolniti po zbiranju podatkov

> **TODO – izpolniti po meritvah P2–P4 med terminom vaj.**
>
> 1. Vpišite čase, uspeh in napake za P2, P3 in P4 v `results-template.csv`.
> 2. Zaženite `python3 docs/naloga-03a/klm.py` in izpis prilepite v razdelek 3.2.
> 3. Dopolnite tabelo v razdelku 3.4.
> 4. Za vsako nalogo navedite povprečje, najkrajši in najdaljši čas ter delež uspešnih izvedb.
> 5. Primerjajte povprečje z uradno napovedjo KLM (absolutna in odstotna razlika).
> 6. Primerjajte člana ekipe (P1, P2) z novima udeležencema (P3, P4).
> 7. Dodajte opažanja iz posnetkov sej in toplotnih kart Clarity (npr. kje so udeleženci iskali gumb).

| Naloga | n | Povprečje (s) | Min (s) | Max (s) | Uspešnost | Razlika do KLM (%) |
|---|---|---|---|---|---|---|
| 1 | TODO | TODO | TODO | TODO | TODO | TODO |
| 2 | TODO | TODO | TODO | TODO | TODO | TODO |

---

## Viri

1. Card, S. K., Moran, T. P. in Newell, A. (1980). The Keystroke-Level Model for User Performance Time with Interactive Systems. *Communications of the ACM*, 23(7), 396–410. https://doi.org/10.1145/358886.358895
2. Card, S. K., Moran, T. P. in Newell, A. (1983). *The Psychology of Human-Computer Interaction*. Hillsdale, NJ: Lawrence Erlbaum Associates.
3. Microsoft. *Microsoft Clarity – dokumentacija: namestitev* (Set up Clarity). https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-setup
4. Microsoft. *Clarity in Content Security Policy* (CSP). https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-csp
