raw_email = "  USER@Example.COM  "
print(raw_email.strip().lower())
assert "  Alex.SMITH@EXAMPLE.com ".strip().lower() == "alex.smith@example.com"
