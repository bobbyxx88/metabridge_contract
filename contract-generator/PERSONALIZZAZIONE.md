# 🎨 Guida alla Personalizzazione

## 🔧 Modifiche Comuni

### 1. Cambiare i Colori dell'Interfaccia

Apri `index.html` e modifica le classi Tailwind:

**Colore primario (bottone):**
```html
<!-- Da blu a rosso -->
Da: class="bg-blue-600 hover:bg-blue-700"
A:  class="bg-red-600 hover:bg-red-700"

<!-- Da blu a verde -->
Da: class="bg-blue-600 hover:bg-blue-700"
A:  class="bg-green-600 hover:bg-green-700"
```

**Bordi e accenti:**
```html
Da: class="border-blue-500 focus:ring-blue-500"
A:  class="border-purple-500 focus:ring-purple-500"
```

### 2. Modificare i Dati del Fornitore

Apri `app.py` e cerca la sezione "Dati Fornitore":

```python
# Modifica questi valori
c.drawString(50, y, "Kappa Team S.r.l., con sede legale in Via Enrico De Nicola, Trani (BT), P. IVA IT12687960968,")
```

Cambia in:

```python
c.drawString(50, y, "TUA AZIENDA S.r.l., con sede legale in TUO INDIRIZZO, P. IVA TUAPARTITAIVA,")
```

### 3. Aggiungere Nuovi Campi al Form

**Nel form HTML (`index.html`):**

```javascript
// Aggiungi nel useState
const [formData, setFormData] = useState({
    // ... campi esistenti ...
    emailCliente: '',  // NUOVO CAMPO
});

// Aggiungi nel form HTML
<div>
    <label className="block text-sm font-medium text-gray-700 mb-1">
        Email Cliente
    </label>
    <input
        type="email"
        name="emailCliente"
        value={formData.emailCliente}
        onChange={handleChange}
        className="w-full px-3 py-2 border border-gray-300 rounded-md"
        placeholder="cliente@email.com"
    />
</div>
```

**Nel PDF (`app.py`):**

```python
# Aggiungi dove vuoi visualizzare l'email
email_cliente = data.get('emailCliente', '')
if email_cliente:
    c.drawString(50, y, f"Email: {email_cliente}")
    y -= 15
```

### 4. Modificare i Valori di Default

In `index.html`, sezione useState:

```javascript
const [formData, setFormData] = useState({
    budgetIniziale: '25000',  // Da 20000 a 25000
    percentualeCommissione: '10',  // Da 7% a 10%
    impegnoMensile: '50000',  // Da 30000 a 50000
    luogoContratto: 'Milano',  // Da Trani a Milano
});
```

### 5. Aggiungere il Logo Aziendale

1. Salva il tuo logo come `metabridge_logo.png` nella cartella principale
2. Il sistema lo inserirà automaticamente nell'intestazione del PDF

Per modificare dimensioni/posizione del logo, in `app.py`:

```python
# Cerca questa riga
c.drawImage(logo_path, width/2 - 50, height - 100, width=100, height=50, ...)

# Modifica i parametri:
# x, y = posizione
# width, height = dimensioni
c.drawImage(logo_path, 50, height - 80, width=150, height=60, ...)
```

### 6. Cambiare Font e Dimensioni

In `app.py`:

```python
# Font titoli
c.setFont("Helvetica-Bold", 24)  # Cambia 24 con altra dimensione

# Font testo normale
c.setFont("Helvetica", 11)  # Cambia 11 con altra dimensione

# Per usare font personalizzati:
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Registra font
pdfmetrics.registerFont(TTFont('MioFont', 'path/to/font.ttf'))

# Usa font
c.setFont("MioFont", 12)
```

### 7. Modificare il Footer

In `app.py`, cerca "Footer" e modifica:

```python
footer_text = "TUA AZIENDA™ – La tua tagline qui"
c.drawCentredString(width/2, 50, footer_text)
```

### 8. Aggiungere Servizi Opzionali

In `index.html`, aggiungi nella sezione "Servizi Opzionali":

```javascript
<div className="flex items-center">
    <input
        type="checkbox"
        name="consulenzaMensile"
        checked={formData.consulenzaMensile}
        onChange={handleChange}
        className="w-4 h-4 text-blue-600 border-gray-300 rounded"
    />
    <label className="ml-2 text-sm text-gray-700">
        Consulenza mensile (€500/mese)
    </label>
</div>
```

In `app.py`, aggiungi nella generazione PDF:

```python
if data.get('consulenzaMensile'):
    c.drawString(70, y, "☑ Consulenza mensile - €500,00/mese")
    y -= 13
```

### 9. Personalizzare i Messaggi di Conferma

In `index.html`, cerca `alert` e modifica:

```javascript
alert('Contratto generato con successo!');
// Cambia in:
alert('🎉 Contratto generato! Controlla la cartella Download.');
```

### 10. Modificare il Nome del File Scaricato

In `app.py`:

```python
download_name=f"Contratto_KT-ONB-2025_{data['numeroContratto']}.pdf"
# Cambia in:
download_name=f"Contratto_{data['ragioneSociale']}_{data['numeroContratto']}.pdf"
```

## 🎨 Temi Colore Pre-Impostati

### Tema Blu (Default)
```html
bg-blue-600 hover:bg-blue-700
border-blue-500 focus:ring-blue-500
```

### Tema Verde Professionale
```html
bg-green-600 hover:bg-green-700
border-green-500 focus:ring-green-500
```

### Tema Viola Moderno
```html
bg-purple-600 hover:bg-purple-700
border-purple-500 focus:ring-purple-500
```

### Tema Rosso/Arancio
```html
bg-orange-600 hover:bg-orange-700
border-orange-500 focus:ring-orange-500
```

### Tema Scuro Elegante
```html
bg-gray-800 hover:bg-gray-900
border-gray-600 focus:ring-gray-500
```

## 📱 Rendere il Form Responsive

Il form è già responsive, ma puoi personalizzare i breakpoint:

```html
<!-- Singola colonna mobile, 2 colonne desktop -->
<div className="grid grid-cols-1 md:grid-cols-2 gap-4">

<!-- Singola colonna mobile, 3 colonne tablet, 4 desktop -->
<div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
```

## 🔒 Aggiungere Autenticazione (Opzionale)

Semplice password di accesso:

```python
# In app.py
from flask import session, redirect, request

app.secret_key = 'tua-chiave-segreta-qui'
PASSWORD = 'tuapassword123'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == PASSWORD:
            session['logged_in'] = True
            return redirect('/')
    return '''
        <form method="post">
            <input type="password" name="password" placeholder="Password">
            <button type="submit">Login</button>
        </form>
    '''

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect('/login')
    # resto del codice...
```

## 💡 Suggerimenti Pro

1. **Backup prima di modificare**: Copia sempre i file prima di modificarli
2. **Testa le modifiche**: Genera un contratto di prova dopo ogni modifica
3. **Usa commenti**: Documenta le tue modifiche con commenti nel codice
4. **Versioning**: Usa Git per tracciare le modifiche
5. **Validazione**: Aggiungi controlli di validazione per campi importanti

## 🐛 Debug

Se qualcosa non funziona dopo le modifiche:

1. Controlla la console del browser (F12)
2. Controlla i log del server Python
3. Verifica la sintassi (virgole, parentesi, apici)
4. Riavvia il server dopo modifiche a `app.py`

---

**Buona personalizzazione!** 🎨
