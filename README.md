
🧠 Reddit User Persona Generator

This project takes a Reddit user's profile URL, scrapes their recent comments and posts, and uses Google's Gemini LLM (via API) to generate a detailed User Persona — including personality traits, motivations, frustrations, and behavior insights.

📌 Features
- 🔗 Input any public Reddit profile URL
- 🔍 Automatically scrapes the user's recent comments and posts
- 🤖 Sends data to Gemini 2.0 Flash API
- 📄 Generates a UX-style persona with citations from real posts/comments
- 💾 Saves the output as a .txt file

🚀 How to Use

1. Clone this Repo

   git clone https://github.com/your-username/reddit-persona-generator.git
   cd reddit-persona-generator

2. Install Dependencies

   Make sure Python 3.7+ is installed, then:

   pip install -r requirements.txt

3. Add Your Gemini API Key

   Edit the persona.py file and replace:

   api_key = "YOUR_GEMINI_API_KEY"

   With your actual Gemini API key from Google AI Studio.

4. Run the Script

   python persona.py

   It will:
   - Prompt you for a Reddit profile URL (e.g. https://www.reddit.com/user/Hungry-Move-6603/)
   - Scrape recent data
   - Call Gemini
   - Save the output to USERNAME_persona.txt

📂 Example Output

Filename: kojied_persona.txt

User Persona: kojied

Age: Likely 25–35
Occupation: Gaming enthusiast or hobbyist
Motivations: Enjoys building strategy in simulation games
Frustrations: Annoyed by bugs or disconnected systems
Cited from: "trading posts randomly disconnect..."
...

📦 Files Included

| File            | Description                |
|-----------------|----------------------------|
| persona.py      | Main script                |
| requirements.txt| Python dependencies        |
| README.txt      | This file (documentation)  |

🛠️ Dependencies

- requests – For web requests and Gemini API
- beautifulsoup4 – Included for any optional HTML parsing

📌 Notes

- This tool works with public Reddit users only.
- Gemini API access is required: https://aistudio.google.com/app/apikey

📧 Contact

Made by Anurag Lawaniya
Feel free to contribute or suggest improvements!
