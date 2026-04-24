def extract_keywords(resume):
    keywords = ["Python", "Django"]
    found = []
    
    for word in keywords:
        if word.lower() in resume.lower():
            found.append(word)
    
    return found
resume = "John has experience in Python, Django, and React."
print(extract_keywords(resume))