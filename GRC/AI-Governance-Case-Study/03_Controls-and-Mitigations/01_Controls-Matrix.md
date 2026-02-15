# Control Matrix  
## AI Governance Case Study — Facial Recognition Access Control System

This Control Matrix maps identified risks to specific governance, technical, and operational controls. Controls align with NIST AI RMF, NIST 800‑53, ISO 27001, and IAM governance best practices.

---

## Control Categories
- **Technical Controls** — system configuration, security mechanisms, model safeguards  
- **Administrative Controls** — policies, procedures, documentation  
- **Operational Controls** — monitoring, human oversight, escalation paths  

---

## Control Matrix Table

| Control ID | Control Name | Description | Risk(s) Mitigated | Control Type | Framework Mapping |
|------------|--------------|-------------|--------------------|--------------|-------------------|
| C‑01 | **Liveness Detection** | Detects whether a real human face is present to prevent spoofing. | R‑02 | Technical | NIST 800‑53 IA‑2, AC‑3; NIST AI RMF: MAP |
| C‑02 | **Threshold Tuning & Performance Calibration** | Adjusts model sensitivity to reduce false acceptances and rejections. | R‑01, R‑03, R‑04 | Technical | NIST AI RMF: MEASURE; ISO 27001 A.12 |
| C‑03 | **Demographic Bias Testing** | Evaluates model performance across demographic groups. | R‑01 | Technical / Administrative | NIST AI RMF: MEASURE; NIST 800‑53 SA‑11 |
| C‑04 | **Human-in-the-Loop Override** | Allows security staff to manually approve or deny access. | R‑03, R‑04 | Operational | NIST AI RMF: GOVERN; ISO 27001 A.9 |
| C‑05 | **Biometric Data Encryption-at-Rest** | Encrypts stored facial templates using strong cryptography. | R‑05, R‑06 | Technical | NIST 800‑53 SC‑28; ISO 27001 A.10 |
| C‑06 | **Strict Access Controls for Biometric Databases** | Limits access to biometric data to authorized personnel only. | R‑06 | Technical / Administrative | NIST 800‑53 AC‑6; SOX Access Governance |
| C‑07 | **Data Minimization & Retention Policy** | Ensures biometric data is stored only as long as necessary. | R‑05 | Administrative | GDPR Art. 5; NIST AI RMF: GOVERN |
| C‑08 | **Continuous Model Monitoring** | Tracks accuracy, drift, and error rates over time. | R‑07 | Operational | NIST AI RMF: MEASURE; ISO 27001 A.12 |
| C‑09 | **Scheduled Model Retraining** | Updates the model to maintain performance as conditions change. | R‑07 | Technical | NIST AI RMF: MANAGE |
| C‑10 | **Redundancy & Failover Procedures** | Ensures authentication continues during outages. | R‑09 | Operational | ISO 27001 A.17; NIST 800‑53 CP‑10 |
| C‑11 | **Manual Access Procedure** | Provides a fallback method when the system is unavailable. | R‑04, R‑09 | Operational | Business Continuity Best Practices |
| C‑12 | **Transparency Notice & User Education** | Communicates how biometric data is used and protected. | R‑10 | Administrative | NIST AI RMF: GOVERN; GDPR Transparency |
| C‑13 | **DPIA (Data Protection Impact Assessment)** | Evaluates privacy risks and compliance obligations. | R‑05, R‑08 | Administrative | GDPR Art. 35; NIST AI RMF: GOVERN |
| C‑14 | **Audit Logging & Monitoring** | Logs access attempts, overrides, and anomalies. | R‑03, R‑06 | Technical / Operational | NIST 800‑53 AU‑2, AU‑6 |
| C‑15 | **Security Awareness Training** | Educates staff on biometric security, spoofing risks, and escalation. | R‑02, R‑10 | Administrative | ISO 27001 A.7 |

---

## Summary

This Control Matrix provides a structured mapping between risks and mitigation strategies. Controls span technical safeguards, governance documentation, and operational procedures to ensure the system operates safely, fairly, and in compliance with regulatory requirements.

---

## Next Steps

Proceed to:

- **02_Mitigation-Plan.md**  
- **03_Governance-Controls-Map.md**
