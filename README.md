[![Python Flask Cowsay Tests](https://github.com/donaldsa18/flask-cowsay/actions/workflows/python-app.yml/badge.svg)](https://github.com/donaldsa18/flask-cowsay/actions/workflows/python-app.yml)

[![Build and Push Docker Image](https://github.com/donaldsa18/flask-cowsay/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/donaldsa18/flask-cowsay/actions/workflows/docker-publish.yml)

# 🐮 Flask Cowsay

A tiny web app + API that wraps the classic [`cowsay`](https://pypi.org/project/cowsay/) library with a Flask interface.  
Say things with ASCII cows (and other animals).

---

## 🚀 Features
- Web UI with form + live ASCII output
- Docker support for easy deployment

---

## 📦 Installation

Clone the repo and set up a virtual environment:

```bash
git clone https://github.com/donaldsa18/flask-cowsay.git
cd flask-cowsay

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```
---

## ▶️ Run (Dev Mode)

Activate your virtual environment and start the server:

```bash
source .venv/bin/activate   # Windows: .venv\Scripts\activate
python app.py
```

---

## ▶️ Tests

Activate your virtual environment and start the server:

```bash
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pytest
```