import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
import time

st.set_page_config(page_title="Reloj Digital", page_icon="🕒", layout="centered")

# Estilo oscuro tipo terminal, igual que la versión de tkinter/HTML
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
    }
    .reloj {
        color: #00ffff;
        font-family: 'Courier New', monospace;
        font-size: 80px;
        font-weight: bold;
        text-align: center;
        margin-top: 40vh;
        transform: translateY(-50%);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

marcador = st.empty()

while True:
    hora_actual = datetime.now(ZoneInfo("America/Merida")).strftime("%H:%M:%S")
    marcador.markdown(f"<div class='reloj'>{hora_actual}</div>", unsafe_allow_html=True)
    time.sleep(1)
