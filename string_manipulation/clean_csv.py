def clean_csv(text):
    text = text.replace("!!", "")
    text = text.replace(",,", ",")
    parts = [word.strip() for word in text.split(",") if word.strip()]
    return ", ".join(parts)
print(clean_csv("John,, Doe!!, New York "))
