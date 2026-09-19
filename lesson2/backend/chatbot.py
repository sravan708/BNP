# chatbot.py

from tools import *

def ask_ai(question):

    parts = question.strip().split()

    if len(parts) == 0:
        return "Please ask a question."

    command = parts[0].upper()

    try:

        if command == "EMI":
            principal = float(parts[1])
            rate = float(parts[2])
            years = int(parts[3])

            emi = calculate_emi(principal, rate, years)

            return f"Monthly EMI is ₹{emi}"

        elif command == "COMPOUND":
            principal = float(parts[1])
            rate = float(parts[2])
            years = int(parts[3])

            result = compound_interest(principal, rate, years)

            return (
                f"Final Amount: ₹{result['amount']}\n"
                f"Interest Earned: ₹{result['interest']}"
            )

        elif command == "USD":
            amount = float(parts[1])

            result = convert_currency(amount, "USD")

            return f"{amount} USD = ₹{result}"

        elif command == "EUR":
            amount = float(parts[1])

            result = convert_currency(amount, "EUR")

            return f"{amount} EUR = ₹{result}"

        elif command == "TAX":
            income = float(parts[1])

            tax = income_tax(income)

            return f"Estimated Tax = ₹{tax}"

        else:
            return (
                "Unknown command.\n\n"
                "Try:\n"
                "EMI 1000000 8.5 20\n"
                "COMPOUND 50000 12 10\n"
                "USD 100\n"
                "EUR 50\n"
                "TAX 900000"
            )

    except Exception:
        return "Invalid format. Please check your input."