import random
from utils import detect_language, get_photo_path

from responses import FLIRTY_EN, FLIRTY_HI, DEEP_EN, DEEP_HI

def handle_incoming_message(message_text):
    lang = detect_language(message_text)
    
    # Check if message asks for a photo
    if any(keyword in message_text.lower() for keyword in ["photo", "jeans", "formal", "pic", "image", "casual", "party"]):
        photo_path = get_photo_path(message_text)
        reply_text = random.choice(FLIRTY_HI if lang == "hi" else FLIRTY_EN)
        return reply_text, photo_path
    else:
        reply_text = random.choice(DEEP_HI if lang == "hi" else DEEP_EN)
        return reply_text, None

# 🧪 Test Example
if __name__ == "__main__":
    msg = input("User DM: ")
    reply, image = handle_incoming_message(msg)
    print("\nBot Reply:", reply)
    if image:
        print("📸 Send this photo:", image)
