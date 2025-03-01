import gradio as gr
import os
from capgen import generate_marketing_content
from utility.script.script_generator import generate_script
from utility.audio.audio_generator import generate_audio
from utility.captions.timed_captions_generator import generate_timed_captions
from utility.video.video_search_query_generator import getVideoSearchQueriesTimed, merge_empty_intervals
from utility.video.background_video_generator import generate_video_url
from utility.render.render_engine import get_output_media
import asyncio

# Main function to generate video and marketing content
def generate_content(niche, goal, business_description="", content_style=""):
    try:
        print("Generating marketing content...")
        # Generate marketing content
        capgen_data = generate_marketing_content(niche, goal, content_style)
        if not capgen_data:
            print("Failed to generate marketing content.")
            return "❌ Failed to generate marketing content", "", "", "", ""

        hashtags = capgen_data["hashtags"]
        posting_time = capgen_data["posting_time"]
        cta = capgen_data["cta"]
        seo_caption = capgen_data["seo_caption"]

        print("Generating script...")
        # Generate script
        script = generate_script(niche, goal, business_description, content_style)

        print("Generating audio...")
        # Generate audio
        audio_file = "audio_tts.wav"
        asyncio.run(generate_audio(script, audio_file))

        print("Generating timed captions...")
        # Generate timed captions
        timed_captions = generate_timed_captions(audio_file)

        print("Generating video search queries...")
        # Generate video search queries
        search_terms = getVideoSearchQueriesTimed(script, timed_captions)

        print("Generating video URLs...")
        # Generate video URLs
        background_video_urls = generate_video_url(search_terms, "pexel") if search_terms else None
        background_video_urls = merge_empty_intervals(background_video_urls)

        print("Rendering video...")
        # Render video
        if background_video_urls:
            video = get_output_media(audio_file, timed_captions, background_video_urls, "pexel", orientation="portrait")
            print("Video generated.")
            return video, hashtags, seo_caption, posting_time, cta
        else:
            print("No video generated.")
            return "No video generated", hashtags, seo_caption, posting_time, cta

    except Exception as e:
        print(f"Error occurred: {e}")
        return f"❌ Error occurred: {e}", "", "", "", ""

# Gradio UI for video output only
def generate_video_only(niche, goal, content_style=""):
    video, _, _, _, _ = generate_content(niche, goal, content_style=content_style)
    return video


css = """
body {
    background: #0a0a0a;
    font-family: 'Poppins', sans-serif;
    margin: 0;
    padding: 0;
    color: #fff;
}

/* Container with glassmorphism effect */
.gradio-container {
    background: rgba(20, 20, 20, 0.7);
    backdrop-filter: blur(15px);
    border-radius: 16px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    padding: 30px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.6);
    max-width: 900px;
    margin: 40px auto;
}

/* Headings */
h1, h2 {
    font-weight: 600;
    text-align: center;
    margin-bottom: 15px;
    color: #fff;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Inputs & Textareas */
input, textarea {
    background: rgba(30, 30, 30, 0.9);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 12px;
    padding: 12px;
    font-size: 14px;
    color: #fff;
    transition: all 0.3s ease;
    box-shadow: 0 2px 10px rgba(0, 255, 255, 0.2);
}

input:focus, textarea:focus {
    border-color: #00ffff;
    outline: none;
    box-shadow: 0 0 10px rgba(0, 255, 255, 0.6);
}

textarea::placeholder, input::placeholder {
    color: rgba(200, 200, 200, 0.5);
}

/* Buttons */
button {
    background: linear-gradient(135deg, #00ffff, #0077ff);
    color: #111;
    border: none;
    padding: 12px 24px;
    font-weight: bold;
    font-size: 14px;
    border-radius: 10px;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 0 15px rgba(0, 255, 255, 0.5);
    text-transform: uppercase;
}

button:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.8);
}

/* Video box with 9:16 perfect fit */
video {
    display: block;
    width: 100%;
    max-width: 360px;   /* Vertical video size */
    height: 640px;      /* 9:16 aspect ratio */
    margin: 15px auto;
    object-fit: cover;
    border: 1px solid rgba(0, 255, 255, 0.3);
    border-radius: 16px;
    box-shadow: 0 4px 20px rgba(0, 255, 255, 0.2);
}

/* Responsive tweaks */
@media (max-width: 768px) {
    .gradio-container {
        padding: 15px;
    }
}
"""

iface = gr.Interface(
    fn=generate_content,
    inputs=[
        gr.Textbox(label="Niche", placeholder="Eg: Fitness, Tech, Fashion"),
        gr.Textbox(label="Marketing Goal", placeholder="Eg: Boost followers, Increase sales"),
        gr.Textbox(label="Business Description (Optional)", placeholder="Briefly describe your brand"),
        gr.Textbox(label="Content Style (Optional)", placeholder="Eg: Trendy, Informative")
    ],
    outputs=[
        gr.Video(label="Generated Vertical Video (9:16)"),
        gr.Textbox(label="Hashtags"),
        gr.Textbox(label="SEO Caption"),
        gr.Textbox(label="Best Posting Time"),
        gr.Textbox(label="Call to Action")
    ],
    title="✨ TrendMate AI Marketing Generator",
    description="🚀 Enter your niche & goal to generate a complete Instagram marketing strategy with captions, hashtags, and a vertical video!",
    css=css
)

iface.launch(share='True')