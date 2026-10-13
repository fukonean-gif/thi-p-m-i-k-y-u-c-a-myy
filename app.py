import base64
import streamlit as st

st.set_page_config(page_title="A Little Dream — Graduation", page_icon="☁️", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');
.stApp { background: radial-gradient(circle at 12% 10%, #fff 0 3%, transparent 3.5%), radial-gradient(circle at 88% 18%, #fff9 0 5%, transparent 5.5%), linear-gradient(155deg,#eaf8ff,#c9e9ff 52%,#effaff); color:#31506d; font-family:'DM Sans',sans-serif; }
[data-testid="stSidebar"] { background:rgba(255,255,255,.86); }
.block-container { max-width:1120px; padding-top:2rem; padding-bottom:4rem; }
h1,h2,h3 { font-family:'Space Grotesk',sans-serif !important; color:#31506d !important; }
.dream-card { background:rgba(255,255,255,.76); border:1px solid white; border-radius:26px; padding:26px; box-shadow:0 12px 36px #5091be20; }
.kicker { letter-spacing:.22em; text-transform:uppercase; font-size:.72rem; font-weight:700; color:#6a9ec4; }
.hero-title { font-family:'Space Grotesk',sans-serif; font-size:clamp(2.7rem,7vw,5.7rem); line-height:.98; letter-spacing:-.06em; color:#31506d; }
.sparkle { color:#91bfe2; letter-spacing:.5em; }
.polaroid { background:white; padding:12px 12px 30px; border-radius:5px; box-shadow:0 12px 26px #3f6f972e; transform:rotate(2deg); }
.small-note { color:#6688a6; font-size:.92rem; }
div.stButton>button { border-radius:999px; border:1px solid #9acdf0; background:#fafdff; color:#31506d; font-weight:700; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## ☁️ Your little dream")
    st.caption("Điền thông tin để cá nhân hoá thiệp.")
    name = st.text_input("Tên của m", "Your Name")
    class_name = st.text_input("Lớp", "Class of 2026")
    school = st.text_input("Trường", "Your School")
    date_text = st.text_input("Ngày", "A day to remember")
    time_text = st.text_input("Thời gian", "At sunset")
    location = st.text_input("Địa điểm", "Somewhere special")
    message = st.text_area("Lời nhắn", "One chapter ends, another begins. Thank you for being part of my little story.", height=120)
    sign_off = st.text_input("Ký tên", "with love,")
    st.markdown("---")
    photo = st.file_uploader("Thêm ảnh (JPG, PNG, WEBP)", type=["jpg","jpeg","png","webp"])
    music = st.file_uploader("Thêm nhạc (MP3, WAV, OGG)", type=["mp3","wav","ogg"])
    st.caption("M có thể đổi thông tin và chọn file ngay tại đây.")

st.markdown('<div class="kicker">✦ a tiny celebration ✦</div>', unsafe_allow_html=True)
st.markdown(f'<div class="hero-title">{name.strip() or "Your Name"}<br><span style="color:#78b7e7;">in the clouds</span></div>', unsafe_allow_html=True)
st.markdown('<div class="sparkle">✧ ☆ ✧ ☆ ✧</div>', unsafe_allow_html=True)
st.write("")
left, right = st.columns([1.08, .92], gap="large")

with left:
    st.markdown('<div class="dream-card">', unsafe_allow_html=True)
    st.markdown(f"### ☁️ {class_name}")
    st.markdown(f"**{school}**")
    st.markdown("---")
    st.markdown(f"**{date_text}** · {time_text}")
    st.markdown(f"📍 {location}")
    st.write("")
    st.markdown(f"> {message}")
    st.write("")
    st.markdown(f"*{sign_off}*")
    st.markdown(f"**{name.strip() or 'Your Name'}** ✧")
    st.markdown("</div>", unsafe_allow_html=True)

with right:
    if photo is not None:
        st.markdown('<div class="polaroid">', unsafe_allow_html=True)
        st.image(photo, use_container_width=True)
        st.caption("a little memory to keep ✧")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="dream-card" style="text-align:center; min-height:300px;">
          <div style="font-size:4.3rem;">☁️ ✦ ☁️</div>
          <h3>your memory goes here</h3>
          <p class="small-note">Chọn ảnh ở thanh bên trái để hiện ảnh polaroid của m.</p>
        </div>
        """, unsafe_allow_html=True)

st.write("")
if music is not None:
    st.markdown('<div class="dream-card">', unsafe_allow_html=True)
    st.markdown("### ♫ A song for this memory")
    st.audio(music)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.info("♫ Chưa có nhạc — m tải file MP3/WAV/OGG lên ở thanh bên trái nhé.")

st.markdown('<div style="text-align:center;color:#7099ba;padding:18px;">made of clouds, little stars, and memories ✧</div>', unsafe_allow_html=True)
