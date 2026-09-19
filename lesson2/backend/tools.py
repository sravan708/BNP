# tools.py

def calculate_emi(principal, rate, years):
    r = rate / 1200
    n = years * 12

    emi = principal * r * ((1 + r) ** n) / (((1 + r) ** n) - 1)

    return round(emi, 2)


def compound_interest(principal, rate, years):
    amount = principal * ((1 + rate / 100) ** years)
    interest = amount - principal

    return {
        "amount": round(amount, 2),
        "interest": round(interest, 2)
    }


exchange_rates = {
    "USD": 87.5,
    "EUR": 102.0,
    "GBP": 118.0
}

def convert_currency(amount, currency):
    if currency not in exchange_rates:
        return "Currency not supported"

    return round(amount * exchange_rates[currency], 2)


def income_tax(income):
    if income <= 700000:
        return 0

    return round(income * 0.10, 2)