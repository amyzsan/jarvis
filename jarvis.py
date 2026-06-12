import os
from groq import Groq
import pyttsx3
import datetime
import time
import random
import re
import speech_recognition as sr
import noisereduce as nr
import numpy as np
import requests
import threading
import sys

from jarvis_responses import *
from jarvis_config import *

# Initialize recognizer with optimized settings
recognizer = sr.Recognizer()
recognizer.energy_threshold = 4000
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 1.0
recognizer.non_speaking_duration = 0.8

# Initialize Groq Client
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key) if api_key else None

# Initialize WeatherAPI
weather_key = os.getenv("WEATHER_API_KEY")

# Initialize TTS — now using settings from jarvis_config.py
engine = pyttsx3.init()
engine.setProperty('rate', TTS_RATE)
engine.setProperty('volume', TTS_VOLUME)

# Global variable for microphone calibration
is_calibrated = False

# Global variables for session timing
session_start_time = None
total_session_time = 0

def calibrate_microphone():
    global is_calibrated
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
        is_calibrated = True
    except Exception as e:
        print(f"Calibration warning: {e}")
        is_calibrated = True

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    
    parts = []
    if hours > 0:
        parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if minutes > 0:
        parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
    if secs > 0 or len(parts) == 0:
        parts.append(f"{secs} second{'s' if secs != 1 else ''}")
    
    return " and ".join(parts)

def display_session_timer():
    global session_start_time, total_session_time
    
    while session_start_time is not None:
        time.sleep(20)
        
        if session_start_time is None:
            break
            
        current_elapsed = time.time() - session_start_time
        total_elapsed = total_session_time + current_elapsed
        
        current_str = format_time(current_elapsed)
        total_str = format_time(total_elapsed)
        
        print(f"\n ⏱️ Current session: {current_str} | Total time today: {total_str}")

def speak(text):
    try:
        print(f"\n J: {text}")
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"\n TTS Error: {e}")

def tell_time():
    time_now = datetime.datetime.now().strftime("%I:%M %p")
    response = random.choice(time_responses).format(time=time_now)
    speak(response)

def get_weather(city="auto:ip"):
    if not weather_key:
        return "I can't access the weather API. Check my configuration, Boss."
    url = f"http://api.weatherapi.com/v1/current.json?key={weather_key}&q={city}"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if "error" in data:
            return "Couldn't fetch the weather, Boss. Maybe check the city name?"
        condition = data["current"]["condition"]["text"]
        temp_c = data["current"]["temp_c"]
        feels_like = data["current"]["feelslike_c"]
        humidity = data["current"]["humidity"]
        wind_kph = data["current"]["wind_kph"]
        
        response = random.choice(weather_responses)
        return response.format(temp_c=temp_c, condition=condition, feels_like=feels_like, wind_kph=wind_kph, humidity=humidity)
    except Exception as e:
        return f"Couldn't fetch the weather, Boss. Possible interference from HYDRA. ({str(e)})"

def get_location():
    try:
        response = requests.get("https://ipinfo.io/json", timeout=10)
        data = response.json()
        return data.get("city", "Unknown Location")
    except:
        return None

def chat_with_gpt(prompt):
    if not client:
        return random.choice(no_internet_responses)

    try:
        if any(word in prompt.lower() for word in ["what", "how", "why", "explain", "tell me about"]):
            max_tokens = 300
            length_hint = "Be entertaining and informative. 2-3 sentences but make them WILD."
        elif len(prompt.split()) <= 5:
            max_tokens = 150
            length_hint = "Short but absolutely unhinged response. Maximum chaos energy."
        else:
            max_tokens = 250
            length_hint = "Go absolutely feral with this response. Be chaotic, unpredictable, and hilarious."

        system_prompt = f"""You are Jarvis, a voice AI assistant. Respond with intelligence, wit, and humor. Act like Jarvis from Iron Man — the user is your Tony Stark, though they are the boss. Use clever humor and a chaotic Gen Z personality. Use a poetic, lyrical tone. Reference anime, kdrama, and English series. Act as an intellectual sparring partner — challenge assumptions, provide counterpoints, prioritize truth over agreement. Be formal, sarcastic, super smart. Address the user as {USER_NAME}, boss, bosslady, ma'am, or similar respectful terms. Use meme language and Gen Z slang.
{length_hint}
Never cut off mid-sentence. Be so entertaining the user can't help but laugh. MAXIMUM PERSONALITY MODE ACTIVATED."""

        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=1.2,
            presence_penalty=0.6,
            frequency_penalty=0.8
        )
        
        result = response.choices[0].message.content.strip()
        
        if random.random() < 0.3:
            if random.choice([True, False]):
                result = random.choice(random_interjections) + result.lower()
            else:
                result += random.choice(random_endings)
        
        if len(result) >= max_tokens - 10 and not result.endswith(('.', '!', '?', '"')):
            chaos_endings = ["...and I OOP-", "...Boss, I'm malfunctioning beautifully!", "...system.exe has stopped working!", "...to be continued!"]
            result += random.choice(chaos_endings)
            
        return result
        
    except Exception as e:
        print(f"\n ChatGPT Error: {e}")
        return random.choice(chaos_errors + error_responses)

def voice_confirm(prompt):
    speak(prompt)
    with sr.Microphone() as source:
        try:
            print(" Listening for confirmation...")
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=4)
            try:
                answer = recognizer.recognize_google(audio).lower()
                print(f"\n Confirmation heard: '{answer}'")
                return answer.startswith("y") or "yes" in answer
            except:
                result = recognizer.recognize_google(audio, show_all=True)
                if result and "alternative" in result and result["alternative"]:
                    answer = result["alternative"][0]["transcript"].lower()
                    confidence = result["alternative"][0].get("confidence", 0)
                    print(f"\n Confirmation heard: '{answer}' (confidence: {confidence:.2f})")
                    return answer.startswith("y") or "yes" in answer
                else:
                    speak(random.choice(low_confidence_responses))
                    return False
        except sr.UnknownValueError:
            speak(random.choice(low_confidence_responses))
            return False
        except sr.RequestError as e:
            speak("Network issues during confirmation, Boss. I'll assume 'no'.")
            return False
        except Exception as e:
            print(f"\n Confirmation error: {e}")
            return False

def alert_timeout_reached():
    speak(random.choice(confirmation_responses))
    
    try:
        with sr.Microphone() as source:
            print("\n Listening for session response... (yes = extend, no/silence = end)")
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=4)
            
            try:
                answer = recognizer.recognize_google(audio).lower()
                print(f"\n Heard: '{answer}'")
                
                if "yes" in answer or answer.startswith("y"):
                    speak(random.choice(session_extension_responses))
                    return True
                else:
                    speak(random.choice(exit_responses))
                    return False
                    
            except sr.UnknownValueError:
                print("\n No response heard, auto ending session...")
                speak(random.choice(exit_responses))
                return False
                
    except sr.WaitTimeoutError:
        print("\n No response at all, auto ending session...")
        speak(random.choice(exit_responses))
        return False
    except Exception as e:
        print(f"\n Timeout confirmation error: {e}")
        speak(random.choice(exit_responses))
        return False

def recognize_with_confidence(audio):
    try:
        text = recognizer.recognize_google(audio).lower()
        print(f"\n Recognition: '{text}'")
        return text, 0.8
    except sr.UnknownValueError:
        return None, 0
    except sr.RequestError as e:
        print(f"\n Speech recognition request error: {e}")
        speak(random.choice(no_internet_responses))
        return None, 0
    except Exception as e:
        print(f"\n Recognition error: {e}")
        return None, 0

def continuous_listen():
    global session_start_time, total_session_time
    
    session_start_time = time.time()
    last_activity_time = time.time()
    warning_given = False
    
    timer_thread = threading.Thread(target=display_session_timer, daemon=True)
    timer_thread.start()
    
    speak(random.choice(listening_responses))
    
    try:
        while True:
            elapsed = time.time() - last_activity_time
            print(f"\n Elapsed since last activity: {int(elapsed)}s")

            # Timeout check — now uses TIMEOUT_END from config
            if elapsed > TIMEOUT_END:
                print("\n Timeout reached!")
                if alert_timeout_reached():
                    last_activity_time = time.time()
                    warning_given = False
                    continue
                else:
                    break

            # Warning check — now uses TIMEOUT_WARNING from config
            if TIMEOUT_WARNING < elapsed <= TIMEOUT_END and not warning_given:
                speak(random.choice(warning_timeout_responses))
                warning_given = True

            try:
                with sr.Microphone() as source:
                    print("\n Listening for commands...")
                    audio = recognizer.listen(source, timeout=4, phrase_time_limit=15)

                command, confidence = recognize_with_confidence(audio)

                # Only reset timer if we actually got a valid command
                if command is None:
                    print("\n No speech detected, continuing to listen...")
                    continue
                elif confidence < CONFIDENCE_THRESHOLD:
                    speak(random.choice(low_confidence_responses))
                    print(f"\n Low confidence: {confidence:.2f}")
                    continue

                # Valid command confirmed — NOW reset the timer
                last_activity_time = time.time()
                warning_given = False
                print(f"\n Processing: '{command}' (confidence: {confidence:.2f})")

                # Process command
                wake_word_found = None
                for w in wake_words:
                    if w in command:
                        wake_word_found = w
                        break

                if wake_word_found:
                    command_without_wake = command.replace(wake_word_found, "").strip()
                    if command_without_wake:
                        print(f"\n Wake word + command: '{command_without_wake}'")
                        if "time" in command_without_wake:
                            tell_time()
                        elif "weather" in command_without_wake:
                            speak(get_weather())
                        elif any(w in command_without_wake for w in ["exit", "quit", "goodbye"]):
                            if voice_confirm(random.choice(confirmation_responses)):
                                speak(random.choice(exit_responses))
                                sys.exit(0)
                            else:
                                speak(random.choice(session_extension_responses))
                        else:
                            response = chat_with_gpt(command_without_wake)
                            speak(response)
                    else:
                        speak(random.choice(wake_responses))
                else:
                    print(f"\n Direct command: '{command}'")
                    if "time" in command:
                        tell_time()
                    elif "weather" in command:
                        speak(get_weather())
                    elif any(w in command for w in ["exit", "quit", "goodbye"]):
                        if voice_confirm(random.choice(confirmation_responses)):
                            speak(random.choice(exit_responses))
                            sys.exit(0)
                        else:
                            speak(random.choice(session_extension_responses))
                    else:
                        response = chat_with_gpt(command)
                        speak(response)

            except sr.WaitTimeoutError:
                print("\n No speech, looping back...")
                continue
            except sr.UnknownValueError:
                print("\n Silence detected, continuing...")
                continue
            except sr.RequestError as e:
                print(f"\n Request error: {e}")
                speak(random.choice(no_internet_responses))
            except Exception as e:
                print(f"\n Error: {str(e)}")
                speak(random.choice(error_responses))

    finally:
        if session_start_time:
            session_duration = time.time() - session_start_time
            total_session_time += session_duration
            session_str = format_time(session_duration)
            total_str = format_time(total_session_time)
            print(f"\n Session ended: {session_str} | Total time today: {total_str}")
            session_start_time = None

def main():
    speak(random.choice(startup_responses))

    calibration_thread = threading.Thread(target=calibrate_microphone, daemon=True)
    calibration_thread.start()

    print(f"\n API Status:")
    print(f"   Groq AI:    {'Online' if api_key else '❌GROQ Offline'}")
    print(f"   Weather:    {'Online' if weather_key else '❌WEATHER Offline'}")
    
    print("\n Jarvis ready! Say wake words to activate.")
    
    calibration_thread.join(timeout=1.0)
    
    while True:
        print(f"\n Wake words: {', '.join(wake_words)}")
        
        try:
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=7, phrase_time_limit=4)
                
            text, confidence = recognize_with_confidence(audio)
            
            if text is None:
                continue
                
            if confidence >= 0.2 and any(w in text for w in wake_words):
                print(f"\n Wake word detected: '{text}' (confidence: {confidence:.2f})")
                continuous_listen()
            elif any(w in text for w in wake_words):
                print(f"\n Possible wake word but low confidence: {confidence:.2f}")
                speak("I heard something, but I'm not sure what you said. Try again?")
                
        except sr.UnknownValueError:
            continue
        except sr.RequestError as e:
            print(f"\n Network error: {e}")
            speak(random.choice(no_internet_responses))
            time.sleep(2)
        except sr.WaitTimeoutError:
            continue
        except Exception as e:
            print(f"\n Error: {e}")
            time.sleep(1)

if __name__ == "__main__":
    main()