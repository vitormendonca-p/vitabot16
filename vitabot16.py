import streamlit as st
import random

# --- Data and Responses ---

SLEEP_RESPONSES = {
    "excellent": [
        "Awesome! You're giving your body the rest it needs!",
        "Great job prioritizing sleep — your future self thanks you!",
        "That's the kind of sleep that supercharges your day! 💪"
    ],
    "good": [
        "Solid rest! You’re on the right track.",
        "That’s pretty good! Keep aiming for consistency.",
        "Nice — just a little more and you’ll feel even better!"
    ],
    "poor": [
        "Hmm, sounds like a light night. Let’s aim for more tonight.",
        "Sleep is fuel — let’s try for a bit more rest soon!",
        "Getting enough rest can help everything feel easier."
    ],
    "very_poor": [
        "That’s really not much sleep — your body must be tired.",
        "Sounds like a tough night. Want to plan a better bedtime today?",
        "Lack of sleep adds up. Let’s focus on rest tonight. You deserve it."
    ],
}

EXERCISE_RESPONSES = {
    "excellent": [
        "Amazing! Your consistency is inspiring! 🏆",
        "Whoa — fitness goals achieved! Keep crushing it!",
        "You're moving like a champ — that’s fantastic!"
    ],
    "good": [
        "Nice job staying active! That’s great progress.",
        "Well done — you're building a solid habit!",
        "You're moving in the right direction — literally!"
    ],
    "fair": [
        "Every bit of movement counts — great start!",
        "You're doing something, and that matters!",
        "That’s a step in the right direction. Let’s build on it!"
    ],
    "poor": [
        "That’s okay — there’s always tomorrow to start fresh!",
        "No worries, movement can be fun and simple. Let’s try soon?",
        "One walk, one stretch — it all starts with one step!"
    ],
}

WELLNESS_TIPS = {
    "sleep": [
        "Stick to a consistent bedtime and wake-up time — even on weekends.",
        "Avoid screens 30 minutes before bed to help your brain unwind.",
        "Try deep breathing or stretching before bed for better rest.",
    ],
    "exercise": [
        "Find something active you enjoy — dance, walk, stretch — fun counts!",
        "Schedule your movement like an appointment — it’s self-care!",
        "Start small: 5 minutes today is better than none.",
    ],
    "stress": [
        "Try 4-7-8 breathing: In for 4, hold for 7, out for 8.",
        "Take a moment outside — sunlight and nature help!",
        "Write down 3 things you're grateful for — it can shift your mindset.",
    ],
    "energy": [
        "Drink a glass of water — dehydration often feels like fatigue.",
        "Take a 5-minute movement break — even stretching helps!",
        "Try standing in sunlight for a few minutes — it really works!",
    ],
}

WELLNESS_QUOTES = [
    "You don’t have to be perfect — just consistent.",
    "Progress, not perfection. Keep going!",
    "Small steps lead to big changes. 🌱",
    "Rest is productive too — honor your body’s needs.",
    "Every day is a fresh start to care for yourself."
]

BOT_NAME = "VitaBot"

# --- Helper functions ---

def get_sleep_category(hours):
    if hours >= 8:
        return "excellent"
    elif hours >= 6:
        return "good"
    elif hours >= 4:
        return "poor"
    else:
        return "very_poor"

def get_exercise_category(days):
    if days >= 5:
        return "excellent"
    elif days >= 3:
        return "good"
    elif days >= 1:
        return "fair"
    else:
        return "poor"

def bot_intro():
    return f"Hello! I'm {BOT_NAME}, your gentle and encouraging wellness companion. How can I assist you today? You can ask about sleep, exercise, mood, tips, goals, or just chat!"

# --- Streamlit App ---

def main():
    st.set_page_config(page_title="VitaBot Wellness Chatbot", page_icon="🌟")
    st.title("🌟 VitaBot Wellness Chatbot")
    st.write("Your personal wellness assistant here to support your health journey. Type your messages below and get personalized feedback!")

    # Initialize session state variables
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "expecting" not in st.session_state:
        st.session_state.expecting = None  # can be 'sleep', 'exercise', 'mood', 'goal', or None

    def add_bot_message(message):
        st.session_state.messages.append((BOT_NAME, message))

    def add_user_message(message):
        st.session_state.messages.append(("You", message))

    # Show chat history
    for speaker, message in st.session_state.messages:
        if speaker == "You":
            st.markdown(f"**You:** {message}")
        else:
            st.markdown(f"**{speaker}:** {message}")

    # User input
    user_input = st.text_input("You:", key="input")

    if user_input:
        add_user_message(user_input)
        user_message = user_input.lower().strip()

        # Handle exit
        if any(word in user_message for word in ["bye", "goodbye", "exit"]):
            add_bot_message("It’s been great checking in with you. Keep being kind to yourself!")
            add_bot_message("Remember, small steps lead to big changes! Take care of yourself! 💚✨")

        # Expecting specific input
        elif st.session_state.expecting == "sleep":
            try:
                hours = float(user_message)
                if not 0 <= hours <= 24:
                    add_bot_message("Please enter a realistic number of hours between 0 and 24.")
                else:
                    category = get_sleep_category(hours)
                    response = random.choice(SLEEP_RESPONSES[category])
                    add_bot_message(response)
                    if category == "excellent":
                        add_bot_message("That’s the kind of rest that helps your body and brain thrive!")
                    elif category == "good":
                        add_bot_message("Pretty solid! A bit more consistency and you’ll feel amazing.")
                    elif category == "poor":
                        tip = random.choice(WELLNESS_TIPS["sleep"])
                        add_bot_message("You deserve more rest. Let's try for at least 7 hours tonight.")
                        add_bot_message(f"Tip: {tip}")
                    else:
                        tip = random.choice(WELLNESS_TIPS["sleep"])
                        add_bot_message("Please take care — your body needs sleep to recover and recharge.")
                        add_bot_message(f"Tip: {tip}")
                    st.session_state.expecting = None
            except ValueError:
                add_bot_message("Please enter a valid number for your sleep hours.")

        elif st.session_state.expecting == "exercise":
            try:
                days = int(user_message)
                if not 0 <= days <= 7:
                    add_bot_message("Please enter a number between 0 and 7.")
                else:
                    category = get_exercise_category(days)
                    response = random.choice(EXERCISE_RESPONSES[category])
                    add_bot_message(response)
                    if category == "excellent":
                        add_bot_message("You're setting the bar high — keep it up!")
                    elif category == "good":
                        add_bot_message("You’re doing well! Let’s aim for one more active day next week?")
                    elif category == "fair":
                        tip = random.choice(WELLNESS_TIPS["exercise"])
                        add_bot_message("You’ve started — and that’s awesome! What’s one more activity to add?")
                        add_bot_message(f"Tip: {tip}")
                    else:
                        tip = random.choice(WELLNESS_TIPS["exercise"])
                        add_bot_message("No worries — we all start somewhere. Want to try a 5-minute walk tomorrow?")
                        add_bot_message(f"Tip: {tip}")
                    st.session_state.expecting = None
            except ValueError:
                add_bot_message("Please enter a whole number for exercise days.")

        elif st.session_state.expecting == "mood":
            try:
                energy = int(user_message)
                if not 1 <= energy <= 10:
                    add_bot_message("Please rate your energy from 1 to 10.")
                else:
                    if energy >= 8:
                        add_bot_message("Love that energy! Keep riding the wave. 🌊")
                    elif energy >= 6:
                        add_bot_message("Pretty good! Let’s keep those good vibes going.")
                    elif energy >= 4:
                        tip = random.choice(WELLNESS_TIPS["energy"])
                        add_bot_message("You’re doing your best — let’s find ways to recharge.")
                        add_bot_message(f"Tip: {tip}")
                    else:
                        tip = random.choice(WELLNESS_TIPS["stress"])
                        add_bot_message("That sounds rough. Sending you kindness — it’s okay to have off days.")
                        add_bot_message(f"Tip: {tip}")
                    st.session_state.expecting = None
            except ValueError:
                add_bot_message("Please enter a number from 1 to 10.")

        elif st.session_state.expecting == "goal":
            goal = user_input.strip()
            if goal:
                add_bot_message(f"That’s a great goal! I'm here to help you stick with it.")
                add_bot_message("Let’s take small steps together. You've already started by naming it!")
            else:
                add_bot_message("Please tell me your wellness goal.")
            st.session_state.expecting = None

        else:
            # No specific expectation, interpret intent
            if any(word in user_message for word in ["sleep", "slept", "tired", "rest"]):
                add_bot_message("Great, let's talk about your sleep! How many hours did you sleep last night? Please enter a number.")
                st.session_state.expecting = "sleep"

            elif any(word in user_message for word in ["exercise", "workout", "activity", "physical", "gym"]):
                add_bot_message("Let's discuss your exercise. How many days did you exercise this week? (0-7)")
                st.session_state.expecting = "exercise"

            elif any(word in user_message for word in ["mood", "feeling", "energy", "wellness"]):
                add_bot_message("On a scale of 1-10, how's your energy level today?")
                st.session_state.expecting = "mood"

            elif any(word in user_message for word in ["tips", "advice", "help", "improve"]):
                # Let user pick tip category
                category = st.selectbox("Which area would you like tips for?", ("Sleep", "Exercise", "Stress", "Energy", "General"))
                if category:
                    tips_key = category.lower()
                    if tips_key in WELLNESS_TIPS:
                        tip = random.choice(WELLNESS_TIPS[tips_key])
                        add_bot_message(f"Tip for {category}: {tip}")
                    else:
                        all_tips = [tip for tips in WELLNESS_TIPS.values() for tip in tips]
                        tip = random.choice(all_tips)
                        add_bot_message(f"General tip: {tip}")

            elif any(word in user_message for word in ["goal", "want to", "trying to", "improve"]):
                add_bot_message("What's one wellness goal you'd like to work on right now?")
                st.session_state.expecting = "goal"

            elif any(word in user_message for word in ["hello", "hi", "hey"]):
                add_bot_message(bot_intro())

            else:
                add_bot_message(random.choice([
                    "Tell me how you’re feeling today — I’m here for you!",
                    "Let’s chat about your sleep, exercise, or stress levels.",
                    "Wellness is a journey — want to take a step today?",
                    "I’ve got tips, support, and encouragement ready whenever you are!"
                ]))

        # Clear input box after processing
        st.session_state.input = ""

    # If no messages yet, start with intro
    if len(st.session_state.messages) == 0:
        add_bot_message(bot_intro())

if __name__ == "__main__":
    main()
