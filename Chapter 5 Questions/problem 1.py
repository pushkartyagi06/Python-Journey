words = {
    "paani": "water",
    "roti": "bread",
    "dost": "friend",
    "ghar": "house"
}

word = input("Enter Hindi word: ")

print("Meaning:", words.get(word, "Word not found"))