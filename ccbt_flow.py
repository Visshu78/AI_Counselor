# ccbt_flow.py

# Predefined CBT-style conversation flow
ccbt_dialogues = [
    "I’m sorry to hear that. Would you like to share what’s been making you feel anxious?",
    "That sounds tough. When you think about that situation, what thoughts usually come to mind?",
    "It’s natural to feel that way sometimes. Can we try to challenge that thought?",
    "What evidence do you have that supports or contradicts that belief?",
    "That’s great insight! How do you feel when you remind yourself of these positive facts?",
    "We can continue recognizing these helpful thoughts together. Would you like to try a short reflection exercise?",
]

def get_ccbt_response(user_input, step):
    # If we've reached the end of flow, loop back or stay calm
    if step >= len(ccbt_dialogues):
        return "You’re doing really well. Take your time and share more if you’d like.", step

    # Get the appropriate response
    response = ccbt_dialogues[step]
    next_step = step + 1
    return response, next_step
