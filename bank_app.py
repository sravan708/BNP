import streamlit as st

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="BNP Paribas AI Banking Assistant",
    page_icon="🏦",
    layout="centered"
)

# -----------------------------
# CUSTOM BNP STYLE
# -----------------------------
st.markdown("""
<style>
.stApp{
    background-color:#F4FFF8;
}

.main-title{
    color:#00843D;
    text-align:center;
    font-size:38px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:#555555;
    font-size:18px;
    margin-bottom:20px;
}

.response-box{
    background-color:#E8FFF0;
    padding:20px;
    border-radius:12px;
    border-left:8px solid #00843D;
    color:black;
    font-size:17px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown("<div class='main-title'>🏦 BNP Paribas AI Banking Assistant</div>", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>Your Smart Banking Companion (Hackathon Demo)</div>", unsafe_allow_html=True)

st.divider()

# -----------------------------
# USER DETAILS
# -----------------------------
name = st.text_input("👤 Enter Your Name")

service = st.selectbox(
    "🏦 Select Banking Service",
    [
        "Savings Account",
        "Home Loan",
        "KYC",
        "Credit Card",
        "Fixed Deposit",
        "General Banking"
    ]
)

question = st.text_area(
    "💬 Ask Your Banking Question",
    placeholder="Example: What documents are required for KYC?"
)

# -----------------------------
# BUTTON
# -----------------------------
if st.button("🤖 Get AI Answer", use_container_width=True):

    q = question.lower()

    # -----------------------------
    # KNOWLEDGE BASE
    # -----------------------------
    if "savings" in q or service == "Savings Account":
        answer = """
### Savings Account

A Savings Account is used to safely keep your money while earning interest.

**Benefits**
- Earn interest on your balance.
- Deposit and withdraw money anytime.
- Secure digital banking access.
- ATM, UPI and Net Banking support.
"""

    elif "home loan" in q or service == "Home Loan":
        answer = """
### Home Loan

A Home Loan helps customers purchase or construct a house.

**Required Documents**
- Aadhaar Card
- PAN Card
- Salary Slips (last 3 months)
- Bank Statements
- Property Documents

**Repayment**
- Paid monthly through EMIs.
"""

    elif "kyc" in q or service == "KYC":
        answer = """
### KYC (Know Your Customer)

KYC verifies customer identity.

**Documents Required**
- Identity Proof
- Address Proof
- PAN Card
- Passport-size Photograph

KYC helps banks prevent fraud and comply with regulations.
"""

    elif "credit card" in q or service == "Credit Card":
        answer = """
### Credit Card

A Credit Card lets you spend up to a bank-approved credit limit.

**Features**
- Buy now, pay later.
- Interest-free period if paid on time.
- Cashback and reward points.
- Online and offline transactions.
"""

    elif "fixed deposit" in q or "fd" in q or service == "Fixed Deposit":
        answer = """
### Fixed Deposit (FD)

A Fixed Deposit is a secure investment option.

**Benefits**
- Higher interest than savings accounts.
- Fixed tenure.
- Guaranteed returns.
- Suitable for long-term savings.
"""

    else:
        answer = f"""
### General Banking Information

Thank you for your question:

**"{question}"**

This demo assistant currently knows:
- Savings Accounts
- Home Loans
- Credit Cards
- KYC
- Fixed Deposits

In the next module, we'll connect this app to a real LLM so it can answer any banking question.
"""

    # -----------------------------
    # DISPLAY RESPONSE
    # -----------------------------
    st.success(f"Hello {name}! Welcome to BNP Paribas.")

    st.markdown(
        f"<div class='response-box'>{answer}</div>",
        unsafe_allow_html=True
    )

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.header("📚 Banking Topics")

st.sidebar.write("""
**This demo supports:**
- Savings Account
- Home Loan
- Credit Card
- KYC
- Fixed Deposit
""")

st.sidebar.info(
    "Module 1: Frontend chatbot built using Python + Streamlit."
)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown(
    "<div class='footer'>Built with ❤️ using Python & Streamlit for BNP Paribas AI Hackathon</div>",
    unsafe_allow_html=True
)