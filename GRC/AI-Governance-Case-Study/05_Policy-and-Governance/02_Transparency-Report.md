# Transparency Report  
## Facial Recognition Access Control System  
### AI Governance Case Study

This Transparency Report explains how the Facial Recognition Access Control System works, what data it uses, how that data is protected, and what rights and safeguards are in place for individuals. It is designed to provide clear, accessible information to employees, visitors, and stakeholders.

---

## 1. Purpose of the System

The system is used to authenticate individuals entering secured areas by verifying their identity through facial recognition. It replaces or supplements badge-based access to improve security and streamline entry.

The system is **not** used for:

- Surveillance  
- Emotion detection  
- Productivity monitoring  
- Law enforcement identification  

---

## 2. How the System Works

### **2.1 Enrollment**
Authorized users provide a facial image during onboarding.  
A biometric template (a mathematical representation of facial features) is created.

### **2.2 Authentication**
When a user approaches an access point:

1. A camera captures a live image  
2. The system generates an embedding  
3. It compares the embedding to stored templates  
4. A match or non-match decision is made  

### **2.3 Human Oversight**
If the system cannot verify identity, security staff can manually approve access.

---

## 3. What Data Is Collected

The system collects:

- Facial biometric template (encrypted)  
- Timestamp of access attempts  
- Access point location  
- System decision (match / no match)  

The system does **not** collect:

- Raw video recordings (unless explicitly configured)  
- Emotion or behavioral data  
- Personal information beyond what is required for authentication  

---

## 4. How Data Is Protected

### **4.1 Encryption**
Biometric templates are encrypted using strong cryptography.

### **4.2 Access Controls**
Only authorized personnel with a legitimate business need may access biometric data.

### **4.3 Retention Limits**
Biometric data is retained only as long as necessary for authentication purposes.

### **4.4 Audit Logging**
All access attempts and administrative actions are logged and monitored.

---

## 5. User Rights & Options

Depending on jurisdiction and organizational policy, users may have the right to:

- Request information about their stored biometric data  
- Request deletion of their biometric template  
- Opt out of biometric authentication (where alternatives exist)  
- Challenge incorrect access decisions  

Users may contact the Privacy Office or Security Team for assistance.

---

## 6. Accuracy & Limitations

The system is highly accurate but may be affected by:

- Lighting conditions  
- Camera angle  
- Facial changes (e.g., glasses, facial hair)  
- Environmental factors  

False rejections may occur.  
False acceptances are rare but possible.

Human oversight is always available to resolve issues.

---

## 7. Fairness & Bias Mitigation

The system is evaluated for demographic performance disparities.  
Mitigation steps include:

- Threshold tuning  
- Bias testing  
- Continuous monitoring  
- Regular model updates  

Results are documented in the Model Card.

---

## 8. Compliance & Governance

The system complies with:

- Biometric privacy laws (e.g., BIPA, GDPR)  
- Organizational security policies  
- Responsible AI principles  
- IAM governance standards  

A Data Protection Impact Assessment (DPIA) is conducted prior to deployment.

---

## 9. Contact Information

For questions or concerns about the system, users may contact:

- **Privacy Office**  
- **Security Engineering**  
- **IAM Governance Team**  
- **Facilities & Operations**  

---

## 10. Summary

This Transparency Report provides clear information about how the Facial Recognition Access Control System works, what data it uses, and how individuals are protected. It supports trust, accountability, and responsible AI practices.
