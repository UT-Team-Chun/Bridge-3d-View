@echo off
echo Starting local server...

REM Check and create required directories
if not exist "nginx\temp" mkdir "nginx\temp"
if not exist "nginx\temp\client_body_temp" mkdir "nginx\temp\client_body_temp"
if not exist "nginx\temp\proxy_temp" mkdir "nginx\temp\proxy_temp"
if not exist "nginx\temp\fastcgi_temp" mkdir "nginx\temp\fastcgi_temp"
if not exist "nginx\logs" mkdir "nginx\logs"

REM Check nginx 
IF NOT EXIST "nginx\nginx.exe" (
  echo Error: nginx.exe not found!
  pause
  exit /b 1
)

REM close nginx if it is running
taskkill /F /IM nginx.exe /T >nul 2>nul

REM star nginx
cd nginx
start nginx.exe
cd ..

REM start http server
start http://localhost:8080

echo Server is running at http://localhost:8080
echo DO NOT close this window if you want to keep the server running.
echo To stop the server, just close this window.

REM keep the window open
pause

REM close nginx
taskkill /F /IM nginx.exe /T >nul 2>nul