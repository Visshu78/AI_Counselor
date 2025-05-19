# chatbot_engine.py

from ccbt_flow import get_ccbt_response
from abc_technique import run_abc_flow

# Track session flow stage
stage = {
    "mode": "ccbt",  # can be: ccbt, abc, stai
    "step": 0
}

def process_input(user_input, bot_reply, ccbt_step, abc_step):
    user_input = user_input.lower()

    if "depress" in user_input:
        bot_reply = "I'm really sorry you're feeling that way. Would you like to talk more about what's making you feel depressed?"
    elif "share" in user_input:
        bot_reply = "I'm here for you. Please feel free to share whatever you feel comfortable with."
    elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
        bot_reply = "Hey there! I'm here to support you. How are you feeling today?"
    else:
        bot_reply = "Let's talk more about that. What's been on your mind lately?"

    # Example: if you want to trigger ABC technique or CCBT steps later
    using_abc = False  # You can customize this later based on stages

    return bot_reply, ccbt_step, abc_step, using_abc




def get_bot_response(user_input):
    global stage

    # ABC Trigger (example: if user mentions negative self-belief)
    if "not good enough" in user_input.lower() or "failure" in user_input.lower():
        stage["mode"] = "abc"
        stage["step"] = 0

    # CCBT flow
    if stage["mode"] == "ccbt":
        response, next_step = get_ccbt_response(user_input, stage["step"])
        stage["step"] = next_step
        return response

    # ABC Technique flow
    elif stage["mode"] == "abc":
        response, done = run_abc_flow(user_input, stage["step"])
        if done:
            stage["mode"] = "ccbt"
            stage["step"] = 0
        else:
            stage["step"] += 1
        return response

    # Future: Add STAI handling here

    return "I'm here to listen. Could you tell me more about how you’re feeling?"
