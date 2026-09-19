import streamlit as st

# ---------------- PAGE ----------------
st.set_page_config(
    page_title="BNP Paribas AI Banking Assistant",
    page_icon="🏦",
    layout="centered"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

.stApp{
    background:#F8FAFC;
}

/* Remove top padding */
.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

/* Header */
.header{
    background:white;
    padding:22px;
    border-radius:18px;
    border:1px solid #E5E7EB;
    box-shadow:0px 4px 12px rgba(0,0,0,0.05);
    text-align:center;
}

.title{
    color:#00843D;
    font-size:34px;
    font-weight:700;
}

.subtitle{
    color:#64748B;
    font-size:16px;
}

/* Card */
.card{
    background:white;
    padding:22px;
    border-radius:18px;
    border:1px solid #E5E7EB;
    margin-top:20px;
}

/* AI response */
.response{
    background:#F0FFF4;
    border-left:6px solid #00843D;
    padding:18px;
    border-radius:12px;
    color:#1E293B;
}

/* Button */
.stButton>button{
    background:#00843D;
    color:white;
    border:none;
    border-radius:10px;
    height:48px;
    width:100%;
    font-size:17px;
    font-weight:600;
}

.stButton>button:hover{
    background:#006C32;
}

/* Inputs */
.stTextInput input,
.stTextArea textarea{
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="header">
    <div class="title">🏦 BNP Paribas AI Banking Assistant</div>
    <div class="subtitle">Smart Banking Companion | AI Powered Customer Support</div>
</div>
""", unsafe_allow_html=True)

# ---------------- FORM ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("Customer Details")

name = st.text_input("Your Name")

service = st.selectbox(
    "Select Banking Service",
    ["Savings Account","Home Loan","KYC","Credit Card","Fixed Deposit","General Banking"]
)

question = st.text_area(
    "Ask Your Banking Question",
    placeholder="Example: What documents are required for KYC?"
)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- AI BUTTON ----------------
if st.button("🤖 Ask AI Assistant"):

    q = question.lower()

    if "savings" in q or service=="Savings Account":
        answer = """
### Savings Account

- Earn interest on deposits.
- Free ATM / UPI / Net Banking.
- Safe place to keep your money.
- 24×7 digital banking support.
"""

    elif "home loan" in q or service=="Home Loan":
        answer = """
### Home Loan

**Required Documents**

- Aadhaar Card
- PAN Card
- Salary Slips
- Bank Statements
- Property Documents

Repayment is done through monthly EMIs.
"""

    elif "kyc" in q or service=="KYC":
        answer = """
### KYC Verification

Documents required:

- Aadhaar / Passport / Driving Licence
- PAN Card
- Address Proof
- Passport-size Photograph
"""

    elif "credit card" in q or service=="Credit Card":
        answer = """
### Credit Card

- Buy Now, Pay Later
- Reward Points
- Cashback Offers
- Interest-free period on timely payment.
"""

    elif "fixed" in q or service=="Fixed Deposit":
        answer = """
### Fixed Deposit

- Guaranteed returns.
- Higher interest than Savings Account.
- Flexible tenure.
"""

    else:
        answer = f"""
### General Banking

Thanks for your question:

**{question}**

This demo currently supports Savings Account, Home Loan, Credit Card, KYC and Fixed Deposit.
"""

    st.success(f"Welcome, {name} 👋")

    st.markdown(
        f'<div class="response">{answer}</div>',
        unsafe_allow_html=True
    )

# ---------------- SIDEBAR ----------------
st.sidebar.title("🏦 BNP Services")

st.sidebar.success("AI Banking Demo")

st.sidebar.markdown("""
- 💳 Credit Cards
- 🏠 Home Loans
- 💰 Savings Accounts
- 📄 KYC Support
- 📈 Fixed Deposits
""")

st.sidebar.info("Hackathon Demo • Streamlit + Python")

# ---------------- FOOTER ----------------
st.markdown("""
<br><hr>
<center style="color:gray;font-size:14px;">
Built for BNP Paribas AI Hackathon • Clean Banking UI
</center>
""", unsafe_allow_html=True)