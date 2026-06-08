@echo off
cd /d F:\math-encyclopedia

echo Stopping old servers...
taskkill /F /IM node.exe >nul 2>&1
timeout /t 2 >nul

echo Building site first...
call npx quartz build
if %ERRORLEVEL% neq 0 (
    echo Build failed!
    pause
    exit /b
)

echo Patching graph controls into all pages...
python patch_graph_controls.py

echo.
echo ========================================
echo  Your local IPs:
for /f "tokens=2 delims=:" %%i in ('ipconfig ^| findstr /C:"IPv4"') do (
    echo    http://%%i:31415
)
echo.
echo  Or try: http://localhost:31415
echo.
echo  Press Ctrl+C to stop
echo ========================================
echo.

python serve_network.py
if %ERRORLEVEL% neq 0 (
    echo Port 31415 might be busy, trying 31416...
    python -c "import http.server, socketserver, os; h=lambda *a,**k: type('H',(http.server.SimpleHTTPRequestHandler,),{'do_GET':lambda s:(setattr(s,'path',s.path+('.html' if not s.path.endswith(('.html','/')) and not os.path.exists(os.path.join('public',s.path.lstrip('/'))) else '')) or http.server.SimpleHTTPRequestHandler.do_GET(s)})(*a,**k); httpd=socketserver.TCPServer(('0.0.0.0',31416),h); httpd.serve_forever()" --directory public
)
pause
