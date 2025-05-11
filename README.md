**🧠 Introduction**

Email Phishing Detector (GUI + CLI) is a Python-based tool that uses machine learning to detect phishing emails based on their textual content. By analyzing patterns commonly found in phishing attempts, this tool can classify emails as either phishing or legitimate. It includes both a command-line interface (CLI) for quick testing and a graphical user interface (GUI) for a user-friendly experience. Built with a Random Forest classifier and TF-IDF vectorization, the system is lightweight, fast, and effective for educational or prototype-level use cases.

**🚨 Problem Statement**
Phishing emails are crafted to trick users into revealing sensitive information such as passwords, bank details, or login credentials. As attackers grow more sophisticated, traditional email filters often fail to detect these threats.
This project aims to build an AI-based email phishing detector that classifies emails as phishing or legitimate based on their content using machine learning. The tool enhances digital safety by providing instant feedback on email authenticity.

**🧰 Features**
- **Text Preprocessing**: Cleans and prepares email content for analysis.
- **Feature Extraction**: Utilizes techniques like TF-IDF to extract meaningful features.
- **Model Training**: Implements ML algorithms such as Logistic Regression and Random Forest.
- **Prediction**: Classifies emails as 'Phishing' or 'Legitimate'.
- **Evaluation**: Assesses model performance using metrics like accuracy and F1-score.

📈 **Workflow Diagram**
Email Content -> TF-IDF Vectorization -> Random Forest Classifier -> Prediction: Phishing / Legitimate

**⚙️ Setup Instructions**
✅ Prerequisites

- Python 3.7 or higher
- Internet connection to install packages
- Tkinter (for GUI; comes pre-installed on Windows/macOS)
    - On Linux: run `sudo apt install python3-tk`📦 Step-by-Step Installation

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/phishing-detector.git
cd phishing-detector/tool/source_code

2. **Install Dependencies** 
pip install -r ../requirements.txt

3. **Train the Model**
python train_model.py
This will save the model to 'model/phishing_model.pkl.'

4.**Run the CLI Tool**
python phishing_detector.py

5. **Run the GUI Tool**
python index.py
```
**Screenshot**
 1. Train model
    ![train model](https://github.com/user-attachments/assets/f14d6fd3-897b-4ab4-a888-0b4b1f99110a)

2. phishing_detector
![phising dtector(1)](https://github.com/user-attachments/assets/9898b6e8-ba6a-4848-8322-9b4101d4f281)
![phising dtector(2)](https://github.com/user-attachments/assets/1affe4e5-466c-49a9-9bf5-476af2fd5428)

3.GUI 
![GUI (1)](https://github.com/user-attachments/assets/5fb20677-0b92-434a-91be-bd41033a33e9)
![GUI(3)](https://github.com/user-attachments/assets/16573076-405d-4328-97a1-98e2aaed21ab)
![GUI(4)](https://github.com/user-attachments/assets/b9397966-d90e-4072-b9d4-beb9c18e0b6d)
![GUI(5)](https://github.com/user-attachments/assets/d1537778-5e2d-4389-8d0a-4b6cf9e20a2f)




