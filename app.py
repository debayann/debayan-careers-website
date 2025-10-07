from flask import Flask, render_template, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix
import os

app = Flask(__name__)

# Configure ProxyFix for Replit's reverse proxy
app.wsgi_app = ProxyFix(
    app.wsgi_app,
    x_for=1,
    x_proto=1,
    x_host=1,
    x_prefix=1
)

# Sample job data
JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'Remote',
        'department': 'Engineering',
        'description': 'We are looking for a talented software engineer to join our team.'
    },
    {
        'id': 2,
        'title': 'Product Manager',
        'location': 'New York, NY',
        'department': 'Product',
        'description': 'Seeking an experienced product manager to lead our product initiatives.'
    },
    {
        'id': 3,
        'title': 'UX Designer',
        'location': 'San Francisco, CA',
        'department': 'Design',
        'description': 'Join our design team to create beautiful and intuitive user experiences.'
    },
    {
        'id': 4,
        'title': 'Data Scientist',
        'location': 'Remote',
        'department': 'Data',
        'description': 'Help us derive insights from data and build machine learning models.'
    }
]

@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def get_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    # Debug mode controlled by environment variable
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)
