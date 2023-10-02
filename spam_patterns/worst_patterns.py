patterns = [
    "amazing",
    "business",
    "cheap[est]?",
    "phone number",
    "4free",
    # US phone number format (1-[3 digits]-[3 digits]-[4 digits]
    # r'' is a 'raw' string (backslash symbol is treated as a literal
    # backslash).
    r"\d-[\d]{3}-[\d]{3}-[\d]{4}",
    "airline[s]?",
    "baggage",
    "booking",
    "vacation[al]?",
    "ticket[s]?",
    "antivirus",
    "cleaner",
    "cookies",
    "laptop",
    "password",
    # r'' is a 'raw' string (backslash symbol is treated as a literal
    # backslash).
    # '\b' stands for 'word boundary'.
    "android",
    r"\bchrome\b",
    r"\bapple\b",
    "icloud",
    r"\bios\b",
    "iphone",
    "macbook",
    "macos",
    "facebook",
    "microsoft",
    "internet explorer",
    "escort",
    "porn",
    "xxx",
]
