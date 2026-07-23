import gradio as gr

# 1. SIMPLE AUTHENTICATION FUNCTION
def check_login(username, password):
    # Set your dashboard Username and Password here
    if username == "admin" and password == "369prapanjam":
        return True
    return False

# 2. MAIN DASHBOARD UI
def build_dashboard():
    with gr.Blocks(title="PRAPANJAM369 Studio", theme=gr.themes.Soft()) as studio:
        gr.Markdown(
            """
            # 🌌 PRAPANJAM369 - Universal AI Movie Studio
            *Your All-in-One Dashboard for Free Image, Video, Voiceover, Lip-Sync & Sound Generation.*
            """
        )

        with gr.Tabs():
            # --- TAB 1: FREE IMAGE MODELS ---
            with gr.Tab("🎨 1. Image Models"):
                gr.Markdown("### Free High-Quality Image Generators")
                with gr.Row():
                    gr.HTML(
                        '<iframe src="https://flux-1-schnell.hf.space" width="100%" height="600" style="border:none; border-radius:10px;"></iframe>'
                    )

            # --- TAB 2: TEXT/IMAGE TO ANIMATION ---
            with gr.Tab("🎬 2. Video & Animation"):
                gr.Markdown("### Free Image-to-Video & Text-to-Video Models")
                with gr.Row():
                    gr.HTML(
                        '<iframe src="https://klingai.com" width="100%" height="600" style="border:none; border-radius:10px;"></iframe>'
                    )

            # --- TAB 3: VOICEOVER & TTS ---
            with gr.Tab("🎙️ 3. Voiceover (Tamil & English)"):
                gr.Markdown("### Bilingual Speech Synthesis")
                text_input = gr.Textbox(
                    label="Script Input",
                    placeholder="Enter script in Tamil or English...",
                )
                voice_select = gr.Dropdown(
                    choices=[
                        "ta-IN-ValluvarNeural (Tamil Male)",
                        "ta-IN-PallaviNeural (Tamil Female)",
                        "en-IN-PrabhatNeural (English Male)",
                    ],
                    label="Voice Model",
                    value="ta-IN-ValluvarNeural (Tamil Male)",
                )
                generate_voice_btn = gr.Button("Generate Voiceover", variant="primary")
                audio_output = gr.Audio(label="Generated Audio")

            # --- TAB 4: LIP-SYNC & SOUND ---
            with gr.Tab("💋 4. Lip-Sync & SFX"):
                gr.Markdown("### Synchronize Character Mouth Movements & Audio")
                with gr.Row():
                    gr.HTML(
                        '<iframe src="https://liveportrait.hf.space" width="100%" height="600" style="border:none; border-radius:10px;"></iframe>'
                    )

            # --- TAB 5: VIDEO & SOUND EDITORS ---
            with gr.Tab("✂️ 5. Combine & Edit"):
                gr.Markdown("### Online Timeline & Audio Assembly Tools")
                gr.Markdown(
                    """
                * **CapCut Web:** [Open CapCut Web Editor](https://www.capcut.com/editor)
                * **Clipchamp:** [Open Microsoft Clipchamp](https://app.clipchamp.com/)
                * **Audacity Online:** [Open Audio Editor](https://wavacity.com/)
                """
                )

    return studio


# 3. LOGIN INTERFACE & APP LAUNCHER
with gr.Blocks(title="PRAPANJAM369 - Login") as app:
    # State variable for authentication
    is_authenticated = gr.State(value=False)

    # LOGIN SCREEN
    with gr.Column(visible=True) as login_box:
        gr.Markdown("# 🔒 PRAPANJAM369 - Studio Login")
        user_input = gr.Textbox(label="Username", placeholder="Enter username")
        pass_input = gr.Textbox(
            label="Password", type="password", placeholder="Enter password"
        )
        login_btn = gr.Button("Login to Dashboard", variant="primary")
        login_error = gr.Markdown("", visible=False)

    # MAIN DASHBOARD AREA (Hidden by default)
    with gr.Column(visible=False) as dashboard_box:
        studio_ui = build_dashboard()

    # LOGIN BUTTON ACTION
    def handle_login(u, p):
        if check_login(u, p):
            return (
                gr.update(visible=False),
                gr.update(visible=True),
                "",
                gr.update(visible=False),
            )
        else:
            return (
                gr.update(visible=True),
                gr.update(visible=False),
                "❌ Incorrect Username or Password",
                gr.update(visible=True),
            )

    login_btn.click(
        fn=handle_login,
        inputs=[user_input, pass_input],
        outputs=[login_box, dashboard_box, login_error, login_error],
    )

if __name__ == "__main__":
    app.launch()