import requests

# Simple test
print("Testing MyMemory Translation API...")

text = "Hello world"
url = f"https://api.mymemory.translated.net/get?q={text}&langpair=en|es"

try:
    response = requests.get(url)
    data = response.json()
    print(f"Original: {text}")
    print(f"Spanish: {data['responseData']['translatedText']}")
    print("✅ Translation API works!")
except Exception as e:
    print(f"❌ Error: {e}")
