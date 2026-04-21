# 🧠 AI-Powered Reinsurance Contract Review

AI system that reviews reinsurance contracts in minutes instead of hours — identifying compliance risks, DORA gaps, and delegated authority issues through a multi-agent workflow.

Built for insurance operations, MGA teams, and reinsurance analysts handling delegated authority agreements.

---

## 🚀 What This Project Does

AI-powered multi-agent system that reviews reinsurance contracts and identifies:

- compliance risks (sanctions, regulatory gaps, DORA)
- missing clauses
- delegated authority weaknesses
- prioritised actions for human review

---

## 📌 Problem

Reinsurance contract review (especially binding authority agreements) is:

- time-consuming  
- repetitive  
- difficult to standardise  
- highly dependent on manual expertise  

Critical risks (sanctions, DORA compliance, delegated authority limits) are often:

- inconsistently identified  
- poorly documented  
- hard to audit  

---

## 💡 Solution

A **three-agent AI workflow** designed to automate and structure contract review:

- **Compliance Agent** → identifies regulatory risks, sanctions issues, and missing clauses  
- **Technical Terms Agent** → extracts operational contract structure (limits, bordereaux, reporting)  
- **Summary Agent** → consolidates outputs into actionable insights and prioritised risks  

Built using **Anthropic Claude API**.

---

## 🏗️ Architecture


Contract Text
↓
[Compliance Agent]
↓
[Technical Terms Agent]
↓
[Summary Agent]
↓
Structured Output
↓
Human Review


---

## 📊 Example Output

The system generates:

- sanctions analysis (including regime gaps)
- DORA compliance gaps
- missing clauses (GDPR, audit rights, escalation procedures)
- delegated authority weaknesses
- prioritised risk list
- actionable remediation steps

👉 See `/examples/sample_output.md`

---

## 💰 Impact

Manual contract review: ~2–4 hours per agreement  
AI-assisted review: minutes  

→ potential **80%+ reduction in review time**  
→ improved consistency and auditability  

---

## 🔄 Before vs After

**Before:**
- manual review  
- inconsistent outputs  
- difficult to audit  

**After:**
- structured outputs  
- consistent risk identification  
- clear human review workflow  

---

## 🤖 Why Multi-Agent Design

Instead of a single model doing everything, this system separates:

- Compliance analysis  
- Technical extraction  
- Executive summarisation  

→ improves accuracy, traceability, and explainability  

---

## 👤 Human-in-the-loop Design

The system does not make final decisions.

It:
- flags risks  
- structures information  
- prioritises actions  

Final decisions remain with human reviewers, aligning with regulatory expectations (e.g. DORA, sanctions frameworks).

---

## ⚙️ How to Run

```bash
pip install anthropic
import os
os.environ["ANTHROPIC_API_KEY"] = "your_api_key_here"

Run the notebook or Python script to execute the workflow.

🧪 Example Use Case

Input:

Binding authority agreement with bordereaux obligations and sanctions clause...

Output:

compliance risks identified
missing DORA obligations
delegated authority weaknesses
prioritised actions
⚠️ Limitations
Relies on prompt-based extraction (no fine-tuning)
Does not yet integrate with real document pipelines (PDF ingestion)
No automated validation of outputs

Future work includes structured outputs, evaluation metrics, and integration into underwriting workflows.

🚀 Next Steps
Convert outputs to structured JSON
Add Human-in-the-loop approval layer

All contracts used in this project are synthetic and generated for demonstration purposes. No real client or proprietary data is included.
Expand to claims triage workflows
Deploy as internal underwriting/compliance tool
🏷️ Tags

ai · llm · anthropic · insurance · reinsurance · agentic-ai · automation
