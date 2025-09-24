"""
 Challenge: Emoji Enhancer for Messages

Create a Python script that takes a message and adds emojis after specific keywords to make it more expressive.

Your program should:
1. Ask the user to input a message.
2. Add emojis after certain keywords (like "happy", "love", "code", "tea", etc.).
3. Print the updated message with emojis.

Example:
Input:
  I love to code and drink tea when I'm happy.

Output:
  I love ❤️ to code 💻 and drink tea 🍵 when I'm happy 😊.

Bonus:
- Make it case-insensitive (match "Happy" or "happy")
- Handle punctuation (like commas or periods right after keywords)

"""
# Input Text from the user

input_text = input("Enter a string: ")

# Dictionary mapping for the emoji
emoji_mapping: dict[str, str] = {
    "love": "❤️",
    "happy": "😊",
    "code": "💻",
    "chai": "☕",
    "tea": "☕",
    "music": "🎵",
    "food": "🍔",
}

# Scan through the user input for saved words to be mapped with emoji
updated_text = []
words = input_text.split()
for word in words:
    cleaned = word.lower().strip(",.?!")
    emoji = emoji_mapping.get(cleaned, "")
    if emoji:
        updated_text.append(f"{word} {emoji} ")
    else:
        updated_text.append(word)

updated_message = " ".join(updated_text)

# Updated text
print(updated_message)
