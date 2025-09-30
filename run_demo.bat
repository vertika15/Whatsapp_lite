@echo off
echo 🟢 Running Step 1: State Machine Test

:: Run state machine test
python state_machine\test_state_machine.py

echo 🟢 Step 1 completed.
echo 🚀 Starting Step 2: Async Chat Server

:: Start server in background
start /B python async_chat\server.py
timeout /t 2

echo ➡️ Running Chat Client...
python async_chat\client.py

echo 🛑 Stopping Chat Server...
taskkill /IM python.exe /F
