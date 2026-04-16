AI Study Assistant

An AI-powered web application that helps students understand topics faster using intelligent workflows. The system can explain concepts, summarize content, and generate quiz questions for better learning and revision.

✨ Features:
- 📘 Explain Mode – Converts complex topics into simple explanations  
- 📝 Summarize Mode – Generates concise bullet-point summaries  
- ❓ Quiz Generator – Creates practice questions with answers  
- 🌙 Light / Dark Mode UI  
- ⚡ Demo Fallback – Works even when API quota is exceeded  

🧠 How It Works:
1. User enters a topic or question  
2. Selects a mode (Explain / Summarize / Quiz)  
3. Backend processes input using LLM-based prompts  
4. Returns structured response to the UI  

If the API is unavailable or quota is exceeded, the app switches to demo mode to maintain functionality.

🛠️ Tech Stack:
- Python  
- Flask  
- HTML, CSS, JavaScript  
- Gemini API (LLM-based workflows)

📂 Project Structure:

 ai-study-assistant/

 │

 ├── app.py

 ├── requirements.txt

 ├── README.md

 ├── .gitignore

 ├── templates/
 
 │ └── index.html

 └── static/

 ├── style.css

 └── script.js


⚙️ Setup Instructions:

 1. Clone the repository

      git clone https://github.com/BeastVivan/ai-study-assistant.git

      cd ai-study-assistant
    
 3. Install dependencies

      pip install -r requirements.txt

 5. Set API Key

      Windows (PowerShell) - $env:GEMINI_API_KEY="your_api_key_here"

      Windows (CMD) - set GEMINI_API_KEY=your_api_key_here

      Mac/Linux - export GEMINI_API_KEY="your_api_key_here"
    
  7. Run the application

      python app.py


⚠️ Notes:

 The app uses Gemini API for content generation
 
 Free-tier API limits may cause temporary quota errors
 
 In such cases, the system automatically switches to demo mode
