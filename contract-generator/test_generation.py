#!/usr/bin/env python3
"""Script di test per verificare la generazione del PDF"""

from app import generate_contract_pdf
import os

# Dati di test (stesso esempio del contratto caricato)
test_data = {
    'nomeCliente': 'CASOTTO DAVIDE',
    'luogoNascita': 'CITTADELLA',
    'dataNascita': '1999-08-24',
    'codiceFiscale': 'CSTDVD99M24C743M',
    'ragioneSociale': 'GS SOLUTIONS INT. LIMITED',
    'sedeCitta': 'HONG KONG',
    'sedeNazione': 'CN',
    'indirizzoCompleto': 'SUITE C, LEVEL 7, WORLD TRUST TOWER STANLEY STREET, CENTRAL',
    'partitaIva': '73853430',
    'numeroContratto': '06',
    'dataContratto': '2025-09-16',
    'luogoContratto': 'Trani',
    'budgetIniziale': '20000.00',
    'percentualeCommissione': '7',
    'commissione': '1400.00',
    'totaleVersamento': '21400.00',
    'impegnoMensile': '30000.00',
    'profiloProxy': True,
    'formazioneAdv': False,
    'prezzoFormazione': ''
}

print("🔍 Inizio test generazione PDF...")
print(f"📋 Dati cliente: {test_data['nomeCliente']}")
print(f"🏢 Azienda: {test_data['ragioneSociale']}")
print(f"📄 Contratto: KT-ONB-2025/{test_data['numeroContratto']}")

try:
    # Genera il PDF
    pdf_buffer = generate_contract_pdf(test_data)
    
    # Salva il PDF di test
    output_path = 'test_contract.pdf'
    with open(output_path, 'wb') as f:
        f.write(pdf_buffer.read())
    
    # Verifica che il file sia stato creato
    if os.path.exists(output_path):
        size = os.path.getsize(output_path)
        print(f"✅ PDF generato con successo!")
        print(f"📁 File: {output_path}")
        print(f"💾 Dimensione: {size} bytes")
        print(f"\n🎉 Test completato! Il sistema funziona correttamente.")
    else:
        print("❌ Errore: file PDF non trovato")
        
except Exception as e:
    print(f"❌ Errore durante la generazione: {str(e)}")
    import traceback
    traceback.print_exc()
