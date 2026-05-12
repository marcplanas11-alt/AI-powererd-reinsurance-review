# 🧠 AI-Powered Reinsurance Contract Review

A multi-agent AI workflow that reviews synthetic reinsurance contracts and 
produces structured risk outputs — designed with insurance operations, MGA 
teams, and reinsurance analysts in mind.

---

## 📌 Problem

Reinsurance contract review — particularly binding authority agreements — is:

- Time-consuming and repetitive
- Difficult to standardise across reviewers
- Highly dependent on individual expertise
- Inconsistent in how critical risks (sanctions, DORA, delegated authority 
  limits) are identified and documented

---

## 💡 Solution

A three-agent AI workflow built on the Anthropic Claude API:

- **Compliance Agent** — identifies regulatory risks, sanctions issues, and 
  missing clauses
- **Technical Terms Agent** — extracts operational contract structure 
  (limits, bordereaux, reporting cadence)
- **Summary Agent** — consolidates outputs into prioritised risks and 
  remediation suggestions

---

## 🏗️ Architecture
---

## 🤖 Why Multi-Agent Design (rationale, not measured outcome)

Instead of a single model handling everything, this system separates:

- Compliance analysis (regulatory framing, sanctions, DORA)
- Technical extraction (limits, bordereaux, reporting structure)
- Executive summarisation (consolidation and prioritisation)

The intent is to make each agent's reasoning auditable in isolation — a 
single chained prompt is harder to debug when an output is wrong.

A controlled comparison against a single-prompt baseline has not yet been 
run; that would be a meaningful next experiment.

---

## 👤 Human-in-the-Loop Design

The system does not make final decisions. It:

- Flags risks
- Structures information into categorised outputs
- Prioritises items for reviewer attention

Final decisions remain with human reviewers. This separation between 
probabilistic AI reasoning and operational decision-making aligns with 
the operational principles of DORA Art. 28 and EU AI Act high-risk system 
requirements (Arts. 9–15).

---

## 📊 Example Output

The system generates structured outputs covering:

- Sanctions analysis (including regime gaps)
- DORA compliance gaps
- Missing clauses (GDPR, audit rights, escalation procedures)
- Delegated authority weaknesses
- Prioritised risk list
- Suggested remediation steps

See `/examples/sample_output.md` for a full sample run.

---

## ⚙️ Model Selection

| Agent | Model | Reason |
|---|---|---|
| Compliance | Claude Sonnet | Regulatory reasoning depth |
| Technical Terms | Claude Sonnet | Structured extraction quality |
| Summary | Claude Sonnet | Synthesis and prioritisation |

Single-model approach for simplicity. Cost optimisation (e.g. switching 
the Technical Terms agent to Haiku for extraction tasks) is a planned 
next iteration.

---

## 💰 Scope and Observed Runtime

On synthetic binding authority contracts (3–5 pages), the pipeline runs in 
approximately 2–3 minutes of API time. Comparable manual review by an 
experienced operations analyst is typically 2–4 hours per agreement based 
on industry-standard practice.

No controlled benchmark has been run on this specific system. The intended 
operational value is **consistency and auditability of risk identification**, 
not time savings as the primary KPI.

---

## 🔄 Design Intent vs. Current State

The system is designed to produce:

- Structured, machine-readable risk outputs
- Consistent identification of named risk categories (sanctions, DORA, 
  delegated authority, missing clauses)
- A clear handoff structure for human reviewers

**Current state**: runs on synthetic contracts. Not yet validated against 
human-reviewer outputs at statistical scale; not yet deployed in a real 
operational workflow.

---

## ⚙️ How to Run

### Web App (recommended)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Launch the browser interface
streamlit run app.py
```

The app opens at `http://localhost:8501`. Enter your Anthropic API key in 
the sidebar, upload a PDF (or use the built-in sample), and click **Run Review**. 
Expect ~2–3 minutes for output to appear.

### Notebook

```bash
pip install anthropic
```

Open `reinsurance_contract_crew.ipynb` in Jupyter or Google Colab and run 
all cells.

---

## 🧪 Evaluation Methodology (current state)

Current evaluation is informal — outputs from sample synthetic contracts 
have been spot-checked manually against expected risk categories. No formal 
evaluation framework is yet in place.

**Planned next iteration:**

- Golden dataset of 15–20 synthetic contracts with hand-annotated expected 
  outputs
- LLM-as-judge scoring on three dimensions:
  - **Faithfulness** — do identified risks map to clauses in the source contract?
  - **Coverage** — does the system catch the risks a senior reviewer would flag?
  - **Format validity** — do outputs conform to the structured schema?
- Pairwise comparison of prompt versions to detect regressions

This evaluation framework is being built in parallel in the 
`agent-evaluation-dashboard` repo.

---

## ⚠️ Limitations and Scope

- Synthetic contracts only — no validation against real reinsurance agreements
- Prompt-based extraction; no fine-tuning
- No automated validation of outputs (planned: JSON schema validation + 
  LLM-as-judge)
- No controlled benchmark of multi-agent vs. single-agent accuracy
- No measurement of false positive / false negative rates on risk identification
- No prompt versioning or regression testing across model versions
- No latency or cost monitoring beyond the Anthropic API console
- Single-language (English); not tested on French or Spanish contracts 
  despite operating in EMEA market
- No real document pipeline integration (PDF ingestion is basic)
- The system is a portfolio prototype — production deployment would require 
  formal conformity assessment, encrypted audit storage with retention 
  policies, access controls, and post-market monitoring

---

## 🚀 Next Steps

- Convert outputs to validated structured JSON (Pydantic schemas + retry on 
  validation failure)
- Build the evaluation framework described above
- Add a Human-in-the-Loop approval gate that enforces reviewer sign-off 
  before output release (current implementation flags risks but does not 
  enforce gating)
- Integrate with `claims-triage-langgraph` (separate repo) for an end-to-end 
  MGA operations pipeline
- Deploy as an internal underwriting/compliance assist tool

---

## 🔗 Related Projects in This Portfolio

- [`claims-triage-langgraph`](https://github.com/intlinsure/claims-triage-langgraph) 
  — LangGraph state machine for the downstream claims workflow
- [`agent-evaluation-dashboard`](https://github.com/intlinsure/agent-evaluation-dashboard) 
  — observability dashboard for monitoring multi-agent AI systems
- [`bordereaux-intake-n8n-mcp`](https://github.com/intlinsure/bordereaux-intake-n8n-mcp) 
  — n8n + MCP workflow for bordereaux ingestion
- [`ba-process-models`](https://github.com/intlinsure/ba-process-models) 
  — BPMN 2.0 process models for the workflows these agents automate
- [`insurance-ai-governance-pack`](https://github.com/intlinsure/insurance-ai-governance-pack) 
  — EU AI Act / DORA documentation patterns applied here

---

## 👤 Context

Built by Marc Planas — operations background in MGA reinsurance and 
delegated authority workflows (Accelerant, Sompo, Zurich, Confide). Python 
(intermediate), Anthropic Skilljar certified. The architectural choices 
reflect ~10 years of seeing where manual reinsurance contract review breaks 
down: inconsistent risk identification, missing audit context, and 
unstructured outputs that are hard to govern.

---

## 🔒 Data Disclosure

All contracts used in this project are **synthetic and generated for 
demonstration purposes**. No real client data, proprietary documents, or 
confidential information is included.

---

## 🏷️ Tags

`ai` · `llm` · `anthropic` · `claude-api` · `insurance` · `reinsurance` · 
`agentic-ai` · `multi-agent` · `automation` · `dora` · `sanctions-screening` · 
`hitl` · `python` · `streamlit`
