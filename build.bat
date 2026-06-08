@echo off
cd /d F:\math-encyclopedia
echo Building site...
call npx quartz build
if %ERRORLEVEL% neq 0 (
    echo Build failed!
    pause
    exit /b
)

echo Patching graph controls into all pages...
python patch_graph_controls.py

echo Done! Output in public/
pause
