import os
import openai
import json
import re

# Check API Key and Client Selection
if len(os.environ.get("GROQ_API_KEY", "")) > 30:
    from groq import Groq
    model = "mixtral-8x7b-32768"
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
else:
    OPENAI_API_KEY = os.getenv('OPENAI_KEY')
    model = "gpt-4o"
    client = openai.OpenAI(api_key=OPENAI_API_KEY)

def generate_script(niche, goal, business_description="", content_style=""):
    """
    Generate a viral, high-retention YouTube Shorts script.

    - niche: The niche of the video (e.g., fitness, tech, travel).
    - goal: The purpose (e.g., educate, entertain, promote).
    - business_description: Optional description of the business.
    - content_style: Optional style of the content (e.g., storytelling, fact-based, inspirational).
    
    Returns a JSON-formatted script.
    """
    prompt = f"""
    🎯 **Your Role:** You are an expert in viral short-form content creation. Your task is to craft a **high-retention, engaging** YouTube Shorts script based on the user's request.

    🔥 **Goal:** The script must grab attention in the first 3 seconds, maintain engagement, and end with a strong hook or twist.

    📌 **User Inputs:**
    - **Niche:** {niche}
    - **Goal:** {goal}
    - **Business Description:** {business_description if business_description else "AI should decide based on the niche"}
    - **Content Style:** {content_style if content_style else "AI should decide based on the niche and goal"}

    🎬 **Guidelines:**
    1️⃣ **Start with a 3s strong hook** (question, shocking fact, bold statement).
    2️⃣ **Keep sentences short and punchy** (highly conversational, no fluff).
    3️⃣ **Use curiosity loops** to keep viewers engaged.
    4️⃣ **End with a twist or an open-ended thought** that encourages engagement.
    5️⃣ **Do NOT include hashtags, CTA, posting time, or SEO captions** (handled separately).

    📝 **Output Format (JSON Only)**:
    {{ "script": "Your generated script here..." }}
    """

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )

        content = response.choices[0].message.content.strip()

        # Extract JSON if response contains extra text
        json_match = re.search(r'(\{.*?"script":.*?\})', content, re.DOTALL)
        if json_match:
            content = json_match.group(1)

        script_data = json.loads(content)  # Attempt to parse as JSON
        return script_data.get("script", "❌ Script generation failed.")

    except Exception as e:
        print(f"❌ Error: {e}")
        return None