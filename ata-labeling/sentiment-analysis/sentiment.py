text = input("Enter a sentence: ")

if any(w in text.lower() for w in ["good","happy","love"]):
    print("Positive")
elif any(w in text.lower() for w in ["bad","sad","hate"]):
    print("Negative")
else:
    print("Neutral")
