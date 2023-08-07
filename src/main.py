import gradio as gr
from chatbot import chatbot
from text_to_speach import html_audio_autoplay


def main(msg, history):
    bot_response = chatbot(msg)
    html = html_audio_autoplay(bot_response)
    return html


gr.ChatInterface(fn=main).launch(server_name="0.0.0.0")
