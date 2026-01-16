# NIST Cybersecurity Framework (CSF) Control Mapping  
Version: 1.0  
Last Updated: 2025-12-14(YYYY-MM-DD)

This document provides a sample mapping of organizational controls to the NIST Cybersecurity Framework (CSF) Core Functions, Categories, and Subcategories.  
The purpose of this mapping is to demonstrate alignment between implemented controls and industry-standard cybersecurity practices.

---

## 🔐 1. Identify (ID)

| Category | Subcategory | Description | Example Control Implementation |
|----------|-------------|-------------|-------------------------------|
| ID.AM | ID.AM-1 | Physical devices and systems are inventoried | Asset inventory maintained in CMDB |
| ID.AM | ID.AM-2 | Software platforms and applications are inventoried | Application inventory tracked in governance tool |
| ID.RA | ID.RA-1 | Asset vulnerabilities are identified and documented | Vulnerability scans performed weekly |
| ID.RA | ID.RA-3 | Threats are identified and documented | Threat intelligence feeds integrated into SIEM |

---

## 🛡️ 2. Protect (PR)

| Category | Subcategory | Description | Example Control Implementation |
|----------|-------------|-------------|-------------------------------|
| PR.AC | PR.AC-1 | Identities and credentials are managed | MFA enforced for all users |
| PR.AC | PR.AC-4 | Access permissions are managed, incorporating least privilege | Quarterly access reviews |
| PR.DS | PR.DS-1 | Data-at-rest is protected | Encryption enabled on all storage |
| PR.AT | PR.AT-1 | All users receive cybersecurity awareness training | Annual training + phishing simulations |

---

## 🔍 3. Detect (DE)

| Category | Subcategory | Description | Example Control Implementation |
|----------|-------------|-------------|-------------------------------|
| DE.CM | DE.CM-1 | The network is monitored to detect cybersecurity events | SIEM monitoring 24/7 |
| DE.CM | DE.CM-7 | Monitoring for unauthorized personnel, connections, devices | EDR alerts and anomaly detection |
| DE.DP | DE.DP-4 | Event detection information is communicated | Alerts routed to SOC analysts |

---

## 🚨 4. Respond (RS)

| Category | Subcategory | Description | Example Control Implementation |
|----------|-------------|-------------|-------------------------------|
| RS.RP | RS.RP-1 | Response plan is executed during or after an incident | Incident Response Plan activated |
| RS.CO | RS.CO-2 | Incidents are reported consistent with criteria | Escalation matrix followed |
| RS.MI | RS.MI-1 | Incidents are contained | SOC isolates affected endpoints |

---

## 🔄 5. Recover (RC)

| Category | Subcategory | Description | Example Control Implementation |
|----------|-------------|-------------|-------------------------------|
| RC.RP | RC.RP-1 | Recovery plan is executed | Disaster Recovery Plan tested annually |
| RC.IM | RC.IM-1 | Recovery improvements are incorporated | Lessons learned documented |
| RC.CO | RC.CO-1 | Public relations managed | Communications team engaged |

---

## 📌 Notes  
- This mapping is a simplified example for portfolio demonstration.  
- Real-world mappings include deeper control references, owners, and evidence requirements.  
- This project aligns with NIST CSF v1.1 (still widely used in industry).

