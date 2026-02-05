@echo off
echo ========================================
echo   LangGraph AI Agent - Quick Start
echo ========================================
echo.
echo Starting Backend Server...
echo.

start "AI Agent Backend" cmd /k "cd /d G:\AI Agent && python backend.py"

timeout /t 5 /nobreak > nul

echo Backend started on http://127.0.0.1:9999
echo.
echo Starting Frontend UI...
echo.

start "AI Agent Frontend" cmd /k "cd /d G:\AI Agent && streamlit run frontend.py"

echo.
echo ========================================
echo   Both servers are starting...
echo   Backend: http://127.0.0.1:9999
echo   Frontend: http://localhost:8501
echo ========================================
echo.
echo Press any key to exit this window...
pause > nul
