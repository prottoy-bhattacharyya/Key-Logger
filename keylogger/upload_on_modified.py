import time
import os
from requests import post
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- CONFIGURATION ---
FILE_PATH = "log.txt" 
SERVER_URL = "http://192.168.1.138:5000/upload"  # Replace with your actual server IP
# ---------------------

class LogFileHandler(FileSystemEventHandler):
    def __init__(self, target_file):
        self.target_file = os.path.abspath(target_file)

    def on_modified(self, event):
        # Ensure we only trigger for our specific log file
        if os.path.abspath(event.src_path) == self.target_file:
            print(f"Changes detected in {FILE_PATH}. Uploading...")
            try:
                with open(self.target_file, 'rb') as f:
                    files = {'file': f}
                    response = post(SERVER_URL, files=files)
                if response.status_code == 200:
                    print("Upload successful.")
                else:
                    print(f"Failed to upload. Server responded with: {response.status_code}")
            except Exception as e:
                print(f"Error during upload: {e}")

if __name__ == "__main__":
    # Create the log file if it doesn't exist yet
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'w') as f:
            f.write("Log initialized.\n")

    event_handler = LogFileHandler(FILE_PATH)
    observer = Observer()
    
    # Watch the directory containing the log file
    watch_dir = os.path.dirname(os.path.abspath(FILE_PATH)) or "."
    observer.schedule(event_handler, path=watch_dir, recursive=False)
    observer.start()
    
    print(f"Monitoring '{FILE_PATH}' for changes... Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()