from flask import Flask, request, send_file, jsonify, session
from flask_cors import CORS
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from io import BytesIO
from datetime import datetime
import os

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = 'kt_bridge_secret_key_2025_secure_random_string'  # Chiave segreta per le sessioni

# Credenziali di accesso
USERNAME = 'kappabridgeteam'
PASSWORD = 'kt2025!@@'

@app.route('/login', methods=['POST'])
def login():
    """Endpoint per il login"""
    data = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')
    
    if username == USERNAME and password == PASSWORD:
        session['authenticated'] = True
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': 'Credenziali non valide'}), 401

@app.route('/check-auth', methods=['GET'])
def check_auth():
    """Verifica se l'utente è autenticato"""
    return jsonify({'authenticated': session.get('authenticated', False)})

@app.route('/logout', methods=['POST'])
def logout():
    """Logout dell'utente"""
    session.pop('authenticated', None)
    return jsonify({'success': True})

def format_date(date_str):
    """Converte data da formato ISO a formato italiano"""
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%d/%m/%Y')
    except:
        return date_str

def format_currency(amount):
    """Formatta importo in euro"""
    try:
        return f"€ {float(amount):,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    except:
        return amount

def generate_contract_pdf(data):
    """Genera il PDF del contratto compilato"""
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    
    # === PAGINA 1 ===
    
    # Logo MetaBridge in alto al centro
    logo_path = 'metabridge_logo.png'
    if os.path.exists(logo_path):
        # Logo centrato in alto
        logo_width = 100
        logo_height = 100
        logo_x = (width - logo_width) / 2
        logo_y = height - 120
        c.drawImage(logo_path, logo_x, logo_y, width=logo_width, height=logo_height, 
                   preserveAspectRatio=True, mask='auto')
    
    # Titolo - posizione fissa
    y = height - 145
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width/2, y, "CONTRATTO AGENCY")
    
    # Codice Contratto
    y -= 30
    c.setFont("Helvetica", 12)
    codice = f"KT-ONB-2025/{data['numeroContratto']}"
    c.drawCentredString(width/2, y, f"Codice Contratto: {codice}")
    
    # Spazio prima di TRA
    y -= 50
    
    # TRA
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "TRA")
    y -= 30
    
    # Dati Fornitore
    c.setFont("Helvetica", 11)
    c.drawString(50, y, "Kappa Team S.r.l., con sede legale in Via Enrico De Nicola, Trani (BT), P. IVA IT12687960968,")
    y -= 15
    c.drawString(50, y, 'in persona del legale rappresentante pro tempore, di seguito denominata "Fornitore",')
    y -= 35
    
    # E
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "E")
    y -= 30
    
    # Dati Cliente
    c.setFont("Helvetica", 11)
    nome_cliente = data['nomeCliente'].upper()
    luogo_nascita = data['luogoNascita'].upper()
    data_nascita_formatted = format_date(data['dataNascita'])
    cf = data['codiceFiscale'].upper()
    
    c.drawString(50, y, f"Il Sig./La Sig.ra {nome_cliente}, nato/a a {luogo_nascita} il {data_nascita_formatted}, C.F.")
    y -= 15
    c.drawString(50, y, f"{cf}, in qualità di legale rappresentante della società {data['ragioneSociale']},")
    y -= 15
    sede = f"con sede in {data['sedeCitta']} ({data['sedeNazione']}), {data['indirizzoCompleto']}"
    c.drawString(50, y, sede[:90])
    y -= 15
    if len(sede) > 90:
        c.drawString(50, y, sede[90:])
        y -= 15
    c.drawString(50, y, f"- P. IVA {data['partitaIva']}, di seguito denominato \"Cliente\".")
    y -= 35
    
    # PREMESSE
    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, y, "PREMESSE")
    y -= 25
    
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "a) Il Fornitore è titolare di infrastrutture pubblicitarie e account pubblicitari Meta (Facebook,")
    y -= 15
    c.drawString(50, y, "Instagram, ecc.) e offre servizi di gestione account pubblicitari a clienti per campagne di")
    y -= 15
    c.drawString(50, y, "marketing online.")
    y -= 20
    
    c.drawString(50, y, "b) Il Cliente intende utilizzare detti account esclusivamente per promuovere i propri prodotti/servizi")
    y -= 15
    c.drawString(50, y, "in conformità alle leggi italiane, europee e alle policy delle piattaforme Meta.")
    y -= 20
    
    c.drawString(50, y, "c) Le parti intendono regolare il rapporto contrattuale secondo le seguenti condizioni, che")
    y -= 15
    c.drawString(50, y, "costituiscono parte integrante e sostanziale del presente contratto.")
    y -= 30
    
    # ART. 1
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "ART. 1 – OGGETTO DEL CONTRATTO")
    y -= 20
    
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "1.1 Il presente contratto disciplina la fornitura, da parte del Fornitore, di account pubblicitari Meta")
    y -= 15
    c.drawString(50, y, "pronti all'uso, assistenza tecnica e strategica, gestione operativa e servizi accessori come indicati")
    y -= 15
    c.drawString(50, y, "all'art. 4.")
    y -= 20
    
    c.drawString(50, y, "1.2 Il Fornitore garantirà continuità di servizio H24, 7 giorni su 7, con sostituzione immediata")
    y -= 15
    c.drawString(50, y, "dell'account in caso di sospensione o ban non motivato e non imputabile al Cliente.")
    y -= 30
    
    # === PAGINA 2 ===
    c.showPage()
    y = height - 50
    
    # ART. 2
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "ART. 2 – OBBLIGHI DEL CLIENTE")
    y -= 20
    
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "2.1 Il Cliente si impegna a:")
    y -= 15
    c.drawString(50, y, "a) Utilizzare gli account esclusivamente per campagne white hat, conformi alle leggi (D.Lgs.")
    y -= 15
    c.drawString(50, y, "206/2005 Codice del Consumo; D.Lgs. 145/2007 sulla pubblicità ingannevole; D.Lgs. 70/2003 sul")
    y -= 15
    c.drawString(50, y, "commercio elettronico) e alle policy Meta;")
    y -= 20
    
    c.drawString(50, y, "b) Non promuovere prodotti o servizi illegali, fraudolenti, scam o fuorvianti, pena la risoluzione")
    y -= 15
    c.drawString(50, y, "immediata del contratto e l'applicazione della penale di cui all'art. 6;")
    y -= 20
    
    c.drawString(50, y, "c) Fornire in onboarding dichiarazioni veritiere circa le tipologie di campagne che intende svolgere;")
    y -= 20
    
    c.drawString(50, y, "d) Non cedere a terzi, vendere o subaffittare gli account pubblicitari forniti.")
    y -= 30
    
    # ART. 3
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "ART. 3 – RESPONSABILITÀ")
    y -= 20
    
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "3.1 Il Cliente è unico ed esclusivo responsabile dei contenuti pubblicitari e delle relative creatività,")
    y -= 15
    c.drawString(50, y, "nonché degli eventuali reclami, sanzioni o procedimenti derivanti dalle campagne.")
    y -= 20
    
    c.drawString(50, y, "3.2 In caso di violazione delle policy Meta o di norme di legge derivante da condotta del Cliente,")
    y -= 15
    c.drawString(50, y, "quest'ultimo manleva e tiene indenne il Fornitore da qualsiasi responsabilità civile, amministrativa")
    y -= 15
    c.drawString(50, y, "e penale.")
    y -= 30
    
    # ART. 4 - COMMISSIONI
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "ART. 4 – COMMISSIONI, SERVIZI E PROMOZIONI")
    y -= 22
    
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "4.1 Commissione sullo spending pubblicitario")
    y -= 18
    
    c.setFont("Helvetica", 10)
    percentuale = float(data['percentualeCommissione'])
    
    # Checkbox account Whitelist (7%)
    checkbox_whitelist = "[X]" if percentuale == 7.0 else "[ ]"
    c.drawString(70, y, f"{checkbox_whitelist} 7% sullo spending (account Whitelist)")
    y -= 15
    
    # Checkbox account Standard (5%)
    checkbox_standard = "[X]" if percentuale == 5.0 else "[ ]"
    c.drawString(70, y, f"{checkbox_standard} 5% sullo spending (account Standard)")
    y -= 25
    
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "4.2 Servizi inclusi")
    y -= 20
    
    c.setFont("Helvetica", 10)
    servizi_inclusi = [
        ("[X]", "Sblocco account", "Intervento tecnico per riattivazione in caso di ban ingiustificato"),
        ("[X]", "Pixel di backup", "Installazione e configurazione per continuità tracking"),
        ("[X]", "Sblocco inserzioni", "Richiesta di revisione e approvazione inserzioni respinte"),
        ("[X]", "Assistenza dedicata H24", "Supporto tecnico e strategico 7/7")
    ]
    
    for check, titolo, descrizione in servizi_inclusi:
        c.setFont("Helvetica-Bold", 10)
        c.drawString(70, y, f"{check} {titolo}")
        c.setFont("Helvetica", 9)
        c.drawString(95, y - 12, f"- {descrizione}")
        y -= 26
    
    y -= 5
    
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "4.3 Servizi opzionali")
    y -= 20
    
    # Profilo con proxy
    checkbox_proxy = "[X]" if data.get('profiloProxy') else "[ ]"
    c.setFont("Helvetica-Bold", 10)
    c.drawString(70, y, f"{checkbox_proxy} Profilo di sistema con proxy dedicato")
    y -= 13
    c.setFont("Helvetica", 9)
    
    # Gestione IVA
    if data.get('proxyEsenteIVA'):
        c.drawString(95, y, "€140,00/mese (esente IVA) – Include sostituzione immediata del profilo in")
    else:
        c.drawString(95, y, "€140,00/mese + IVA – Include sostituzione immediata del profilo in")
    y -= 11
    c.drawString(95, y, "caso di ban e proxy residenziale italiano")
    y -= 18
    
    # Formazione
    checkbox_form = "[X]" if data.get('formazioneAdv') else "[ ]"
    c.setFont("Helvetica-Bold", 10)
    c.drawString(70, y, f"{checkbox_form} Formazione advertising")
    y -= 13
    if data.get('formazioneAdv') and data.get('prezzoFormazione'):
        c.setFont("Helvetica", 9)
        c.drawString(95, y, f"Corso personalizzato su Meta Ads - €{data.get('prezzoFormazione')} + IVA")
        y -= 11
    else:
        c.setFont("Helvetica", 9)
        c.drawString(95, y, "Corso personalizzato su Meta Ads e strategie avanzate")
        y -= 11
    y -= 10
    
    y -= 10
    
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "4.4 La commissione pattuita e i costi dei servizi aggiuntivi restano acquisiti al Fornitore anche in")
    y -= 13
    c.drawString(50, y, "caso di recesso anticipato.")
    
    # === PAGINA 3 ===
    c.showPage()
    y = height - 50
    
    # ART. 5
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "ART. 5 – RECESSO DEL CLIENTE")
    y -= 16
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "5.1 Il Cliente può recedere in qualsiasi momento con comunicazione scritta.")
    y -= 13
    c.drawString(50, y, "5.2 L'importo netto sarà bonificato al Cliente entro 10 giorni lavorativi dalla verifica contabile.")
    y -= 20
    
    # ART. 6
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "ART. 6 – CLAUSOLA PENALE")
    y -= 16
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "6.1 Se il Cliente, dichiarando di fare pubblicità white hat, viene accertato nell'uso di tecniche")
    y -= 13
    c.drawString(50, y, "black hat o nella promozione di prodotti vietati, il Fornitore avrà diritto ad una penale di €3.000,00 + IVA.")
    y -= 20
    
    # ART. 7
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "ART. 7 – RISERVATEZZA E NDA")
    y -= 16
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "7.1 Tutti gli operatori del Fornitore sono vincolati da accordi di non divulgazione (NDA).")
    y -= 20
    
    # ART. 8
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "ART. 8 – PRIVACY")
    y -= 16
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "8.1 Ai sensi del Regolamento UE 2016/679 (GDPR), le parti dichiarano di aver preso visione")
    y -= 13
    c.drawString(50, y, "dell'Informativa Privacy allegata.")
    y -= 20
    
    # ART. 9
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "ART. 9 – LEGGE APPLICABILE E FORO COMPETENTE")
    y -= 16
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "9.1 Il presente contratto è regolato dalla legge italiana.")
    y -= 13
    c.drawString(50, y, "9.2 Foro competente: Trani (BAT)")
    y -= 25
    
    # ART. 10 - DATI FINANZIARI (stessa pagina 3)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "ART. 10 – PRIMO VERSAMENTO E MODALITÀ DI PAGAMENTO")
    y -= 18
    
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "1. Primo versamento")
    y -= 14
    
    c.setFont("Helvetica", 10)
    totale = format_currency(data['totaleVersamento'])
    c.drawString(50, y, f"Alla sottoscrizione del presente contratto, il Cliente si impegna a corrispondere al Fornitore")
    y -= 13
    c.drawString(50, y, f"un importo iniziale pari a complessivi {totale}, così ripartiti:")
    y -= 16
    
    # Calcola budget netto e commissione in base alla modalità
    budget_iniziale = float(data['budgetIniziale'])
    percentuale = float(data['percentualeCommissione'])
    commissione_compresa = data.get('commissioneCompresa', False)
    proxy_compreso = data.get('proxyCompreso', False)
    proxy_amount = 140 if data.get('profiloProxy') else 0
    
    # Commissione SEMPRE calcolata sul budget iniziale (stesso importo)
    commissione_val = budget_iniziale * percentuale / 100
    
    if commissione_compresa:
        # Budget netto = budget - commissione - proxy (se compreso)
        budget_netto = budget_iniziale - commissione_val
        if proxy_compreso and proxy_amount > 0:
            budget_netto -= proxy_amount
    else:
        # Commissione AGGIUNTIVA
        budget_netto = budget_iniziale
    
    budget = format_currency(budget_netto)
    commissione = format_currency(commissione_val)
    
    c.drawString(70, y, f"{budget} a titolo di budget pubblicitario iniziale;")
    y -= 13
    
    # Testo commissione
    if commissione_compresa:
        c.drawString(70, y, f"{commissione} a titolo di commissione pari al {data['percentualeCommissione']}% (compresa nel totale);")
    else:
        c.drawString(70, y, f"{commissione} a titolo di commissione pari al {data['percentualeCommissione']}% sul budget pubblicitario;")
    
    # Aggiungi proxy se selezionato
    if data.get('profiloProxy'):
        y -= 13
        if proxy_compreso:
            c.drawString(70, y, "€ 140,00 a titolo di servizio Profilo sistema con proxy dedicato (compreso nel totale);")
        else:
            c.drawString(70, y, "€ 140,00 a titolo di servizio Profilo sistema con proxy dedicato;")
    
    # Formazione
    if data.get('formazioneAdv') and data.get('prezzoFormazione'):
        y -= 13
        prezzo_form = format_currency(data.get('prezzoFormazione'))
        c.drawString(70, y, f"{prezzo_form} + IVA a titolo di Formazione advertising;")
    
    y -= 18
    
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "2. Impegno di spesa mensile")
    y -= 14
    
    c.setFont("Helvetica", 10)
    impegno = format_currency(data['impegnoMensile'])
    c.drawString(50, y, f"Il Cliente si obbliga a garantire, per ciascun mese di durata contrattuale, un investimento pubblicitario")
    y -= 13
    c.drawString(50, y, f"minimo pari a {impegno}, da effettuarsi mediante più ricariche successive in funzione delle esigenze operative.")
    y -= 18
    
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "3. Commissioni e corrispettivi sulle ricariche")
    y -= 14
    
    c.setFont("Helvetica", 10)
    c.drawString(50, y, f"Per ogni ricarica effettuata, il Cliente dovrà corrispondere al Fornitore:")
    y -= 13
    c.drawString(50, y, f"- una commissione pari al {data['percentualeCommissione']}% dell'importo ricaricato, fino al raggiungimento della soglia")
    y -= 13
    c.drawString(50, y, "  minima di spesa pubblicitaria di cui al precedente comma 2;")
    y -= 13
    
    # Aggiungi corrispettivo proxy se selezionato
    if data.get('profiloProxy'):
        c.drawString(50, y, "- un corrispettivo fisso pari a € 140,00 mensili per il servizio accessorio (profilo + proxy),")
        y -= 13
        c.drawString(50, y, "  da versarsi in aggiunta rispetto all'importo pubblicitario.")
        y -= 13
    
    y -= 8
    
    # NUOVO: Punto 4 - Saldo quota residua
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "4. Saldo della quota residua")
    y -= 14
    
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "La parte residua del budget pubblicitario mensile, dovrà essere corrisposta dal Cliente in due o")
    y -= 13
    c.drawString(50, y, "più tranche concordate con il fornitore e alle scadenze che verranno comunicate dallo stesso.")
    y -= 20
    
    # Dati bonifico
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "Dati bonifico:")
    y -= 14
    
    c.setFont("Helvetica", 10)
    c.drawString(70, y, "Beneficiario: KAPPA TEAM SRL")
    y -= 13
    c.drawString(70, y, "IBAN: LT443250040432947135")
    y -= 13
    c.drawString(70, y, "BIC: REVOLT21")
    y -= 13
    c.drawString(70, y, f"Causale: Codice Contratto KT-ONB-2025/{data['numeroContratto']} – Servizi advertising")
    
    # === PAGINA 4 - SOLO FIRME ===
    c.showPage()
    y = height - 100
    
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Letto, confermato e sottoscritto.")
    y -= 35
    
    c.setFont("Helvetica", 11)
    data_formatted = format_date(data['dataContratto'])
    c.drawString(50, y, f"Luogo e data: {data['luogoContratto']}, {data_formatted}")
    y -= 70
    
    # Firma Cliente
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "Il Cliente")
    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(50, y, f"{nome_cliente} – {data['ragioneSociale']}")
    y -= 100
    
    # Firma Fornitore
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "Il Fornitore")
    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "Kappa Team S.r.l.")
    y -= 10
    
    # Inserisci firma digitale PIÙ VICINA
    firma_path = 'firma_kappa_team.png'
    if os.path.exists(firma_path):
        c.drawImage(firma_path, 50, y - 55, width=120, height=60, preserveAspectRatio=True, mask='auto')
    
    y = 130
    
    # Logo MetaBridge nel footer
    logo_path = 'metabridge_logo.png'
    if os.path.exists(logo_path):
        footer_logo_width = 60
        footer_logo_height = 60
        footer_logo_x = (width - footer_logo_width) / 2
        c.drawImage(logo_path, footer_logo_x, 60, width=footer_logo_width, height=footer_logo_height,
                   preserveAspectRatio=True, mask='auto')
    
    # Footer
    c.setFont("Helvetica", 8)
    footer_text = "MetaBridge™ – Operato da Kappa Team S.r.l. – Italia. Orgogliosamente parte della Kappa Team Brand"
    c.drawCentredString(width/2, 35, footer_text)
    c.drawCentredString(width/2, 23, "Family, leader nelle soluzioni adv ad alto rendimento.")
    
    c.save()
    buffer.seek(0)
    return buffer

@app.route('/')
def index():
    with open('index.html', 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/generate-contract', methods=['POST'])
def generate_contract():
    try:
        data = request.json
        pdf_buffer = generate_contract_pdf(data)
        
        # Salva anche su Google Sheets (opzionale - da implementare)
        # save_to_google_sheets(data)
        
        return send_file(
            pdf_buffer,
            mimetype='application/pdf',
            as_attachment=True,
            download_name=f"Contratto_KT-ONB-2025_{data['numeroContratto']}.pdf"
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Per uso locale
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
