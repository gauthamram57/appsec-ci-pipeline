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
├── docs/
│   └── linux-docker-pipeline-setup.md
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

## Visual Representations

### Homepage

<img width="1919" height="1019" alt="Screenshot 2026-06-08 212413" src="https://github.com/user-attachments/assets/58c8655d-56b3-413b-80df-9c5db217e8ff" />

### Comments Page

<img width="1919" height="1013" alt="Screenshot 2026-06-09 094933" src="https://github.com/user-attachments/assets/4b128b9c-d892-4c80-b9f2-cc3e58bad65d" />

### GitHub Actions Security Pipeline

The CI/CD pipeline automatically executes:

- Semgrep (SAST)
- Trivy Filesystem Scan
- Trivy Container Image Scan
- Docker Build Validation
- OWASP ZAP DAST Scan

The OWASP ZAP scan successfully analyzes the deployed application and automatically creates GitHub Issues containing discovered security findings.

<img width="1913" height="856" alt="Screenshot 2026-06-09 095603" src="https://github.com/user-attachments/assets/9f114985-c3ea-4c01-b678-f04b7b4349c7" />


Note: The workflow is marked as failed due to a known artifact-upload issue in the upstream OWASP ZAP GitHub Action (`zaproxy/action-baseline`). Security scanning completes successfully and vulnerability reports are generated in the repository Issues section.

### OWASP ZAP Findings

<img width="1891" height="850" alt="image" src="https://github.com/user-attachments/assets/752fc873-bf18-4aea-b17a-94fd6ef753d1" />
<img width="1879" height="857" alt="image" src="https://github.com/user-attachments/assets/cca76041-b33e-4075-bcbc-cfc110ecef37" />
<img width="1881" height="839" alt="image" src="https://github.com/user-attachments/assets/787554fb-c63d-42b4-9aec-8504338b8e19" />

### Render Deployment

<img width="1919" height="1018" alt="Screenshot 2026-06-09 094309" src="https://github.com/user-attachments/assets/0e5ac068-b677-46a6-8b3f-4d4c0104a128" />

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
