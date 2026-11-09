# Navodila za udeleženca – Naloga 1: Povezava računa Gmail in pošiljanje sporočila

**Predmet:** Vrednotenje uporabniške izkušnje (UM FERI), naloga 03a
**Aplikacija:** MailBridge – https://mailbridge-og1u.onrender.com/

## Vaša naloga

V aplikaciji MailBridge ste že prijavljeni. Prijava in registracija nista del naloge.

V MailBridge povežite svoj račun Gmail. Nato z njega pošljite sporočilo s temi podatki:

- **Prejemnik:** aplazl55@gmail.com
- **Zadeva:** Test
- **Besedilo:** Pozdrav

Naloga je končana, ko aplikacija potrdi, da je bilo sporočilo poslano.

Pot do cilja izberite sami. Če obtičite, lahko nalogo kadar koli prekinete. Med izvedbo vam ne bomo pomagali, merili pa bomo čas.

## Prostovoljno sodelovanje

Sodelovanje je prostovoljno. Kadar koli lahko odstopite, ne da bi navedli razlog, in odstop za vas nima nobenih posledic.

## Hramba podatkov

- **Kaj zbiramo:** čas izvedbe naloge (meren s štoparico), uspešnost izvedbe in podatke o seji na spletni strani, ki jih zbira orodje Microsoft Clarity (premiki miške, kliki, drsenje, ogledane strani).
- **Namen:** podatki se uporabijo izključno za ta predmet.
- **Anonimnost:** podatke hranimo anonimno. Udeleženci so označeni samo z oznakami P1 do P4, vaše ime pa ni povezano z rezultati.
- **Izbris:** podatke izbrišemo po koncu semestra.

## Kontakt

- Marko Spasovski – markospasovski222@gmail.com
- Anže Plazl – aplazl55@gmail.com

---

## Primer uporabe (za izvajalca, ne za udeleženca)

**Akter:** prijavljeni uporabnik MailBridge
**Predpogoj:** uporabnik je prijavljen in je na strani z nabiralnikom (`app.html`); računa Gmail še nima povezanega; njegov Google račun je dodan med testne uporabnike aplikacije v Google Cloud.
**Uspešen izid:** prikaže se obvestilo »Message sent.«, sporočilo pa prispe na aplazl55@gmail.com.

Besedila v narekovajih so točne oznake v uporabniškem vmesniku (vmesnik je v angleščini).

1. Uporabnik v stranski vrstici v razdelku »Accounts« klikne gumb »+« (»Add an account«).
   - **1.a** Uporabnik v zgornji vrstici klikne ikono zobnika (»Settings«) ali odpre meni računa (»Account menu«) in izbere »Profile and accounts«. Na strani z nastavitvami v razdelku »Mail accounts« klikne »Add Gmail«. Postopek se nadaljuje pri koraku 3.
   - **1.b** Če uporabnik nima povezanega nobenega računa, je nabiralnik prazen in prikazuje gumb »Connect Gmail«. Uporabnik ga klikne in nadaljuje pri koraku 3.
2. V meniju »Add an account« izbere »Gmail«.
3. Aplikacija ga preusmeri k Googlu. Na zaslonu za izbiro računa izbere svoj Google račun.
   - **3.a** Če v brskalniku ni prijavljen v Google, vnese e-naslov in geslo (ter po potrebi drugi faktor).
4. Google prikaže opozorilo, da aplikacija ni preverjena (»Google hasn't verified this app«). Uporabnik klikne »Continue«.
5. Na zaslonu z dovoljenji označi vsa dovoljenja (»Select all«) in klikne »Continue«.
   - **5.a** Če ne označi vseh dovoljenj za Gmail, se vrne v MailBridge z obvestilom »Allow every requested Gmail permission (read, manage and send) to connect this account.«. Račun ni povezan, zato mora začeti znova pri koraku 1.
6. Google ga preusmeri nazaj v MailBridge. Prikaže se obvestilo »Account connected. Syncing your mail…«, novi račun pa je izbran v stranski vrstici.
7. Uporabnik klikne »New mail«. Odpre se okno »New message«, kurzor je že v polju »To«, v polju »From« pa je izbran novi račun Gmail.
8. V polje »To« vpiše aplazl55@gmail.com.
9. Klikne v polje »Subject« in vpiše »Test«.
   - **9.a** Med polji se premika s tipko Tab namesto z miško (velja tudi za korak 10).
10. Klikne v polje za besedilo in vpiše »Pozdrav«.
11. Klikne »Send«.
    - **11.a** Če katero od polj To, Subject ali besedilo ostane prazno, se izpiše »Add a recipient, a subject and a message.«. Uporabnik dopolni polje in ponovno klikne »Send«.
12. Okno se zapre in prikaže se obvestilo »Message sent.«. Naloga je končana.
