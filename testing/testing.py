from google.cloud import translate_v2 as translate

def test_translate():
    # Initialize client
    translate_client = translate.Client()

    # Example: Translate "Hello World" into Spanish
    text = "Hello, world!"
    target_language = "es"  # Spanish

    result = translate_client.translate(text, target_language=target_language)

    print("Original Text:", result["input"])
    print("Translated Text:", result["translatedText"])
    print("Detected Source Language:", result["detectedSourceLanguage"])

if __name__ == "__main__":
    test_translate()
