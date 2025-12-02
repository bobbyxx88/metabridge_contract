# 🚀 GUIDA DEPLOY SU VERCEL - Passo per Passo

## 📋 COSA FARAI

Pubblicherai il sistema online in modo che sia accessibile da qualsiasi dispositivo, 24/7, gratuitamente!

**Tempo richiesto:** 10-15 minuti
**Costo:** GRATIS
**Risultato:** Sito tipo `https://contratti-kappateam.vercel.app`

---

## 🎯 PASSO 1: CREA ACCOUNT VERCEL

### 1.1 Vai su Vercel
Apri il browser e vai su: **https://vercel.com**

### 1.2 Registrati
- Clicca su **"Sign Up"** (in alto a destra)
- Scegli **"Continue with GitHub"** (consigliato)
  - Oppure usa email se preferisci
- Segui la procedura di registrazione
- Conferma l'email se richiesto

### 1.3 Completa il profilo
- Nome: Kappa Team (o quello che vuoi)
- Tipo account: Personal (va benissimo il free)

✅ **Account creato!** Ora sei nella dashboard di Vercel.

---

## 🎯 PASSO 2: PREPARA IL CODICE SU GITHUB

### Opzione A: Usa GitHub (Consigliato - Più Facile)

#### 2.1 Crea account GitHub
Se non ce l'hai già:
- Vai su **https://github.com**
- Clicca **"Sign up"**
- Crea account gratuito

#### 2.2 Crea un nuovo repository
1. Una volta loggato, clicca sul **"+"** in alto a destra
2. Clicca **"New repository"**
3. Dai un nome: `contratti-agency` (o quello che vuoi)
4. Scegli **"Private"** (così è privato, solo tu lo vedi)
5. Clicca **"Create repository"**

#### 2.3 Carica i file
**Metodo semplice (tramite web):**

1. Nella pagina del repository, clicca **"uploading an existing file"**
2. **SCARICA** prima lo ZIP aggiornato dal link in fondo a questa guida
3. **ESTRAI** lo ZIP sul tuo Mac
4. **TRASCINA** tutti i file della cartella `contract-generator` nella pagina GitHub
   - app.py
   - index.html
   - requirements.txt
   - vercel.json
   - firma_kappa_team.png
   - metabridge_logo.png
   - (tutti gli altri file)
5. Scrivi un messaggio tipo: "Initial commit"
6. Clicca **"Commit changes"**

✅ **Codice caricato su GitHub!**

---

### Opzione B: Caricamento Diretto su Vercel (Alternativa)

Se non vuoi usare GitHub, puoi caricare direttamente su Vercel:

1. Vai su Vercel Dashboard
2. Clicca **"Add New..."** → **"Project"**
3. Nella schermata, cerca l'opzione **"Deploy from template"** o **"Import"**
4. Scegli l'opzione per caricare file locali
5. Carica lo ZIP (vedi link in fondo)

⚠️ **NOTA:** Il metodo GitHub è più comodo per aggiornamenti futuri!

---

## 🎯 PASSO 3: DEPLOY SU VERCEL

### 3.1 Importa il progetto
1. Nella **Vercel Dashboard**, clicca **"Add New..."** → **"Project"**
2. Ti chiederà di collegare GitHub (se non l'hai già fatto)
3. Clicca **"Import"** accanto al repository `contratti-agency`

### 3.2 Configura il progetto
Vercel rileverà automaticamente che è un'app Python Flask.

**Configurazione:**
- **Framework Preset:** Other
- **Root Directory:** `./` (lascia così)
- **Build Command:** (lascia vuoto)
- **Output Directory:** (lascia vuoto)

### 3.3 Variabili d'ambiente (Opzionale)
Per ora non servono, clicca **"Deploy"**!

### 3.4 Aspetta il deploy
- Vedrai una schermata con un caricamento
- Ci vorranno 2-3 minuti
- Quando vedi **"Congratulations"** o icone di festa 🎉, è pronto!

✅ **SITO ONLINE!**

---

## 🎯 PASSO 4: TESTA IL SITO

### 4.1 Trova l'URL
Nella schermata di successo, vedrai un link tipo:
```
https://contratti-agency-abc123.vercel.app
```

Clicca su **"Visit"** o copia l'URL.

### 4.2 Prova a generare un contratto
1. Apri l'URL nel browser
2. Dovresti vedere il tuo form!
3. Compila i dati di un contratto di test
4. Clicca "Genera Contratto PDF"
5. Scarica e verifica il PDF

✅ **FUNZIONA!** Il tuo sistema è online!

---

## 🎯 PASSO 5: PERSONALIZZA IL DOMINIO (Opzionale)

### 5.1 Cambia il nome
Il nome predefinito è tipo `contratti-agency-abc123.vercel.app`

Per cambiarlo:
1. Vai nelle **Settings** del progetto su Vercel
2. Clicca **"Domains"**
3. Clicca **"Edit"** accanto al dominio
4. Scegli un nome tipo: `contratti-kappateam.vercel.app`
5. Salva

Ora il tuo URL sarà più carino! 🎨

### 5.2 Usa dominio personalizzato (Avanzato)
Se hai un dominio tuo (es. `contratti.kappateam.com`):
1. Vai in **Domains**
2. Clicca **"Add"**
3. Inserisci il tuo dominio
4. Segui le istruzioni per configurare il DNS

---

## 🔒 PASSO 6: AGGIUNGI PASSWORD (IMPORTANTE!)

⚠️ **ATTENZIONE:** Per ora chiunque con il link può accedere!

### Per aggiungere protezione password:

**Metodo 1: Password Semplice (5 min)**
Ti invio un file aggiornato con login. Dimmi se vuoi che te lo prepari!

**Metodo 2: Vercel Password Protection (PRO)**
Serve abbonamento Vercel Pro ($20/mese) - ha protezione integrata

**Metodo 3: Oscurare il Link**
Usa un nome difficile tipo: `contratti-kt-x7h2k9p.vercel.app`
Così è difficile da indovinare (ma non sicuro al 100%)

---

## 📱 PASSO 7: USA DA QUALSIASI DISPOSITIVO

Ora puoi:

**Dal Mac:**
- Apri Safari → `https://tuo-link.vercel.app`

**Dall'iPhone:**
- Apri Safari → `https://tuo-link.vercel.app`
- Puoi salvarlo come icona nella home screen!

**Da qualsiasi PC:**
- Apri Chrome → `https://tuo-link.vercel.app`

**Condividi con colleghi:**
- Invia il link a chi deve usarlo

---

## 🔄 AGGIORNAMENTI FUTURI

### Come aggiornare il sistema:

**Se usi GitHub:**
1. Modifica i file su GitHub
2. Vercel rileverà automaticamente
3. Ri-deploya in automatico (2-3 min)

**Caricamento diretto:**
1. Vai su Vercel → Deployments
2. Clicca "Redeploy"
3. Carica nuovi file

---

## 💰 COSTI

**Vercel Free Tier include:**
- ✅ 100GB bandwidth/mese (più che sufficiente!)
- ✅ Deploy illimitati
- ✅ HTTPS automatico
- ✅ Nessuna carta di credito richiesta

**Quando serve pagare:**
- Solo se superi 100GB/mese (improbabile)
- O se vuoi funzionalità PRO (password protection integrata)

---

## 🆘 PROBLEMI COMUNI

### "Build Failed"
- Controlla che tutti i file siano caricati
- Verifica che `requirements.txt` e `vercel.json` ci siano

### "404 Not Found"
- Aspetta 2-3 minuti dopo il deploy
- Ricarica la pagina

### "PDF non si genera"
- Verifica che `firma_kappa_team.png` e `metabridge_logo.png` siano caricati
- Controlla i log su Vercel

### "Sito lento"
- Normale al primo caricamento (cold start)
- Dopo i primi usi sarà veloce

---

## 📥 FILE DA SCARICARE

**Scarica il pacchetto aggiornato per Vercel:**
[📦 Download ZIP per Vercel](computer:///mnt/user-data/outputs/contract-generator.zip)

**Contiene:**
- app.py (modificato per Vercel)
- vercel.json (configurazione)
- .gitignore (file da ignorare)
- Tutti gli altri file necessari

---

## ✅ CHECKLIST FINALE

Prima di iniziare, assicurati di avere:
- [ ] Account Vercel creato
- [ ] Account GitHub creato (se usi GitHub)
- [ ] ZIP scaricato ed estratto
- [ ] File caricati su GitHub o pronti per Vercel
- [ ] 10-15 minuti di tempo

---

## 🎉 FATTO!

Una volta completato, avrai:
- ✅ Sistema online 24/7
- ✅ Accessibile da qualsiasi dispositivo
- ✅ HTTPS sicuro
- ✅ Zero manutenzione
- ✅ GRATIS

---

## 💡 PROSSIMI PASSI CONSIGLIATI

1. **Aggiungi password** (te lo preparo se vuoi)
2. **Salva l'URL** nei preferiti
3. **Testa da telefono** per sicurezza
4. **Crea backup** del codice su GitHub

---

## 📞 SUPPORTO

Problemi durante il deploy?
- Mandami screenshot dell'errore
- Dimmi a che passo sei
- Ti aiuto subito!

---

**Sei pronto? Inizia dal PASSO 1!** 🚀

Se hai dubbi su qualche passaggio, chiedimi prima di procedere! 😊
