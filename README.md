# TrendMate

## Project Overview
TrendMate is an AI-powered platform designed for entrepreneurs to streamline their marketing efforts with minimal effort. Users simply input their niche and content script, and the platform generates engaging marketing videos using AI. The system also provides trending hashtags, captions, call-to-actions (CTA), and optimal posting times to maximize reach and engagement.

## Features
- AI-generated video content using modified open-source models
- Automatic trending hashtag and caption generation
- AI-driven CTA suggestions
- Optimized posting time recommendations
- User-friendly interface for seamless content creation

## Tech Stack
- **Frontend:** Vite, React
- **Backend:** Flask (Integration in Progress)
- **AI Models:** LLaMA, Grok AI, and other open-source tools
- **APIs Used:** Hashtag Grok AI, Open-source AI video generation models
```
## Setup Instructions
# 1. Clone the Repository:
```
git clone https://github.com/sanjushri777/TrendMate.git
```
# 2. Navigate to the Project Directory:
```
cd TrendMate
```

# 3. Install Backend Dependencies:
```
cd Backend/Ai_tasks
pip install -r requirements.txt
```
# 4. Set Up API Keys:
```
 Replace 'your_grok_api_key' and 'your_pixel_api_key' with your actual API keys.

# On Windows Command Prompt:(without quotes)
```
set GROK_API_KEY=your_grok_api_key
set PIXEL_API_KEY=your_pixel_api_key
```
```
# On Windows PowerShell:
$env:GROK_API_KEY="your_grok_api_key"
$env:PIXEL_API_KEY="your_pixel_api_key"
```
```
# On Unix/Linux or macOS:
export GROK_API_KEY=your_grok_api_key
export PIXEL_API_KEY=your_pixel_api_key
```

# 5. Run the Backend Application:
```
 Replace 'your_niche' with your specific niche or content focus.
 

python app.py "your_niche"

```
  

## Project Status
🚧 Backend integration is in progress. The project is not yet completed, and further enhancements are being made.

## Team Members
- **DURGADEVI P**-FRONTEND
- **ASWINI M**-FRONTEND
- **SUBHASHINI B**-BACKEND
- **SANJUSHRI A**-BACKEND

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

