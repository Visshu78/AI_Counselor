# abc_technique.py

# ABC dialogue steps
abc_prompts = [
    "Let's try the ABC technique. Can you describe a situation that recently upset you? (This is the Antecedent)",
    "Now, what belief or thought did you have in that moment? (This is the Belief)",
    "What was the result or emotional consequence of that thought? (This is the Consequence)",
    "Thank you for sharing. Let's now look at whether that belief is realistic or helpful.",
    "Can you think of an alternative, more balanced thought you could have had in that situation?",
    "That’s a great step forward. How do you feel when you think of this new belief?",
    "Well done! These small steps really matter. Feel free to talk more or continue with reflection exercises."
]

def run_abc_flow(user_input, step):
    if step >= len(abc_prompts):
        return "Thanks for sharing. Let’s return to our regular chat whenever you’re ready.", True

    response = abc_prompts[step]
    done = (step == len(abc_prompts) - 1)
    return response, done
