# 🐧 Linux & Docker Environment Setup for AppSec CI Pipelines

Engineering notes for configuring Linux (Ubuntu/Debian) hosts and Docker container engines for automated application security scanning pipelines.

---

## 🛠️ System Prerequisites

Most AppSec tooling (Semgrep, Trivy, OWASP ZAP, Nuclei) operates natively on Linux container environments.

```bash
# Update base system packages
sudo apt update && sudo apt upgrade -y

# Install core CLI tools & dependencies
sudo apt install -y curl wget git jq python3-pip apt-transport-https ca-certificates

# Install Docker Engine
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
```

---

## ⚙️ Security Pipeline Scanning Architecture

```
[GitHub Trigger / Push] ──> [Runner Environment (Ubuntu)]
                                  │
          ┌───────────────────────┼───────────────────────┐
          ▼                       ▼                       ▼
   [Semgrep SAST]          [Trivy SCA Scan]       [OWASP ZAP DAST]
  (Code Vulnerabilities) (Dependency CVEs)       (Live HTTP Attacks)
          │                       │                       │
          └───────────────────────┼───────────────────────┘
                                  ▼
                    [GitHub Issues Auto-Creation]
```
