import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

#page configuration
st.set_page_config(
    page_title="SPHEREx Sky Change Explorer",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

#styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Plus+Jakarta+Sans:wght@400;600&display=swap');

    /* Transparent top header bar */
    header[data-testid="stHeader"] {
        background: transparent !important;
    }

    /* Scrolling Galaxy Background Image */
    .stApp {
        background-image: linear-gradient(rgba(5, 8, 22, 0.75), rgba(5, 8, 22, 0.85)), 
                          url('https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?q=80&w=2000&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #F1F5F9;
    }

    /* Custom Header Font for Specific Sections */
    .section-header {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.4rem;
        color: #C084FC;
        margin-bottom: 10px;
        text-shadow: 0 0 10px rgba(192, 132, 252, 0.4);
    }

    /* Cosmic Glass Cards with Glowing Shapes */
    .cosmic-card {
        background: rgba(15, 23, 42, 0.75);
        backdrop-filter: blur(14px);
        border: 1px solid rgba(56, 189, 248, 0.3);
        padding: 22px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
        position: relative;
        overflow: hidden;
    }

    .cosmic-card::before {
        content: "";
        position: absolute;
        top: -50px;
        right: -50px;
        width: 100px;
        height: 100px;
        background: radial-gradient(circle, rgba(56,189,248,0.2) 0%, rgba(0,0,0,0) 70%);
        border-radius: 50%;
    }

    /* Sidebar Forced Dark Background & White Font */
    section[data-testid="stSidebar"] {
        background-color: #0B0F19 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    section[data-testid="stSidebar"] *, section[data-testid="stSidebar"] label, section[data-testid="stSidebar"] span {
        color: #FFFFFF !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    /* DARK GREY SELECTBOX */
.stSelectbox div[data-baseweb="select"] {
    background-color: #343A40 !important;
    border-color: #525B65 !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    background-color: #343A40 !important;
}

.stSelectbox div[data-baseweb="select"] * {
    color: #FFFFFF !important;
}

div[data-baseweb="popover"] * {
    background-color: #343A40 !important;
    color: #FFFFFF !important;
}

div[data-baseweb="menu"] {
    background-color: #343A40 !important;
}

div[data-baseweb="menu"] * {
    color: #FFFFFF !important;
}

/* Change the text color inside the selectbox to space grey (#71717A) */
    div[data-baseweb="select"] span {
        color: #71717A !important;
        font-weight: 600 !important;
    }

    </style>
""", unsafe_allow_html=True)

#header
st.markdown(
    '<h1 style="font-family: Orbitron, sans-serif; font-size: 3.5rem; font-weight: 950; color: #38BDF8; text-shadow: 0 0 35px rgba(56, 189, 248, 0.8); margin-bottom: 0px; line-height: 1.1;">🌌 SPHEREx Mission: Sky Change Explorer</h1>',
    unsafe_allow_html=True
)
st.markdown(
    '<p style="font-size: 1.8rem; color: #CBD5E1; font-weight: 700; letter-spacing: 0.5px; margin-top: 8px; margin-bottom: 25px;">Near-Infrared Time-Series Sky Survey</p>',
    unsafe_allow_html=True
)

#siderbar controls
st.sidebar.markdown("### 🎛️ Observation Controls")
selected_band = st.sidebar.radio(
    "Select Near-Infrared Band:",
    ["Band 1 (0.75 - 1.1 µm)", "Band 2 (1.1 - 1.6 µm)", "Band 3 (1.6 - 2.4 µm)"]
)

time_epoch = st.sidebar.slider("Select Mission Timeline (Months)", 1, 24, 2)

st.sidebar.markdown("---")
st.sidebar.markdown("✨ **Status:** Nominal Survey Ops")
st.sidebar.markdown("🚀 **Telescope:** SPHEREx NIR")

#dashboard
col1, col2 = st.columns([1.1, 0.9])

with col1:
    st.markdown(f'<p class="section-header">🔭 Sky View Grid (Epoch {time_epoch})</p>', unsafe_allow_html=True)
    st.markdown(f"Wavelength Region: **{selected_band}**")
    
    # Styled Matplotlib Plot with Dark Theme Background
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(6, 5.2))
    fig.patch.set_facecolor('#0B0F19')
    fig.patch.set_alpha(0.8)
    ax.set_facecolor('#0B0F19')
    
    np.random.seed(time_epoch * 7)
    sky_data = np.random.randn(100, 100) * (time_epoch * 0.8)
    
    cax = ax.imshow(sky_data, cmap='inferno', origin='lower')
    ax.axis('off')
    
    cbar = fig.colorbar(cax, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label('Flux Intensity (MJy/sr)', rotation=270, labelpad=15, color='#FFFFFF')
    
    st.pyplot(fig)

with col2:
    st.markdown('<p class="section-header">📊 Temporal Analysis & Tracking</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="cosmic-card">
        <h4 style="margin-top:0; color:#38BDF8; font-family:'Orbitron', sans-serif; font-size:1.1rem;">🛰️ Target Object Metadata</h4>
        <b>Target ID:</b> SPX-2026-ObjectA<br>
        <b>Status:</b> <span style="color:#4ADE80; font-weight:bold;">● Active Tracking</span><br>
        <b>Classification:</b> High-Latitude Transient Source<br>
        <b>Coordinates:</b> 18h 36m 56s | +38° 47' 01"
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='color:#E2E8F0; font-size:0.95rem;'><b>Observation Notes:</b> Positional flux variance detected across survey intervals, indicating potential variable stellar activity or moving cosmic bodies.</p>", unsafe_allow_html=True)

    fig2, ax2 = plt.subplots(figsize=(6, 3.0))
    fig2.patch.set_facecolor('#0B0F19')
    fig2.patch.set_alpha(0.8)
    ax2.set_facecolor('#0B0F19')
    
    months = np.arange(1, 25)
    flux_values = np.sin(months / 3) * 4 + 22 + np.random.normal(0, 0.3, 24)
    
    ax2.plot(months, flux_values, marker='o', color='#38BDF8', linewidth=2, markersize=5)
    ax2.set_xlabel("Mission Timeline (Months)", fontsize=9, color='#CBD5E1')
    ax2.set_ylabel("Brightness / Flux", fontsize=9, color='#CBD5E1')
    ax2.set_title("Light Curve Variation Over Time", fontsize=10, color='#C084FC', pad=8)
    ax2.grid(True, linestyle='--', alpha=0.2, color='#CBD5E1')
    ax2.tick_params(colors='#CBD5E1', labelsize=8)
    
    st.pyplot(fig2)
