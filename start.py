import subprocess
import sys
import time
import os

def main():
    print("🚀 Starting CareerLens AI...")
    
    # 1. Start FastAPI Backend
    print("-> Booting Backend (Port 8000)")
    backend_process = subprocess.Popen(
        [sys.executable, "main.py"], 
        cwd=os.path.join(os.getcwd(), "backend")
    )
    
    time.sleep(2)
    
    # 2. Start Vite Frontend
    print("-> Booting Frontend (Port 5173)")
    is_windows = sys.platform.startswith('win')
    frontend_process = subprocess.Popen(
        ["npm", "run", "dev"], 
        cwd=os.path.join(os.getcwd(), "frontend"),
        shell=is_windows 
    )

    try:
        print("\n✅ System running! Press Ctrl+C to shut everything down.\n")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Shutting down servers...")
        backend_process.terminate()
        frontend_process.terminate()
        sys.exit(0)

if __name__ == "__main__":
    main()