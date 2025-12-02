# 🎯 GENERATORE CONTRATTI AGENCY - KAPPA TEAM

Sistema completo per la generazione automatica di contratti PDF firmati.

---

## 📁 CONTENUTO DEL PACCHETTO

```
contract-generator/
├── 🚀 START.bat                          # Avvio rapido Windows
├── 🚀 START.sh                           # Avvio rapido Mac/Linux
├── 📘 LEGGIMI_PRIMA.md                   # Questo file
├── 📖 GUIDA_RAPIDA.md                    # Istruzioni veloci
├── 📚 README.md                          # Documentazione completa
├── 🎨 PERSONALIZZAZIONE.md               # Guida personalizzazione
├── 📊 GOOGLE_SHEETS_INTEGRATION.md       # Integrazione Google Sheets
├── 📄 ESEMPIO_CONTRATTO_GENERATO.pdf     # Esempio di output
├── app.py                                # Server backend
├── index.html                            # Interfaccia web
├── requirements.txt                      # Dipendenze Python
├── firma_kappa_team.png                  # Firma digitale
└── test_generation.py                    # Script di test
```

---

## ⚡ INIZIO RAPIDO (3 MINUTI)

### 📌 Requisiti
- Python 3.8+ installato ([scarica qui](https://www.python.org/downloads/))
- Browser moderno (Chrome, Firefox, Safari, Edge)

### 🚀 Avvio

**Windows:**
```
1. Doppio click su START.bat
2. Aspetta che si apra il browser
3. Inizia a generare contratti!
```

**Mac/Linux:**
```bash
1. Apri Terminale
2. cd nella cartella contract-generator
3. ./START.sh
4. Apri http://localhost:5000
```

**Manuale:**
```bash
pip install -r requirements.txt
python app.py
```

---

## 📖 DOCUMENTAZIONE

### 🎓 Per Iniziare
1. **[GUIDA_RAPIDA.md](GUIDA_RAPIDA.md)** - Primi passi e tutorial base
2. **[README.md](README.md)** - Documentazione tecnica completa
3. **[ESEMPIO_CONTRATTO_GENERATO.pdf](ESEMPIO_CONTRATTO_GENERATO.pdf)** - Vedi un esempio di output

### 🔧 Personalizzazione
4. **[PERSONALIZZAZIONE.md](PERSONALIZZAZIONE.md)** - Modificare colori, loghi, campi, ecc.
5. **[GOOGLE_SHEETS_INTEGRATION.md](GOOGLE_SHEETS_INTEGRATION.md)** - Salvare contratti online

---

## ✨ CARATTERISTICHE PRINCIPALI

### 🎯 Funzionalità Core
- ✅ Form web intuitivo e professionale
- ✅ Generazione PDF automatica
- ✅ Firma digitale pre-inserita
- ✅ Calcoli automatici (commissioni, totali)
- ✅ Download immediato
- ✅ Dati compilati dal modello originale

### 💡 Campi Gestiti
- Dati cliente (nome, nascita, CF)
- Dati azienda (ragione sociale, sede, P.IVA)
- Dati contrattuali (numero, data, luogo)
- Dati finanziari (budget, commissioni, impegni)
- Servizi opzionali (proxy, formazione)

### 🔒 Sicurezza
- Nessun dato salvato di default (privacy)
- Possibile integrazione Google Sheets opzionale
- Sistema locale o hosting sicuro

---

## 🎬 TUTORIAL VIDEO

### Come Usare il Sistema
1. **Primo Avvio** - [Video 1min]
2. **Generare un Contratto** - [Video 2min]
3. **Personalizzare l'Aspetto** - [Video 3min]
4. **Integrazione Google Sheets** - [Video 5min]

*(Link ai video da aggiungere)*

---

## 💡 CASI D'USO COMUNI

### Scenario 1: Generazione Standard
```
1. Avvia sistema
2. Compila form cliente
3. Genera PDF
4. Invia al cliente
```

### Scenario 2: Con Storico Google Sheets
```
1. Configura Google Sheets (una volta)
2. Genera contratto
3. Automaticamente salvato online
4. Consulta dashboard contratti
```

### Scenario 3: Personalizzato per la Tua Azienda
```
1. Modifica dati fornitore
2. Carica tuo logo
3. Cambia colori interfaccia
4. Aggiungi campi personalizzati
```

---

## 🔧 CONFIGURAZIONE AVANZATA

### Hosting Online (Opzionale)

**Vercel (Gratuito):**
```bash
npm install -g vercel
vercel
```

**Google Cloud:**
```bash
gcloud app deploy
```

**Heroku:**
```bash
heroku create
git push heroku main
```

### Automazioni

**Invio Email Automatico:**
- Configura SMTP
- Allega PDF
- Invia a cliente e copia a te

**Notifiche Telegram:**
- Crea bot Telegram
- Ricevi notifica per ogni contratto

**Backup Automatico:**
- Salva su Google Drive
- Sincronizza con Dropbox
- Archivia su server FTP

---

## 🆘 SUPPORTO E RISORSE

### 📞 Contatti
- **Email:** support@kappateam.com
- **Telefono:** [inserire]
- **Web:** www.kappateam.com

### 🐛 Problemi Comuni

**Il server non parte:**
- Verifica Python installato: `python --version`
- Reinstalla dipendenze: `pip install -r requirements.txt`
- Controlla porta 5000 libera

**PDF non si genera:**
- Compila tutti i campi obbligatori (*)
- Verifica firma_kappa_team.png presente
- Controlla console browser (F12)

**Errori di formattazione:**
- Verifica date nel formato corretto
- Controlla numeri senza simboli
- Usa MAIUSCOLE per codice fiscale

### 📚 Documentazione Tecnica
- [Documentazione ReportLab](https://www.reportlab.com/docs/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Tailwind CSS](https://tailwindcss.com/)

---

## 🎯 ROADMAP FUTURI SVILUPPI

### Versione 1.1 (Pianificata)
- [ ] Dashboard contratti generati
- [ ] Ricerca e filtri avanzati
- [ ] Esportazione Excel
- [ ] Template multipli

### Versione 1.2 (Pianificata)
- [ ] Sistema login utenti
- [ ] Firma digitale cliente
- [ ] Invio automatico email
- [ ] API REST

### Versione 2.0 (Futura)
- [ ] App mobile
- [ ] Integrazione CRM
- [ ] Workflow approvazione
- [ ] Analytics avanzati

---

## 📊 STATISTICHE E METRICHE

### Cosa Puoi Tracciare
Con l'integrazione Google Sheets puoi monitorare:
- Numero contratti generati
- Fatturato totale e mensile
- Budget medio per cliente
- Commissioni totali
- Trend temporali

---

## 🎓 BEST PRACTICES

### Organizzazione
1. Usa numeri contratto progressivi (01, 02, 03...)
2. Salva PDF in cartelle per anno/mese
3. Mantieni backup regolari
4. Documenta personalizzazioni

### Sicurezza
1. Non condividere credenziali API
2. Usa HTTPS in produzione
3. Limita accesso al sistema
4. Fai backup regolari

### Efficienza
1. Prepara template dati clienti ricorrenti
2. Usa abbreviazioni consistenti
3. Automatizza con Google Sheets
4. Crea checklist pre-generazione

---

## 📝 CHANGELOG

### Versione 1.0 (Corrente)
- ✅ Sistema base funzionante
- ✅ Form completo
- ✅ Generazione PDF
- ✅ Firma digitale
- ✅ Calcoli automatici
- ✅ Documentazione completa

---

## 🏆 CREDITI

**Sviluppato per:** Kappa Team S.r.l.  
**Prodotto:** MetaBridge™  
**Versione:** 1.0  
**Data:** Novembre 2025

---

## 📜 LICENZA

Questo sistema è proprietà di Kappa Team S.r.l.  
Tutti i diritti riservati.

---

## 🚀 INIZIA ORA!

**Non perdere altro tempo - genera il tuo primo contratto in 3 minuti!**

1. 📂 Doppio click su `START.bat` (Windows) o esegui `./START.sh` (Mac/Linux)
2. 🌐 Apri http://localhost:5000 nel browser
3. 📝 Compila il form
4. 🎉 Genera il tuo primo contratto PDF!

---

**MetaBridge™** - Kappa Team S.r.l.  
*Sistema di generazione contratti automatizzato*

💬 *Hai domande? Leggi la [GUIDA_RAPIDA.md](GUIDA_RAPIDA.md) o contatta il supporto!*
