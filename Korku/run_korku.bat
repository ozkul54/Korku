@echo off
setlocal

where py >nul 2>nul
if errorlevel 1 (
	echo Python bulunamadı. "py" komutunu çalıştırabilir hale getirin.
	exit /b 1
)

py -3.13 -m pip install -r "%~dp0requirements.txt"
py -3.13 "%~dp0korku"

exit /b %ERRORLEVEL%
