# Risk Heat Map  
Version: 1.1  
Last Updated: 2026-01-10 (YYYY-MM-DD)

This heat map visualizes risks based on a 5x5 likelihood and impact model commonly used in enterprise risk management programs.

---

## 🎨 Severity Legend

| Severity | Meaning |
|---------|---------|
| 🟩 Low | Minimal impact, routine monitoring |
| 🟨 Moderate | Requires planned mitigation |
| 🟧 High | Requires prioritized action |
| 🟥 Critical | Requires immediate action |

---

## 📊 5x5 Risk Matrix

| **Likelihood ↓ / Impact →** | **Insignificant** | **Minor** | **Moderate** | **Major** | **Severe** |
|-----------------------------|-------------------|-----------|--------------|-----------|------------|
| **Almost Certain** | 🟨 | 🟧 | 🟥 | 🟥 | 🟥 |
| **Likely**          | 🟨 | 🟨 | 🟧 | 🟥 | 🟥 |
| **Possible**        | 🟩 | 🟨 | 🟨 | 🟧 | 🟥 |
| **Unlikely**        | 🟩 | 🟩 | 🟨 | 🟨 | 🟧 |
| **Rare**            | 🟩 | 🟩 | 🟩 | 🟨 | 🟨 |

---

## 📌 Risk Mapping Table

| Risk ID | Likelihood | Impact | Severity | Heat Map Position |
|--------|------------|--------|----------|-------------------|
| R-001 | Possible | Major | 🟧 High | (Possible, Major) |
| R-002 | Rare | Severe | 🟨 Moderate | (Rare, Severe) |
| R-003 | Almost Certain | Moderate | 🟥 Critical | (Almost Certain, Moderate) |
| R-004 | Likely | Major | 🟥 Critical | (Likely, Major) |
| R-005 | Possible | Major | 🟧 High | (Possible, Major) |

---

## 📝 Notes

- Severity is determined by combining likelihood and impact using the matrix above.  
- Risks rated **🟥 Critical** require immediate mitigation planning and executive visibility.  
- Risks rated **🟧 High** require prioritized remediation within the current cycle.  
- Risks rated **🟨 Moderate** require planned mitigation and monitoring.  
- Risks rated **🟩 Low** require routine monitoring only.

---

## 📅 Review Cycle

This heat map should be reviewed quarterly or when major changes occur in technology, business operations, or regulatory requirements.
