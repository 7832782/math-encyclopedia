@echo off
cd /d F:\math-encyclopedia
echo Killing old server...
taskkill /F /IM node.exe >nul 2>&1
timeout /t 2 >nul
echo Building and starting...
call npx quartz build --serve --port 31415
pause
