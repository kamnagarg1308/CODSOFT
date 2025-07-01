import random
import string

class PasswordEngine:
    def __init__(self, length):
        self.length = length
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = string.punctuation
        self.character_pool = self.lowercase + self.uppercase + self.digits + self.symbols

    def generate(self):
        if self.length < 8:
            raise ValueError("Security alert: Password must have at least 8 characters.")

        # Guarantee at least one of each type
        base = [
            random.choice(self.lowercase),
            random.choice(self.uppercase),
            random.choice(self.digits),
            random.choice(self.symbols)
        ]

        # Fill the rest
        base += [random.choice(self.character_pool) for _ in range(self.length - 4)]
        random.shuffle(base)
        return ''.join(base)

def display_banner():
    print("=" * 40)
    print("||        SecurePass Generator        ||")
    print("=" * 40)

def main():
    display_banner()

    while True:
        try:
            length = int(input("\nEnter desired password length (min 8): "))
            password_gen = PasswordEngine(length)
            break
        except ValueError:
            print("Oops! Please enter a valid integer.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    password = password_gen.generate()
    print("\n🎉 Your new secure password:")
    print(password)
    print("\nBe sure to store this password securely and avoid sharing it with anyone.")

if __name__ == "__main__":
    main()
