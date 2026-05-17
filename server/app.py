from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'stored_logs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
SAVED_LOG_PATH = os.path.join(UPLOAD_FOLDER, 'log.txt')

@app.route('/')
def index():
    # Serves the HTML monitoring dashboard
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    # Overwrites the old log file with the new version
    file.save(SAVED_LOG_PATH)
    return jsonify({"status": "success", "message": "Log updated successfully"}), 200

@app.route('/api/log-content', methods=['GET'])
def get_log_content():
    if not os.path.exists(SAVED_LOG_PATH):
        return jsonify({"content": "Waiting for the first log upload..."})
    
    try:
        with open(SAVED_LOG_PATH, 'r', errors='ignore') as f:
            content = f.read()
        return jsonify({"content": content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # '0.0.0.0' allows external connections to reach the server
    app.run(host='0.0.0.0', port=5000, debug=True)