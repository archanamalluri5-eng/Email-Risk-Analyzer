def analyze_email(email_text):
    risk_keywords = [
        "urgent",
        "click here",
        "verify your account",
        "password",
        "bank details",
        "credit card",
        "login immediately",
        "winner",
        "prize",
        "otp"
    ]

    risk_score = 0
    detected = []

    email_text = email_text.lower()

    for keyword in risk_keywords:
        if keyword in email_text:
            risk_score += 1
            detected.append(keyword)

    if risk_score >= 4:
        risk_level = "HIGH RISK"
    elif risk_score >= 2:
        risk_level = "MEDIUM RISK"
    else:
        risk_level = "LOW RISK"

    print("\n----- Email Analysis Report -----")
    print("Risk Level:", risk_level)

    if detected:
        print("Suspicious Keywords Found:")
        for word in detected:
            print("-", word)
    else:
        print("No suspicious keywords detected.")


email = input("Paste Email Content:\n")
analyze_email(email)
