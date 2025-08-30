import requests
import json

def test_free_translate():
    """Test translation using MyMemory free API"""
    
    # Text to translate
    text = "Hello, world! How are you feeling today?"
    source_lang = "en"
    target_lang = "es"  # Spanish
    
    # MyMemory API endpoint
    url = "https://api.mymemory.translated.net/get"
    
    # Parameters
    params = {
        'q': text,
        'langpair': f"{source_lang}|{target_lang}"
    }
    
    try:
        print(f"Testing translation API...")
        print(f"Original text: {text}")
        print(f"Translating from {source_lang} to {target_lang}")
        print("-" * 50)
        
        # Make request
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('responseStatus') == 200:
                translated_text = data['responseData']['translatedText']
                print(f"✅ Translation successful!")
                print(f"Translated text: {translated_text}")
                
                # Test multiple languages
                languages_to_test = [
                    ('hi', 'Hindi'),
                    ('fr', 'French'), 
                    ('de', 'German'),
                    ('it', 'Italian')
                ]
                
                print("\n" + "="*50)
                print("Testing multiple languages:")
                print("="*50)
                
                for lang_code, lang_name in languages_to_test:
                    test_params = {
                        'q': "Welcome to Saathi",
                        'langpair': f"en|{lang_code}"
                    }
                    
                    test_response = requests.get(url, params=test_params)
                    if test_response.status_code == 200:
                        test_data = test_response.json()
                        if test_data.get('responseStatus') == 200:
                            translation = test_data['responseData']['translatedText']
                            print(f"{lang_name} ({lang_code}): {translation}")
                        else:
                            print(f"{lang_name} ({lang_code}): ❌ Translation failed")
                    else:
                        print(f"{lang_name} ({lang_code}): ❌ API error")
                
                return True
            else:
                print(f"❌ Translation API error: {data.get('responseDetails', 'Unknown error')}")
                return False
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def test_google_translate_with_key():
    """Test Google Translate with API key (if available)"""
    
    # You would need to set your API key here
    api_key = "YOUR_GOOGLE_TRANSLATE_API_KEY"  # Replace with actual key
    
    if api_key == "YOUR_GOOGLE_TRANSLATE_API_KEY":
        print("⚠️  Google Translate API key not configured")
        print("To test Google Translate:")
        print("1. Go to Google Cloud Console")
        print("2. Enable Cloud Translation API") 
        print("3. Create an API key")
        print("4. Replace 'YOUR_GOOGLE_TRANSLATE_API_KEY' in this file")
        return False
    
    url = "https://translation.googleapis.com/language/translate/v2"
    
    params = {
        'key': api_key,
        'q': 'Hello, how are you?',
        'source': 'en',
        'target': 'es',
        'format': 'text'
    }
    
    try:
        response = requests.post(url, data=params)
        if response.status_code == 200:
            data = response.json()
            translation = data['data']['translations'][0]['translatedText']
            print(f"✅ Google Translate successful: {translation}")
            return True
        else:
            print(f"❌ Google Translate error: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Google Translate error: {str(e)}")
        return False

if __name__ == "__main__":
    print("🌍 Translation API Testing")
    print("=" * 50)
    
    # Test free API
    print("\n1. Testing FREE MyMemory API:")
    free_success = test_free_translate()
    
    print("\n" + "=" * 50)
    
    # Test Google Translate API
    print("\n2. Testing Google Translate API:")
    google_success = test_google_translate_with_key()
    
    print("\n" + "=" * 50)
    print("SUMMARY:")
    print(f"Free API (MyMemory): {'✅ Working' if free_success else '❌ Failed'}")
    print(f"Google Translate API: {'✅ Working' if google_success else '⚠️  Not configured'}")
    
    if free_success:
        print("\n🎉 You can use the free translation API for your Saathi app!")
        print("Benefits:")
        print("- No API key required")
        print("- 1000 words per day limit")
        print("- Supports 50+ languages")
        print("- Good quality translations")
