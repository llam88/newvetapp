#!/usr/bin/env python3
"""
Quick test script to verify local development setup.
Run this BEFORE starting the full app to catch any issues.
"""

import os

def test_local_setup():
    """Test local development environment setup"""
    print("🧪 VetScribe AI - Local Development Setup Test")
    print("=" * 50)
    
    # Test 1: Check if .env file exists
    if os.path.exists(".env"):
        print("✅ .env file found")
    else:
        print("❌ .env file NOT found")
        print("📝 Create .env file with: OPENAI_API_KEY=your_key_here")
        return False
    
    # Test 2: Try loading environment variables
    try:
        from dotenv import load_dotenv
        load_dotenv()
        print("✅ python-dotenv loaded successfully")
    except ImportError:
        print("❌ python-dotenv not installed")
        print("📦 Run: pip install python-dotenv")
        return False
    
    # Test 3: Check if API key is loaded
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        if api_key == "your_new_api_key_here":
            print("⚠️  API key found but appears to be template value")
            print("🔑 Replace 'your_new_api_key_here' with your actual OpenAI API key")
            return False
        elif api_key.startswith("sk-"):
            print(f"✅ Valid OpenAI API key found (starts with: {api_key[:8]}...)")
        else:
            print("⚠️  API key found but format looks unusual")
            print("🔍 OpenAI API keys should start with 'sk-'")
            return False
    else:
        print("❌ OPENAI_API_KEY not found in environment")
        print("📝 Check your .env file contains: OPENAI_API_KEY=your_actual_key")
        return False
    
    # Test 4: Check dependencies
    try:
        import streamlit
        import openai
        import pandas
        import numpy
        print("✅ Core dependencies available")
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("📦 Run: pip install -r requirements.txt")
        return False
    
    # Test 5: Test OpenAI connection (optional)
    try:
        openai.api_key = api_key
        # Quick test call (this will cost ~$0.001)
        test_input = input("\n🧪 Test OpenAI connection? This will make a small API call (~$0.001) [y/N]: ")
        if test_input.lower() == 'y':
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": "Hello, say 'API test successful' if you can read this."}],
                max_tokens=10
            )
            if "successful" in response.choices[0].message.content.lower():
                print("✅ OpenAI API connection successful!")
            else:
                print("⚠️  OpenAI responded but unexpected response")
        else:
            print("⏭️  Skipped OpenAI connection test")
    except Exception as e:
        print(f"❌ OpenAI API Error: {str(e)}")
        print("🔑 Check your API key is valid and has credits")
        return False
    
    print("\n🎉 LOCAL SETUP COMPLETE!")
    print("✅ Environment variables configured")
    print("✅ Dependencies installed")
    print("✅ API key validated")
    print("\n🚀 Ready to run:")
    print("   streamlit run main.py")
    print("   OR")
    print("   streamlit run main_refactored.py")
    
    return True

if __name__ == "__main__":
    success = test_local_setup()
    if not success:
        print("\n❌ Setup incomplete - fix issues above before running VetScribe AI")
    else:
        print("\n🐾 VetScribe AI ready for local development!")
