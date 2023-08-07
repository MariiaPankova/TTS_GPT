from gtts import gTTS
from io import BytesIO
from base64 import b64encode


def tts(text: str, lang: str = "en"):
    return gTTS(text=text, lang=lang, slow=False)


def tts_to_bytesio(tts_object: object) -> bytes:
    bytes_object = BytesIO()
    tts_object.write_to_fp(bytes_object)
    bytes_object.seek(0)
    return bytes_object.getvalue()


def html_audio_autoplay(mesage: str) -> object:
    voice_message = tts(mesage)
    bytes = tts_to_bytesio(voice_message)
    b64 = b64encode(bytes).decode()
    html_msg = mesage.replace("\n", "</br>")
    html = f"""
    <audio style="height: 25px;" controls autoplay>
    <source src="data:audio/wav;base64,{b64}" type="audio/wav">
    </audio>
    </br>
    {html_msg}
    """

    return html
