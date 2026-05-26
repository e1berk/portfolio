import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time

# --- SAYFA YAPILANDIRMASI ---
st.set_page_config(page_title="Ege Berk Çınar | System Architect & Researcher", page_icon="🚀", layout="wide")

# --- ÖZEL CSS TASARIMI ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; font-family: 'Inter', sans-serif; }
    h1, h2, h3 { color: #3498db; }
    .stHeader { background-color: #1a2a3a; }
    
    /* TROIA Analiz Butonu */
    div.stButton > button:first-child {
        background-color: #2E7D32 !important;
        color: white !important;
    }
    
    /* IAC Container Vurgusu */
    .iac-container {
        border: 2px solid #f39c12;
        border-radius: 10px;
        padding: 20px;
        background-color: #1c1c1c;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (PROFESYONEL KİMLİK) ---
with st.sidebar:
    st.title("Ege Berk Çınar")
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", caption="System Architect & Researcher", width=120)
    
    # beVisioneers Global Kimlik Rozeti
    st.success("🏅 **beVisioneers: The Mercedes-Benz Fellow**")
    
    st.markdown("📍 **Aydın, Turkey**")
    st.markdown("📞 **+90 505 093 4509**")
    st.markdown("✉️ **cinaregeberk00@gmail.com**")
    st.markdown("[🔗 LinkedIn Profile](https://linkedin.com/in/egeberkcinar)")
    
    st.divider()
    
    st.subheader("💼 System Architecture & Skills")
    st.write("""
    **Strategy & Ecosystems:**
    • R&D & Science Management
    • AI Implementation Strategy
    • System & Architecture Design
    • Venture Building
    
    **Technical & Tools:**
    • Python & Streamlit UI
    • LLM Prompt Engineering & APIs
    • Data Visualization (Plotly)
    • Random Forest Classification
    """)

# --- ANA SAYFA HEADER ---
st.markdown("""
    <div style='text-align: center; padding: 20px 0;'>
        <h1 style='font-size: 45px; margin-bottom: 10px; color: #ffffff;'>Ege Berk Çınar</h1>
        <h3 style='color: #3498db; font-weight: normal; margin-top: 0;'>Researcher & System Architect</h3>
        <p style='font-size: 18px; font-style: italic; color: #a1a1a1; margin-top: 15px;'>
        "Designing structured systems to bridge predictive analytics, aerospace, and environmental sustainability."
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- FLAGSHIP: IAC 2026 & FIREGUARD-1 ---
st.markdown('<div class="iac-container">', unsafe_allow_html=True)
st.header("🌍 Flagship Research: IAC 2026 & Space Technologies")
st.subheader("FIREGUARD-1: AI-BASED PREDICTIVE WILDFIRE EARLY WARNING SYSTEM USING MULTI-SOURCE SATELLITE DATA")

iac_col1, iac_col2 = st.columns([2, 1])

with iac_col1:
    st.markdown("""
    **Event:** 77th International Astronautical Congress (IAC 2026), Antalya[cite: 3]
    **Symposium & Session:** 33rd IAA SYMPOSIUM ON SMALL SATELLITE MISSIONS (B4) | Small Satellite Missions Global Technical Session (9-GTS.5)[cite: 2, 3]
    **Format:** Oral Presentation[cite: 2, 3]
    **Paper ID:** IAC-26,B4,9-GTS.5,11,x114716[cite: 3]
    
    **Abstract:**[cite: 2]
    The large-scale wildfires that occurred in Türkiye in 2021 devastated more than 200,000 hectares of land, caused multiple fatalities, and resulted in economic losses exceeding USD 1 billion[cite: 2]. Existing wildfire monitoring systems, including MODIS-based satellite detection and ground-based watchtowers, are inherently reactive, detecting fires only after ignition and failing to utilize the critical 24-72 hour prevention window[cite: 2]. This limitation is further exacerbated by the inability of aerial firefighting assets to operate during nighttime, creating a significant operational gap[cite: 2].
    
    This study presents an AI-powered early warning system designed to predict wildfire risk several days before ignition by integrating multi-source satellite imagery and meteorological data[cite: 2]. Historical wildfire events between 2019 and 2024 were analyzed using multi-temporal Sentinel-2 and Sentinel-3 observations[cite: 2]. Vegetation stress and fuel moisture conditions were quantified using Normalized Difference Vegetation Index (NDVI), Normalized Difference Water Index (NDWI), and Normalized Difference Moisture Index (NDMI), alongside Land Surface Temperature (LST) measurements[cite: 2]. These parameters were integrated with meteorological variables including air temperature, relative humidity, wind speed, and cumulative precipitation[cite: 2]. A Random Forest classifier was trained using 15 features extracted from 30-day pre-fire temporal windows[cite: 2].
    
    The model achieved an overall accuracy of 73%[cite: 2]. Based on these findings, the FireGuard-1 concept proposes a regional 3U CubeSat constellation providing a 90-minute revisit time over high-risk Mediterranean zones[cite: 2]. This approach addresses the temporal limitations of existing Earth observation systems and enables continuous nighttime monitoring[cite: 2]. The system generates explainable, real-time wildfire risk scores on a 0-10 scale, supporting preventive resource allocation before ignition occurs[cite: 2]. This proof-of-concept demonstrates that predictive wildfire monitoring using artificial intelligence and open satellite data is technically feasible and economically viable, offering a scalable framework for fire-prone regions worldwide[cite: 2].
    """)
    
with iac_col2:
    st.success("✅ **Accepted for 10-Minute Oral Presentation**[cite: 3]")
    st.info("📅 **Schedule:** 6 October 2026 | 15:00 @ Room Hall 28[cite: 3]")
    st.markdown("### 📋 Verification References")
    st.caption("• **Official Notification Letter:** Confirmed & Verified (Paper ID: 114716)[cite: 3]")
    st.caption("• **Technical Session Assignment:** Registered under B4-33rd IAA Symposium[cite: 3]")

st.markdown('</div>', unsafe_allow_html=True)
st.divider()

# --- INTERACTIVE MODULE: TROIA ---
st.header("🤖 Live System Demo: TROIA (Agri-Tech Deep Engine)")
st.caption("This module demonstrates the live runtime of TROIA's automated fertilizer optimization matrix using Generative Logic and biochemical gap analytics.")

t_col1, t_col2 = st.columns([1, 2])

with t_col1:
    st.markdown("#### 📊 Real-Time Telemetry Input")
    lokasyon = st.text_input("Target Sub-Region / District", "Aydın / Söke", key="troia_loc")
    mahsul = st.selectbox("Target Agricultural Crop", ["Pamuk", "Mısır", "Buğday", "Domates"], key="troia_crop")
    
    st.markdown("**🔬 Soil Biochemical Values**")
    ph_degeri = st.slider("Soil pH Matrix", 0.0, 14.0, 7.4, 0.1, key="troia_ph")
    mevcut_n = st.number_input("Current Nitrogen (N) (mg/kg)", min_value=0, max_value=200, value=45, key="troia_n")
    mevcut_p = st.number_input("Current Phosphorus (P) (mg/kg)", min_value=0, max_value=150, value=20, key="troia_p")
    mevcut_k = st.number_input("Current Potassium (K) (mg/kg)", min_value=0, max_value=300, value=110, key="troia_k")
    
    hidrojel_modu = st.toggle("Integrate Intelligent Hydrogel Network", value=True, key="troia_hydro")
    analiz_butonu = st.button("Execute Core Gap Analysis & Recipe", key="troia_run")

ideal_degerler = {"Pamuk": {"N": 120, "P": 60, "K": 150}, "Mısır": {"N": 150, "P": 70, "K": 180}, "Buğday": {"N": 90, "P": 40, "K": 100}, "Domates": {"N": 130, "P": 80, "K": 200}}

with t_col2:
    if analiz_butonu:
        with st.spinner("TROIA Engine executing multi-agent biochemical gap computation..."):
            time.sleep(1)
            
        gap_n = max(0, ideal_degerler[mahsul]["N"] - mevcut_n)
        gap_p = max(0, ideal_degerler[mahsul]["P"] - mevcut_p)
        gap_k = max(0, ideal_degerler[mahsul]["K"] - mevcut_k)
        
        fig = go.Figure()
        fig.add_trace(go.Bar(x=['Nitrogen (N)', 'Phosphorus (P)', 'Potassium (K)'], y=[mevcut_n, mevcut_p, mevcut_k], name='Current Soil Assays', marker_color='#8D6E63'))
        fig.add_trace(go.Bar(x=['Nitrogen (N)', 'Phosphorus (P)', 'Potassium (K)'], y=[ideal_degerler[mahsul]["N"], ideal_degerler[mahsul]["P"], ideal_degerler[mahsul]["K"]], name='Target Equilibrium', marker_color='#2E7D32'))
        fig.update_layout(title=f'Biochemical Gap Model for {mahsul}', barmode='group', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="white"), legend=dict(bgcolor='rgba(14,17,23,0.8)'))
        st.plotly_chart(fig, use_container_width=True)
        
        st.success(f"**Custom Matrix:** {gap_n*0.45:.1f}kg Urea, {gap_p*0.3:.1f}kg Phosphate, {gap_k*0.5:.1f}kg Sulfate per acre.")
    else:
        st.info("👈 Enter localized field assays on the left panel to execute runtime logic.")

st.divider()

# --- GLOBAL FELLOWSHIPS & EXECUTIVE LEADERSHIP ---
st.header("🌍 Global Fellowships & Executive Leadership")

with st.container():
    # beVisioneers: Mercedes-Benz Fellowship Bölümü
    st.markdown("### beVisioneers: The Mercedes-Benz Fellowship")
    st.markdown("*Global Innovator & Fellow* | **2024 - Present**")
    st.write("""
    - **Global Selection:** Appointed as a fellow within the Mercedes-Benz supported beVisioneers sustainability intensive, focusing on scalable ecological frameworks.
    - **Venture Incubation:** Actively engaging in advanced venture building labs, international leadership seminars, and cohort-driven systemic environmental design.
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Youth Leadership Academy Bölümü
    st.markdown("### President | Youth Leadership Academy")
    st.markdown("*High-impact systemic initiative resolving regional career and innovation literacy gaps* | **2022 - 2024**")
    
    l_col1, l_col2 = st.columns(2)
    with l_col1:
        st.write("""
        - **Executive Governance:** Founded and scaled a comprehensive leadership infrastructure targeting regional ecosystem fragmentation, directly managing onboarding and curricula for **250+ students**.
        - **Cross-Functional Team Building:** Formed, trained, and orchestrated a high-performing **9-member executive core board** split across tactical operational nodes.
        """)
    with l_col2:
        st.write("""
        - **Corporate Summits:** Structured and executed the *Women's Day Business Summit*, securing partnerships with **8 corporate executive speakers** to align academic tracks with industrial needs.
        - **Systemic Impact:** Drove a measurable cultural transition across the student body, shifting institutional focus from passive consumption to agile, milestone-driven execution.
        """)

st.divider()

# --- ARCHIVE: PREVIOUS ITERATIONS ---
st.header("🗄️ System Archives & Previous Iterations")
st.caption("Past experiments, technical milestones, and operational pilots preserved for architectural continuity.")

with st.expander("🌱 KarbonAT | Predictive Carbon Analytics (TEKNOFEST Finalist Top 17)", expanded=False):
    st.write("Engineered an AI-assisted carbon accounting and automated compliance reporting SaaS platform tailored for the commercial hospitality industry. Reached national top 17 among 10,000+ projects and presented at Cyprus.")

with st.expander("✨ NeOn | AI-Powered Personalized Cognitive Platform (Gen-E European Finalist Pilot)", expanded=False):
    st.write("Developed an adaptive learning layer MVP to optimize cognitive pathways based on user intent. Selected for GençBizzTech Accelerator. (Status: Deprecated/Archived to focus on deep-tech research).")

with st.expander("🔬 Accessible Chiral Molecule Detection System", expanded=False):
    st.write("Designed a low-cost optical polarization array allowing high school laboratory environments to explicitly assay molecular chirality, democratizing access to spatial chemistry.")

with st.expander("📚 Formal Research: TÜBİTAK 2204-A Initiatives", expanded=False):
    st.write("1. Socio-Anthropological Assay on Shamanism's impact on modern culture. \n2. Biochemical Synthesis of Aloe Vera based hydrogels for agricultural water retention.")

st.divider()

# --- FOOTER ---
st.markdown("""
    <div style='text-align: center; padding: 20px 0; color: #666; font-size: 14px;'>
        <p>© 2026 Ege Berk Çınar | Engineered and Maintained with Streamlit Engine 🚀</p>
        <p>System State: Production Verified | Last Structural Upgrade: May 2026</p>
    </div>
    """, unsafe_allow_html=True)
