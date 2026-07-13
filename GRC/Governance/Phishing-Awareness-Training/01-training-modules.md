# Phishing Awareness Training Program
### Employee Security Awareness Series — Module Set 1: Phishing & Social Engineering

**Prepared by:** John Garcia Jr.

**Audience:** General non-technical employees

**Format:** Self-paced training with knowledge check

**Estimated time:** 20–25 minutes

---

## Program Objectives

By the end of this training, employees will be able to:

1. Define phishing and explain why it remains the most common initial access vector for attackers
2. Identify the major delivery channels used in phishing attacks (email, SMS, voice, social media)
3. Recognize the common psychological triggers social engineers rely on
4. Spot red flags in a suspicious message before acting on it
5. Know the correct reporting procedure when something looks off

This maps loosely to the intent behind NIST's security awareness and training guidance (SP 800-50 / SP 800-16) — I don't have the current section-by-section structure memorized with full confidence, so if you cite specific clause numbers in your portfolio README, verify against the current NIST publication before publishing.

---

## Module 1: What Is Phishing, and Why Does It Work?

**Definition:** Phishing is a social engineering attack where an attacker impersonates a trusted entity — a coworker, vendor, bank, or internal system — to trick a person into taking an action that benefits the attacker: clicking a link, opening an attachment, entering credentials, or transferring money/data.

**Why it works — the psychology behind it:**

Attackers exploit predictable human decision-making shortcuts rather than technical vulnerabilities. The most commonly used levers are:

| Trigger | How it's used |
|---|---|
| **Urgency / time pressure** | "Your account will be suspended in 2 hours" — pushes the target to skip verification steps |
| **Authority** | Impersonating a CEO, IT admin, or auditor so the request feels non-optional |
| **Fear** | Fake security alerts, fake law enforcement notices, threats of account/legal consequences |
| **Curiosity** | "See who viewed your profile," unexpected invoice or shipment notices |
| **Trust / familiarity** | Spoofing a known coworker or vendor's name and writing style |
| **Reciprocity / helpfulness** | Posing as someone who needs a quick favor (gift cards, wire transfers, password resets) |

**Key point for employees:** Phishing succeeds by targeting *behavior*, not just technology. Even well-patched, well-monitored organizations get breached because one person clicked one link.

---

## Module 2: Threat Vectors — Where Phishing Shows Up

| Vector | Description | Example |
|---|---|---|
| **Email phishing** | Mass or semi-targeted fraudulent emails | Fake "password expired" notice |
| **Spear phishing** | Targeted at a specific individual using personal/organizational detail | Email referencing a real project name or coworker |
| **Whaling** | Spear phishing targeted at executives or high-value individuals | Fake board member requesting a wire transfer |
| **Business Email Compromise (BEC)** | Attacker compromises or spoofs a real business email account to request payment or data | "Vendor" invoice change request |
| **Smishing** | Phishing via SMS/text | "Your package couldn't be delivered, confirm address" |
| **Vishing** | Phishing via phone call, often combined with caller-ID spoofing | Fake "IT support" calling to "verify" a password |
| **Quishing** | Phishing via malicious QR codes | QR code on a flyer or parking meter leading to a credential-harvesting page |

---

## Module 3: Red Flags Checklist

Employees should be trained to pause and check for these signals before clicking, replying, or acting:

- **Sender mismatch** — display name looks legitimate, but the actual email address domain is off (extra letter, wrong TLD, look-alike domain)
- **Generic greeting** — "Dear Customer" instead of your name, from a sender who should know your name
- **Urgency or threat language** — pressure to act immediately, threats of account closure, legal action, or missed deadlines
- **Unexpected attachment or link** — especially `.zip`, `.exe`, or a link that doesn't match the display text (hovering shows a different URL)
- **Request for credentials or payment info** — legitimate IT/finance will not ask for a password via email or text
- **Poor grammar/formatting inconsistent with the sender** — not always present in sophisticated attacks, but still a useful signal
- **Unusual request from a known contact** — especially involving money, gift cards, or sensitive data, even if the tone sounds right — verify through a second channel (phone call, in-person) before acting

**One clarifying note for your own use:** the specific weighting or scoring of these red flags (i.e., which ones are the "strongest" predictors) varies by organization and by the phishing simulation vendor's own research (e.g., KnowBe4, Proofpoint publish their own phishing report statistics periodically). I don't have current, verifiable figures for those reports memorized, so if you want to cite a specific statistic like "X% of breaches start with phishing" in your published README, pull the current figure directly from a source like Verizon's DBIR or Proofpoint's State of the Phish report rather than a number I generate, since those percentages change year to year and I can't confirm the current one without checking.

---

## Module 4: What To Do When You Spot Something Suspicious

1. **Do not click, reply, forward, or download** anything in the message
2. **Do not enter credentials** on any linked page
3. **Report it** using your organization's official reporting channel (e.g., "Report Phishing" button, forwarding to a security mailbox, or a ticket to IT/Security)
4. **If you already clicked or entered credentials:** report immediately anyway — fast reporting is what limits damage, and organizations should have a no-blame reporting culture for this reason
5. **Verify unusual requests through a separate channel** — call the person or vendor using a known phone number, not one provided in the suspicious message

---

## Module 5: Knowledge Check (Quiz)

See companion file `03-knowledge-check.md` for a formatted 8-question quiz with answer key, suitable for a simple LMS or Google Form.

---

## Notes for Portfolio Presentation

- This is designed to demonstrate **security awareness program design**, one of the practical skill areas GRC/analyst roles look for beyond framework/control mapping.
- Pair this with the phishing sample set (`02-phishing-samples-answer-key.md`) and, if you want to go further, a one-page "training effectiveness metrics" template showing how you'd measure click-rate reduction and reporting-rate increase over time.
- Consider explicitly noting in your README that this is an original training deliverable you built for portfolio purposes, not sourced from a specific employer's proprietary program — that keeps things clean for public GitHub posting.
