**🧰 Tool Directory — AI-Powered Phishing Email Detection**

This folder contains the **core implementation** of the phishing detection system, including training, prediction via CLI, and a graphical user interface (GUI).

**🚨 Problem Statement**

Phishing attacks exploit users through deceptive emails that appear legitimate. These attacks are difficult to detect with traditional rule-based filters. This tool solves the problem by using machine learning to analyze and classify email text as either **phishing** or **legitimate**, helping users avoid threats.

**⚙️ Setup Instructions**

**1. Install Required Packages**
Navigate into the `tool/` directory and run:

```bash
pip install -r requirements.txt

Or manually install:
pip install pandas scikit-learn joblib

Note: For GUI support, Linux users may also need:
   sudo apt install python3-tk
```
**2. Train the Model**
Go into source_code/ and run:
```
python train_model.py
```
This trains a Random Forest model and saves it to model/phishing_model.pkl.

**3. Predict Using CLI**
```
python phishing_detector.py
```
- Choose between typing the email or loading from a .txt file.
- Get instant prediction as Phishing or Legitimate.

**4.Predict Using GUI**
```
python index.py
```

**Features:**
- Text input box for emails
- File upload support
- Real-time prediction with confidence score
- Save results to .txt

**🔍 System Flow**


  ![system flow](https://github.com/user-attachments/assets/70d11087-af2d-4a9b-85bd-920f127b7485)


  

