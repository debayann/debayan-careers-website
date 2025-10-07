import os
from flask import Flask, render_template, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'San Francisco, CA',
        'salary': '$120,000 - $150,000'
    },
    {
        'id': 2,
        'title': 'Data Analyst',
        'location': 'Remote',
        'salary': '$80,000 - $100,000'
    },
    {
        'id': 3,
        'title': 'Product Manager',
        'location': 'New York, NY',
        'salary': '$130,000 - $160,000'
    },
    {
        'id': 4,
        'title': 'DevOps Engineer',
        'location': 'Austin, TX',
        'salary': '$110,000 - $140,000'
    }
]

@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)
