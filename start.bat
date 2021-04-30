@echo off
start data.bat
title Loading... By El Mano
color 0a
set load=
set/a loadnum=0

:Loading
set load=%load%[]
cls
echo.
echo Loading... Please Wait...
echo --------------------
echo %load%
echo --------------------
ping localhost -n 2 >nul

set/a loadnum=%loadnum% +1
if %loadnum%==10 goto Done

goto Loading
:Done
call bot.bat
pause

exit
