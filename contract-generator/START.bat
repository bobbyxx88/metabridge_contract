@echo off
echo ========================================
echo  Generatore Contratti Kappa Team
echo ========================================
echo.
echo Installazione dipendenze...
pip install -r requirements.txt
echo.
echo Avvio server...
echo.
echo Il sistema sara' disponibile su: http://localhost:5000
echo.
echo Premi CTRL+C per fermare il server
echo.
python app.py
pause
