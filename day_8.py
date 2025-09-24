import getpass
import random
import string


def password_strength_checker(given_password: str) -> list[str]:
    """Returns the strength of the input password"""
    list_of_issues: list[str] = []
    if len(given_password) < 8:
        list_of_issues.append("The input password should be atleast 8 characters long.")

    if not any(char.islower() for char in given_password):
        list_of_issues.append(
            "The password should contain atleast one lowercase character"
        )
    if not any(char.isupper() for char in given_password):
        list_of_issues.append(
            "The password should contain atleast one uppercase character"
        )

    if not any(char.isdigit() for char in given_password):
        list_of_issues.append("The password should contain atleast one digit.")
    if not any(char in string.punctuation for char in given_password):
        list_of_issues.append(
            "The password should contain atleast one special character."
        )

    return list_of_issues


def generate_strong_password(length=15) -> str:
    total_characters: string.LiteralString = (
        string.punctuation + string.ascii_letters + string.digits
    )

    return "".join(random.choice(total_characters) for _ in range(length))


if __name__ == "__main__":
    user_input: str = getpass.getpass("Enter the password : ").strip()
    issues: list[str] = password_strength_checker(user_input)
    if issues:
        print("You have a weak password!")
        for issue in issues:
            print(f"* {issue}")
        print(f"Suggested password for you : {generate_strong_password()}")
    else:
        print("You have a strong password")
