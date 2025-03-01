import os
import json
import re
import argparse
import subprocess
import openai


# Check if using Groq or OpenAI
if len(os.environ.get("GROQ_API_KEY", "")) > 30:
    from groq import Groq
    model = "mixtral-8x7b-32768"
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
else:
    OPENAI_API_KEY = os.getenv('OPENAI_KEY')
    model = "gpt-4o"
    client = openai(api_key=OPENAI_API_KEY)

def generate_marketing_content(niche, goal,business_description="", content_style=""):
    prompt = f"""
    You are an expert in digital marketing and social media growth. Based on the given niche, target goal, and content style, generate:
    1. The top 10 trending hashtags for the niche.
    2. The best time to post for maximum engagement.
    3. A highly effective call-to-action (CTA).
    4. An SEO-optimized caption.

    If no content style is provided, determine the best content style based on the niche.

    **IMPORTANT:** 
    - Return ONLY a JSON object, without any additional text or explanation.
    - Ensure the JSON format is correct.

    JSON Format:
    ```json
    {{"hashtags": "#hashtag1 #hashtag2 #hashtag3 ...",
      "posting_time": "Best time to post: ...",
      "cta": "Your CTA message here.",
      "seo_caption": "Your SEO-optimized caption here."
    }}
    ```

    Now generate for:
    Niche: {niche}
    Goal: {goal}
    Business Description: {business_description}
    Content Style: {content_style}
    """

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": prompt}]
    )

    content = response.choices[0].message.content

    # Try extracting JSON using regex (handles non-JSON responses)
    match = re.search(r"\{.*\}", content, re.DOTALL)
    if match:
        json_str = match.group(0)
        try:
            return json.loads(json_str)  # Return parsed JSON response
        except json.JSONDecodeError:
            print("❌ JSON parsing failed")
            print("Response received:\n", content)
            return None
    else:
        print("❌ No valid JSON found in response")
        print("Response received:\n", content)
        return None
