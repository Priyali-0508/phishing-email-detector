import joblib
import os

def load_model():
    return joblib.load("model/phishing_model.pkl")

def predict_email(text, model, vectorizer):
    features = vectorizer.transform([text])
    prediction = model.predict(features)[0]
    return "🔴 Phishing" if prediction == 1 else "🟢 Legitimate"

def read_multiline_input():
    print("\n✍️ Enter the email content (end with a blank line):")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    return " ".join(lines)

def main():
    print("\n📧 AI-Powered Phishing Email Detector\n")
    choice = input("Choose input mode:\n1. Type email content\n2. Load from .txt file\n> ")

    if choice == "1":
        content = read_multiline_input()
    elif choice == "2":
        filename = input("Enter path to .txt file (e.g., sample_emails/sample1.txt): ")
        if not os.path.isfile(filename):
            print("❌ File not found.")
            return
        with open(filename, 'r') as f:
            content = f.read()
    else:
        print("❌ Invalid choice.")
        return

    model, vectorizer = load_model()
    result = predict_email(content, model, vectorizer)
    print(f"\n🧠 Prediction: {result}")

if __name__ == "__main__":
    main()
