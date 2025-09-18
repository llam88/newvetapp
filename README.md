# 🐾 VetScribe AI - Veterinary AI Scribe

A comprehensive Streamlit application that replicates the functionality of ScribbleVet.com, providing AI-powered veterinary documentation using ChatGPT.

## ✨ Features

- **🎙️ Audio Recording**: Record client consultations directly in the app
- **🤖 AI-Powered SOAP Notes**: Automatic generation using ChatGPT-4
- **📋 Multiple Templates**: SOAP notes, client summaries, and custom formats
- **👥 Patient Management**: Track patient information and appointment history
- **📁 Export Options**: Download notes as text files
- **🔒 Client Consent**: Built-in consent management for recordings
- **📊 Dashboard**: Track appointments and patient statistics
- **⚙️ Customizable**: Modify templates and settings to match your practice

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (ChatGPT access)

### Installation

1. **Clone or download this project**
   ```bash
   git clone <repository-url>
   cd vetscribe-ai
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env and add your OpenAI API key
   OPENAI_API_KEY=your_actual_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run main.py
   ```

5. **Open your browser** to `http://localhost:8501`

## 🔑 Getting an OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Create a new secret key
5. Copy the key and add it to your `.env` file

**Note**: ChatGPT API usage has costs. Check OpenAI's current pricing.

## 📖 How to Use

### 1. **Home Dashboard**
- View appointment statistics
- Quick overview of patients
- Feature highlights

### 2. **Create New Appointment**
- **Client Consent**: Confirm client consent for recording
- **Patient Info**: Enter patient and client details
- **Recording**: Record audio or enter manual notes
- **AI Generation**: Generate SOAP notes and client summaries
- **Export**: Download generated notes

### 3. **View Appointments**
- Browse appointment history
- Search and filter appointments
- View detailed notes for each appointment
- Export individual appointment notes

### 4. **Patient Management**
- View all registered patients
- Patient statistics and analytics
- Automatic patient tracking

### 5. **Settings**
- Configure OpenAI API key
- Customize note templates
- Export/import data
- Clear application data

## 📋 SOAP Note Format

The app generates professional veterinary SOAP notes:

- **Subjective**: Client observations and concerns
- **Objective**: Physical exam findings and measurements
- **Assessment**: Diagnosis and clinical evaluation
- **Plan**: Treatment recommendations and follow-up

## 🛡️ Privacy & Security

- **Client Consent**: Built-in consent verification
- **Local Storage**: Data stored in session (not persistent by default)
- **API Security**: Secure communication with OpenAI
- **No Data Persistence**: Session data clears on restart (configurable)

## 🎨 Customization

### Template Modification
- Access Settings → Template Customization
- Modify SOAP note format
- Customize client summary style
- Save custom templates

### Adding New Templates
Extend the `generate_ai_response()` function to add new note types:

```python
CUSTOM_TEMPLATE = """
Your custom template prompt here...
Input: {input_text}
"""
```

## 📁 File Structure

```
vetscribe-ai/
├── main.py              # Main Streamlit application
├── requirements.txt     # Python dependencies
├── .env.example        # Environment variables template
├── README.md           # This file
└── .gitignore         # Git ignore file
```

## 🔧 Technical Details

### Dependencies
- **Streamlit**: Web application framework
- **OpenAI**: ChatGPT API integration
- **audio-recorder-streamlit**: Audio recording functionality
- **pandas**: Data management
- **python-dotenv**: Environment variable management

### AI Model
- Uses ChatGPT-4 for note generation
- Veterinary-specific prompts
- Temperature setting for consistency
- Token limits for cost control

## 🚀 Deployment Options

### Local Development
```bash
streamlit run main.py
```

### Streamlit Cloud
1. Push to GitHub repository
2. Connect to Streamlit Cloud
3. Add secrets for OpenAI API key
4. Deploy

### Docker (Optional)
```dockerfile
FROM python:3.9-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "main.py"]
```

## ⚠️ Important Notes

1. **API Costs**: OpenAI API usage incurs costs. Monitor your usage.
2. **Data Privacy**: Consider HIPAA compliance for production use
3. **Client Consent**: Always obtain proper consent before recording
4. **Backup**: Export data regularly as session storage is temporary
5. **Internet Required**: App requires internet connection for AI features

## 🆘 Troubleshooting

### Common Issues

**"API Key Error"**
- Check that your OpenAI API key is correctly set in `.env`
- Verify the API key is valid and has credits

**"Recording Not Working"**
- Ensure microphone permissions are granted
- Try the manual text input as alternative

**"Dependencies Error"**
```bash
pip install --upgrade -r requirements.txt
```

**"Streamlit Not Found"**
```bash
pip install streamlit
```

## 🔄 Updates & Maintenance

- **Regular Updates**: Keep dependencies updated
- **API Monitoring**: Monitor OpenAI API usage and costs
- **Template Refinement**: Continuously improve note templates
- **User Feedback**: Gather feedback to enhance functionality

## 📞 Support

For issues and questions:
1. Check the troubleshooting section
2. Review OpenAI documentation
3. Check Streamlit documentation
4. Verify all dependencies are installed

## 📄 License

This project is for educational and professional use. Ensure compliance with:
- OpenAI's usage policies
- Local veterinary regulations
- Data privacy laws (HIPAA, etc.)
- Recording consent requirements

## 🎯 Future Enhancements

Potential improvements:
- **Database Integration**: Persistent data storage
- **PIMS Integration**: Connect with practice management systems
- **Advanced Templates**: More specialized note types
- **User Authentication**: Multi-user support
- **Scheduling**: Appointment scheduling features
- **Analytics**: Advanced reporting and insights

---

**🐾 VetScribe AI - Making veterinary documentation easier, one note at a time!** 