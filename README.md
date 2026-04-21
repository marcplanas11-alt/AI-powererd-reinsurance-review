## 🚀 What This Project Does

AI-powered multi-agent system that reviews reinsurance contracts and identifies:
- compliance risks (sanctions, DORA)
- missing clauses
- delegated authority issues
- prioritised actions for human review

🧠 AI-Powered Reinsurance Contract Review
📌 Problem

Reinsurance contract review (especially binding authority agreements) is:

time-consuming
repetitive
difficult to standardise
highly dependent on manual expertise

Critical risks (sanctions, DORA compliance, delegated authority limits) are often:

inconsistently identified
poorly documented
hard to audit

## 💰 Impact

Manual contract review: ~2–4 hours per agreement  
AI-assisted review: minutes  

→ potential 80%+ reduction in review time
→ improved consistency and auditability

A three-agent AI workflow designed to automate and structure contract review:

Compliance Agent → identifies regulatory risks, sanctions issues, and missing clauses
Technical Terms Agent → extracts operational contract structure (limits, bordereaux, reporting)
Summary Agent → consolidates outputs into actionable insights and prioritised risks

Built using Anthropic Claude API.

🏗️ Architecture
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
📊 Example Output

The system generates:

sanctions analysis (incl. regime gaps)
DORA compliance gaps
missing clauses (GDPR, audit rights, escalation procedures)
delegated authority weaknesses
prioritised risk list
actionable remediation steps

🎯 Why This Matters (Insurance Context)

This system directly addresses high-friction workflows in:

MGA operations
Lloyd’s delegated authority
reinsurance contract onboarding

Aligned with:

DORA (EU Digital Operational Resilience Act)
Sanctions frameworks (OFAC, EU, HMT/OFSI)
Operational risk & auditability requirements# AI-powererd-reinsurance-review

⚙️ How to Run
pip install -r requirements.txt
# Set your API key
import os
os.environ["ANTHROPIC_API_KEY"] = "your_key_here"
# Run the workflow
python main.py
🧪 Example Use Case

Input:

Binding authority agreement with bordereaux obligations and sanctions clause...

Output:

Compliance risks identified
Missing DORA obligations
Delegated authority weaknesses
Prioritised actions
