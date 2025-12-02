#!/bin/bash

echo "========================================"
echo " Generatore Contratti Kappa Team"
echo "========================================"
echo ""
echo "Installazione dipendenze..."
pip3 install -r requirements.txt
echo ""
echo "Avvio server..."
echo ""
echo "Il sistema sarà disponibile su: http://localhost:5000"
echo ""
echo "Premi CTRL+C per fermare il server"
echo ""
python3 app.py
