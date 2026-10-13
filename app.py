import os
import streamlit as st

# Cấu hình trang web
st.set_page_config(page_title="A Little Dream - Y2K Edition", page_icon="🪩", layout="wide")

# CSS tích hợp Y2K, Ép Light Mode & Tăng font chữ to rõ
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Pixelify+Sans:wght@500;700&family=Syne:wght@700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap');

/* Ép màu chữ chính toàn trang sáng & rõ */
html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #0f172a !important;
}

/* Background chuyển màu Dreamcore tươi sáng */
.stApp {
    background: linear-gradient(-45deg, #e0f2fe, #bae6fd, #f0f9ff, #7dd3fc) !important;
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Sidebar nổi bật */
[data-testid="stSidebar"] {
    background: rgba(255, 255, 255, 0.95) !important;
    border-right: 2px dashed #38bdf8;
    backdrop-filter: blur(10px);
}

/* Thẻ thông tin Dream Card */
.dream-card {
    background: rgba(255, 255, 255, 0.92) !important;
    border: 2.5px solid #ffffff;
    border-radius: 24px;
    padding: 32px;
    box-shadow: 0 12px 35px rgba(56, 189, 248, 0.25);
    margin-bottom: 20px;
    color: #0f172a !important;
    font-size: 1.15rem;
    line-height: 1.7;
}

.dream-card h3 {
    font-size: 1.8rem !important;
    color: #0369a1 !important;
    font-weight: 800 !important;
}

.dream-card strong {
    color: #0284c7 !important;
}

/* Tiêu đề chính Y2K Chrome */
.hero-title {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: clamp(3.2rem, 7vw, 5.2rem);
    background: linear-gradient(180deg, #ffffff 10%, #38bdf8 50%, #0284c7 90%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(3px 4px 0px rgba(3, 105, 161, 0.35));
    line-height: 1.1;
    text-transform: uppercase;
    animation: floatTitle 3s ease-in-out infinite;
}

@keyframes floatTitle {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-6px); }
}

.sparkle-text {
    font-family: 'Pixelify Sans', cursive;
    color: #0369a1 !important;
    font-size: 1.4rem !important;
    font-weight: 700;
}

/* Màn hình chờ mở thiệp Y2K */
.y2k-cover {
    text-align: center;
    padding: 50px 24px;
    background: rgba(255, 255, 255, 0.95);
    border: 3px solid #38bdf8;
    border-radius: 28px;
    box-shadow: 0 0 35px rgba(2, 132, 199, 0.3);
    max-width: 650px;
    margin: 40px auto;
}

.pixel-title {
    font-family: 'Pixelify Sans', cursive;
    font-size: 3rem;
    background: linear-gradient(180deg, #ffffff 0%, #38bdf8 50%, #0284c7 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 15px;
}

.polaroid {
    background: white;
    padding: 16px 16px 36px;
    border-radius: 8px;
    box-shadow: 0 14px 35px rgba(0,0,0,0.15);
    transform: rotate(2.5deg);
    border: 1px solid #e2e8f0;
}

/* Đĩa CD xoay tròn */
.spinning-cd {
    animation: spin 4s linear infinite;
    display: inline-block;
    font-size: 2.2rem;
}

@keyframes spin {
    100% { transform: rotate(360deg); }
}
</style>
""", unsafe_allow_html=True)

# Khởi tạo trạng thái mở thiệp
if "opened" not in st.session_state:
    st.session_state.opened = False

# --- MÀN HÌNH CHỜ (INTRO COVER) ---
if not st.session_state.opened:
    st.markdown("""
    <div class="y2k-cover">
        <div class="spinning-cd">💿</div>
        <div class="pixel-title">★ THIỆP MỜI KÝ YẾU ★</div>
        <p style="font-size: 1.25rem; color: #1e293b; font-weight: 700; margin-bottom: 25px;">
            🪩 <span class="sparkle-text">NewJeans - Ditto Vibe</span> | Y2K Dreamcore 🪩<br>
            Bấm nút bên dưới để mở thiệp và thưởng thức âm nhạc nha!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("💿 MỞ THIỆP & BẬT NHẠC NGAY", use_container_width=True):
            st.session_state.opened = True
            st.rerun()

else:
    # --- GIAO DIỆN CHÍNH SAU KHI MỞ THIỆP ---
    with st.sidebar:
        st.markdown("## 🪩 Quét QR Chia Sẻ Nhanh")
        st.image("https://api.qrserver.com/v1/create-qr-code/?size=220x220&data=https://thi-p-m-i-k-y-u-c-a-myy-htugr7lb8bvdaml7hwskor.streamlit.app", caption="Dùng điện thoại quét mã này để mở thiệp!", use_container_width=True)
        st.markdown("---")
        st.markdown("## ☁️ Tùy chỉnh thiệp")
        name = st.text_input("Tên người mời", value="NGUYỄN HÀ MY")
        class_name = st.text_input("Lớp", value="Lớp 12A5 (K63)")
        school = st.text_input("Trường", value="THPT NGÔ GIA TỰ")
        date_text = st.text_input("Ngày chụp", value="Chủ nhật, ngày 25, tháng 10, năm 2026")
        time_text = st.text_input("Thời gian", value="10:00 - 12:00 sáng")
        location = st.text_input("Địa điểm", value="Trường THPT Ngô Gia Tự")
        message = st.text_area("Lời nhắn", value="Mong cậu có thể đến và cùng tớ tạo ra thật nhiều kỷ niệm đẹp đẽ nhất của thời học sinh nhé! ✨")
        sign_off = st.text_input("Chữ ký", value="hà myy")
        
        st.markdown("---")
        photo = st.file_uploader("Tải ảnh kỷ yếu khác (nếu muốn)", type=["jpg", "jpeg", "png", "webp"])

    # Tiêu đề chính
    st.markdown('<div style="text-align:center; margin-bottom: 20px;">', unsafe_allow_html=True)
    st.markdown('<div class="hero-title">★ THIỆP MỜI ★</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="sparkle-text">✦ Người mời: {name.strip()} ✦</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    left, right = st.columns([1.1, 0.9], gap="large")

    with left:
        st.markdown('<div class="dream-card">', unsafe_allow_html=True)
        st.markdown(f"### ☁️ {class_name}")
        st.markdown(f"**{school}**")
        st.markdown("---")
        st.markdown(f"🗓 **Ngày:** {date_text} — {time_text}")
        st.markdown(f"📍 **Địa điểm:** {location}")
        st.write("")
        st.markdown(f"💌 *\"{message}\"*")
        st.write("")
        st.markdown(f"**Thân mời,**  \n*{sign_off}* <span class='spinning-cd' style='font-size:1.3rem;'>🪩</span>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        if photo is not None:
            st.markdown('<div class="polaroid">', unsafe_allow_html=True)
            st.image(photo, use_container_width=True)
            st.caption("★ a little memory to keep ★")
            st.markdown('</div>', unsafe_allow_html=True)
        elif os.path.exists("photo.jpg"):
            st.markdown('<div class="polaroid">', unsafe_allow_html=True)
            st.image("photo.jpg", use_container_width=True)
            st.caption("★ a little memory to keep ★")
            st.markdown('</div>', unsafe_allow_html=True)
        elif os.path.exists("photo.png"):
            st.markdown('<div class="polaroid">', unsafe_allow_html=True)
            st.image("photo.png", use_container_width=True)
            st.caption("★ a little memory to keep ★")
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="dream-card" style="text-align:center; min-height:280px; padding-top: 40px;">
                <div style="font-size:3.8rem;" class="spinning-cd">💿</div>
                <h3 style="margin-top:10px;">your memory goes here</h3>
            </div>
            """, unsafe_allow_html=True)

    st.write("")

    # Khung nhạc Ditto Y2K
    st.markdown('<div class="dream-card">', unsafe_allow_html=True)
    st.markdown("### <span class='spinning-cd' style='font-size:1.6rem;'>🎶</span> Ditto (250 Remix) - NewJeans", unsafe_allow_html=True)
    
    if os.path.exists("ditto.mp3"):
        st.audio("ditto.mp3")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div style="text-align:center; color:#0284c7; padding:15px;" class="sparkle-text">★ MADE OF CLOUDS, STAR SYMBOLS, AND SWEET MEMORIES 💙 ★</div>', unsafe_allow_html=True)
