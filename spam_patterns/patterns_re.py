patterns = [
    "amazing",
    "business",
    "cheap[est]?",
    "credit[s]?",
    "customer[s]?",
    r"\bdeal[s]?\b",
    "phone number",
    "price",
    "4free",
    # US phone number format (1-[3 digits]-[3 digits]-[4 digits]
    # r'' is a 'raw' string (backslash symbol is treated as a literal
    # backslash).
    r"\d-[\d]{3}-[\d]{3}-[\d]{4}",
    "airline[s]?",
    "baggage",
    "booking",
    "flight[s]?",
    r"\breservation\b",
    "vacation[al]?",
    "ticket[s]?",
    r"\baccount\b",
    "antivirus",
    "cleaner",
    "cookies",
    "[e]?mail",
    "laptop",
    "password",
    "sign up",
    "sign in",
    "wi[-]?fi",
    # r'' is a 'raw' string (backslash symbol is treated as a literal
    # backslash).
    # '\b' stands for 'word boundary'.
    r"\bgoogle\b",
    "android",
    r"\bchrome\b",
    r"\bapple\b",
    "icloud",
    r"\bios\b",
    "iphone",
    r"\bmac\b",
    "macbook",
    "macos",
    "facebook",
    "microsoft",
    "internet explorer",
    "adult",
    "escort",
    "porn",
    "xxx",
]
