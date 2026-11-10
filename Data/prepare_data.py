import pandas as pd

emails = [
    # Spam emails
    ["Congratulations! You won $500! Claim your prize now!", 8, 2, 1, 1, 0, 2, "spam"],
    ["URGENT! Get your FREE gift today!", 6, 1, 1, 2, 0, 2, "spam"],
    ["Click here to win a free gift card!", 8, 1, 0, 0, 1, 0, "spam"],
    ["Limited time offer! Get money now!", 6, 1, 1, 0, 0, 1, "spam"],
    ["You have been selected for a cash reward!", 8, 1, 1, 0, 0, 0, "spam"],
    ["Act now! Claim your free prize before it expires!", 9, 1, 0, 0, 1, 2, "spam"],
    ["Earn money from home with this amazing offer!", 8, 1, 1, 0, 1, 0, "spam"],
    ["WIN BIG TODAY! Visit our website for details!", 8, 2, 0, 2, 1, 0, "spam"],

    # Legitimate emails
    ["Hi, are we still meeting for lunch tomorrow?", 9, 0, 0, 0, 0, 0, "legitimate"],
    ["Please review the document I sent you yesterday.", 8, 0, 0, 0, 0, 0, "legitimate"],
    ["Your appointment is confirmed for Monday morning.", 8, 0, 0, 0, 0, 0, "legitimate"],
    ["Thanks for helping me with the project.", 7, 0, 0, 0, 0, 0, "legitimate"],
    ["Can you send me the notes from class?", 8, 0, 0, 0, 0, 0, "legitimate"],
    ["I will see you at the meeting next week.", 9, 0, 0, 0, 0, 0, "legitimate"],
    ["The report is attached. Let me know what you think.", 10, 0, 0, 0, 0, 0, "legitimate"],
    ["Happy birthday! Hope you have a great day!", 9, 1, 0, 0, 0, 0, "legitimate"]
]

columns = [
    "email_text",
    "word_count",
    "exclamations",
    "money_words",
    "all_caps",
    "personal_pronouns",
    "urgent_words",
    "label"
]

df = pd.DataFrame(emails, columns=columns)

df.to_csv("data/emails.csv", index=False)

print("Dataset created successfully!")
print(df)