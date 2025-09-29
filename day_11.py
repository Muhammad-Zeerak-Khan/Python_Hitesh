def calculate_compatibility_score(name1: str, name2: str) -> int:
    name1 = name1.lower()
    name2 = name2.lower()
    score: int = 0
    shared_letters: set[str] = set(name1) & set(name2)
    vowels: set[str] = set("aeiou")
    print(f"shared letters : {shared_letters}")
    # Scoring
    score += (
        len(shared_letters) * 15
    )  # If 5 letters are common, just assign the score 50%
    score += len(vowels & shared_letters) * 10

    return min(score, 100)


def run_friendship_calculator():
    print("💗 Friendship Compatibility Calculator 💗")
    name1: str = input("Enter the first name : ")
    name2: str = input("Enter the second name : ")
    score: int = calculate_compatibility_score(name1, name2)
    print(f"\nThe friendship compatibility score is : {score}")
    if score >= 80:
        print("\nYou are like chai and samosa. Made for each other! 🤗")
    elif score >= 50:
        print("\nYou are kind of warm spices! 🫚")
    else:
        print("You guys are like tea 🫖  and Coffee ☕. You might not gel together 😟")


if __name__ == "__main__":
    run_friendship_calculator()
