# ⚡ RENDER - GUIDA VELOCE 10 MINUTI

## 🎯 Setup Rapido

### 1️⃣ Aggiorna GitHub (3 min)
- Vai su: https://github.com/bobbyxx88/metabridge_contract
- **Elimina** eventuali file vecchi
- **"Upload files"** → Trascina TUTTI i file dal nuovo ZIP
- **Commit**

### 2️⃣ Crea Account Render (2 min)
- Vai su: **https://render.com**
- **Sign up with GitHub**
- Autorizza Render

### 3️⃣ Crea Web Service (3 min)
- **New +** → **Web Service**
- Scegli **"metabridge_contract"**
- **Connect**

### 4️⃣ Configurazione (2 min)
```
Name: contratti-kappateam
Region: Frankfurt (EU Central)
Runtime: Python 3
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
Instance Type: Free
```

- Clicca **"Create Web Service"**

### 5️⃣ Aspetta Deploy (3-5 min)
- Vedrai i log
- Quando diventa verde "Live" → **FATTO!** ✅

### 6️⃣ Testa e Condividi (1 min)
- Copia URL: `https://contratti-kappateam.onrender.com`
- Apri nel browser
- Genera un contratto di test
- **Funziona!** 🎉
- Condividi URL con colleghi

---

## 📥 FILE DA SCARICARE

[📦 SCARICA ZIP PER RENDER](computer:///mnt/user-data/outputs/contract-generator-render.zip)

**Nuovi file importanti:**
- ✅ `Procfile` (necessario per Render)
- ✅ `requirements.txt` (con gunicorn aggiunto)
- ✅ GUIDA_RENDER.md (dettagli completi)

---

## ⚠️ IMPORTANTE

**Dopo il deploy, aggiungi una PASSWORD!**
Altrimenti chiunque con il link può accedere.

Dimmi quando è online e ti preparo il login! 🔒

---

## 🆘 Problemi?

**Build fallisce?**
→ Verifica che `Procfile` sia caricato su GitHub

**Sito lento?**
→ Normale al primo caricamento (sleep mode)
→ Dopo 30 sec va veloce

**Errore 502?**
→ Aspetta 2-3 minuti, è in fase di startup

---

**Tempo totale: 15 minuti** ⏱️
**Costo: GRATIS** 💰
**Risultato: App online 24/7** 🚀

Buon deploy! 😊
