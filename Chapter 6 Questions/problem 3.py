text = input("Enter comment: ")

if ("make a lot of money" in text.lower() or
    "buy now" in text.lower() or
    "subscribe this" in text.lower() or
    "like this" in text.lower()):
    
    print("Spam detected!")
else:
    print("Not spam")