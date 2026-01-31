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
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    .achievement-badge {
        background-color: #3498db;
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        display: inline-block;
        margin: 5px;
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (KİMLİK) ---
with st.sidebar:
    st.title("Ege Berk Çınar")
    st.image("https://via.placeholder.com/150", caption="Founder & AI Integrator")
    st.markdown("📍 Aydın, Turkey")
    st.markdown("📞 +90 505 093 4509")
    st.markdown("✉️ cinaregeberk00@gmail.com")
    st.markdown("[🔗 LinkedIn](https://linkedin.com/in/egeberkcinar)")
    
    st.divider()
    
    st.subheader("🎯 Quick Stats")
    st.metric("Students Reached", "250+")
    st.metric("Team Members Led", "9")
    st.metric("GPA", "98.5/100")
    st.metric("TEKNOFEST Ranking", "Top 17")
    
    st.divider()
    
    st.subheader("💼 Skills")
    st.write("""
    **Strategy & Startups:**
    • Product Concept Design
    • Business Model Canvas
    • Pitching & Stakeholder Management
    
    **Technical:**
    • GenAI Integration
    • Prompt Engineering
    • API Usage
    • Video Production
    
    **Languages:**
    🇹🇷 Turkish (Native)
    🇬🇧 English (B2+)
    🇩🇪 German (A1+)
    """)

# --- ANA SAYFA (HEADER) ---
st.markdown("""
    <div style='text-align: center; padding: 40px 0;'>
        <h1 style='font-size: 48px; margin-bottom: 10px;'>Ege Berk Çınar</h1>
        <h3 style='color: #3498db; font-weight: normal;'>Impact-Driven Founder & AI Integrator</h3>
        <p style='font-size: 18px; font-style: italic; color: #666; margin-top: 20px;'>
        "Uniting people, knowledge, and action to build future-ready ecosystems."
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- PROFILE ---
st.header("🚀 About Me")
st.write("""
A visionary leader who goes beyond ideas by uniting people, knowledge, and action to build impact-driven ecosystems. 
Founded youth-focused communities (Leadership Academy, VisionUp) reaching **250+ students**, fostering vision-oriented 
learning and entrepreneurial initiative. Currently developing **AI-driven ventures** that translate education and 
sustainability challenges into structured systems with measurable social and environmental impact.
""")

# --- BAŞARILAR (BADGES) ---
st.markdown("### 🏆 Key Achievements")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="achievement-badge">🥇 TEKNOFEST Finalist</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="achievement-badge">🎓 GPA 98.5/100</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="achievement-badge">👥 250+ Students</div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="achievement-badge">🚀 3 Startups</div>', unsafe_allow_html=True)

st.divider()

# --- GİRİŞİMCİLİK VE PROJELER ---
st.header("💡 Entrepreneurial Ventures")

# NeOn
with st.expander("✨ NeOn | AI-Powered Personalized Learning Platform", expanded=True):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("**Founder & Product Lead** | 2025 - Present")
        st.write("""
        Building an adaptive learning platform that personalizes information flow based on user curiosity, 
        learning depth, and cognitive pathways.
        
        **My Role:**
        - Leading product vision and brand positioning
        - Developing go-to-market strategy
        - Building MVP for Gen-E European Finals (Riga)
        
        **Achievement:**
        - ✅ Selected for GençBizzTech Accelerator
        """)
    with col2:
        st.info("**Status:** Active Development")
        st.write("**Tech Stack:**")
        st.write("• AI/ML Integration")
        st.write("• Adaptive Algorithms")
        st.write("• UX/UI Design")

# KarbonAT
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
        st.write("**Tech Stack:**")
        st.write("• LLM Integration")
        st.write("• API Development")
        st.write("• Sustainability Analytics")

st.divider()

# --- LİDERLİK DENEYİMİ ---
st.header("📣 Leadership Experience")

with st.container():
    st.markdown("### Founder & President | Leadership Academy")
    st.markdown("*Student-led leadership, entrepreneurship & 21st-century skills initiative* | **2022 - 2024**")
    st.caption("(Successfully operated school-wide for two academic years until school closure in 2024)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🎯 Core Achievements")
        st.write("""
        - **Founded and led** a student-run Leadership Academy addressing the absence of entrepreneurship, 
          communication, and career literacy across the entire high school (≈250 students)
        
        - **Built and managed** a 9-member core team across specialized departments 
          (Events, Content, Outreach, Operations)
        
        - **Designed and delivered** peer-to-peer workshops on 21st-century skills 
          (communication, entrepreneurship, presentation, leadership)
        
        - **Organized 7 career talks** with professionals from public administration, healthcare, 
          engineering, design, and social sciences
        """)
    
    with col2:
        st.markdown("#### 🌟 Flagship Events & Projects")
        st.write("""
        **Women's Day Business Summit:**
        - Hosted 8 accomplished businesswomen
        - Managed end-to-end planning, logistics, and stakeholder communication
        
        **On-Site Professional Visits:**
        - Olive oil factory
        - Çıldır Airport
        - Dental clinics
        - Provided hands-on career exposure
        
        **Social Impact Projects:**
        - Book donation campaigns
        - Winter aid for low-income families
        - Animal welfare initiatives
        
        **Operations:**
        - Managed Academy's Instagram presence
        - Ensured sustained student engagement
        """)
    
    st.info("**Impact:** Contributed to a cultural shift from passive participation to initiative-driven, student-led action across the school community.")

st.divider()

# --- ARAŞTIRMA VE İNOVASYON ---
st.header("🧪 Innovation & Research")

tab1, tab2, tab3 = st.tabs(["🌾 GübreAI (Agri-Tech)", "🔬 Chiral Molecule Detection", "📚 TÜBİTAK Research"])

with tab1:
    st.markdown("### Project Lead | GübreAI")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("""
        Developing an AI-driven system for crop-specific fertilizer formulation using hydrogel technology.
        
        **Technical Focus:**
        - Designing agent-based workflows to optimize fertilizer selection
        - Building supplier decision-making algorithms for farmers
        - Integrating sustainable agriculture practices with AI
        """)
    with col2:
        st.warning("Status: In Development")
        st.write("**Focus Areas:**")
        st.write("• AI Agents")
        st.write("• Hydrogel Tech")
        st.write("• Agri Optimization")

with tab2:
    st.markdown("### Research Assistant | Chiral Molecule Detection System")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("""
        Designing a low-cost experimental system to detect chiral molecules in high school laboratory settings.
        
        **Mission:**
        Democratize access to advanced chemistry experimentation through scalable, cost-effective design.
        
        **Goals:**
        - Make advanced chemistry accessible to all high schools
        - Reduce equipment costs significantly
        - Enable hands-on chirality experiments
        """)
    with col2:
        st.warning("Status: In Development")
        st.write("**Impact Goal:**")
        st.write("• Accessible Science")
        st.write("• Low-Cost Design")
        st.write("• Educational Equity")

with tab3:
    st.markdown("### TÜBİTAK 2204-A Research Projects")
    st.write("""
    Completed two research projects under Turkey's national scientific research program:
    
    1. **Early Turkic Belief Systems**
       - Historical and anthropological research
       - Cultural heritage documentation
    
    2. **Aloe Vera-Based Hydrogel Synthesis**
       - Biochemical experimentation
       - Sustainable materials research
    """)

st.divider()

# --- EĞİTİM VE ÖDÜLLER ---
col1, col2 = st.columns(2)

with col1:
    st.header("🎓 Education")
    st.markdown("### Ortaklar Science High School")
    st.markdown("*Aydın, Turkey* | **Expected June 2026**")
    st.write("")
    st.metric("GPA", "98.5 / 100", "≈ 3.95 / 4.00")
    st.write("")
    st.write("**Honors:**")
    st.write("🏅 Certificate of Honor (4×)")
    st.write("")
    st.write("**Selected Coursework:**")
    st.write("• Advanced Mathematics")
    st.write("• Physics")
    st.write("• Scientific Research Methods")

with col2:
    st.header("🏆 Awards & Competitions")
    
    st.markdown("#### 🥇 TEKNOFEST Tourism Technologies 2024")
    st.success("""
    **National Finalist & Top 17**
    - Advanced from 10,000+ projects nationwide
    - Represented Turkey at Cyprus finals
    - Exhibited solution with dedicated stand
    """)
    
    st.markdown("#### 🥈 Tales Science Olympiad")
    st.info("**8th Place Nationally** (Turkey)")
    
    st.markdown("#### 🥉 Tales Math Olympiad")
    st.info("**National Finalist**")
    
    st.markdown("#### 🎤 Model United Nations")
    st.write("""
    **Best Delegate & Outstanding Delegate** awards across multiple conferences
    - Including one national-level conference
    """)

st.divider()

# --- EK AKTİVİTELER ---
st.header("🌟 Additional Activities & Initiatives")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### VisionUp (Founder)")
    st.write("""
    Initiated a youth-focused community centered on innovation culture and long-term transformation.
    
    **Status:** Currently on hold (2025)
    
    **Vision:** Creating a platform for youth to explore innovation, entrepreneurship, 
    and transformative thinking beyond traditional education.
    """)

with col2:
    st.markdown("### Community Impact")
    st.write("""
    **Social Responsibility Projects:**
    - 📚 Book donation campaigns
    - ❄️ Winter aid for low-income families
    - 🐾 Animal welfare initiatives
    
    **Professional Development:**
    - 🎯 Career guidance sessions
    - 🏭 Industry observation visits
    - 👥 Networking events with professionals
    """)

st.divider()

# --- FOOTER ---
st.markdown("""
    <div style='text-align: center; padding: 30px 0; color: #666;'>
        <p>© 2026 Ege Berk Çınar | Built with Streamlit & Passion 🚀</p>
        <p style='font-size: 14px;'>Last Updated: February 2026</p>
    </div>
    """, unsafe_allow_html=True)
