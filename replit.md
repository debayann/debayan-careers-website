# Debayan Careers Website

## Overview
A Flask-based careers website showcasing open job positions. This project was created as a Flask practice project and successfully imported and configured for the Replit environment.

**Purpose**: Careers website to display open job positions
**Technology Stack**: Python 3.11, Flask 3.0.0, HTML5, CSS3
**Current State**: Fully functional and ready for development/deployment

## Recent Changes
- **October 7, 2025**: Initial project setup in Replit environment
  - Installed Python 3.11 and Flask dependencies
  - Created Flask application with routing and templates
  - Added responsive CSS styling with gradient design
  - Configured Flask workflow for development server
  - Added Werkzeug ProxyFix middleware for Replit proxy compatibility
  - Set up deployment configuration with Gunicorn
  - Made debug mode environment-controlled (FLASK_DEBUG)
  - Created project documentation

## Project Architecture

### File Structure
```
.
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── templates/
│   └── home.html          # Main careers page template
├── static/
│   └── css/
│       └── style.css      # Application styling
└── replit.md              # Project documentation
```

### Application Components

#### Backend (app.py)
- Flask web server configured to run on 0.0.0.0:5000
- **Proxy Configuration**: Uses Werkzeug ProxyFix middleware to handle Replit's reverse proxy
  - Trusts proxy headers: X-Forwarded-For, X-Forwarded-Proto, X-Forwarded-Host, X-Forwarded-Prefix
  - Ensures correct URL generation and request handling in Replit environment
- Two routes:
  - `/` - Renders the careers homepage with job listings
  - `/api/jobs` - JSON API endpoint for job data
- In-memory job data storage (JOBS list)
- Debug mode controlled by FLASK_DEBUG environment variable (defaults to False for production safety)

#### Frontend
- **home.html**: Responsive careers page with job cards
- **style.css**: Modern gradient design with purple theme
  - Responsive grid layout for job cards
  - Hover effects and smooth transitions
  - Mobile-friendly design

### Dependencies
- Flask==3.0.0 - Web framework
- Werkzeug==3.0.1 - WSGI utilities
- gunicorn==21.2.0 - Production WSGI server

### Development Workflow
- **Name**: Flask Server
- **Command**: `python app.py`
- **Port**: 5000
- **Type**: Webview (displays website preview)
- **Environment**: Debug mode disabled by default (set FLASK_DEBUG=true to enable)

### Deployment Configuration
- **Target**: Autoscale (for stateless web applications)
- **Server**: Gunicorn - Production-grade WSGI server
- **Command**: `gunicorn --bind=0.0.0.0:5000 --reuse-port app:app`
- **Features**:
  - Port reuse for zero-downtime deployments
  - ProxyFix middleware handles Replit's reverse proxy headers
  - No debug mode in production for security

## Features
- Displays 4 sample job positions:
  - Software Engineer (San Francisco, CA)
  - Data Analyst (Remote)
  - Product Manager (New York, NY)
  - DevOps Engineer (Austin, TX)
- Each job card shows:
  - Job title
  - Location with icon
  - Salary range with icon
  - Apply Now button
- Responsive design adapts to mobile devices
- JSON API endpoint for programmatic access

## User Preferences
- No specific preferences documented yet

## Future Enhancement Ideas
- Add job application form functionality
- Connect to a database for persistent job storage
- Implement job search and filtering
- Add job categories/departments
- Create admin panel for managing job postings
- Integrate with applicant tracking system
