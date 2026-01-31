import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="Ege Berk Çınar | Portfolio", page_icon="🚀", layout="wide")

# --- CSS ile Şıklaştırma ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stHeader { background-color: #1a2a3a; }
    h1, h2, h3 { color: #1a2a3a; }
    .highlight { color: #3498db; font-weight: bold; }
    .stButton>button { background-color: #3498db; color: white; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (KİMLİK) ---
with st.sidebar:
    st.title("Ege Berk Çınar")
    st.image("https://via.placeholder.com/150", caption="Visionary Leader & Founder") # Kendi fotonun linkini buraya koyabilirsin
    st.markdown("📍 Aydın, Turkey")
    st.markdown("✉️ cinaregeberk00@gmail.com")
    st.markdown("[LinkedIn](https://linkedin.com/in/egeberkcinar)")
    st.divider()
    st.subheader("Skills")
    st.write("• Product Concept Design\n• GenAI & Prompt Engineering\n• Stakeholder Management\n• Crisis Navigation")
    st.subheader("Languages")
    st.write("🇹🇷 Turkish (Native)\n🇬🇧 English (B2+)\n🇩🇪 German (A1+)")

# --- ANA SAYFA (HEADER) ---
col1, col2 = st.columns([3, 1])
with col1:
    st.title("Impact-Driven Founder & AI Integrator")
    st.markdown("""
    <p style='font-size: 20px; font-style: italic; color: #555;'>
    "Uniting people, knowledge, and action to build future-ready ecosystems."
    </p>
    """, unsafe_allow_html=True)

# --- PROFILE ---
st.header("🚀 Profile")
st.write("""
A visionary leader who goes beyond ideas by uniting people, knowledge, and action to build impact-driven ecosystems. 
Founded youth-focused communities reaching 250+ students. Currently developing AI-driven ventures that translate 
education and sustainability challenges into structured systems.
""")

# --- GİRİŞİMCİLİK VE PROJELER (KARTLAR) ---
st.header("💡 Entrepreneurial Ventures")
col_neon, col_karbon = st.columns(2)

with col_neon:
    with st.expander("✨ NeOn | AI Learning Platform", expanded=True):
        st.write("**Founder & Product Lead** (2025 - Present)")
        st.write("Developing an AI-driven adaptive learning platform for Gen-E European Finals in Riga.")
        st.info("Selected for GençBizzTech Accelerator.")

with col_karbon:
    with st.expander("🌱 KarbonAT | Sustainability Tech", expanded=True):
        st.write("**Co-Founder** (2024 - 2025)")
        st.write("AI-assisted carbon tracking for the tourism industry using custom LLM prompts.")
        st.success("National Finalist & Top 17 at TEKNOFEST (10,000+ projects).")

# --- LİDERLİK ---
st.header("📣 Leadership & Impact")
st.markdown("#### Founder & President | Leadership Academy (2022-2024)")
st.write("""
- Managed a 9-member team reaching 250+ students.
- Spearheaded the **Women's Day Business Summit** with 8 top executives.
- Negotiated with administration to secure on-site professional observation visits.
""")

# --- DİĞER PROJELER ---
st.header("🧪 Innovation & Research")
tab1, tab2, tab3 = st.tabs(["GübreAI", "Chiral Molecule", "Academic"])

with tab1:
    st.write("Designing AI-driven fertilizer formulation using hydrogel technology for sustainable agriculture.")
with tab2:
    st.write("Designing a low-cost detection system to democratize advanced chemistry lab access in high schools.")
with tab3:
    st.write("**Ortaklar Science High School** | GPA: 98.5/100")
    st.write("8th Place Nationally (Tales Science Olympiad) | MUN Best Delegate Awards")

# --- FOOTER ---
st.divider()
st.center = st.write("© 2026 Ege Berk Çınar - Built with Streamlit")