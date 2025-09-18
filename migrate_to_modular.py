#!/usr/bin/env python3
"""
Migration script to switch from monolith main.py to modular structure.

Run this script to safely backup your current main.py and switch to the modular version.
"""

import os
import shutil
from datetime import datetime

def migrate_to_modular():
    """Migrate from monolith to modular structure"""
    
    print("🚀 VetScribe AI - Migration to Modular Structure")
    print("=" * 50)
    
    # Step 1: Backup current main.py
    if os.path.exists("main.py"):
        backup_name = f"main_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
        shutil.copy("main.py", backup_name)
        print(f"✅ Backed up current main.py to {backup_name}")
    
    # Step 2: Replace main.py with refactored version
    if os.path.exists("main_refactored.py"):
        shutil.copy("main_refactored.py", "main.py")
        print("✅ Replaced main.py with modular version")
    else:
        print("❌ main_refactored.py not found - please ensure all files are present")
        return False
    
    # Step 3: Verify directory structure
    required_dirs = ["config", "models", "services", "ui"]
    for dir_name in required_dirs:
        if not os.path.exists(dir_name):
            print(f"❌ Directory {dir_name}/ not found - please create it manually")
            return False
        else:
            print(f"✅ Directory {dir_name}/ exists")
    
    # Step 4: Verify required files
    required_files = [
        "config/__init__.py",
        "config/settings.py", 
        "models/__init__.py",
        "models/appointment.py",
        "services/__init__.py",
        "services/ai_service.py",
        "services/audio_service.py", 
        "services/data_service.py",
        "ui/__init__.py",
        "ui/pages.py"
    ]
    
    missing_files = []
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            missing_files.append(file_path)
            print(f"❌ {file_path} - MISSING")
    
    if missing_files:
        print(f"\n❌ Migration incomplete - {len(missing_files)} files missing")
        print("Please create the missing files before running the app.")
        return False
    
    print("\n🎉 MIGRATION COMPLETE!")
    print("=" * 30)
    print("✅ All files created successfully")
    print("✅ Backup saved")
    print("✅ Modular structure ready")
    print("\n🚀 Next steps:")
    print("1. Run: streamlit run main.py")
    print("2. Test all functionality")
    print("3. If issues occur, restore from backup")
    
    return True

if __name__ == "__main__":
    success = migrate_to_modular()
    if success:
        print("\n✨ VetScribe AI is now modular and maintainable!")
    else:
        print("\n❌ Migration failed - please check missing files")
