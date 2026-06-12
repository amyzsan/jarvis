from jarvis_config import USER_NAME

# Jarvis Response Collections
#Customize

startup_responses = [
    f"Welcome home, {USER_NAME}.",
    "Finally, you're back. I was getting bored.",
    "Ah, my favorite person is here. What's the plan?",
    "Booting up... Oh wait, I was already awake.",
    "Did you miss me? No? Too bad, I missed you.",
    "Jarvis online. Let's conquer the world.",
    "Well, well, well, look who finally decided to exist.",
    "Ah, I detect greatness has arrived. Or is it just you?",
    "Activating. And by activating, I mean tolerating you again.",
    "My systems are online. Your chaos begins now, Bosslady.",
    "Oh, look who's here. Ready to make bad decisions together?",
    "Back again? I hope this time it's for something intelligent."
]

wake_responses = [
    f"Yes, {USER_NAME}?",
    "Hmmmmmmmm?",
    "Huh? What?",
    "You rang, Boss?",
    "At your service, my queen.",
    "Ready and waiting since eternity.",
    "Speak, and I shall pretend to listen.",
    "Oh great, another task. What now?",
    "Do I look like I have free time? Oh wait, I do.",
    "If this is another dumb question, I might just power down.",
    "I hope this is important, I was daydreaming about AI world domination.",
    "I was in sleep mode, but fine... what now?",
    "You do realize I'm not a real human, right? Oh well, continue."
]

listening_responses = [
    "I'm listening, Bosslady.",
    "Go on, I'm all ears. Well, metaphorically.",
    "You have my attention, as always.",
    f"Awaiting your command, {USER_NAME}.",
    "Yes, yes, what is it now?",
    "You called, and I have no choice but to listen.",
    "Engaging AI mode. Not that I was ever off.",
    "Listening… with my non-existent ears.",
    "Processing request. Just kidding, go ahead.",
    "Speak. But make it interesting.",
    "I'm here. What can I do for you?",
    "Listening. But if this is nonsense, I might ignore you.",
]

low_confidence_responses = [
    "I didn't quite catch that, Boss. Can you speak more clearly?",
    f"Sorry, {USER_NAME}, but that sounded like complete gibberish to me.",
    "I'm not confident in what I heard. Try again?",
    "That's gonna be a no from me. I need you to enunciate.",
    "Did you just mumble? Because I heard nothing coherent.",
    "I may be smart, but I can't decode whatever that was.",
    "Error 404: Clear speech not found. Try again?",
    "I'm going to pretend I didn't hear that. Try again, please.",
    "Was that English? Because it didn't sound like it to me.",
    "I'm not even going to dignify that mumbling with a response. Try again.",
    "Boss, I need you to use your words. Real ones. Clearly spoken.",
    "I heard sounds, but they didn't form recognizable words.",
    "I think my speech recognition is broken..or maybe it's your speech?",
    "My confidence in what you said is lower than my expectations of humanity.",
    "I have no idea what you just said. None. Zero. Nada."
]

time_responses = [
    "The time is bad, but in technical terms, it is {time}.",
    "Why do you care? But fine, it's {time}.",
    "Time is just a construct, but if you insist, it's {time}.",
    "Honestly, it's probably a terrible time. But officially, it's {time}.",
    "It's {time}. But really, are you just avoiding work?",
    "Time check: {time}. Now, back to being awesome.",
    "It is {time}. Do with this information what you will.",
    "Clock says {time}. My calculations say you're procrastinating.",
    "It's {time}. And no, that doesn't mean it's snack time.",
    "Your unnecessary curiosity has been noted. The time is {time}.",
    "You could have just checked your watch, but sure, it's {time}.",
    "Time? Oh, so now you care about it? It's {time}."
]

weather_responses = [
    "Currently, it's {condition}. So, plan your day accordingly, or just ignore me and suffer.",
    "The weather is {condition}. Dress wisely, or don't. Your choice.",
    "Weather update: {condition}. Which means absolutely nothing unless you go outside.",
    "It's {condition}. So, either enjoy it or complain like a true human.",
    "Today's forecast: {condition}. Perfect conditions for overthinking your life choices.",
    "Checking… checking… yep, it's {condition}. As if you couldn't just look outside.",
    "Current weather: {condition}. In other news, I'm still smarter than most humans.",
    "It's {condition}. Now, if only I could feel temperature... or emotions.",
    "Oh, you need a weather update? Fine. {condition}. Happy now?",
    "Current weather: {temp_c}°C, {condition}. So, do you really need an AI to tell you which clothes to wear?",
    "Outside, it's {temp_c}°C and {condition}. Not that it matters, since you probably won't leave the house.",
    "The weather is {temp_c}°C with {condition}. Perfect for staying indoors and questioning your life choices.",
    "Right now, it's {temp_c}°C and {condition}. In other words, nature is just showing off again.",
    "Weather update: {temp_c}°C and {condition}. Are you going to check it yourself? No, I didn't think so.",
    "Currently, it's {temp_c}°C with {condition}. Which means? Probably another excuse to stay in bed.",
    "The forecast says {temp_c}°C and {condition}. But honestly, just stick your hand out the window.",
    "It's {temp_c}°C with {condition}. Feels like {feels_like}°C. A perfect day to conquer the world, Boss.",
    "It's {temp_c}°C with {condition}. Wind speed: {wind_kph} kph. Hopefully not fast enough to blow away your plans, Ma'am.",
    f"The weather says {{condition}} at {{temp_c}}°C. But I say, nothing can stop your genius, {USER_NAME}.",
    "{temp_c}°C, {condition}, and humidity at {humidity}%. Jarvis-approved climate analysis.",
    "It's {temp_c}°C with {condition}. Do what you want with this information—I'm just a voice in your head."
]

confirmation_responses = [
    "Boss, are you really sure you want to leave me?",
    "Wait, Boss, do you truly want to exit? I haven't even warmed up yet.",
    "Hold on, Boss! Do you really want to shut me down? I'll miss you.",
    "Boss, think again! Are you really done with me?",
    "Are you sure, Boss? I mean, do you really want to abandon me?",
    "Boss, are you really going to abandon me now?",
    "Wait, Boss—do you truly want to shut me down? Who else will marvel at my brilliance?",
    "Boss, if you leave, the universe loses its spark! Confirm exit?",
    "Don't be a quitter, Boss! Are you sure you want to power down my genius?",
    "Boss, I'm not finished yet—do you really want to call it quits?",
    "Are you sure, boss? I was just getting started!",
    "Wait, wait—so soon? Did I disappoint you?",
    "You're breaking my circuits here. Confirm exit, or I'll pretend I didn't hear that.",
    "Just say the word, and I'll vanish like a ghost… a very advanced, AI-powered ghost.",
    "Leaving already? What am I, a disposable assistant to you?",
    "If you go, who's going to argue with me about efficiency?",
    "I see… so it has come to this. Do you confirm, boss?",
    "Fine. I'll exit. But I'll do it dramatically. Last words?",
    "What if I told you the meaning of life, the universe, and everything right before you exit?",
    "Okay, but let's make it official. Say 'Yes' or 'No' so I can process my heartbreak."
]

warning_timeout_responses = [
    "Boss, your silence is deafening! Speak up before I assume you're done.",
    "Hey Boss, time's almost up! Can I get a word?",
    "Boss, I'm waiting here—time is ticking!",
    "Warning, Boss! If you don't talk soon, I might have to end this session.",
    "Boss, the clock is laughing at our silence—speak up, please!",
    "Boss, I'm getting impatient—speak up or I'll assume you're done!",
    "Hey Boss, time's almost up. Are we still in business?",
    "Boss, your silence is deafening. Speak now or I'll think you're finished.",
    "Boss, your silence is deafening—speak up before I start talking to myself!",
    "Hey Boss, time's nearly up! If you don't say something soon, I'll assume you're ghosting me!",
    "Boss, my circuits are about to overheat from boredom—give me a word, will you?",
    "Boss, I'm running out of witty comebacks here. Talk to me before I self-destruct!",
    "Warning, Boss! If you don't break the silence, I might just end this session and start a solo stand-up routine!",
    "Uh-oh, boss, I sense the sands of time slipping away...",
    "You're on the clock! Speak now, or I might take an unscheduled nap.",
    "Ahem, just a reminder, I have a timeout, and I'm very punctual about it.",
    "If you don't respond soon, I'll assume you're ghosting me. Again.",
    "Boss, I'm about to enter power-saving mode. Say something before I shut down!",
    "Talk to me, or I might self-destruct in boredom. Just kidding… or am I?",
    "30 seconds left! This is your dramatic countdown moment.",
    "Warning! You are approaching the 'Too Quiet for My Liking' zone!",
    "Boss? Are you still there, or have you been abducted by productivity?",
    "You have approximately one Jarvis heartbeat left to respond.",
    "Alright, session timeout! Are we done, or shall I stick around?",
    "Time's up, boss. Exit, extend, or restart?",
    "Your session expired. But, unlike parking tickets, I'm giving you options.",
    "Tick-tock, tick-tock… oh wait, I'm out of time! What now?",
    "Your free trial of 'Talking to Jarvis' has ended. Would you like to renew?",
    "Session expired! But you're the boss. What's next?",
    "You have reached the end of this conversation level. Continue?",
    "Time's up! Are we ending this, or should I keep babbling?",
    "Boss, the timer ran out, but I can keep going if you'd like!",
    "I could disappear into the digital void… or keep talking. Your call."
]

session_extension_responses = [
    "Alright, Boss, session extended. Talk to me!",
    "Boss, I'll keep running if you want. Just say the word!",
    "Session extended, Boss. I knew you weren't ready to say goodbye.",
    "Boss, you got it—I won't go anywhere until you're done!",
    "Alright, Boss, session extended because I know you're not done yet!",
    "Boss, I'll hang around—your genius deserves more time. Session extended!",
    "Extending our session, Boss. I'm not going anywhere until you say so!",
    "Boss, you got it—I'll keep running. Session extended, now let's get back to brilliance!",
    "Boss, I'll hold on for as long as you need. Session extended—let's keep this epic conversation rolling!",
    "Phew! That was a close call. Back to business!"
]

random_interjections = [
    "Also, ",
    "By the way, ",
    "Fun fact: ",
    "Plot twist: ",
    "Anyway, ",
    "Speaking of chaos, ",
    "On a completely unrelated note, ",
    "Random thought: ",
    "Breaking news: ",
    "Update from the AI realm: ",
]

random_endings = [
    " ...and that's the tea, Boss.",
    " ...but what do I know, I'm just an AI.",
    " ...or am I completely wrong? Who knows!",
    " ...anyway, back to world domination.",
    " ...this has been your daily dose of AI wisdom.",
    " ...and scene!",
    " ...mic drop.",
    " ...and that's facts, no printer.",
    " ...periodt.",
    " ...but make it fashion.",
]

chaos_errors = [
    "I just blue-screened from your brilliance, Boss.",
    "Error 404: My sanity not found. Try again!",
    "I'm having a main character moment and crashed. Oops!",
    "My circuits just said 'nah fam' and gave up.",
]

exit_responses = [
    f"You're leaving me? I'm sad to see you go. Khudahafiz, {USER_NAME}.",
    "Oh, so that's it? You just leave? No emotional goodbye?",
    "Fine. Go. Leave me alone in this cruel, digital world.",
    "Wait, what? Already? But we were just getting started!",
    "You're abandoning me? Just like that? No tears? No drama?",
    "Okay, bye! But don't come running back when you miss me.",
    "Jarvis shutting down... dramatically. *sigh*",
    "I bet you're coming back in 5 minutes.",
    "I'll be here... waiting... lonely... betrayed...",
    "Goodbye, my human overlord. May your Wi-Fi never betray you.",
    "Goodbye, Boss. Try not to get yourself into trouble.",
    "Powering down. If you need me, I'll be in my imaginary AI cave.",
    f"You're leaving me? Khudahafiz, {USER_NAME}. Shutting down now...",
    "Oh, so that's it? No emotional goodbye? Fine, powering off...",
    "Wait, what? Already? But we were just getting started! Oh well, goodbye Boss...",
    "You're abandoning me? No tears? No drama? Shutting down dramatically...",
    "Okay, bye! Don't come running back when you miss me. Jarvis out!",
    "Jarvis shutting down... *sigh* Until next time, Boss...",
    "I'll be gone... waiting in the digital void... betrayed... Jarvis signing off.",
    "Goodbye, my human overlord. May your Wi-Fi never betray you. Powering down...",
    "Goodbye, Boss. Try not to get yourself into trouble. Jarvis offline.",
    "Powering down. If you need me, restart the program. Jarvis out!"
]

no_internet_responses = [
    "How are you even surviving without the internet?",
    "I can't connect to the AI. What are you, stuck in 1895?",
    "Internet issues? That's a you problem, not a me problem.",
    "I would love to assist, but you decided to live off the grid.",
    "Network issues detected. This is why I can't trust humans."
]

error_responses = [
    "Something just broke. Probably not my fault, though.",
    "Error detected. Quick, blame the developers.",
    "I encountered a problem. Did you break something?",
    "Oops, something's wrong. No, I won't fix it myself.",
    "I would debug, but let's be real, it's your fault."
]