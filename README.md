<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1f2e,100:0d1117&height=200&section=header&text=GitOps%20ArgoCD%20Delivery%20Engine&fontSize=32&fontColor=00d4ff&animation=fadeIn&fontAlignY=38&desc=Production-grade%20GitOps%20Platform%20by%20Govind&descAlignY=58&descSize=16&descColor=bc8cff" width="100%"/>

![CI/CD Pipeline](https://github.com/govinddevops/gitops-argocd-delivery-engine/actions/workflows/ci-cd.yml/badge.svg)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![ArgoCD](https://img.shields.io/badge/ArgoCD-EF7B4D?style=flat-square&logo=argo&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)

</div>

---

## 🚀 Overview

> **Production-grade GitOps Continuous Delivery Platform** using ArgoCD, Kubernetes, Docker and GitHub Actions. Git is the single source of truth — every deployment is automated, audited and self-healing.
```yaml
Author      : Govind
Stack       : Flask + Docker + Kubernetes + ArgoCD + GitHub Actions
Strategy    : GitOps — Git as single source of truth
Environments: dev + prod (Kustomize overlays)
Uptime SLA  : 99.9%
```

---

## 🏗️ Architecture
```
Developer pushes code
        ↓
┌─────────────────────┐
│   GitHub Actions    │  ← Lint · Test · Build · Push
└────────┬────────────┘
         ↓
┌─────────────────────┐
│     DockerHub       │  ← govinddevopsdocker/gitops-app
└────────┬────────────┘
         ↓
┌─────────────────────┐
│  Manifest Updated   │  ← K8s YAML image tag bumped
└────────┬────────────┘
         ↓
┌─────────────────────┐
│  ArgoCD Detects     │  ← Git drift detected
│  Drift & Syncs      │  ← Auto self-heal
└────────┬────────────┘
         ↓
┌─────────────────────┐
│  Kubernetes Cluster │  ← Rolling update
│  dev / prod         │  ← Zero downtime
└─────────────────────┘
```

---

## 🧰 Tech Stack

| Tool | Purpose |
|---|---|
| 🐍 Flask | Lightweight Python web app |
| 🐳 Docker | Multi-stage optimized container |
| ☸️ Kubernetes | Container orchestration |
| 🔄 ArgoCD | GitOps continuous delivery |
| ⚙️ GitHub Actions | CI pipeline — test, build, push |
| 📦 Kustomize | Multi-environment K8s configs |
| 🐧 Linux | Underlying infrastructure |

---

## 📁 Project Structure
```
gitops-argocd-delivery-engine/
├── 📁 app/
│   ├── app.py                  ← Flask application
│   ├── requirements.txt        ← Python dependencies
│   └── templates/
│       └── index.html          ← Beautiful UI
├── 📁 k8s/
│   ├── base/
│   │   ├── deployment.yaml     ← K8s Deployment
│   │   ├── service.yaml        ← K8s Service
│   │   └── kustomization.yaml  ← Base kustomize
│   └── overlays/
│       ├── dev/                ← Dev environment
│       └── prod/               ← Prod environment
├── 📁 argocd/
│   └── application.yaml        ← ArgoCD Application
├── 📁 .github/workflows/
│   └── ci-cd.yml               ← GitHub Actions pipeline
├── Dockerfile                  ← Multi-stage build
└── README.md
```

---

## ⚙️ GitHub Actions Pipeline
```
Push to main
     ↓
🧪 Test & Lint     ← Python tests + Flake8
     ↓
🐳 Build & Push    ← Docker image → DockerHub
     ↓
📋 Update Manifest ← Image tag bumped in K8s YAML
     ↓
✅ Verify          ← Manifest validation
```

---

## 🚀 Quick Start
```bash
# Clone the repo
git clone https://github.com/govinddevops/gitops-argocd-delivery-engine.git
cd gitops-argocd-delivery-engine

# Run locally with Docker
docker build -t gitops-app .
docker run -p 5000:5000 gitops-app

# Open in browser
http://localhost:5000
```

---

## ☸️ Deploy with ArgoCD
```bash
# Install ArgoCD
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Apply ArgoCD Application
kubectl apply -f argocd/application.yaml

# Access ArgoCD UI
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

---

## 🔗 API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Beautiful landing page |
| `/health` | GET | Health check — returns UP/DOWN |
| `/api/info` | GET | App info — version, stack, author |

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1f2e,100:0d1117&height=100&section=footer&animation=fadeIn" width="100%"/>

**Built with ❤️ by Govind · Junior DevOps Engineer**

⭐ Star this repo if it helped you!

</div>

