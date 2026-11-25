import string

print("=== Password Strength Checker ===")
password = input("Enter a password to check: ")

checks = {
    "At least 8 characters": len(password) >= 8,
    "Contains an uppercase letter": any(c.isupper() for c in password),
    "Contains a lowercase letter": any(c.islower() for c in password),
    "Contains a number": any(c.isdigit() for c in password),
    "Contains a special character": any(c in string.punctuation for c in password),
}

for description, passed in checks.items():
    print(("✓ " if passed else "✗ ") + description)

score = sum(checks.values())

if score <= 2:
    strength = "WEAK"
elif score <= 4:
    strength = "MEDIUM"
else:
    strength = "STRONG"

print(f"\nPassword strength: {strength}")
print("Note: Do not enter a real password that you currently use.")
