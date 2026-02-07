import streamlit as st
import time

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="StyleSense Elite", page_icon="👠", layout="wide")

# --- 2. THEME LOGIC (Based on Season) ---
if 'season_select' not in st.session_state:
    st.session_state.season_select = "Spring"

colors = {"Spring": "#7C9473", "Summer": "#E9C46A", "Fall": "#A85832", "Winter": "#264653"}
theme_color = colors.get(st.session_state.get('season_select', "Spring"), "#FF4B4B")

# --- 3. CUSTOM CSS ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #ffffff; }}
    .main-title {{ font-family: 'serif'; color: {theme_color}; font-size: 3rem; font-weight: 700; text-align: center; }}
    .style-card {{ 
        background-color: white; padding: 25px; border-radius: 15px; 
        border-left: 10px solid {theme_color}; box-shadow: 0 4px 15px rgba(0,0,0,0.1); color: #333;
    }}
    div.stButton > button {{
        background-color: {theme_color} !important; color: white !important; 
        border-radius: 25px !important; height: 50px; font-weight: bold; width: 100%;
    }}
    .avoid-box {{
        background-color: #fff5f5; border: 1px solid #feb2b2; padding: 15px;
        border-radius: 8px; color: #c53030; margin-top: 15px; font-weight: bold;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🏗️ Foundation")
    season = st.radio("Current Season", ["Spring", "Summer", "Fall", "Winter"], key="season_select")
    gender = st.radio("Gender Identity", ["Masculine", "Feminine", "Unisex"])
    silhouette = st.selectbox("Body Silhouette", ["Tailored/Slim", "Oversized/Relaxed", "Athletic", "Classic Fit"])
    st.divider()
    st.success("🚀 Mock Mode: ACTIVE")

# --- 5. MAIN INTERFACE ---
st.markdown(f'<h1 class="main-title">StyleSense {season}</h1>', unsafe_allow_html=True)
st.write("<p style='text-align: center;'>AI-Powered Wardrobe Intelligence</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📋 Input Parameters")
    main_piece = st.text_input("Main Piece (The Anchor):", placeholder="e.g., Black Leather Jacket")
    
    c1, c2 = st.columns(2)
    with c1:
        occasion = st.selectbox("Occasion", ["Work", "Casual", "Date Night", "Party", "Travel"])
        aesthetic = st.selectbox("Aesthetic", ["Minimalist", "Old Money", "Streetwear", "Grunge", "Preppy"])
    with c2:
        time_of_day = st.selectbox("Time of Day", ["Day", "Night"])
        accent_color = st.color_picker("Accent Mood", "#D4AF37")
        
    generate_btn = st.button("✨ CURATE MY LOOK")

# --- 6. MOCK LOGIC ---
def get_mock_style(piece, occ, aes, tod):
    bottoms = {"Minimalist": "Grey Wool Trousers", "Streetwear": "Baggy Cargo Pants", "Old Money": "White Chinos", "Grunge": "Ripped Black Jeans", "Preppy": "Slim Khakis"}
    return {
        "vibe": f"{aes} / {occ} / {tod}",
        "top": f"{piece} layered with a premium basic tee",
        "bottom": bottoms.get(aes, "Classic Denim"),
        "acc": "Tonal leather boots, a minimalist watch, and a structured bag.",
        "exp": f"This ensemble uses the {piece} to anchor a {aes} look. It is balanced for a {occ} setting.",
        "avoid": "Avoid heavy branding or logos; let the silhouette speak for itself."
    }

# --- 7. OUTPUT ---
with col2:
    st.subheader("🎨 Your Dossier")
    if generate_btn and main_piece:
        with st.spinner("Styling..."):
            time.sleep(1)
            res = get_mock_style(main_piece, occasion, aesthetic, time_of_day)
            st.markdown(f"""
                <div class="style-card">
                    <h2 style="color:{theme_color};">The {aesthetic} {occasion} Edit</h2>
                    <p><b>VIBE:</b> {res['vibe']}</p>
                    <hr>
                    <p><b>👕 TOP:</b> {res['top']}</p>
                    <p><b>👖 BOTTOM:</b> {res['bottom']}</p>
                    <p><b>💍 ACCESSORIES:</b> {res['acc']}</p>
                    <p><b>💡 EXPLANATION:</b> {res['exp']}</p>
                    <div class="avoid-box">⚠️ AVOID: {res['avoid']}</div>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Complete the inputs and click 'Curate' to see your mock styling result.")
