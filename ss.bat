@echo off
echo Teams Keep-Alive script running. Close this window to stop.
echo.

:loop
echo Simulating keypress at %time%
powershell -command "$wsh = New-Object -ComObject WScript.Shell; $wsh.SendKeys('{F15}')"
timeout /t 120 /nobreak
goto loop
