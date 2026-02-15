# Harm Scenarios  
## AI Governance Case Study — Facial Recognition Access Control System

This document outlines realistic harm scenarios that illustrate how failures, misuse, or weaknesses in the Facial Recognition Access Control System could negatively impact individuals, operations, and the organization. These scenarios support risk prioritization and guide the development of appropriate controls.

---

## Scenario 1: Unauthorized Access via Spoofing Attack

**Description:**  
An attacker uses a high‑resolution printed photo or a deepfake video to fool the facial recognition camera. The system incorrectly identifies the attacker as an authorized employee.

**Potential Harms:**  
- Unauthorized entry into restricted areas  
- Theft of sensitive equipment or data  
- Physical safety risks to staff  
- Incident response costs and operational disruption  
- Loss of trust in security systems  

**Contributing Factors:**  
- Weak or absent liveness detection  
- Overly permissive matching thresholds  
- Lack of secondary authentication  

---

## Scenario 2: Legitimate Employee Locked Out (False Rejection)

**Description:**  
A legitimate employee is repeatedly denied access due to lighting changes, camera angle issues, or demographic bias in the model.

**Potential Harms:**  
- Delayed access to work areas  
- Missed shifts or reduced productivity  
- Increased frustration and morale impact  
- Higher helpdesk workload  
- Perception of unfair or discriminatory treatment  

**Contributing Factors:**  
- Model bias across demographic groups  
- Environmental variability  
- Insufficient fallback or override processes  

---

## Scenario 3: Biometric Data Breach

**Description:**  
A threat actor gains unauthorized access to the biometric template database due to misconfigured access controls or weak encryption.

**Potential Harms:**  
- Permanent compromise of individuals’ biometric identifiers  
- Regulatory penalties (e.g., BIPA, GDPR)  
- Class‑action lawsuits  
- Reputational damage  
- Mandatory system shutdown or redesign  

**Contributing Factors:**  
- Inadequate encryption-at-rest  
- Excessive retention of biometric data  
- Weak IAM controls around privileged access  

---

## Scenario 4: Model Drift Leading to Widespread Failures

**Description:**  
Over time, environmental changes (new lighting, updated cameras, aging workforce) cause the model’s accuracy to degrade. False rejections and false acceptances increase significantly.

**Potential Harms:**  
- Operational bottlenecks  
- Increased security incidents  
- Loss of confidence in the system  
- Emergency fallback to manual processes  

**Contributing Factors:**  
- Lack of continuous monitoring  
- No scheduled model retraining  
- Insufficient performance metrics tracking  

---

## Scenario 5: Misuse of Biometric Data for Surveillance

**Description:**  
Employees fear that facial recognition data is being used to track their movements or behavior beyond access control purposes.

**Potential Harms:**  
- Reduced morale and trust  
- Perceived or actual privacy violations  
- Ethical concerns and internal complaints  
- Potential legal exposure  

**Contributing Factors:**  
- Lack of transparency  
- Insufficient policy boundaries  
- Poor communication about system purpose  

---

## Scenario 6: System Outage During Peak Hours

**Description:**  
A network outage or camera failure prevents the system from authenticating users during a high‑traffic period.

**Potential Harms:**  
- Long entry lines and operational delays  
- Safety risks if emergency access is needed  
- Increased manual verification workload  
- Business continuity impacts  

**Contributing Factors:**  
- No redundancy or failover  
- Single point of failure in network or hardware  
- Lack of manual access procedures  

---

## Summary

These harm scenarios illustrate how failures in fairness, security, privacy, or reliability can create meaningful risks for individuals and the organization. They inform the control design and mitigation strategies developed in the next section of the case study.

---

## Next Steps

Proceed to the **03_Controls-and-Mitigations** folder to begin designing the control matrix and mitigation plan.
