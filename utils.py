from langdetect import detect
import os

def detect_language(text):
    try:
        lang = detect(text)
        return "hi" if lang == "hi" else "en"
    except:
        return "en"

def get_photo_path(message_text):
    message_text = message_text.lower()
    keywords = ["jeans", "formal", "casual", "party"]
    for word in keywords:
        if word in message_text:
            filename = f"{word}.jpg"
            path = os.path.join("photos", filename)
            if os.path.exists(path):
                return path
    return os.path.join("photos", "default.jpg")
