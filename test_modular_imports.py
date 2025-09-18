#!/usr/bin/env python3
"""
Test script to verify all modular imports work correctly.
Run this before switching to modular structure.
"""

def test_imports():
    """Test all imports to verify modular structure is complete"""
    print("🧪 Testing Modular VetScribe AI Imports")
    print("=" * 40)
    
    try:
        # Test config imports
        print("📁 Testing config imports...")
        from config.settings import (
            DATA_FILE, OPENAI_API_KEY, PAGE_CONFIG, 
            SOAP_TEMPLATE, CLIENT_SUMMARY_TEMPLATE,
            PIMS_OPTIONS, CANINE_TEETH, FELINE_TEETH, 
            DENTAL_CONDITIONS, DENTAL_KEYWORDS,
            AUDIO_RECORDER_AVAILABLE, BASIC_RECORDER_AVAILABLE, RECORDING_OPTIONS
        )
        print("✅ Config imports successful")
        
        # Test models imports
        print("📁 Testing models imports...")
        from models import AppointmentData, PatientData, create_appointment_data, create_patient_data
        print("✅ Models imports successful")
        
        # Test data service imports
        print("📁 Testing data service imports...")
        from services.data_service import (
            initialize_session_state, save_data, save_appointment,
            export_to_text, clear_all_data, export_all_data, add_patient_if_new
        )
        print("✅ Data service imports successful")
        
        # Test AI service imports  
        print("📁 Testing AI service imports...")
        from services.ai_service import (
            transcribe_audio, transcribe_audio_bytes, transcribe_uploaded_file,
            generate_ai_response, generate_client_email, simulate_pims_integration,
            extract_dental_findings_from_text, generate_dental_chart_data,
            analyze_dental_findings, generate_dental_recommendations
        )
        print("✅ AI service imports successful")
        
        # Test audio service imports
        print("📁 Testing audio service imports...")
        from services.audio_service import (
            render_audio_recording_section, render_audio_upload_section
        )
        print("✅ Audio service imports successful")
        
        # Test UI imports
        print("📁 Testing UI imports...")
        from ui.pages import (
            render_home_page, render_new_appointment, render_appointments,
            render_patients, render_settings
        )
        print("✅ UI imports successful")
        
        print("\n🎉 ALL IMPORTS SUCCESSFUL!")
        print("✅ Modular structure is complete and ready to use")
        print("\n🚀 Next steps:")
        print("1. Run: python migrate_to_modular.py")
        print("2. Test: streamlit run main.py")
        
        return True
        
    except ImportError as e:
        print(f"\n❌ IMPORT ERROR: {str(e)}")
        print("🔧 Fix missing imports before using modular structure")
        return False
        
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_imports()
    if not success:
        print("\n⚠️  Modular structure needs fixes before use")
        print("🔄 Keep using main.py until issues are resolved")
