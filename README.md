# Jarvis AI Assistant

A voice-activated AI assistant inspired by Tony Stark's Jarvis.
Built with Python, Groq AI, and speech recognition.

---

## Features

- Wake word activation ("Jarvis", "Wake up", etc.)
- Voice commands with no phrase limit
- Real-time weather updates
- Time telling
- Sarcastic, Gen Z, chaotic AI personality
- Session timeout with auto standby mode
- Fully customizable responses

---

## Requirements

- Python 3.8 or higher
- A microphone
- Internet connection
- Free Groq API key
- Free WeatherAPI key

---

## Setup Instructions

### 1. Clone the project
Open terminal and run:
git clone https://github.com/amyzsan/jarvis.git

cd jarvis

### 2. Install dependencies
pip install -r requirements.txt

If you get a PyAudio error on Windows:
pip install pipwin

pipwin install pyaudio

### 3. Get your free API keys

**Groq API (for AI responses):**
1. Go to https://console.groq.com
2. Sign up for free
3. Go to API Keys → Create API Key
4. Copy the key

**WeatherAPI (for weather):**
1. Go to https://www.weatherapi.com
2. Sign up for free
3. Copy your API key from the dashboard

### 4. Set environment variables

On Windows, open terminal and run:
setx GROQ_API_KEY "your_groq_key_here"

setx WEATHER_API_KEY "your_weather_key_here"
Then close and reopen your terminal.

On Mac/Linux:
export GROQ_API_KEY="your_groq_key_here"

export WEATHER_API_KEY="your_weather_key_here"

### 5. Set up your personal config
Copy the example config file:
cp jarvis_config.example.py jarvis_config.py
Open `jarvis_config.py` and change `USER_NAME` to your own name.

### 6. Run Jarvis!
python jarvis.py

---

## How to use

1. Run the program
2. Say a wake word: **"Jarvis"**, **"Wake up"**, **"Hey"**, or **"Listen"** or the ones that you've put in
3. Speak your command freely
4. Jarvis will respond!

**Example commands:**
- "What time is it?"
- "What's the weather?"
- "Who is Gojo?" 
- "Explain black holes"
- "Exit" / "Goodbye"

---

## File Structure
jarvis/

├── jarvis.py                   # Main code

├── jarvis_responses.py         # All AI responses (customize these!)

├── jarvis_config.example.py    # Config template for new users

├── requirements.txt            # Dependencies

├── .gitignore                  # Git security

└── README.md                   # This file

---

## Customization

Want to change Jarvis's personality or responses?
Open `jarvis_responses.py` and edit any of the response lists!

Want to change timeout, wake words, or your name?
Open `jarvis_config.py` and edit accordingly.

---

## Privacy & Security

- API keys are stored as environment variables, never in code
- No data is collected or stored anywhere

---

## Built With

- [Python](https://python.org)
- [Groq API](https://console.groq.com)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [WeatherAPI](https://weatherapi.com)

---

## License

Feel free to use, modify, and build on this project! 
Started project on 15th Jan 2025.
Ended on 12th June 2026.
Leaving now.
Regards,
Amy.
