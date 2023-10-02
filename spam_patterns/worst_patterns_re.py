patterns = [
    "cheap[est]?",
    "phone number",
    "4free",
    # US phone number format (1-[3 digits]-[3 digits]-[4 digits]
    # r'' is a 'raw' string (backslash symbol is treated as a literal
    # backslash).
    r"\d-[\d]{3}-[\d]{3}-[\d]{4}",
    "baggage",
    "booking",
    "antivirus",
    "cleaner",
    "cookies",
    "laptop",
    # r'' is a 'raw' string (backslash symbol is treated as a literal
    # backslash).
    # '\b' stands for 'word boundary'.
    "android",
    r"\bapple\b",
    "icloud",
    "iphone",
    "macbook",
    "macos",
    "internet explorer",
    "escort",
    "porn",
]
