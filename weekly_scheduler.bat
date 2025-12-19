@echo off
cd /d "D:\Downloads\AMDARI CONSULTANCY\Amdari Retailio Datalake"

python generateWeekly.py >> weekly_output.txt 2>&1 || exit /b 1
python load.py >> weekly_output.txt 2>&1 || exit /b 1

exit /b 0
