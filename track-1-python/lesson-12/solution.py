def clean_email(email):
    return email.strip().lower()

leads = [" ALICE@example.com ", "BOB@example.com", " carol@Example.com ", " "]
clean = [clean_email(value) for value in leads if value.strip()]
assert clean_email(" TEST@EXAMPLE.COM ") == "test@example.com"
assert len(clean) == 3
with open("clean_leads.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(clean) + "\n")
with open("clean_leads.txt", encoding="utf-8") as file:
    assert file.read().splitlines() == clean
print("\n".join(clean))
print(f"Accepted: {len(clean)}")
