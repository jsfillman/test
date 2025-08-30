import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    title = os.getenv('TITLE', 'Hello from Intern Workshop')
    subtitle = os.getenv('SUBTITLE', 'Built live with GitHub + Docker 🚀')
    button_text = os.getenv('BUTTON_TEXT', 'Interns Rule ✨')
    
    return render_template('index.html', 
                         title=title, 
                         subtitle=subtitle, 
                         button_text=button_text)

@app.route('/status')
def status():
    return jsonify({
        "ok": True,
        "version": "1.0.0"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)