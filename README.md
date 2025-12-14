# Codesafe Secure File Download Challenge

Proof-of-concept Codesafe challenge for INF 113 Homework 6
Nathan Hillyer, Chisom Eze, James Kim

The challenge is designed to teach **secure software engineering principles**
through a realistic, scenario-based coding task. Learners are given an existing
Python codebase with real functionality and must identify and remediate a
**directory traversal vulnerability** without breaking existing behavior.

---

## 🔐 Challenge Overview: Secure File Download Service

**Concepts covered:**
- Secure file handling
- Directory traversal vulnerabilities (CWE-22)
- Defensive programming
- Preserving existing functionality while patching security flaws

**Difficulty:** Beginner → Intermediate  
**Estimated completion time:** 30–60 minutes  
**Language:** Python

---

## 📁 Repository Structure
```
platform-tutorial/
└── secure-file-download/
├── DESCRIPTION.md # Scenario and challenge instructions
├── modify_me.py # Starter source code (100+ LOC)
├── checker # Automated tests and security checks
├── .init # Environment initialization script
└── backups/
└── modify_me.py # Immutable backup of starter code
```
---

## 🎯 Educational Goals

This challenge aligns with the **Codesafe Product Vision, Goals, and Scope** by:

- Providing hands-on practice with real-world software vulnerabilities
- Reinforcing secure coding practices in an authentic engineering context
- Allowing learners to experiment safely in a sandboxed environment
- Supporting incremental skill development in software security

---

## 🚀 Deployment

This challenge is compatible with the Codesafe / DOJO infrastructure and can be
deployed by importing this repository as a dojo within the Codesafe platform.

