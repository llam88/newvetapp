import streamlit as st
from config.settings import PAGE_CONFIG, DATA_FILE
from services.data_service import initialize_session_state
from ui.pages import render_home_page, render_new_appointment, render_appointments, render_patients, render_settings

# Page configuration
st.set_page_config(**PAGE_CONFIG)

# Initialize session state and data
initialize_session_state(DATA_FILE)

# Check API key configuration
from config.settings import OPENAI_API_KEY
if not OPENAI_API_KEY:
    st.error("🔑 **OpenAI API Key Required**")
    st.markdown("### Setup Instructions:")
    st.markdown("**For Local Development:**")
    st.code("# Create .env file in your project directory\nOPENAI_API_KEY=your_new_api_key_here")
    st.markdown("**For Streamlit Cloud:**")
    st.markdown("1. Go to your app settings in Streamlit Cloud")
    st.markdown("2. Click on 'Secrets'")
    st.markdown("3. Add: `OPENAI_API_KEY = \"your_new_api_key_here\"`")
    st.info("💡 **Get a new API key from:** https://platform.openai.com/api-keys")
    st.warning("🔒 **Security Note:** Your previous key was revoked due to public exposure. This is normal security behavior.")
    st.stop()

# Initialize transcribed text from session state
transcribed_text = st.session_state.last_transcription

# Sidebar Navigation
st.sidebar.title("VetScribe AI")
st.sidebar.markdown("*Professional Veterinary AI Scribe*")

menu_option = st.sidebar.selectbox(
    "Navigation",
    ["Home", "New Appointment", "View Appointments", "Patients", "Settings"]
)

# Route to appropriate page
if menu_option == "Home":
    render_home_page()
elif menu_option == "New Appointment":
    render_new_appointment()
elif menu_option == "View Appointments":
    render_appointments()
elif menu_option == "Patients":
    render_patients()
elif menu_option == "Settings":
    render_settings()

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; padding: 20px;'>
        <p>VetScribe AI - Professional Veterinary Documentation</p>
        <p><small>Built with Streamlit, OpenAI GPT-4 & Whisper • AI Veterinarian Assistant • Secure Design</small></p>
    </div>
    """,
    unsafe_allow_html=True
)
