# 📊 Integrazione Google Sheets (Opzionale)

Questa guida spiega come salvare automaticamente i contratti generati su Google Sheets.

## 🎯 Vantaggi

- ✅ Storico completo dei contratti
- ✅ Facile ricerca e filtro
- ✅ Condivisione con il team
- ✅ Analisi e report automatici
- ✅ Backup cloud gratuito

## 📋 Prerequisiti

1. Account Google
2. Python già installato (dal sistema principale)

## 🔧 Setup (10 minuti)

### Passo 1: Crea il Google Sheet

1. Vai su [sheets.google.com](https://sheets.google.com)
2. Crea un nuovo foglio chiamato "Contratti Agency"
3. Crea le seguenti colonne nella prima riga:
   - A: Data Contratto
   - B: Numero Contratto
   - C: Nome Cliente
   - D: Ragione Sociale
   - E: Budget Iniziale
   - F: Commissione
   - G: Totale
   - H: Impegno Mensile
   - I: Partita IVA
   - J: Email (se raccolto)

### Passo 2: Ottieni le credenziali API

1. Vai su [console.cloud.google.com](https://console.cloud.google.com)
2. Crea un nuovo progetto (es. "Contratti Agency")
3. Abilita "Google Sheets API"
4. Crea credenziali → "Service Account"
5. Scarica il file JSON delle credenziali
6. Rinominalo in `credentials.json` e mettilo nella cartella del progetto

### Passo 3: Condividi il foglio con il Service Account

1. Apri il file `credentials.json`
2. Copia l'email del tipo: `nome@progetto.iam.gserviceaccount.com`
3. Nel tuo Google Sheet, clicca "Condividi"
4. Incolla l'email e dai permesso "Editor"

### Passo 4: Installa le librerie

```bash
pip install gspread oauth2client
```

### Passo 5: Modifica app.py

Aggiungi questo codice all'inizio di `app.py`:

```python
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Setup Google Sheets
def get_google_sheet():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('Contratti Agency').sheet1
    return sheet

def save_to_google_sheets(data):
    try:
        sheet = get_google_sheet()
        row = [
            data['dataContratto'],
            data['numeroContratto'],
            data['nomeCliente'],
            data['ragioneSociale'],
            data['budgetIniziale'],
            data['commissione'],
            data['totaleVersamento'],
            data['impegnoMensile'],
            data['partitaIva'],
            data.get('email', '')
        ]
        sheet.append_row(row)
        print(f"✅ Contratto salvato su Google Sheets")
    except Exception as e:
        print(f"⚠️ Errore salvataggio Google Sheets: {e}")
```

Poi modifica la funzione `generate_contract()`:

```python
@app.route('/generate-contract', methods=['POST'])
def generate_contract():
    try:
        data = request.json
        pdf_buffer = generate_contract_pdf(data)
        
        # DECOMMENTARE questa riga per attivare il salvataggio
        # save_to_google_sheets(data)
        
        return send_file(...)
```

## ✅ Test

1. Genera un contratto
2. Controlla il Google Sheet
3. Dovresti vedere una nuova riga con i dati!

## 📊 Analisi Dati

Con Google Sheets puoi:
- Creare grafici delle entrate mensili
- Filtrare contratti per cliente
- Calcolare totali commissioni
- Esportare report in Excel

## 🔒 Sicurezza

⚠️ **IMPORTANTE**:
- NON committare `credentials.json` su GitHub
- Aggiungi al `.gitignore`: `credentials.json`
- Mantieni private le credenziali API
- Usa permessi minimi necessari

## 💡 Funzionalità Avanzate (Opzionali)

### 1. Invio Email Automatico

Aggiungi questa funzione:

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_contract_email(pdf_buffer, client_email, contract_data):
    msg = MIMEMultipart()
    msg['From'] = 'tuaemail@kappateam.com'
    msg['To'] = client_email
    msg['Subject'] = f"Contratto Agency KT-ONB-2025/{contract_data['numeroContratto']}"
    
    # Allega PDF
    part = MIMEBase('application', 'pdf')
    part.set_payload(pdf_buffer.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename=Contratto.pdf')
    msg.attach(part)
    
    # Invia
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('tuaemail@gmail.com', 'password')
    server.send_message(msg)
    server.quit()
```

### 2. Dashboard Statistiche

Crea un nuovo foglio "Dashboard" con formule:
- `=SUM(G:G)` → Totale fatturato
- `=COUNTIF(A:A, ">="&TODAY()-30)` → Contratti ultimo mese
- `=AVERAGE(E:E)` → Budget medio

### 3. Notifiche Telegram

Ricevi notifica quando viene generato un contratto:

```python
import requests

def notify_telegram(message):
    bot_token = 'TUO_BOT_TOKEN'
    chat_id = 'TUO_CHAT_ID'
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    requests.post(url, data={'chat_id': chat_id, 'text': message})
```

## 🎓 Risorse Utili

- [Documentazione gspread](https://docs.gspread.org/)
- [Google Sheets API](https://developers.google.com/sheets/api)
- [Tutorial video](https://www.youtube.com/watch?v=...)

---

**Hai bisogno di aiuto?** Contatta il supporto tecnico Kappa Team
