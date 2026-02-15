# Impact Analysis  
## AI Governance Case Study — Facial Recognition Access Control System

This Impact Analysis evaluates how identified risks affect operations, privacy, security, fairness, and regulatory compliance. It provides deeper context for the Risk Register and supports prioritization of controls and governance actions.

---

## 1. Operational Impact

### **1.1 False Rejections (Legitimate Users Denied Access)**
- Disrupts employee workflow and productivity  
- Causes delays at entry points during peak hours  
- Increases helpdesk tickets and manual override requests  
- May require temporary fallback to badge-based access  

### **1.2 False Acceptances (Unauthorized Users Granted Access)**
- Compromises physical security  
- Enables unauthorized access to restricted areas  
- Increases incident response workload  
- May trigger internal investigations and facility lockdowns  

### **1.3 System Downtime or Camera Failure**
- Halts authentication entirely  
- Forces manual check-in procedures  
- Creates bottlenecks and operational slowdowns  
- Impacts business continuity  

---

## 2. Privacy Impact

### **2.1 Biometric Data Exposure**
- Facial templates are highly sensitive and irreversible  
- Breach could cause long-term identity risks  
- Users may lose trust in the organization’s security posture  

### **2.2 Excessive Data Retention**
- Storing biometric data longer than necessary increases risk  
- Violates privacy-by-design principles  
- May conflict with regional biometric laws  

### **2.3 Lack of Transparency**
- Users may not understand how their data is collected, stored, or used  
- Increases perception of surveillance  
- Reduces willingness to participate in biometric programs  

---

## 3. Security Impact

### **3.1 Spoofing and Deepfake Attacks**
- Attackers may bypass authentication using masks, photos, or digital forgeries  
- Leads to unauthorized access and potential data theft  
- Undermines trust in the system’s integrity  

### **3.2 Unauthorized Access to Biometric Databases**
- Compromised biometric templates cannot be “reset” like passwords  
- Attackers may use stolen templates for future impersonation  
- Requires costly incident response and forensic analysis  

### **3.3 Model Drift**
- Environmental changes (lighting, camera angle) reduce accuracy  
- Increased false positives/negatives over time  
- Requires ongoing monitoring and retraining  

---

## 4. Fairness & Ethical Impact

### **4.1 Demographic Bias**
- Uneven performance across age, gender, or ethnicity  
- Higher false rejection rates for certain groups  
- Creates inequitable access experiences  
- May lead to discrimination claims  

### **4.2 Lack of Human Oversight**
- Automated decisions without human review increase harm  
- Users may feel powerless when denied access  
- Violates responsible AI principles  

### **4.3 Perceived Surveillance**
- Facial recognition may create discomfort or fear  
- Impacts employee morale and workplace culture  

---

## 5. Compliance & Regulatory Impact

### **5.1 Violations of Biometric Privacy Laws**
- Laws such as BIPA, GDPR, and state-level biometric acts impose strict requirements  
- Non-compliance may result in:  
  - Fines  
  - Lawsuits  
  - Mandatory system shutdown  
  - Regulatory audits  

### **5.2 Insufficient Documentation**
- Missing DPIAs, model cards, or transparency reports  
- Fails audit requirements  
- Creates gaps in governance evidence  

### **5.3 Inadequate Access Controls**
- Violates IAM and SOX-aligned control expectations  
- Leads to audit findings and remediation requirements  

---

## Summary

The Facial Recognition Access Control System introduces significant operational, privacy, security, fairness, and compliance impacts. High-risk areas include biometric data protection, spoofing vulnerabilities, demographic bias, and regulatory exposure. These impacts guide the control design and mitigation strategies documented in the next section.

---

## Next Steps
Proceed to:

- **03_Harm-Scenarios.md**
