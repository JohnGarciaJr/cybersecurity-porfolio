# Risk Register  
## AI Governance Case Study — Facial Recognition Access Control System

This Risk Register identifies and categorizes risks associated with the Facial Recognition Access Control System. Each risk includes likelihood, impact, risk score, and mapped controls aligned with NIST AI RMF, NIST 800‑53, ISO 27001, and IAM governance practices.

---

## Risk Scoring Method
- **Likelihood:** Low (1), Medium (2), High (3)  
- **Impact:** Low (1), Medium (2), High (3)  
- **Risk Score:** Likelihood × Impact  
- **Risk Level:**  
  - 1–2 = Low  
  - 3–4 = Medium  
  - 6–9 = High  

---

## Risk Register Table

| ID | Risk Category | Description | Likelihood | Impact | Risk Score | Risk Level | Control Mapping | Owner |
|----|---------------|-------------|------------|--------|------------|------------|-----------------|--------|
| R‑01 | **Bias / Fairness** | Model performs unevenly across demographic groups, leading to false rejections or approvals. | 3 | 3 | **9** | **High** | NIST AI RMF: MAP, MEASURE; NIST 800‑53: RA‑3, SA‑11; Fairness Testing | AI/ML Team |
| R‑02 | **Security – Spoofing** | Attackers use printed photos, masks, or deepfakes to bypass facial recognition. | 3 | 3 | **9** | **High** | Liveness Detection, MFA, AC‑3, IA‑2 | Security Engineering |
| R‑03 | **False Acceptance** | System incorrectly grants access to an unauthorized individual. | 2 | 3 | **6** | **High** | Threshold Tuning, Human-in-the-Loop, Audit Logs | IAM Governance |
| R‑04 | **False Rejection** | Authorized users are denied access, disrupting operations. | 2 | 2 | **4** | Medium | Override Process, Helpdesk Escalation, Monitoring | Operations |
| R‑05 | **Privacy – Biometric Retention** | Improper storage or excessive retention of biometric templates. | 2 | 3 | **6** | High | Data Minimization, Encryption, Retention Policy | Privacy Office |
| R‑06 | **Unauthorized Access to Biometric Data** | Breach exposes sensitive biometric templates. | 2 | 3 | **6** | High | Encryption-at-Rest, Access Controls, Key Management | Security Engineering |
| R‑07 | **Model Drift** | Accuracy degrades over time due to environmental or demographic changes. | 2 | 2 | **4** | Medium | Continuous Monitoring, Retraining Schedule | AI/ML Team |
| R‑08 | **Regulatory Non-Compliance** | System violates biometric privacy laws (e.g., BIPA, GDPR). | 1 | 3 | **3** | Medium | Legal Review, DPIA, Policy Alignment | Compliance |
| R‑09 | **Operational Failure** | Camera malfunction or network outage prevents authentication. | 2 | 2 | **4** | Medium | Redundancy, Failover, Manual Access Procedure | IT Operations |
| R‑10 | **Transparency Gaps** | Users do not understand how their biometric data is used. | 2 | 1 | **2** | Low | Transparency Notice, Model Card, User Education | Governance |

---

## Notes
- High‑risk items (scores 6–9) require immediate mitigation planning.  
- Medium‑risk items require monitoring and documented controls.  
- Low‑risk items require periodic review.  
- Controls will be expanded in **03_Controls-and-Mitigations**.

---

## Next Steps
Proceed to:

- **02_Impact-Analysis.md**  
- **03_Harm-Scenarios.md**
