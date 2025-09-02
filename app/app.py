from flask import Flask, jsonify, render_template
import os
import time

app = Flask(__name__)
START_TIME = time.time()

@app.route('/')
def home():
    return render_template('index.html',
        version=os.environ.get('APP_VERSION', 'v1.0.0'),
        environment=os.environ.get('ENVIRONMENT', 'production')
    )

@app.route('/health')
def health():
    return jsonify({
        'status': 'UP',
        'version': os.environ.get('APP_VERSION', 'v1.0.0'),
        'environment': os.environ.get('ENVIRONMENT', 'production'),
        'uptime_seconds': round(time.time() - START_TIME, 2)
    }), 200

@app.route('/api/info')
def info():
    return jsonify({
        'app': 'GitOps ArgoCD Delivery Engine',
        'author': 'Govind',
        'stack': ['Flask', 'Docker', 'Kubernetes', 'ArgoCD', 'GitOps'],
        'version': os.environ.get('APP_VERSION', 'v1.0.0'),
        'environment': os.environ.get('ENVIRONMENT', 'production')
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

