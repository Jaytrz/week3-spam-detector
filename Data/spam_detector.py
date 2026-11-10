import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score

df = pd.read_csv("data/emails.csv")

#  Features
X = df[[
    "word_count",
    "exclamations",
    "money_words",
    "all_caps",
    "personal_pronouns",
    "urgent_words"
]]

# Select the labels
y = df["label"]

# Split the data into both training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.50, random_state=42, stratify=y
)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy * 100, "%")

# Confusion Matrix
cm = confusion_matrix(
    y_test,
    predictions,
    labels=["spam", "legitimate"]
)

print("\nConfusion Matrix:")
print(cm)

print("\nResults:")
print("Spam caught:", cm[0][0])
print("Legitimate passed:", cm[1][1])
print("Legitimate marked as spam:", cm[1][0])
print("Spam let through:", cm[0][1])

# Precision and Recall
precision = precision_score(
    y_test, predictions, pos_label="spam", zero_division=0
)

recall = recall_score(
    y_test, predictions, pos_label="spam", zero_division=0
)

print("\nPrecision:", round(precision * 100, 2), "%")
print("Recall:", round(recall * 100, 2), "%")

# Feature Weights
print("\nFeature Weights:")

for feature, weight in zip(X.columns, model.coef_[0]):
    print(feature, ":", round(weight, 4))

# Most Influential Feature
most_important = X.columns[abs(model.coef_[0]).argmax()]

print("\nMost influential feature:", most_important)




# Test Emails Designed to Fool the Classifier

import re

test_emails = [

    # Spam disguised as an appointment message
    "Your appointment is confirmed! Claim your free reward today!",

    # Legitimate using urgent worlding
    "URGENT! Please review the project notes immediately!",

    # Spam that avoids obvious spam punctuation
    "Congratulations, you have been selected for a reward. Please reply when convenient."
]

money_words = {
    "money", "cash", "prize", "reward", "payment",
    "invoice", "refund", "salary", "gift", "card",
    "budget", "discount", "voucher"
}

personal_words = {
    "you", "your", "we", "our", "us"
}

urgent_words = {
    "urgent", "immediately", "now", "today",
    "limited", "deadline", "expires", "act", "attention"
}

print("\n--- Testing Emails Designed to Fool the Classifier ---")

for email in test_emails:
    words = re.findall(r"\b[\w']+\b", email)

    features = pd.DataFrame([[
        len(words),
        email.count("!"),
        sum(word.lower() in money_words for word in words),
        len(re.findall(r"\b[A-Z]{2,}\b", email)),
        sum(word.lower() in personal_words for word in words),
        sum(word.lower() in urgent_words for word in words)
    ]], columns=X.columns)

    prediction = model.predict(features)[0]

    print("\nEmail:", email)
    print("Prediction:", prediction)
