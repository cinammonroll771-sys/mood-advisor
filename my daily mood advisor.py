import datetime

# Step 1 & 2: Get current date and time
now = datetime.datetime.now()
current_day = now.strftime("%A")  # e.g. Monday
current_hour = now.hour
current_date_str = now.strftime("%Y-%m-%d %H:%M:%S")

print(f"Today is {current_day}, {current_date_str}")

# Step 3: Define moods (the platform expects these variables)
# You can change the mood to test: happy, sad, tired, stressed, excited
mood = "happy"  # change this for testing
# If they ask for input, use: mood = input("How are you feeling today? (happy/sad/tired/stressed/excited): ").lower()

# Step 4: Daily Mood Advisor Logic
def mood_advisor(day, hour, mood):
    # Time based greeting
    if hour < 12:
        time_greeting = "Good Morning"
    elif hour < 18:
        time_greeting = "Good Afternoon"
    else:
        time_greeting = "Good Evening"

    # Day based advice
    if day == "Monday":
        day_message = "Monday can be tough, start slow and stay positive!"
    elif day == "Friday":
        day_message = "It's Friday! Finish strong!"
    elif day in ["Saturday", "Sunday"]:
        day_message = "It's the weekend! Time to relax and recharge!"
    else:
        day_message = f"Happy {day}! Make the most of your day!"

    # Mood based advice
    if mood == "happy":
        mood_message = "Keep smiling! Share your positivity with others."
    elif mood == "sad":
        mood_message = "It's okay to feel sad. Take a walk, listen to music, and talk to someone you trust."
    elif mood == "tired":
        mood_message = "You seem tired. Get some rest, drink water, and take a short break."
    elif mood == "stressed":
        mood_message = "Take a deep breath. Try meditation, organize your tasks, and don't overthink."
    elif mood == "excited":
        mood_message = "Awesome! Use that energy to do something creative!"
    else:
        mood_message = "No matter how you feel, remember every day is a new opportunity."

    # Final combined message
    final_advice = f"{time_greeting}! {day_message} {mood_message}"
    return final_advice

# Step 5: Print final result
advice = mood_advisor(current_day, current_hour, mood)
print(f"\nYour Mood: {mood.capitalize()}")
print(f"Advice: {advice}")