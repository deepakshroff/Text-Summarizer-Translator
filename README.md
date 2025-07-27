# 🌍 Multi-Language Translator

**Multi-Language Translator** is a powerful Streamlit web app that allows users to translate text between multiple languages using **Google Gemini**. It supports automatic language detection, parameter tuning, and real-time translation with a beautiful, intuitive interface.

![Screenshot](Screenshot%202025-07-27%20001550.png)

---

## 🚀 Features

- 🔄 Translate between 10+ major global languages  
- 🌐 Auto-detect source language  
- 🤖 Powered by Google Gemini (`gemini-1.5-flash`)  
- 🎛️ Adjustable temperature for creativity control  
- 📋 Live translation history  
- 💡 Clean and responsive Streamlit interface

---

## 🧪 Tech Stack

### 🖥️ Frontend
- Streamlit (UI Framework)
- Responsive column layout
- Sidebar with live parameter inputs

### 🧠 Backend
- Google Gemini API (`langchain_google_genai`)
- LangChain Prompt Template for custom translation instructions
- Python

### 🛠 Development Tools
- VS Code
- Browser: Chrome / Edge
- Localhost / Streamlit sharing

---

## 📁 Project Structure
- Multi-Language-Translator/
- ├── app.py # Main Streamlit application
- ├── Screenshot 2025-07-27 001550.png # App screenshot for README
- └── README.md # Project documentation

---

## 💡 How to Use

### 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Multi-Language-Translator.git
   cd Multi-Language-Translator

---

## Provide Google Gemini API Key
- Add your Google Gemini API key in the left sidebar input field when the app launches.

--- 

### 🌐 Supported Languages
- English 🇬🇧
- Hindi 🇮🇳
- Spanish 🇪🇸
- French 🇫🇷
- German 🇩🇪
- Italian 🇮🇹
- Portuguese 🇵🇹
- Russian 🇷🇺
- Chinese 🇨🇳
- Japanese 🇯🇵

## 📌 Translation Options
- 🔍 Source Language: Auto Detect or manual selection
- 🎯 Target Language: Choose any available language
- 🌡️ Temperature: Controls randomness (0 = focused, 1 = creative)
- 🧠 Model: Currently supports gemini-1.5-flash


## 🧠 How It Works
- You input text and select source/target languages
- Gemini is prompted using LangChain with translation instructions
- The translated text is shown with an option to view past translations

---

## 🙌 Acknowledgements
- 🤖 Google Gemini for powerful translation capabilities
- 🔗 LangChain for prompt chaining
- 💬 Streamlit for the intuitive web interface
- 🙏 Mr. Lokesh Sir for guidance and mentorship

---