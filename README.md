# 🏋️ AI Fitness Planner

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)
![OpenAI SDK](https://img.shields.io/badge/OpenAI-SDK-412991)
![OpenRouter](https://img.shields.io/badge/OpenRouter-AI-5A67D8)


## 🚀 Live Demo

🔗 https://aifitnessplannerproject-6vetngqrxjkgm8pxfut9wm.streamlit.app/

## 1. Project Title
AI Fitness Planner

## 2. Project Overview
This project is a Streamlit-based web application that generates personalized workout and diet guidance using AI. It collects user details such as age, weight, height, goal, diet preference, budget, and activity level, calculates BMI, and uses an OpenRouter-backed language model to create a plan. The app also allows the generated plan to be downloaded as a PDF.

## 3. Features
- Personalized weekly workout recommendations
- Daily diet suggestions based on user preferences
- BMI calculation and health status summary
- Goal-based plan generation for weight loss, muscle gain, or staying fit
- Budget-aware dietary recommendations
- PDF export for the generated plan
- Simple, interactive Streamlit interface

## 4. Tech Stack
- Python 3.10+
- Streamlit for the user interface
- OpenAI Python SDK for API communication
- OpenRouter API as the model provider
- FPDF for PDF export
- Requests for HTTP-based integrations
- Matplotlib (included in requirements; currently not used directly in the current app logic)

## 5. Project Architecture
The application follows a lightweight front-end + AI integration architecture:
1. Streamlit UI renders the input form and action buttons.
2. User details are collected from the sidebar.
3. BMI is calculated locally in the app.
4. A prompt is generated using the user profile.
5. The prompt is sent to the OpenRouter-compatible model endpoint via the OpenAI client.
6. The AI response is displayed in the app and can be exported to a PDF.

## 6. Installation Guide
1. Clone the repository.
2. Create a Python virtual environment.
3. Install dependencies from requirements.txt.
4. Configure the OpenRouter API key in Streamlit secrets.
5. Run the app with Streamlit.

## 7. Virtual Environment Setup
Use the following commands from the project root:

```bash
python -m venv venv
```

On Windows:

```powershell
.\venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

## 8. Dependency Installation
Install the dependencies listed in requirements.txt:

```bash
pip install -r requirements.txt
```

### Dependency breakdown
- streamlit: Builds the interactive web application interface.
- requests: Supports HTTP requests for external service communication.
- matplotlib: Available for charts, visual aids, and future analytics features.
- fpdf: Creates the downloadable PDF version of the generated AI plan.
- openai: Provides the Python client used to access the OpenRouter model endpoint.

## 9. Environment Variables / Secrets Configuration
This project uses Streamlit secrets rather than a separate .env file.

Create a file at:

```text
.streamlit/secrets.toml
```

Add your API key as follows:

```toml
OPENROUTER_API_KEY = "your_openrouter_api_key_here"
```

Important notes:
- The current code reads the key from `st.secrets["OPENROUTER_API_KEY"]`.
- The repository already ignores `.streamlit/secrets.toml` in `.gitignore` for security.
- Do not commit real API keys to version control.

## 10. Running the Application
From the project root, run:

```bash
streamlit run app.py
```

The app will open in your browser with the AI Fitness Planner interface.

## 11. Screenshots Section
> Placeholder for future screenshots.

- Main dashboard with user inputs
- BMI result card and summary
- AI-generated plan output section
- Exported PDF download flow

## 12. Folder Structure
```text
AI_Fitness_Planner_Project/
├── app.py                   # Main Streamlit application
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── .gitignore               # Git ignore rules
├── .streamlit/
│   └── secrets.toml         # API secrets (local only)
└── venv/                    # Local virtual environment
```

## 13. How the AI Workflow Works
1. The user enters personal fitness and dietary preferences in the sidebar.
2. The app calculates BMI and determines a health status label.
3. A detailed prompt is assembled from the selected values.
4. The prompt is sent to the OpenRouter-hosted model `meta-llama/llama-3-8b-instruct` through the OpenAI SDK.
5. The AI-generated plan is displayed in the Streamlit interface.
6. If the user chooses, the same content is exported into a PDF file for download.

## 14. API Integration Details
The application currently uses one external integration:
- OpenRouter API via the OpenAI-compatible endpoint
- Base URL: `https://openrouter.ai/api/v1`
- Model used: `meta-llama/llama-3-8b-instruct`

The code uses:

```python
client = OpenAI(
    api_key=st.secrets["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api/v1"
)
```

No other custom backend API routes are defined in the current repository.

## 15. Future Enhancements
- Add user authentication and saved profiles
- Support weekly meal prep and calorie tracking
- Visual charts for BMI and fitness trends
- Export to DOCX, CSV, or JSON
- Add multilingual support
- Improve prompt engineering for more accurate fitness advice

## 16. Troubleshooting
- If you see an API error, confirm that your OpenRouter API key is valid and that the secret file is configured correctly.
- If Streamlit cannot start, make sure your virtual environment is activated and dependencies are installed.
- If the PDF download does not work, generate an AI plan first; the PDF option depends on `st.session_state["plan"]`.
- If you get module import errors, reinstall requirements with `pip install -r requirements.txt`.

## 17. Contributing Guidelines
Contributions are welcome. Please follow these guidelines:
1. Fork the repository.
2. Create a feature branch.
3. Keep secrets out of the codebase.
4. Test the app locally before submitting a pull request.
5. Document significant changes in the README or code comments.

## 18. License
This repository does not currently include a license file. If you plan to share or publish the project publicly, add an appropriate open-source license before distribution.

## 19. Author Section
Developed by: Apeksha Vishwasrao
