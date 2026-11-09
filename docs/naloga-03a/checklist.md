# Kontrolni seznam – naloga 03a

Ročni koraki po vrstnem redu. Rok oddaje: **torek, 10. 11. 2026, ob 17.00**.

## 1. Objava Clarity

- [ ] Potisnite vejo `feat/clarity-analytics`: `git push -u origin feat/clarity-analytics`.
- [ ] Odprite PR, počakajte na zelene preverbe (CI) in ga združite v `main`.
- [ ] Preverite, da je Render objavil novo različico (`autoDeployTrigger: checksPass` objavi šele, ko so preverbe zelene). Po potrebi sprožite »Manual Deploy«. **Clarity deluje šele po objavi.**

## 2. Preverjanje Clarity v živo

- [ ] Odprite https://mailbridge-og1u.onrender.com/ v brskalniku **brez blokatorja oglasov** (ali v zasebnem oknu brez razširitev).
- [ ] Odprite orodja za razvijalce (F12):
  - zavihek **Network**: zahteva na `www.clarity.ms/tag/zb5jhevix7` uspe, med klikanjem pa se pojavljajo zahteve POST na `clarity.ms/collect`, ki niso blokirane;
  - zavihek **Console**: ni napak »Content-Security-Policy« ali »Refused to load«.
- [ ] Nekaj minut klikajte po aplikaciji (prijava, nabiralnik, nastavitve).
- [ ] V nadzorni plošči Clarity preverite, ali se pojavijo seje. **Prikaz lahko traja do 2 ur.**
- [ ] V Clarity (Settings → Masking) nastavite maskiranje na **Strict**, da posnetki ne vsebujejo zadev, pošiljateljev ali drugih besedil iz nabiralnika.

## 3. Priprava Google OAuth

- [ ] V Google Cloud Console (APIs & Services → OAuth consent screen → Audience → Test users) dodajte Google račune **vseh** testirancev. Aplikacija v načinu »Testing« zavrne vse druge račune (napaka 403 `access_denied`).
  - Druga možnost: pripravite en testni Google račun, ki ga uporabijo vsi udeleženci.
- [ ] Na Renderju preverite spremenljivko `GMAIL_ALLOWED_EMAILS`. Če ni prazna, mora vsebovati **prijavni e-naslov MailBridge** testnega uporabnika, sicer se možnost Gmail v meniju »Add an account« sploh ne prikaže.
- [ ] Udeležence vnaprej opozorite na Googlov zaslon »Google hasn't verified this app«. Pri testnih uporabnikih kliknejo »Continue«.
- [ ] Pred vsakim udeležencem v MailBridge (Settings → Mail accounts) odstranite prej povezani račun Gmail. Sicer bo povezava »obnovljena« (»Sign-in renewed.«), ne nova.
- [ ] Pred vsakim udeležencem prikazno ime ponastavite na nekaj drugega kot »Test«.
- [ ] Pred začetkom odprite stran (in nekaj sekund počakajte), da se Render prebudi iz hladnega zagona.
- [ ] S poskusno izvedbo preverite število klikov na Googlovih zaslonih (predpostavka v KLM: izbira računa, »Continue«, »Select all«, »Continue«). Če se razlikuje, popravite `klm.py` in poročilo.

## 4. Meritve P2–P4 (med terminom vaj)

- [ ] Meritve izvedite **med terminom vaj** (zahteva naloge pri merjenju s štoparico).
- [ ] Udeleženec je prijavljen in začne na `app.html`. Izvajalec prebere ali da v branje navodila (`navodila-naloga-1.md`, `navodila-naloga-2.md`) in izjavo o prostovoljnem sodelovanju ter hrambi podatkov.
- [ ] Ena oseba meri čas s štoparico na telefonu. Začetek: »Zdaj« in prvi premik miške. Konec: obvestilo »Message sent.« oz. »Profile saved.«.
- [ ] Zabeležite čas, uspeh, število napak in opombe **samo pod oznako P2, P3 ali P4**, nikoli z imenom.
- [ ] Rezultate vpišite v `results-template.csv`.
- [ ] Zaženite `python3 docs/naloga-03a/klm.py` in posodobite razdelke 3.2, 3.4 in 3.6 v `report.md`.

## 5. Oddaja

- [ ] `report.md` izvozite v PDF (ali v obliko, ki jo zahteva eŠtudij) in ga oddajte na eŠtudij do 10. 11. 2026, 17.00.
- [ ] Asistentu pokažite navodila za obe nalogi in pridobite odobritev.

## 6. Priprava na zagovor

1. **Zakaj je izmerjeni čas daljši od napovedi KLM?**
   Osnovni KLM ne vsebuje miselnih operacij (M) in čakanja na sistem (R). Pri nalogi 1 vplivajo še preusmeritve OAuth pri Googlu in hladni zagon Renderja.
2. **Zakaj je uradna napoved brez M?**
   Postavitev operatorjev M je pri KLM subjektivna (pravila Card et al.). Za primerjavo smo zato dodali ločeno napoved z enim M na logični korak.
3. **Kako ste vključili Clarity, če CSP blokira vrinjene skripte?**
   Kodo smo premaknili v zunanjo datoteko `analytics.js` in v CSP dovolili samo domene `clarity.ms` in `c.bing.com`, brez `'unsafe-inline'`.
4. **Kako zagotavljate anonimnost?**
   Rezultati so označeni samo s P1–P4, imena niso nikjer povezana s časi, v Clarity nastavimo maskiranje Strict (točka 2), podatki pa se po koncu semestra izbrišejo.
5. **Zakaj Ctrl+A pri nalogi 2?**
   Polje »Display name« je vnaprej izpolnjeno s trenutnim imenom, zato ga mora uporabnik pred vnosom označiti ali izbrisati.
