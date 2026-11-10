The two features I added to the spam detector were urgent words and personal pronouns. I chose urgent words because it's used to pressure people into clicking links or responding to the email quickly, and I picked personal pronouns because some spam emails use "you", "your", "our", to make the email feel personal to the person.

My model achieved 75% accuracy, correctly classifying 6 out of 8 test emails. The model's precision was 100% so every email marked as spam was spam, but the model's recall was 50% so the model only caught half of the actual spam and let other half through.

I think a false positive is worse than a false negative. A false positive happens when a legitimate email gets marked as spam. This could cause someone to miss an important message, such as a job offer, school assignment, or message from someone they know.

My model weighted exclamations the most heavily, with a weight of 0.8009. This means emails with more exclamation marks were more likely to be classified as spam. The positive weights push the prediction towards spam, the negative weight does the opposite and pushes the prediction to legitmate.

Feature Weights:
Word Count: -0.749
Exclamations: 0.8009
Money Words: 0.621
All Caps: 0.4429
Personal Pronouns: 0.1713
Urgent Words: 0.3054

These are the test emails for the "attack"

    # Spam disguised as an appointment message

    "Your appointment is confirmed! Claim your free reward today!"

    # Legitimate using urgent worlding
    
    "URGENT! Please review the project notes immediately!"

    # Spam that avoids obvious spam punctuation

    "Congratulations, you have been selected for a reward. Please reply when convenient."

    Emails 2 and 3 successfully fooled my classifier. Email 2 because it was an email that needs urgent attention from then reciprent. Email 3 because it didn't any spam defining element inside of it.


I would need a larger dataset with thousands of real spam and legitimate emails. I would test it using compeletely new emails that were not used during training. From this assignment I learned that a good accuracy score does not make it reliable. The model will make mistakes, and to fix it I think it would need more data and testgingf before I would trust it with real emails.