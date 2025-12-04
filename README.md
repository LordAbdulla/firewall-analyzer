# Firewall Analyzer Tool v1

A Python-based firewall rule analyzer that helps you manage, inspect, and detect potential issues in your firewall rules.  
Author: LordAbdulla

---

## Features

- List existing firewall rules  
- Add or remove rules interactively  
- Detect duplicate rules  
- Detect conflicting rules (ALLOW vs DENY on same port/protocol)  
- Identify open TCP/UDP ports  
- Save and load rules from a file  
- Command-line interface for quick and easy use  

---

## Clone the Repository

```bash
git clone https://github.com/LordAbdulla/firewall-analyzer-tool
cd firewall-analyzer-tool
-- Installation
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
-- Usage
python main.py
