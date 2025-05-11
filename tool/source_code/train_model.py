import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Combined dataset with phishing and legitimate emails
data = {
    "text": [
        # PHISHING EXAMPLES (label 1)
        "Your account has been suspended. Click to verify.",
        "Urgent: Update bank details to avoid penalty.",
        "Congratulations! You've won a new iPhone. Claim now!",
        "Re-enter your password to keep your account active.",
        "CEO needs urgent wire transfer – respond now.",
        "Here’s the invoice you asked for. Open the attached link.",
        "Please update our vendor banking info immediately.",
        "You’ve received a document. Login to view it.",
        "Get your tax refund now – enter your details.",
        "Microsoft detected a virus on your PC. Call support now!",
        "Free COVID-19 Test Kit - Confirm shipping details.",
        "Remote job offer: Earn $5000/month – apply now.",
        "Tax Refund Notification - Claim $832.45 now.",
        "Microsoft Alert: Virus detected. Call support.",
        "Job Opportunity – Immediate Hire. Start today!",
        "You've Received a Secure Document. Sign in to view.",

        # LEGITIMATE EXAMPLES (label 0)
        "Security alert: Sign-in from new device detected.",
        "Reminder: Your bank statement is now available.",
        "Employee raffle results – see if you won!",
        "Password successfully changed on your request.",
        "Please join our executive meeting at 10 AM.",
        "Invoice for March services attached for review.",
        "Reminder: Submit vendor details via procurement portal.",
        "Project specs shared via Google Docs.",
        "Your tax return has been accepted. Refund pending.",
        "Windows update completed successfully.",
        "As part of quarterly updates, verify vendor list with procurement before changes.",
        "John Smith has shared a document: 'Team Budget 2025' via Google Docs.",
        "Your 2024 tax return is under review. Refunds issued in 21 business days.",
        "Microsoft account login detected in New York. Secure if not recognized.",
        "CDC offering free COVID-19 test kits. Order via official site.",
        "Job opening for Junior Data Analyst. Apply via company careers page."
    ],
    "label": [1]*16 + [0]*16 # 1 = phishing, 0 = legitimate
}

# Load data into DataFrame
df = pd.DataFrame(data)

# Vectorize the text using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

# Train the random forest classifier model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the model and vectorizer
model_path = "model/phishing_model.pkl"
os.makedirs(os.path.dirname(model_path), exist_ok=True)
joblib.dump((model, vectorizer), model_path)

print(f"✅ Phishing detection model trained and saved to '{model_path}'")
