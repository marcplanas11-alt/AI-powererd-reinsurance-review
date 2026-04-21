import os
import streamlit as st
import anthropic
from pypdf import PdfReader

st.set_page_config(page_title="Reinsurance Contract Review AI", layout="wide")

st.title("AI-Powered Reinsurance Contract Review")
st.write(
    "Upload a reinsurance contract PDF to generate a structured compliance, technical, and summary review."
)

api_key = st.text_input("Anthropic API Key", type="password")
st.caption("Enter your Anthropic API key. The key is used only to run the review in your current session.")

uploaded_file = st.file_uploader("Upload contract PDF", type=["pdf"])
use_sample = st.checkbox("Use sample contract text instead of uploading a PDF")

def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = []
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text.append(page_text)
    return "\n".join(text)

def get_client(api_key):
    return anthropic.Anthropic(api_key=api_key)

def compliance_agent(client, contract_text):
    prompt = f"""
    You are a reinsurance compliance analyst.

    Analyse the contract below and identify ONLY compliance-related issues.

    Focus on:
    - sanctions clauses (including specificity of regimes)
    - regulatory obligations (including DORA)
    - missing compliance clauses
    - red flags requiring human review

    Do NOT analyse technical contract terms.

    Return structured markdown with:
    1. Sanctions Clauses
    2. Regulatory Clauses
    3. Missing Clauses
    4. Red Flags
    5. Human Review Required

    Contract:
    {contract_text}
    """
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=900,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text

def terms_agent(client, contract_text):
    prompt = f"""
    You are a reinsurance technical analyst.

    Extract ONLY operational and technical terms from this contract.

    Focus on:
    - delegated authority limits
    - bordereaux obligations
    - reporting frequency
    - unclear or ambiguous wording

    Do NOT analyse compliance or regulatory issues.

    Return structured markdown with:
    1. Limits
    2. Bordereaux Obligations
    3. Reporting Frequency
    4. Unclear Wording

    Contract:
    {contract_text}
    """
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=900,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text

def summary_agent(client, compliance_output, terms_output):
    prompt = f"""
    You are a senior insurance operations reviewer.

    Based on the following analyses:

    COMPLIANCE:
    {compliance_output}

    TECHNICAL TERMS:
    {terms_output}

    Provide:
    - Top 5 risks
    - Key contract weaknesses
    - Priority actions
    - Human review recommendation (Yes/No + reason)

    Be concise, structured, and business-oriented.
    """
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=900,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text

if st.button("Run Review", type="primary"):
    if not api_key:
        st.error("Please enter your Anthropic API key.")
    elif not uploaded_file and not use_sample:
        st.error("Please upload a PDF or use the sample input.")
    else:
        try:
            with st.spinner("Preparing contract text..."):
                if use_sample:
                    contract_text = """
                    This binding authority agreement includes monthly bordereaux reporting obligations.
                    The coverholder must comply with all applicable sanctions laws.
                    No explicit DORA-related operational resilience obligations are included.
                    The agreement does not clearly define escalation procedures for regulatory breaches.
                    The wording on delegated authority limits is partially unclear.
                    """
                else:
                    contract_text = extract_text_from_pdf(uploaded_file)

            if not contract_text.strip():
                st.error("No text could be extracted from the PDF.")
            else:
                client = get_client(api_key)

                with st.spinner("Running compliance review..."):
                    compliance_output = compliance_agent(client, contract_text)

                with st.spinner("Running technical review..."):
                    terms_output = terms_agent(client, contract_text)

                with st.spinner("Generating summary..."):
                    summary_output = summary_agent(client, compliance_output, terms_output)

                st.success("Review completed.")

                tab1, tab2, tab3 = st.tabs(["Compliance", "Technical Terms", "Summary"])

                with tab1:
                    st.markdown(compliance_output)

                with tab2:
                    st.markdown(terms_output)

                with tab3:
                    st.markdown(summary_output)

                with st.expander("Extracted text preview"):
                    st.text(contract_text[:5000])

        except Exception as e:
            st.error(f"Error: {e}")

st.info(
    "This tool is a proof of concept designed to support human review. "
    "It does not replace legal, compliance, or underwriting judgement."
)
