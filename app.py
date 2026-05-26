import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="Ege Berk Çınar | Portfolio", page_icon="🚀", layout="wide")

# --- CSS ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1, h2, h3 { color: #1a2a3a; }
    .stButton>button { background-color: #3498db; color: white; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("Ege Berk Çınar")
    st.image("https://via.placeholder.com/150", caption="Social Entrepreneur & Ecosystem Builder")
    st.markdown("📍 Aydın, Turkey")
    st.markdown("📞 +90 505 093 4509")
    st.markdown("✉️ cinaregeberk00@gmail.com")
    st.markdown("[🔗 LinkedIn](https://linkedin.com/in/egeberkcinar)")
    st.divider()
    st.subheader("💼 Skills")
    st.write("""
    **Strategy & Startups:**
    • Leadership & Management
    • Entrepreneurship
    • R&D & Science
    • AI & Innovation

    **Technical:**
    • Visual Storytelling
    • Prompt Engineering
    • API Usage
    • Video Production

    **Languages:**
    🇹🇷 Turkish (Native)
    🇬🇧 English (B2+)
    🇩🇪 German (A1+)
    """)

# --- HEADER (native Streamlit, no raw HTML) ---
st.markdown("<br>", unsafe_allow_html=True)
_, center, _ = st.columns([1, 3, 1])
with center:
    st.markdown("# Ege Berk Çınar")
    st.markdown("### :blue[Social Entrepreneur & Ecosystem Builder]")
    st.markdown("*\"Systems for Impact. Vision for Change.\"*")
st.markdown("---")

# --- PROFILE ---
st.header("🚀 Profile")
st.write("""
A visionary leader who goes beyond ideas by uniting people, knowledge, and action to build impact-driven ecosystems.
Founded youth-focused communities (Leadership Academy, VisionUp) reaching 250+ students, fostering vision-oriented
learning and entrepreneurial initiative. Developing AI-driven ventures that translate education and sustainability
challenges into structured systems with measurable social and environmental impact.
""")

# --- HIGHLIGHTS ---
st.markdown("### 🏆 Highlights")
col1, col2, col3, col4, col5 = st.columns(5)
col1.success("🎓 Leadership Academy")
col2.success("🥇 TEKNOFEST Finalist")
col3.success("🌱 KarbonAT Co-Founder")
col4.info("🌍 beVisioneers Fellow")
col5.warning("🛰️ IAC 2026 Speaker")

st.divider()

# --- IAC 2026 FEATURED ---
st.header("🛰️ IAC 2026 — International Astronautical Congress")

iac_col1, iac_col2 = st.columns([3, 1])
with iac_col1:
    st.subheader("Accepted for Oral Presentation ✨")
    st.markdown("""
**77th International Astronautical Congress** — Antalya, Turkey | 5–9 October 2026

*"fireguard-1: AI-based predictive wildfire early warning system using multi-source satellite data"*
""")
    st.markdown("""
| Field | Detail |
|---|---|
| 🏛️ Symposium | B4 — 33rd IAA Symposium on Small Satellite Missions |
| 📅 Presentation | 6 October 2026, 15:00 — Hall 28 |
| 📄 Paper ID | IAC-26,B4,9-GTS.5,11,x114716 |
| 📚 Indexed | SCOPUS & EI Compendex, DOI assigned |
""")

with iac_col2:
    st.metric("Session", "B4 / GTS.5")
    st.metric("Presentation Type", "Oral (10 min)")
    st.metric("Congress", "77th IAC")

st.write("""
**fireguard-1** is an AI-powered satellite data fusion system designed to detect and predict wildfires
before they spread. By integrating multi-source satellite imagery with predictive machine learning models,
the system enables early warnings that can save ecosystems, communities, and lives.
""")

st.divider()

# --- ENTREPRENEURIAL VENTURES ---
st.header("💡 Entrepreneurial Ventures")

with st.expander("🌍 beVisioneers | The Mercedes-Benz Fellowship — TROIA (GübreAI)", expanded=True):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("**Fellow** | 2025 - Present")
        st.write("""
        Accepted into **beVisioneers: The Mercedes-Benz Fellowship** — a globally competitive, fully-funded
        sustainability fellowship designed and implemented by The DO School Fellowships, backed by Mercedes-Benz
        with a €135M foundation.

        **Accepted with TROIA (GübreAI):**
        - AI-driven crop-specific fertilizer formulation system using hydrogel technology
        - Planet-positive agriculture solution targeting sustainable farming at scale

        **Fellowship Benefits:**
        - 🏆 Dedicated **Venture Coach** for TROIA's development and go-to-market strategy
        - 🤝 **1:1 Mentorship** from industry experts for personal career development
        - 🎓 Award-winning innovation training (online modules + regional summits)
        - 💰 Eligible for **up to €20,000** project scholarship after Year 1
        - 🌐 Access to a global network of environmental innovators
        """)
    with col2:
        st.success("**Status:** Active Fellow")
        st.write("**Focus:**")
        st.write("• Sustainable Agriculture")
        st.write("• AI Agents")
        st.write("• Hydrogel Tech")
        st.write("• Global Fellowship")

with st.expander("🌱 KarbonAT | Sustainability Tech for Tourism", expanded=True):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("**Co-Founder** | 2024 - 2025")
        st.write("""
        Developed an AI-assisted carbon emission tracking and sustainability management solution for hotels.

        **My Contributions:**
        - Integrated AI APIs for data analysis
        - Designed custom LLM prompt structures for tourism-specific sustainability reports
        - Led technical development and compliance automation

        **Major Achievement:**
        - 🥇 **National Finalist & Top 17** at TEKNOFEST Tourism Technologies Competition
        - 📊 Advanced from **10,000+ competing projects** nationwide
        - 🇨🇾 Represented Turkey at international finals in **Cyprus** with exhibition stand
        """)
    with col2:
        st.success("**TEKNOFEST 2024**\nTop 17 Nationally")

st.divider()

# --- LEADERSHIP ---
st.header("📣 Leadership Experience")

st.markdown("### President | Leadership Academy")
st.markdown("*Student-led leadership, entrepreneurship & 21st-century skills initiative* | **2022 - 2024**")
st.caption("(Successfully operated school-wide for two academic years until school closure in 2024)")

col1, col2 = st.columns(2)
with col1:
    st.markdown("#### 🎯 Core Responsibilities")
    st.write("""
    - **Led as President** of a student-run Leadership Academy addressing the absence of
      entrepreneurship and career literacy across the entire high school (≈250 students)
    - **Built and managed** a 9-member core team across specialized departments
      (Events, Content, Outreach, Operations, Media)
    - **Designed and delivered** peer-to-peer workshops on 21st-century skills
      (communication, entrepreneurship, presentation, leadership)
    - **Organized 7 career talks** with professionals from diverse industries
    """)
with col2:
    st.markdown("#### 🌟 Key Initiatives")
    st.write("""
    **Flagship Events:**
    - Women's Day Business Summit (8 executive speakers)
    - On-site professional observation visits
    - Career guidance sessions

    **Social Impact Projects:**
    - Book donation campaigns
    - Winter aid for low-income families
    - Animal welfare initiatives
    """)

st.info("**Impact:** Contributed to a cultural shift from passive participation to initiative-driven, student-led action across the school community.")

st.divider()

# --- INNOVATION & RESEARCH ---
st.header("🧪 Innovation & Research")

tab1, tab2, tab3 = st.tabs(["🔬 Chiral Molecule Detection", "🌾 TROIA / GübreAI (Agri-Tech)", "📚 TÜBİTAK Research"])

with tab1:
    st.markdown("### Research Assistant | Chiral Molecule Detection System")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("""
        Designing a low-cost experimental system to detect **chiral molecules** in high school laboratory settings.

        **Why Chirality Matters:**
        Chirality is fundamental to understanding molecular interactions in chemistry, biology, and pharmacology.
        Many biological molecules (amino acids, sugars) are chiral, and detecting chirality is essential for
        advanced chemistry education—but current equipment is prohibitively expensive for most schools.

        **Mission:**
        Democratize access to advanced chemistry experimentation through scalable, cost-effective design,
        enabling hands-on learning about molecular structure and optical activity.
        """)
    with col2:
        st.warning("Status: In Development")
        st.write("**Goal:**\n• Accessible Science\n• Low-Cost Design")

with tab2:
    st.markdown("### Project Lead | TROIA (GübreAI)")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("""
        Developing an AI-driven system for crop-specific fertilizer formulation using hydrogel technology
        with a focus on **planet-positive sustainability**.

        **Technical Focus:**
        - Designing agent-based workflows to optimize fertilizer selection
        - Building supplier decision-making algorithms for farmers
        - Integrating sustainable agriculture practices with AI

        **Recognition:**
        - 🌍 Accepted into **beVisioneers: The Mercedes-Benz Fellowship**
        """)
    with col2:
        st.success("Active — beVisioneers Fellow")
        st.write("**Focus:**\n• Sustainability\n• AI Agents\n• Hydrogel Tech")

with tab3:
    st.markdown("### TÜBİTAK 2204-A Research Projects")
    st.write("""
    Completed two research projects under Turkey's national scientific research program:

    1. **Eski Türk Kültür İnancı Şamanizmin Aktif Türk Kültürüne Etkileri**
       - Historical and anthropological research on shamanism's impact on modern Turkish culture

    2. **Aloe Vera Bazlı Hidrojel Üretimi**
       - Biochemical experimentation for sustainable hydrogel synthesis
    """)

st.divider()

# --- EDUCATION & AWARDS ---
col1, col2 = st.columns(2)

with col1:
    st.header("🎓 Education")
    st.markdown("### Ortaklar Science High School")
    st.markdown("*Aydın, Turkey* | **Expected June 2026**")
    st.metric("GPA", "98.5 / 100", "≈ 3.95 / 4.00")
    st.write("""
    **Honors:** 🏅 Certificate of Honor (4×)

    **Selected Coursework:**
    • Advanced Mathematics
    • Physics
    • Scientific Research Methods
    """)

with col2:
    st.header("🏆 Awards & Competitions")

    st.markdown("#### 🛰️ IAC 2026 — International Astronautical Congress")
    st.warning("""
    **Accepted for Oral Presentation**
    77th IAC · Antalya, Turkey · October 2026
    Symposium B4 — Small Satellite Missions
    SCOPUS & EI Compendex Indexed
    """)

    st.markdown("#### 🥇 TEKNOFEST Tourism Technologies 2024")
    st.success("""
    **National Finalist & Top 17**
    - Advanced from 10,000+ projects nationwide
    - Represented Turkey at Cyprus finals
    - Exhibited solution with dedicated stand
    """)

    st.markdown("#### 🧪 Science & Math Olympiads")
    st.info("""
    **National Finalists:**
    - Tales Science Olympiad (8th Place Nationally)
    - Tales Math Olympiad · URFODU
    - Chemistry, Biology, Mathematics, Geography
    """)

    st.markdown("#### 🎤 Model United Nations")
    st.write("**Best Delegate & Outstanding Delegate** awards")

st.divider()

# --- ADDITIONAL INITIATIVES ---
st.header("🌟 Additional Initiatives")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### VisionUp (Founder)")
    st.write("""
    Youth-focused community initiative aimed at building a **young entrepreneurial ecosystem in Aydın**.

    **Goals:**
    - Organize competitions and innovation challenges
    - Foster entrepreneurial culture among youth
    - Create a sustainable young entrepreneurial ecosystem in Aydın

    **Status:** Currently on hold (2025)
    """)

with col2:
    st.markdown("### Community Impact")
    st.write("""
    **Through Leadership Academy:**
    - 📚 Book donation campaigns
    - ❄️ Winter aid for low-income families
    - 🐾 Animal welfare initiatives
    - 🏭 Industry observation visits
    - 👥 Professional networking events
    """)

st.divider()

# --- FOOTER ---
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#888;'>© 2026 Ege Berk Çınar | Built with Streamlit 🚀 | Last Updated: May 2026</p>",
    unsafe_allow_html=True
)
