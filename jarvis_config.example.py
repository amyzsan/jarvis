# JARVIS PERSONAL CONFIGURATION — EXAMPLE FILE
# Copy this file, rename it to jarvis_config.py
# Then fill in your own details

# Your name — Jarvis will address you by this
USER_NAME = "Boss"  # e.g. "Miss Sarah", "Mr. Bro"

# Wake words — words that activate Jarvis
WAKE_WORDS = ["jarvis", "wake up", "hey", "listen"]

# Session timeout settings (in seconds)
TIMEOUT_WARNING = 100   # Warning at 1 min 40 seconds
TIMEOUT_END = 120       # Session ends at 2 minutes

# Confidence threshold for speech recognition (0.0 to 1.0)
CONFIDENCE_THRESHOLD = 0.3

# AI Model — don't change unless you know what you're doing
GROQ_MODEL = "llama-3.1-8b-instant"

# TTS Settings
TTS_RATE = 180
TTS_VOLUME = 0.9