print("=" * 45)
print("🏦 BNP PARIBAS AI BANKING ASSISTANT")
print("=" * 45)

question = input("\nAsk your banking question: ").lower()

# Demo knowledge base
if "savings account" in question:
    answer = """
A Savings Account is a bank account used to keep your money safely.
Benefits:
1. Earn interest on your money.
2. Deposit and withdraw money anytime.
3. Suitable for daily banking needs.
"""

elif "home loan" in question:
    answer = """
A Home Loan helps you buy a house.

Documents usually required:
• PAN Card
• Aadhaar Card
• Salary slips
• Bank statements
• Property documents
"""

elif "kyc" in question:
    answer = """
KYC (Know Your Customer) is the verification process.

Required documents:
• Identity Proof
• Address Proof
• PAN Card
• Passport-size photograph
"""

elif "credit card" in question:
    answer = """
A Credit Card lets you borrow money from the bank up to a credit limit.

Pay the amount before the due date to avoid interest charges.
"""

else:
    answer = """
Sorry, I don't know that yet.

(Real GPT API will answer any banking question. This is our practice version.)
"""

print("\n🤖 BNP Assistant Answer:")
print(answer)