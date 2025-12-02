# 📄 Generatore Contratti Agency - Kappa Team

Sistema automatico per la generazione di contratti PDF compilati con firma digitale.

## 🚀 Caratteristiche

- ✅ Form web intuitivo per inserimento dati
- ✅ Generazione PDF automatica
- ✅ Firma digitale Kappa Team pre-inserita
- ✅ Calcoli automatici (commissioni, totali)
- ✅ Download immediato del contratto
- ✅ Pronto per integrazione con Google Sheets

## 📋 Requisiti

- Python 3.8 o superiore
- Browser moderno (Chrome, Firefox, Safari, Edge)

## 🔧 Installazione

### 1. Installa le dipendenze Python

```bash
pip install -r requirements.txt
```

### 2. Avvia il server

```bash
python app.py
```

Il server si avvierà su `http://localhost:5000`

## 💻 Utilizzo

1. Apri il browser e vai su `http://localhost:5000`
2. Compila tutti i campi obbligatori del form
3. Clicca su "Genera Contratto PDF"
4. Il PDF verrà scaricato automaticamente

## 📁 Struttura File

```
contract-generator/
├── app.py                      # Server Flask backend
├── index.html                  # Form frontend
├── requirements.txt            # Dipendenze Python
├── firma_kappa_team.png       # Firma digitale aziendale
└── README.md                  # Questo file
```

## 🎨 Personalizzazione

### Modificare i dati del Fornitore

Modifica il file `app.py` alla sezione "Dati Fornitore" per cambiare:
- Indirizzo sede legale
- P.IVA
- Nome legale rappresentante

### Aggiungere il logo aziendale

1. Salva il logo come `metabridge_logo.png` nella stessa cartella
2. Il sistema lo inserirà automaticamente nell'intestazione

## 🌐 Deploy Online (Opzionale)

### Opzione 1: Vercel (Gratuito)

1. Crea account su Vercel.com
2. Installa Vercel CLI: `npm install -g vercel`
3. Nella cartella del progetto: `vercel`
4. Segui le istruzioni

### Opzione 2: Google Cloud (con Free Tier)

1. Crea progetto su Google Cloud
2. Abilita App Engine
3. Crea file `app.yaml`:

```yaml
runtime: python39
entrypoint: gunicorn -b :$PORT app:app

instance_class: F1
```

4. Deploy: `gcloud app deploy`

### Opzione 3: Hosting tradizionale

Qualsiasi hosting che supporta Python + Flask funzionerà.

## 📊 Integrazione Google Sheets (Opzionale)

Per salvare automaticamente i contratti su Google Sheets:

1. Crea un Google Sheet
2. Ottieni le credenziali API da Google Cloud Console
3. Installa: `pip install gspread oauth2client`
4. Decommentare la funzione `save_to_google_sheets()` in `app.py`

## 🔒 Sicurezza

- ⚠️ Non esporre direttamente su internet senza autenticazione
- Considera l'aggiunta di login/password
- Usa HTTPS in produzione
- Mantieni private le credenziali API

## 📞 Supporto

Per problemi o domande:
- Email: support@kappateam.com
- Website: www.kappateam.com

## 📝 Note

- I contratti vengono generati in tempo reale
- Nessun dato viene salvato automaticamente (privacy)
- Per salvare storico contratti, attiva integrazione Google Sheets

## 🎯 Prossimi Sviluppi

- [ ] Dashboard per visualizzare contratti generati
- [ ] Invio automatico via email
- [ ] Sistema di autenticazione
- [ ] Template contratti multipli
- [ ] Esportazione CSV storico

---

**MetaBridge™** - Operato da Kappa Team S.r.l.
