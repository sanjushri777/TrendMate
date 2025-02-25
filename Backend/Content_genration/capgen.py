import os
from openai import OpenAI
import json
import re
import datetime
import ast
import subprocess

if len(os.environ.get("GROQ_API_KEY", "")) > 30:
    from groq import Groq
    model = "mixtral-8x7b-32768"
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
else:
    OPENAI_API_KEY = os.getenv('OPENAI_KEY')
    model = "gpt-4o"
    client = OpenAI(api_key=OPENAI_API_KEY)

def get_best_posting_time(niche):
    try:
        query = f"best time to post on social media for {niche} today"
        result = subprocess.run(
            ["python", "-c", f"import web; print(web.search('{query}'))"],
            capture_output=True, text=True
        ).stdout.strip()
        return result if result and "best time" in result.lower() else "Default best posting time: 6-9 PM"
    except Exception:
        return "Default best posting time: 6-9 PM"

def generate_instagram_strategy(niche, goal, content_style=""):
    best_time = get_best_posting_time(niche)

    prompt = f"""
    Act as an expert Instagram marketing strategist with a deep understanding of Instagram's current algorithm and engagement trends. Your task is to generate a highly effective Instagram content strategy for a given niche that will help posts go viral within one month.

    For the specified niche, provide the following:

    1. Top 10 Trending Hashtags:
    Identify the most trending and relevant hashtags based on current Instagram engagement.
    Ensure a mix of high, medium, and low-competition hashtags to maximize reach.
    Example: For the fitness niche, you might suggest: #FitLife #WorkoutMotivation #HealthyVibes #FitnessJourney #NoExcuses #FitAndStrong #DailyWorkout #MindsetMatters #StayActive

    2. Best Posting Times:
    Suggest the optimal posting times based on Instagram's current engagement data.
    Provide the best time slots in the user's time zone.
    Example: For the fashion niche, suggest: "Monday to Friday: 11 AM, 3 PM, and 7 PM | Saturday and Sunday: 10 AM and 6 PM."

    3. SEO-Optimized Captions (At least 3-4 lines):
    Create an engaging caption tailored to the niche.
    The caption should naturally incorporate SEO keywords, hook the audience, provide value, and encourage interaction.
    Example (Entrepreneur niche):
    "Success is not about luck. It is about consistency, strategy, and smart decisions. Every small step today builds the foundation for your future. What is one goal you are working toward this week?"

    4. Strong Call-to-Action (CTA):
    Provide a compelling CTA that encourages likes, comments, saves, and shares.
    Example:
    "Comment your biggest goal below and save this post as a reminder to stay focused. Let’s build success together."

    Ensure that the recommendations align with Instagram’s current algorithm and are designed to help posts achieve viral growth within one month.

    Here’s the niche to focus on:
    Niche: {niche}
    Goal: {goal}
    Content Style: {content_style or "Auto-detected"}
    """

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": prompt}]
    )

    content = response.choices[0].message.content

    try:
        content = content.encode().decode('unicode_escape')  
        return ast.literal_eval(content)
    except Exception:
        return None

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate Instagram marketing strategy.")
    parser.add_argument("niche", type=str, help="The niche for content generation")
    parser.add_argument("goal", type=str, help="The target goal (e.g., engagement, conversions)")
    parser.add_argument("--content_style", type=str, help="The content style (optional)", default="")

    args = parser.parse_args()
    result = generate_instagram_strategy(args.niche, args.goal, args.content_style)

    if result:
        print(json.dumps(result, indent=4, ensure_ascii=False))
    else:
        print("Failed to generate Instagram marketing strategy.")
