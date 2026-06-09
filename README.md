# AppSec CI Pipeline

A hands-on Application Security (AppSec) and DevSecOps project demonstrating how modern security testing can be integrated into a CI/CD pipeline.

This project contains a deliberately vulnerable Django web application, automated security scanning with Semgrep, Trivy, and OWASP ZAP, Docker containerization, GitHub Actions automation, and cloud deployment on Render.

---

## Live Demo

Deployed Application:

https://appsec-ci-pipeline.onrender.com

---

## Project Overview

The goal of this project is to demonstrate how security can be integrated into the Software Development Lifecycle (SDLC).

The pipeline automatically performs:

- Static Application Security Testing (SAST)
- Software Composition Analysis (SCA)
- Dynamic Application Security Testing (DAST)
- Docker Image Building
- Automated Security Issue Creation

Whenever code is pushed to GitHub, security scans are executed automatically.

---

## Architecture

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
 ├── Semgrep (SAST)
 ├── Trivy (SCA)
 ├── Docker Build
 └── OWASP ZAP (DAST)
    │
    ▼
Security Findings
    │
    ▼
GitHub Issues
```

---

## Technology Stack

### Application

- Python 3.12
- Django
- SQLite

### Security

- Semgrep
- Trivy
- OWASP ZAP

### DevOps

- Docker
- GitHub Actions
- Render

---

## Features

- Django Web Application
- Search Functionality
- User Comment System
- Stored XSS Demonstration
- Dockerized Deployment
- Automated Security Testing Pipeline
- Cloud Deployment using Render
- Automatic GitHub Issue Creation from OWASP ZAP Findings

---

## Security Testing Pipeline

### Semgrep (SAST)

Semgrep performs Static Application Security Testing by analyzing source code without executing the application.

#### Purpose

- Detect insecure coding patterns
- Identify security vulnerabilities
- Enforce secure coding practices

#### Examples

- XSS vulnerabilities
- Insecure configurations
- Dangerous function usage

---

### Trivy (SCA)

Trivy performs Software Composition Analysis.

#### Purpose

- Scan dependencies
- Detect vulnerable packages
- Identify known CVEs

#### Examples

- Vulnerable Python packages
- Dependency risks
- Container vulnerabilities

---

### OWASP ZAP (DAST)

OWASP ZAP performs Dynamic Application Security Testing against the running application.

#### Purpose

- Simulate attacker behavior
- Discover security misconfigurations
- Detect missing security headers

#### Example Findings

- Missing Content Security Policy
- Missing HSTS Header
- Missing Permissions Policy
- Cache Control Issues

---

## Stored XSS Demonstration

This application intentionally contains a Stored Cross-Site Scripting (XSS) vulnerability for educational purposes.

### Workflow

1. User submits a comment.
2. Comment is stored in the database.
3. Comment is rendered without proper sanitization.
4. JavaScript executes in other users' browsers.

### Example Payload

```html
<script>alert('XSS')</script>
```

This vulnerability exists only for educational and testing purposes.

---

## CI/CD Workflow

GitHub Actions automatically executes the following workflow:

```text
Push Code
   │
   ▼
GitHub Actions
   │
   ├── Semgrep Scan
   ├── Trivy Scan
   ├── Docker Build
   └── OWASP ZAP Scan
   │
   ▼
Security Findings
```

---

## Deployment

The application is deployed on Render.

### Deployment Process

1. Push code to GitHub.
2. GitHub Actions runs security checks.
3. Docker image is built.
4. Render deploys the application.

---

## Project Structure

```text
appsec-ci-pipeline/
│
├── app/
├── webapp/
├── .github/
│   └── workflows/
│       └── security.yml
├── Dockerfile
├── requirements.txt
├── manage.py
└── README.md
```

---

## Screenshots

Add screenshots here after uploading them.

### Homepage

<img width="1919" height="1019" alt="Screenshot 2026-06-08 212413" src="https://github.com/user-attachments/assets/58c8655d-56b3-413b-80df-9c5db217e8ff" />

### Comments Page

![Comments](screenshots/comments.png)

### GitHub Actions

![Actions](screenshots/actions.png)

### OWASP ZAP Findings

![ZAP](screenshots/zap.png)

### Render Deployment

![Render](screenshots/render.png)

---

## Skills Demonstrated

### Application Security

- Web Application Security
- Cross-Site Scripting (XSS)
- Security Testing Methodologies
- Threat Detection

### DevSecOps

- CI/CD Security Automation
- Security Pipelines
- GitHub Actions
- Container Security

### Cloud & Infrastructure

- Docker
- Render Deployment
- Linux
- Git

---

## Learning Outcomes

This project helped develop practical experience in:

- Secure SDLC Concepts
- Application Security Testing
- DevSecOps Workflows
- Docker Containerization
- CI/CD Automation
- Cloud Deployment
- Vulnerability Management

---

## Disclaimer

This project intentionally contains security vulnerabilities for educational and research purposes.

Do not deploy intentionally vulnerable applications in production environments.

---

## Author

**Gautham Ram**

Application Security | DevSecOps | Cloud Security

GitHub: https://github.com/gauthamram57
