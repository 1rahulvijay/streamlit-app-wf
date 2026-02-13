"""
BizView Executive Dashboard - ULTRA PREMIUM EDITION v7.0
Enterprise-Grade Streamlit Application with:
- Animated Loading Screen with Logo Reveal & Progress Bar
- Icon-Only Sidebar Collapse Mode
- Rich & Expressive Animations (400ms)
- Deep Navy Blue Premium Theme
- Fixed Top Padding & KPI Alignment
- Smooth Sidebar Open/Close Animation
- React/Next.js Enterprise Dashboard Feel
- 8K Typography & Visual Quality
"""

import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from datetime import datetime
import io
import math
import time

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="BizView Executive Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================================
# LOADING SCREEN - PREMIUM ANIMATED LOGO REVEAL
# ============================================================================
if "loaded" not in st.session_state:
    st.session_state.loaded = False

if not st.session_state.loaded:
    loading_placeholder = st.empty()

    loading_placeholder.markdown(
        """
    <style>
        /* Hide everything during loading */
        [data-testid="stSidebar"] { display: none !important; }
        .main .block-container { padding: 0 !important; }
        [data-testid="stHeader"] { display: none !important; }
        
        /* Loading screen styles */
        .loading-screen {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, #020617 0%, #0f172a 40%, #1e293b 100%);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            z-index: 999999;
            overflow: hidden;
        }
        
        /* Animated background mesh */
        .loading-screen::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: 
                radial-gradient(circle at 20% 20%, rgba(59, 130, 246, 0.15) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(139, 92, 246, 0.12) 0%, transparent 50%),
                radial-gradient(circle at 50% 50%, rgba(6, 182, 212, 0.08) 0%, transparent 50%);
            animation: meshRotate 20s linear infinite;
        }
        
        @keyframes meshRotate {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        /* Logo container */
        .logo-container {
            position: relative;
            z-index: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            animation: logoReveal 1.2s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
        }
        
        @keyframes logoReveal {
            0% {
                opacity: 0;
                transform: translateY(40px) scale(0.8);
                filter: blur(10px);
            }
            50% {
                opacity: 1;
                filter: blur(0);
            }
            100% {
                opacity: 1;
                transform: translateY(0) scale(1);
                filter: blur(0);
            }
        }
        
        /* Logo icon */
        .logo-icon {
            width: 100px;
            height: 100px;
            background: linear-gradient(145deg, #3b82f6 0%, #8b5cf6 50%, #06b6d4 100%);
            border-radius: 28px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3.5rem;
            margin-bottom: 2rem;
            box-shadow: 
                0 20px 60px rgba(59, 130, 246, 0.4),
                0 0 0 1px rgba(255, 255, 255, 0.1),
                inset 0 1px 0 rgba(255, 255, 255, 0.2);
            animation: iconPulse 2s ease-in-out infinite, iconFloat 3s ease-in-out infinite;
        }
        
        @keyframes iconPulse {
            0%, 100% { box-shadow: 0 20px 60px rgba(59, 130, 246, 0.4), 0 0 0 1px rgba(255, 255, 255, 0.1); }
            50% { box-shadow: 0 25px 80px rgba(59, 130, 246, 0.6), 0 0 0 1px rgba(255, 255, 255, 0.2); }
        }
        
        @keyframes iconFloat {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        
        /* Brand text */
        .brand-text {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            font-size: 2.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #ffffff 0%, rgba(255,255,255,0.8) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -0.04em;
            margin-bottom: 0.5rem;
            animation: textReveal 1s ease-out 0.3s both;
        }
        
        @keyframes textReveal {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        
        .brand-subtitle {
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            color: rgba(148, 163, 184, 0.9);
            font-weight: 500;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            animation: textReveal 1s ease-out 0.5s both;
        }
        
        /* Progress bar container */
        .progress-container {
            width: 280px;
            margin-top: 3rem;
            animation: textReveal 1s ease-out 0.7s both;
        }
        
        .progress-label {
            font-family: 'Inter', sans-serif;
            font-size: 0.75rem;
            color: rgba(148, 163, 184, 0.7);
            text-align: center;
            margin-bottom: 1rem;
            letter-spacing: 0.05em;
        }
        
        .progress-bar-bg {
            width: 100%;
            height: 4px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 100px;
            overflow: hidden;
            position: relative;
        }
        
        .progress-bar-fill {
            height: 100%;
            background: linear-gradient(90deg, #3b82f6, #8b5cf6, #06b6d4);
            background-size: 200% 100%;
            border-radius: 100px;
            animation: progressFill 2s ease-out forwards, gradientMove 2s linear infinite;
        }
        
        @keyframes progressFill {
            0% { width: 0%; }
            100% { width: 100%; }
        }
        
        @keyframes gradientMove {
            0% { background-position: 0% 50%; }
            100% { background-position: 200% 50%; }
        }
        
        /* Spinner dots */
        .spinner-dots {
            display: flex;
            gap: 8px;
            margin-top: 2rem;
            animation: textReveal 1s ease-out 0.9s both;
        }
        
        .spinner-dot {
            width: 8px;
            height: 8px;
            background: #3b82f6;
            border-radius: 50%;
            animation: dotBounce 1.4s ease-in-out infinite;
        }
        
        .spinner-dot:nth-child(1) { animation-delay: 0s; }
        .spinner-dot:nth-child(2) { animation-delay: 0.2s; }
        .spinner-dot:nth-child(3) { animation-delay: 0.4s; }
        
        @keyframes dotBounce {
            0%, 80%, 100% { transform: scale(0.6); opacity: 0.5; }
            40% { transform: scale(1); opacity: 1; }
        }
    </style>
    
    <div class="loading-screen">
        <div class="logo-container">
            <div class="logo-icon">📊</div>
            <div class="brand-text">BizView</div>
            <div class="brand-subtitle">Executive Dashboard</div>
            <div class="progress-container">
                <div class="progress-label">Initializing your workspace...</div>
                <div class="progress-bar-bg">
                    <div class="progress-bar-fill"></div>
                </div>
            </div>
            <div class="spinner-dots">
                <div class="spinner-dot"></div>
                <div class="spinner-dot"></div>
                <div class="spinner-dot"></div>
            </div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    time.sleep(2.5)
    st.session_state.loaded = True
    loading_placeholder.empty()
    st.rerun()

# ============================================================================
# PREMIUM CSS - ULTRA MODERN DESIGN SYSTEM v7.0
# Icon-Only Sidebar Collapse + Rich Animations + Deep Navy Theme
# ============================================================================
st.markdown(
    """
<style>
    /* ========== 8K PREMIUM FONTS ========== */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Outfit:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

    /* ========== CSS VARIABLES - DESIGN TOKENS ========== */
    :root {
        /* Primary Colors - Deep Navy Palette */
        --navy-950: #020617;
        --navy-900: #0f172a;
        --navy-800: #1e293b;
        --navy-700: #334155;
        --navy-600: #475569;
        --navy-500: #64748b;

        /* Accent Colors - Vibrant & Crisp */
        --blue-400: #60a5fa;
        --blue-500: #3b82f6;
        --blue-600: #2563eb;
        --cyan-400: #22d3ee;
        --cyan-500: #06b6d4;
        --emerald-400: #34d399;
        --emerald-500: #10b981;
        --amber-400: #fbbf24;
        --amber-500: #f59e0b;
        --rose-400: #fb7185;
        --rose-500: #f43f5e;
        --violet-400: #a78bfa;
        --violet-500: #8b5cf6;
        --indigo-500: #6366f1;

        /* Neutral Colors */
        --white: #ffffff;
        --gray-50: #f8fafc;
        --gray-100: #f1f5f9;
        --gray-200: #e2e8f0;
        --gray-300: #cbd5e1;
        --gray-400: #94a3b8;
        --gray-500: #64748b;
        --gray-600: #475569;

        /* Premium Shadows - Layered Depth */
        --shadow-xs: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
        --shadow-sm: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1);
        --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
        --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
        --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
        --shadow-2xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
        --shadow-glow-blue: 0 0 40px rgba(59, 130, 246, 0.4);
        --shadow-glow-cyan: 0 0 40px rgba(6, 182, 212, 0.4);
        --shadow-glow-violet: 0 0 40px rgba(139, 92, 246, 0.4);

        /* Animation Timing - Rich & Expressive */
        --timing-smooth: 400ms cubic-bezier(0.34, 1.56, 0.64, 1);
        --timing-bounce: 500ms cubic-bezier(0.68, -0.55, 0.265, 1.55);
        --timing-ease: 400ms ease-out;
    }

    /* ========== GLOBAL RESETS - 8K CLARITY ========== */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
        -webkit-font-smoothing: antialiased !important;
        -moz-osx-font-smoothing: grayscale !important;
        text-rendering: optimizeLegibility !important;
        box-sizing: border-box !important;
    }

    /* ========== HIDE STREAMLIT BRANDING ========== */
    #MainMenu, footer, .stDeployButton {
        visibility: hidden !important;
        height: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    [data-testid="stToolbar"] { display: none !important; }

    [data-testid="stHeader"] {
        background: transparent !important;
        height: 0 !important;
        min-height: 0 !important;
        overflow: visible !important;
        pointer-events: none !important;
    }

    [data-testid="stHeader"] button { pointer-events: auto !important; }

    /* ========== SIDEBAR TOGGLE BUTTON - ALWAYS VISIBLE ========== */
    [data-testid="collapsedControl"],
    button[kind="header"],
    .st-emotion-cache-1dp5vir,
    [data-testid="stSidebarCollapsedControl"],
    [data-testid="baseButton-header"] {
        position: fixed !important;
        top: 1rem !important;
        left: 1rem !important;
        z-index: 999999 !important;
        background: linear-gradient(145deg, #0f172a 0%, #1e293b 100%) !important;
        border: 1px solid rgba(59, 130, 246, 0.4) !important;
        border-radius: 14px !important;
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.4),
            0 0 0 1px rgba(255, 255, 255, 0.05),
            0 0 30px rgba(59, 130, 246, 0.25) !important;
        padding: 0.75rem !important;
        width: 3rem !important;
        height: 3rem !important;
        min-width: 3rem !important;
        min-height: 3rem !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        opacity: 1 !important;
        visibility: visible !important;
        cursor: pointer !important;
        transition: all var(--timing-smooth) !important;
        backdrop-filter: blur(16px) !important;
    }

    [data-testid="collapsedControl"]:hover,
    button[kind="header"]:hover,
    [data-testid="baseButton-header"]:hover {
        background: linear-gradient(145deg, #1e293b 0%, #334155 100%) !important;
        transform: scale(1.15) rotate(5deg) !important;
        box-shadow: 
            0 16px 48px rgba(0, 0, 0, 0.5),
            0 0 0 1px rgba(255, 255, 255, 0.1),
            0 0 40px rgba(59, 130, 246, 0.5) !important;
        border-color: rgba(59, 130, 246, 0.7) !important;
    }

    [data-testid="collapsedControl"] svg,
    button[kind="header"] svg,
    [data-testid="baseButton-header"] svg {
        color: #ffffff !important;
        width: 1.5rem !important;
        height: 1.5rem !important;
        stroke-width: 2.5 !important;
        filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.3)) !important;
        transition: transform var(--timing-smooth) !important;
    }

    [data-testid="collapsedControl"]:hover svg {
        transform: rotate(180deg) !important;
    }

    /* ========== MAIN APP BACKGROUND ========== */
    .stApp {
        background: linear-gradient(180deg, #ffffff 0%, #f8fafc 50%, #f1f5f9 100%) !important;
    }

    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: 
            radial-gradient(at 0% 0%, rgba(59, 130, 246, 0.08) 0%, transparent 50%),
            radial-gradient(at 100% 0%, rgba(139, 92, 246, 0.08) 0%, transparent 50%),
            radial-gradient(at 100% 100%, rgba(6, 182, 212, 0.08) 0%, transparent 50%),
            radial-gradient(at 0% 100%, rgba(16, 185, 129, 0.08) 0%, transparent 50%);
        pointer-events: none;
        z-index: 0;
    }

    /* ========== MAIN CONTENT - ZERO TOP PADDING ========== */
    .main .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 2rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 100% !important;
        margin: 0 auto !important;
        position: relative !important;
        z-index: 1 !important;
        min-height: 100vh !important;
        animation: contentFadeIn 0.8s ease-out !important;
    }

    /* Adjust main content when sidebar is visible */
    .main {
        margin-left: 0 !important;
        padding-left: 0 !important;
    }

    @keyframes contentFadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    .main > div:first-child {
        padding-top: 0 !important;
        margin-top: 0 !important;
    }

    [data-testid="stVerticalBlock"] {
        gap: 0.75rem !important;
    }

    [data-testid="stAppViewContainer"] {
        padding-top: 0 !important;
    }

    /* ========== COLUMN ALIGNMENT ========== */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        align-items: stretch !important;
        gap: 1.25rem !important;
        margin-top: 0 !important;
        flex-wrap: nowrap !important;
    }

    [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
        display: flex !important;
        flex-direction: column !important;
        flex: 1 !important;
        min-width: 0 !important;
    }

    /* ========== SIDEBAR - ICON-ONLY COLLAPSE MODE ========== */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #020617 0%, #0a1628 30%, #0f172a 70%, #0a1628 100%) !important;
        border-right: 1px solid rgba(59, 130, 246, 0.15) !important;
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        height: 100vh !important;
        overflow-y: auto !important;
        overflow-x: hidden !important;
        z-index: 100 !important;
        backdrop-filter: blur(24px) saturate(200%) !important;
        box-shadow: 
            4px 0 40px rgba(0, 0, 0, 0.3),
            1px 0 0 rgba(59, 130, 246, 0.1) !important;
        transition: 
            width var(--timing-smooth),
            transform var(--timing-smooth),
            opacity var(--timing-ease),
            box-shadow var(--timing-ease) !important;
        will-change: width, transform !important;
        width: 240px !important;
        min-width: 240px !important;
    }

    /* Premium texture overlay */
    [data-testid="stSidebar"]::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: 
            radial-gradient(ellipse at top right, rgba(59, 130, 246, 0.1) 0%, transparent 60%),
            radial-gradient(ellipse at bottom left, rgba(139, 92, 246, 0.08) 0%, transparent 60%);
        pointer-events: none;
        z-index: 0;
    }

    /* Animated border glow */
    [data-testid="stSidebar"]::after {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 2px;
        height: 100%;
        background: linear-gradient(180deg, 
            transparent 0%, 
            rgba(59, 130, 246, 0.5) 30%, 
            rgba(139, 92, 246, 0.5) 50%, 
            rgba(6, 182, 212, 0.5) 70%, 
            transparent 100%);
        opacity: 0;
        transition: opacity var(--timing-ease);
    }

    [data-testid="stSidebar"]:hover::after {
        opacity: 1;
    }

    /* Sidebar collapsed state - icon only mode */
    [data-testid="stSidebar"][aria-expanded="false"] {
        width: 80px !important;
        min-width: 80px !important;
    }

    [data-testid="stSidebar"][aria-expanded="false"] .sidebar-text {
        opacity: 0 !important;
        width: 0 !important;
        overflow: hidden !important;
    }

    /* Sidebar content */
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        padding-bottom: 1.5rem !important;
        position: relative;
        z-index: 1;
    }

    [data-testid="stSidebarContent"],
    [data-testid="stSidebarUserContent"] {
        padding-top: 0 !important;
        margin-top: 0 !important;
    }

    /* Sidebar Typography */
    [data-testid="stSidebar"] .stMarkdown,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label {
        color: rgba(255, 255, 255, 0.92) !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 500 !important;
        letter-spacing: -0.01em !important;
    }

    /* ========== SIDEBAR NAVIGATION BUTTONS - PREMIUM STYLE ========== */
    [data-testid="stSidebar"] .stButton > button {
        width: 100% !important;
        background: rgba(255, 255, 255, 0.03) !important;
        color: #94a3b8 !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        border-radius: 12px !important;
        padding: 0.875rem 1rem !important;
        margin: 0.25rem 0 !important;
        font-size: 0.875rem !important;
        font-weight: 500 !important;
        text-align: left !important;
        display: flex !important;
        justify-content: flex-start !important;
        align-items: center !important;
        transition: all var(--timing-smooth) !important;
        position: relative !important;
        overflow: hidden !important;
    }

    /* Shimmer effect on hover */
    [data-testid="stSidebar"] .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(59, 130, 246, 0.15), transparent);
        transition: left 0.6s ease;
    }

    [data-testid="stSidebar"] .stButton > button:hover {
        background: rgba(59, 130, 246, 0.15) !important;
        color: #f8fafc !important;
        border-color: rgba(59, 130, 246, 0.4) !important;
        transform: translateX(8px) scale(1.02) !important;
        box-shadow: 
            0 8px 24px rgba(59, 130, 246, 0.2),
            0 0 0 1px rgba(59, 130, 246, 0.1) !important;
    }

    [data-testid="stSidebar"] .stButton > button:hover::before {
        left: 100%;
    }

    /* Active state with glow */
    [data-testid="stSidebar"] .stButton > button[kind="primary"] {
        background: linear-gradient(90deg, rgba(59, 130, 246, 0.3) 0%, rgba(59, 130, 246, 0.1) 100%) !important;
        color: #ffffff !important;
        border-left: 4px solid #3b82f6 !important;
        border-radius: 4px 12px 12px 4px !important;
        padding-left: 1.25rem !important;
        box-shadow: 
            0 8px 32px rgba(59, 130, 246, 0.25),
            inset 0 1px 0 rgba(255, 255, 255, 0.1),
            0 0 0 1px rgba(59, 130, 246, 0.2) !important;
        font-weight: 600 !important;
        animation: activeGlow 2s ease-in-out infinite;
    }

    @keyframes activeGlow {
        0%, 100% { box-shadow: 0 8px 32px rgba(59, 130, 246, 0.25), 0 0 0 1px rgba(59, 130, 246, 0.2); }
        50% { box-shadow: 0 8px 40px rgba(59, 130, 246, 0.4), 0 0 0 1px rgba(59, 130, 246, 0.3); }
    }

    /* ========== 8K TYPOGRAPHY ========== */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: -0.03em !important;
        color: var(--navy-900) !important;
        margin-top: 0 !important;
    }

    h1 {
        font-size: 2.5rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 40%, #334155 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.1 !important;
        padding-top: 0 !important;
        margin-bottom: 0.5rem !important;
        animation: titleReveal 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
    }

    @keyframes titleReveal {
        0% { opacity: 0; transform: translateY(-20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    h2 { font-size: 1.875rem !important; line-height: 1.2 !important; }
    h3 { font-size: 1.5rem !important; line-height: 1.3 !important; }
    h4 { font-size: 1.125rem !important; line-height: 1.4 !important; }

    /* ========== KPI CARDS - GLASSMORPHISM WITH RICH ANIMATIONS ========== */
    .kpi-card {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.98) 0%, rgba(255, 255, 255, 0.92) 100%);
        backdrop-filter: blur(40px) saturate(200%);
        -webkit-backdrop-filter: blur(40px) saturate(200%);
        border: 1px solid rgba(255, 255, 255, 0.8);
        border-radius: 20px;
        padding: 1.5rem;
        position: relative;
        overflow: hidden;
        transition: all var(--timing-smooth) !important;
        box-shadow: 
            0 4px 24px rgba(0, 0, 0, 0.06),
            0 1px 6px rgba(0, 0, 0, 0.04),
            inset 0 1px 0 rgba(255, 255, 255, 0.9);
        animation: kpiEntrance 0.7s cubic-bezier(0.34, 1.56, 0.64, 1) both;
        will-change: transform, box-shadow;
        flex: 1 !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
        min-height: 140px;
        max-height: 180px;
    }

    /* Glass reflection */
    .kpi-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 50%;
        background: linear-gradient(180deg, rgba(255, 255, 255, 0.8) 0%, rgba(255, 255, 255, 0) 100%);
        opacity: 0.5;
        pointer-events: none;
        border-radius: 20px 20px 0 0;
    }

    /* Animated accent bar */
    .kpi-card::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6, #06b6d4, #10b981, #3b82f6);
        background-size: 400% 100%;
        opacity: 0;
        transition: opacity var(--timing-ease);
        border-radius: 20px 20px 0 0;
    }

    .kpi-card:hover {
        transform: translateY(-14px) scale(1.03) !important;
        box-shadow: 
            0 24px 60px rgba(59, 130, 246, 0.2),
            0 12px 24px rgba(0, 0, 0, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 1),
            0 0 0 1px rgba(59, 130, 246, 0.15) !important;
        border-color: rgba(59, 130, 246, 0.4) !important;
    }

    .kpi-card:hover::after {
        opacity: 1;
        animation: gradientShift 3s linear infinite;
    }

    @keyframes gradientShift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }

    @keyframes kpiEntrance {
        0% {
            opacity: 0;
            transform: translateY(20px) scale(0.95);
            filter: blur(4px);
        }
        60% {
            opacity: 1;
            transform: translateY(-5px) scale(1.02);
            filter: blur(0);
        }
        100% {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }

    /* Icon wrapper with glow */
    .kpi-icon-wrapper {
        width: 48px;
        height: 48px;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        transition: all var(--timing-smooth);
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.12);
        flex-shrink: 0;
    }

    .kpi-icon-wrapper::after {
        content: '';
        position: absolute;
        inset: -2px;
        border-radius: 16px;
        background: linear-gradient(135deg, rgba(255,255,255,0.8), rgba(255,255,255,0.1));
        -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        padding: 2px;
        opacity: 0;
        transition: opacity var(--timing-ease);
    }

    .kpi-card:hover .kpi-icon-wrapper {
        transform: scale(1.15) rotate(8deg);
    }

    .kpi-card:hover .kpi-icon-wrapper::after {
        opacity: 1;
    }

    .kpi-icon-wrapper.success {
        background: linear-gradient(145deg, #d1fae5 0%, #a7f3d0 100%);
        box-shadow: 0 8px 24px rgba(16, 185, 129, 0.4);
    }

    .kpi-icon-wrapper.warning {
        background: linear-gradient(145deg, #fed7aa 0%, #fdba74 100%);
        box-shadow: 0 8px 24px rgba(245, 158, 11, 0.4);
    }

    .kpi-icon-wrapper.error {
        background: linear-gradient(145deg, #fecaca 0%, #fca5a5 100%);
        box-shadow: 0 8px 24px rgba(239, 68, 68, 0.4);
    }

    .kpi-icon-wrapper.info {
        background: linear-gradient(145deg, #dbeafe 0%, #bfdbfe 100%);
        box-shadow: 0 8px 24px rgba(59, 130, 246, 0.4);
    }

    .kpi-icon {
        font-size: 1.5rem;
        filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.15));
        animation: iconFloat 4s ease-in-out infinite;
    }

    @keyframes iconFloat {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        25% { transform: translateY(-4px) rotate(3deg); }
        75% { transform: translateY(-4px) rotate(-3deg); }
    }

    /* KPI Value - count up animation ready */
    .kpi-value {
        font-family: 'Outfit', sans-serif !important;
        font-size: 2.25rem !important;
        font-weight: 900 !important;
        line-height: 1 !important;
        letter-spacing: -0.04em !important;
        background: linear-gradient(145deg, #0f172a 0%, #1e293b 40%, #475569 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0.5rem 0;
        animation: valueReveal 0.9s cubic-bezier(0.34, 1.56, 0.64, 1);
    }

    @keyframes valueReveal {
        0% { opacity: 0; transform: translateY(15px) scale(0.9); filter: blur(8px); }
        60% { opacity: 1; transform: translateY(-3px) scale(1.03); filter: blur(0); }
        100% { opacity: 1; transform: translateY(0) scale(1); }
    }

    .kpi-label {
        font-size: 0.75rem;
        font-weight: 700;
        color: #94a3b8;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-top: 0;
    }

    /* Change indicator badge */
    .kpi-change {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        padding: 0.4rem 0.875rem;
        border-radius: 100px;
        font-size: 0.8125rem;
        font-weight: 700;
        margin-top: 0.625rem;
        transition: all var(--timing-smooth);
        animation: badgeSlide 0.6s ease-out 0.4s backwards;
    }

    @keyframes badgeSlide {
        from { opacity: 0; transform: translateX(12px); }
        to { opacity: 1; transform: translateX(0); }
    }

    .kpi-change-positive {
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        color: #065f46;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
    }

    .kpi-change-negative {
        background: linear-gradient(135deg, #fecaca 0%, #fca5a5 100%);
        color: #991b1b;
        box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3);
    }

    .kpi-change:hover {
        transform: scale(1.08);
    }

    /* ========== CHART CARDS ========== */
    .chart-card {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.98) 0%, rgba(255, 255, 255, 0.94) 100%);
        backdrop-filter: blur(40px) saturate(200%);
        border: 1px solid rgba(255, 255, 255, 0.8);
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 
            0 4px 24px rgba(0, 0, 0, 0.06),
            0 1px 6px rgba(0, 0, 0, 0.04),
            inset 0 1px 0 rgba(255, 255, 255, 0.9);
        transition: all var(--timing-smooth);
        animation: cardEntrance 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) both;
        margin-bottom: 1.75rem;
        will-change: transform, box-shadow;
    }

    @keyframes cardEntrance {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .chart-card:hover {
        box-shadow: 
            0 20px 56px rgba(59, 130, 246, 0.12),
            0 8px 20px rgba(0, 0, 0, 0.06),
            inset 0 1px 0 rgba(255, 255, 255, 1),
            0 0 0 1px rgba(59, 130, 246, 0.1);
        transform: translateY(-8px);
        border-color: rgba(59, 130, 246, 0.3);
    }

    .chart-card-header {
        padding: 1.5rem 1.75rem;
        background: linear-gradient(180deg, rgba(248, 250, 252, 0.98) 0%, rgba(255, 255, 255, 0.7) 100%);
        border-bottom: 1px solid rgba(226, 232, 240, 0.7);
        position: relative;
    }

    .chart-card-header::after {
        content: '';
        position: absolute;
        bottom: -1px;
        left: 1.75rem;
        right: 1.75rem;
        height: 3px;
        background: linear-gradient(90deg, transparent, var(--blue-500), transparent);
        opacity: 0;
        transition: opacity var(--timing-ease);
    }

    .chart-card:hover .chart-card-header::after {
        opacity: 1;
    }

    .chart-card-title {
        font-family: 'Outfit', sans-serif !important;
        font-size: 0.875rem !important;
        font-weight: 800 !important;
        color: #0f172a !important;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin: 0 !important;
    }

    .chart-card-subtitle {
        font-size: 0.75rem;
        color: #94a3b8;
        margin-top: 0.375rem;
        font-weight: 500;
    }

    .chart-card-content {
        padding: 1.75rem;
    }

    /* ========== SUMMARY CARDS - PREMIUM DARK ========== */
    .summary-card {
        background: linear-gradient(145deg, #050a14 0%, #0a1628 40%, #0f172a 70%, #1e293b 100%);
        border-radius: 22px;
        padding: 2.25rem;
        position: relative;
        overflow: hidden;
        box-shadow: 
            0 24px 60px rgba(0, 0, 0, 0.3),
            0 0 0 1px rgba(59, 130, 246, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.05);
        transition: all var(--timing-smooth);
        animation: cardEntrance 0.9s cubic-bezier(0.34, 1.56, 0.64, 1) both;
        height: 100%;
    }

    .summary-card::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 100%;
        height: 200%;
        background: radial-gradient(circle, rgba(59, 130, 246, 0.2) 0%, transparent 65%);
        animation: rotateGlow 12s linear infinite;
        pointer-events: none;
    }

    .summary-card::after {
        content: '';
        position: absolute;
        bottom: -50%;
        left: -50%;
        width: 100%;
        height: 200%;
        background: radial-gradient(circle, rgba(139, 92, 246, 0.15) 0%, transparent 65%);
        animation: rotateGlow 15s linear infinite reverse;
        pointer-events: none;
    }

    @keyframes rotateGlow {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    .summary-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 
            0 32px 72px rgba(0, 0, 0, 0.35),
            0 0 0 1px rgba(59, 130, 246, 0.25),
            0 0 60px rgba(59, 130, 246, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
    }

    .summary-card-icon {
        width: 52px;
        height: 52px;
        border-radius: 16px;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(12px);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.625rem;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
        transition: all var(--timing-smooth);
        position: relative;
        z-index: 1;
    }

    .summary-card:hover .summary-card-icon {
        transform: scale(1.15) rotate(8deg);
        box-shadow: 0 12px 36px rgba(0, 0, 0, 0.25);
        background: rgba(255, 255, 255, 0.15);
    }

    .summary-card-title {
        color: #fbbf24 !important;
        font-family: 'Outfit', sans-serif !important;
        font-weight: 800 !important;
        font-size: 1.1875rem !important;
        margin-bottom: 0.875rem !important;
        letter-spacing: -0.02em;
        position: relative;
        z-index: 1;
    }

    .summary-card-content {
        font-size: 0.9375rem;
        line-height: 1.75;
        color: rgba(255, 255, 255, 0.85);
        margin-bottom: 1.5rem;
        position: relative;
        z-index: 1;
    }

    .summary-metric {
        padding-top: 1.5rem;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: relative;
        z-index: 1;
    }

    .summary-metric-value {
        font-family: 'Outfit', sans-serif !important;
        font-size: 2.25rem !important;
        font-weight: 900 !important;
        background: linear-gradient(135deg, #ffffff 0%, rgba(255,255,255,0.75) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .summary-metric-label {
        font-size: 0.75rem;
        color: rgba(255, 255, 255, 0.5);
        text-transform: uppercase;
        letter-spacing: 0.12em;
        font-weight: 600;
    }

    /* ========== INSIGHT CARDS ========== */
    .insight-card {
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(24px);
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 1.75rem;
        transition: all var(--timing-smooth);
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
        animation: cardEntrance 0.7s cubic-bezier(0.34, 1.56, 0.64, 1) both;
        height: 100%;
    }

    .insight-card:hover {
        box-shadow: 
            0 16px 48px rgba(0, 0, 0, 0.1),
            0 0 0 1px rgba(59, 130, 246, 0.1);
        transform: translateY(-6px);
        border-color: #3b82f6;
    }

    .insight-card h4 {
        font-size: 0.75rem !important;
        font-weight: 700 !important;
        color: #64748b !important;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        margin-bottom: 0.875rem !important;
    }

    .insight-value {
        font-family: 'Outfit', sans-serif !important;
        font-size: 2.5rem !important;
        font-weight: 900 !important;
        letter-spacing: -0.03em;
        line-height: 1;
    }

    .insight-label {
        font-size: 0.875rem;
        color: #64748b;
        margin-top: 0.5rem;
        font-weight: 500;
    }

    /* ========== BADGES ========== */
    .badge {
        display: inline-flex;
        align-items: center;
        padding: 0.5rem 1rem;
        border-radius: 100px;
        font-size: 0.8125rem;
        font-weight: 700;
        letter-spacing: 0.02em;
        transition: all var(--timing-smooth);
    }

    .badge:hover {
        transform: scale(1.08);
    }

    .badge-success {
        background: linear-gradient(135deg, #d1fae5, #a7f3d0);
        color: #065f46;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.25);
    }

    .badge-warning {
        background: linear-gradient(135deg, #fef3c7, #fde68a);
        color: #92400e;
        box-shadow: 0 4px 12px rgba(245, 158, 11, 0.25);
    }

    .badge-error {
        background: linear-gradient(135deg, #fee2e2, #fecaca);
        color: #991b1b;
        box-shadow: 0 4px 12px rgba(239, 68, 68, 0.25);
    }

    .badge-info {
        background: linear-gradient(135deg, #dbeafe, #bfdbfe);
        color: #1e40af;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.25);
    }

    /* ========== BUTTONS ========== */
    .stButton > button {
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        border-radius: 12px !important;
        padding: 0.75rem 1.5rem !important;
        transition: all var(--timing-smooth) !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1) !important;
    }

    .stButton > button:hover {
        transform: translateY(-4px) !important;
        box-shadow: 0 12px 32px rgba(0, 0, 0, 0.15) !important;
    }

    .stDownloadButton > button {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%) !important;
        color: white !important;
        border: none !important;
    }

    .stDownloadButton > button:hover {
        box-shadow: 0 16px 40px rgba(15, 23, 42, 0.4) !important;
    }

    /* ========== TABLES ========== */
    .aesthetic-table-container {
        background: rgba(255, 255, 255, 0.9) !important;
        backdrop-filter: blur(24px) !important;
        border: 1px solid rgba(255, 255, 255, 0.6) !important;
        border-radius: 20px !important;
        padding: 1rem !important;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.04) !important;
        margin-bottom: 1.75rem !important;
        transition: all var(--timing-smooth) !important;
    }

    .aesthetic-table-container:hover {
        transform: translateY(-4px);
        box-shadow: 0 20px 48px rgba(0, 0, 0, 0.08) !important;
    }

    .dataframe, [data-testid="stDataFrame"], [data-testid="stTable"] {
        font-family: 'Inter', sans-serif !important;
        font-size: 0.875rem !important;
        border-radius: 16px !important;
        overflow: hidden !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05) !important;
        border: 1px solid #e2e8f0 !important;
    }

    .dataframe thead tr th {
        font-family: 'Outfit', sans-serif !important;
        font-size: 0.75rem !important;
        font-weight: 800 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
        color: #475569 !important;
        padding: 1.125rem 1.5rem !important;
        background: linear-gradient(90deg, #f8fafc 0%, #ffffff 100%) !important;
        border: none !important;
    }

    .dataframe tbody tr td {
        padding: 1.125rem 1.5rem !important;
        color: #0f172a !important;
        border-bottom: 1px solid #f1f5f9 !important;
        transition: all var(--timing-ease) !important;
    }

    .dataframe tbody tr:hover td {
        background-color: #f8fafc !important;
        color: #2563eb !important;
    }

    /* ========== SCROLLBAR ========== */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }

    ::-webkit-scrollbar-track {
        background: #f1f5f9;
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #3b82f6, #8b5cf6);
        border-radius: 10px;
        border: 2px solid #f1f5f9;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #2563eb, #7c3aed);
    }

    /* ========== SPACING UTILITIES ========== */
    .mt-0 { margin-top: 0 !important; }
    .mt-1 { margin-top: 0.5rem; }
    .mt-2 { margin-top: 1rem; }
    .mt-3 { margin-top: 1.5rem; }
    .mt-4 { margin-top: 2rem; }
    .mb-0 { margin-bottom: 0 !important; }
    .mb-1 { margin-bottom: 0.5rem; }
    .mb-2 { margin-bottom: 1rem; }
    .mb-3 { margin-bottom: 1.5rem; }
    .mb-4 { margin-bottom: 2rem; }

    /* ========== RESPONSIVE ========== */
    @media (max-width: 1920px) {
        .main .block-container {
            padding: 0.5rem 2rem 2rem 2rem !important;
        }
        .kpi-value { font-size: 2.5rem !important; }
    }

    @media (max-width: 1600px) {
        h1 { font-size: 2rem !important; }
        .kpi-value { font-size: 2.25rem !important; }
    }

    @media (max-width: 1400px) {
        .kpi-value { font-size: 2rem !important; }
        .kpi-card { padding: 1.5rem; }
    }

    /* ========== PRINT ========== */
    @media print {
        [data-testid="stSidebar"] { display: none !important; }
        .no-print { display: none !important; }
        .stApp { background: white !important; }
        .chart-card, .kpi-card { box-shadow: none !important; break-inside: avoid; }
    }
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================================
# COLOR PALETTE
# ============================================================================
COLORS = {
    "primary": "#3b82f6",
    "secondary": "#8b5cf6",
    "accent": "#06b6d4",
    "success": "#10b981",
    "warning": "#f59e0b",
    "error": "#ef4444",
    "navy": "#0f172a",
    "gray": "#64748b",
    "light": "#f8fafc",
}

# ============================================================================
# MOCK DATA
# ============================================================================
kpi_data = {
    "workflow_count": {
        "value": 1247,
        "change": 12.5,
        "trend": "up",
        "label": "Total Workflows",
        "icon": "📊",
    },
    "volume_gearing_ratio": {
        "value": 2.45,
        "change": 8.3,
        "trend": "up",
        "label": "Volume Gearing Ratio",
        "icon": "📈",
    },
    "productivity": {
        "value": 87.3,
        "change": 5.2,
        "trend": "up",
        "label": "Productivity Score",
        "icon": "👥",
    },
    "tech_adoption": {
        "value": 76.8,
        "change": -2.1,
        "trend": "down",
        "label": "Tech Adoption Rate",
        "icon": "💻",
    },
}

workflow_trend_data = pd.DataFrame(
    {
        "Month": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ],
        "Completed": [
            892,
            1023,
            1156,
            1089,
            1234,
            1345,
            1267,
            1423,
            1512,
            1398,
            1567,
            1689,
        ],
        "In Progress": [156, 178, 145, 167, 189, 201, 178, 212, 198, 223, 234, 245],
        "Pending": [89, 76, 92, 83, 71, 65, 78, 58, 67, 72, 54, 48],
    }
)

productivity_data = pd.DataFrame(
    {
        "Department": [
            "Engineering",
            "Sales",
            "Marketing",
            "Operations",
            "Finance",
            "HR",
            "Customer Success",
            "Product",
        ],
        "Score": [92.5, 88.3, 76.4, 91.2, 85.7, 72.8, 89.6, 94.1],
        "Target": [90, 85, 80, 88, 82, 75, 85, 90],
        "Employees": [145, 89, 67, 112, 45, 38, 56, 78],
    }
)

tech_adoption_data = pd.DataFrame(
    {
        "Tool": [
            "Slack",
            "Jira",
            "Confluence",
            "GitHub",
            "Figma",
            "Notion",
            "Zoom",
            "Google Workspace",
            "Salesforce",
            "AI Assistant",
        ],
        "Adoption": [95, 88, 72, 91, 68, 82, 97, 99, 76, 45],
        "Category": [
            "Communication",
            "Project Management",
            "Documentation",
            "Development",
            "Design",
            "Documentation",
            "Communication",
            "Productivity",
            "CRM",
            "Emerging",
        ],
    }
)

monthly_performance = pd.DataFrame(
    {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Revenue": [125000, 142000, 138000, 156000, 178000, 195000],
        "Expenses": [95000, 98000, 102000, 108000, 115000, 118000],
        "Profit": [30000, 44000, 36000, 48000, 63000, 77000],
    }
)

recent_workflows = pd.DataFrame(
    {
        "ID": ["WF-1247", "WF-1246", "WF-1245", "WF-1244", "WF-1243"],
        "Name": [
            "Q4 Report Generation",
            "Customer Onboarding",
            "Invoice Processing",
            "Data Migration",
            "Security Audit",
        ],
        "Status": ["Completed", "In Progress", "Completed", "Pending", "In Progress"],
        "Owner": ["Alice Chen", "Bob Smith", "Carol Davis", "David Lee", "Emma Wilson"],
        "Due Date": ["Dec 15", "Dec 18", "Dec 12", "Dec 20", "Dec 22"],
    }
)

executive_summaries = [
    {
        "title": "Workflow Performance",
        "icon": "📊",
        "content": "Total workflows increased by 12.5% this quarter, with automated processes now handling 68% of routine tasks. This represents a significant improvement in operational efficiency.",
        "metric_label": "Automation Rate",
        "metric_value": "68%",
    },
    {
        "title": "Team Productivity",
        "icon": "⚡",
        "content": "Average team productivity score reached 87.3%, exceeding the quarterly target of 85%. Engineering and Product teams lead with scores above 92%.",
        "metric_label": "Above Target",
        "metric_value": "6/8",
    },
    {
        "title": "Technology Stack",
        "icon": "🔧",
        "content": "Technology adoption remains strong at 76.8% overall. Communication tools lead at 97% while emerging AI tools show rapid growth at 45% adoption.",
        "metric_label": "Tools Active",
        "metric_value": "10",
    },
    {
        "title": "Financial Health",
        "icon": "💰",
        "content": "Revenue grew 15% month-over-month while maintaining controlled expense growth at 8%. Profit margins improved to 28% from 24% last quarter.",
        "metric_label": "Profit Margin",
        "metric_value": "28%",
    },
]

# ============================================================================
# SESSION STATE
# ============================================================================
if "current_page" not in st.session_state:
    st.session_state.current_page = "Dashboard"


# ============================================================================
# CHART CONFIG & LAYOUT
# ============================================================================
def get_chart_config():
    return {
        "displayModeBar": False,
        "responsive": True,
        "staticPlot": False,
    }


def get_chart_layout(height=400):
    return {
        "height": height,
        "margin": dict(l=50, r=30, t=50, b=50),
        "paper_bgcolor": "rgba(0,0,0,0)",
        "plot_bgcolor": "rgba(0,0,0,0)",
        "font": {"family": "Inter, sans-serif", "color": "#334155", "size": 12},
        "xaxis": {
            "showgrid": True,
            "gridcolor": "rgba(226, 232, 240, 0.6)",
            "gridwidth": 1,
            "tickfont": {"size": 11, "color": "#64748b"},
            "linecolor": "#e2e8f0",
            "zeroline": False,
        },
        "yaxis": {
            "showgrid": True,
            "gridcolor": "rgba(226, 232, 240, 0.6)",
            "gridwidth": 1,
            "tickfont": {"size": 11, "color": "#64748b"},
            "linecolor": "#e2e8f0",
            "zeroline": False,
        },
        "legend": {
            "orientation": "h",
            "yanchor": "bottom",
            "y": 1.02,
            "xanchor": "right",
            "x": 1,
            "font": {"size": 11},
        },
        "hovermode": "x unified",
        "hoverlabel": {
            "bgcolor": "#0f172a",
            "font_size": 12,
            "font_family": "Inter, sans-serif",
            "bordercolor": "#0f172a",
        },
    }


# ============================================================================
# CHART FUNCTIONS
# ============================================================================
def create_workflow_trend_chart(data):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=data["Month"],
            y=data["Completed"],
            name="Completed",
            mode="lines+markers",
            line=dict(color=COLORS["success"], width=3, shape="spline"),
            marker=dict(size=8, symbol="circle", line=dict(width=2, color="white")),
            fill="tozeroy",
            fillcolor="rgba(16, 185, 129, 0.1)",
            hovertemplate="<b>%{x}</b><br>Completed: %{y:,}<extra></extra>",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=data["Month"],
            y=data["In Progress"],
            name="In Progress",
            mode="lines+markers",
            line=dict(color=COLORS["primary"], width=3, shape="spline"),
            marker=dict(size=8, symbol="circle", line=dict(width=2, color="white")),
            hovertemplate="<b>%{x}</b><br>In Progress: %{y:,}<extra></extra>",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=data["Month"],
            y=data["Pending"],
            name="Pending",
            mode="lines+markers",
            line=dict(color=COLORS["warning"], width=3, shape="spline"),
            marker=dict(size=8, symbol="circle", line=dict(width=2, color="white")),
            hovertemplate="<b>%{x}</b><br>Pending: %{y:,}<extra></extra>",
        )
    )

    layout = get_chart_layout(height=380)
    fig.update_layout(**layout)
    return fig


def create_horizontal_bar_chart(data):
    colors = [
        COLORS["success"] if score >= target else COLORS["warning"]
        for score, target in zip(data["Score"], data["Target"])
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            y=data["Department"],
            x=data["Score"],
            orientation="h",
            name="Score",
            marker=dict(color=colors, line=dict(width=0), cornerradius=6),
            text=[f"{s}%" for s in data["Score"]],
            textposition="inside",
            textfont=dict(color="white", size=12, weight="bold"),
            hovertemplate="<b>%{y}</b><br>Score: %{x}%<extra></extra>",
        )
    )

    fig.add_trace(
        go.Scatter(
            y=data["Department"],
            x=data["Target"],
            mode="markers",
            name="Target",
            marker=dict(
                color="#0f172a",
                size=12,
                symbol="diamond",
                line=dict(width=2, color="white"),
            ),
            hovertemplate="<b>%{y}</b><br>Target: %{x}%<extra></extra>",
        )
    )

    layout = get_chart_layout(height=360)
    layout.update(
        {
            "barmode": "overlay",
            "xaxis": {**layout["xaxis"], "range": [0, 100], "dtick": 20},
            "yaxis": {**layout["yaxis"], "categoryorder": "total ascending"},
        }
    )
    fig.update_layout(**layout)
    return fig


def create_line_chart(data, x_col, y_col, name, color):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=data[x_col],
            y=data[y_col],
            name=name,
            mode="lines+markers",
            line=dict(color=color, width=3, shape="spline"),
            marker=dict(size=8, symbol="circle", line=dict(width=2, color="white")),
            fill="tozeroy",
            fillcolor=f"rgba{tuple(list(int(color.lstrip('#')[i : i + 2], 16) for i in (0, 2, 4)) + [0.1])}",
            hovertemplate="<b>%{x}</b><br>" + name + ": %{y:,}<extra></extra>",
        )
    )

    layout = get_chart_layout(height=350)
    fig.update_layout(**layout)
    return fig


def create_tech_adoption_chart(data):
    sorted_data = data.sort_values("Adoption", ascending=True)
    colors = [
        COLORS["success"]
        if a >= 80
        else COLORS["warning"]
        if a >= 60
        else COLORS["error"]
        for a in sorted_data["Adoption"]
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            y=sorted_data["Tool"],
            x=sorted_data["Adoption"],
            orientation="h",
            marker=dict(color=colors, line=dict(width=0), cornerradius=6),
            text=[f"{a}%" for a in sorted_data["Adoption"]],
            textposition="inside",
            textfont=dict(color="white", size=11, weight="bold"),
            hovertemplate="<b>%{y}</b><br>Adoption: %{x}%<br>Category: "
            + sorted_data["Category"]
            + "<extra></extra>",
        )
    )

    # Add threshold lines
    for threshold, label, color in [
        (80, "High", COLORS["success"]),
        (60, "Medium", COLORS["warning"]),
    ]:
        fig.add_vline(
            x=threshold, line=dict(color=color, width=2, dash="dash"), opacity=0.7
        )

    layout = get_chart_layout(height=420)
    layout.update({"xaxis": {**layout["xaxis"], "range": [0, 105], "dtick": 20}})
    fig.update_layout(**layout)
    return fig


def create_donut_chart(values, labels, colors, title=""):
    fig = go.Figure(
        data=[
            go.Pie(
                values=values,
                labels=labels,
                hole=0.65,
                marker=dict(colors=colors, line=dict(color="white", width=3)),
                textinfo="percent",
                textposition="outside",
                textfont=dict(size=12, color="#334155"),
                hovertemplate="<b>%{label}</b><br>Value: %{value:,}<br>Percent: %{percent}<extra></extra>",
                pull=[0.02] * len(values),
            )
        ]
    )

    fig.update_layout(
        height=350,
        margin=dict(l=30, r=30, t=50, b=30),
        paper_bgcolor="rgba(0,0,0,0)",
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.15,
            xanchor="center",
            x=0.5,
            font=dict(size=11),
        ),
        annotations=[
            dict(
                text=f"<b>{title}</b>",
                x=0.5,
                y=0.5,
                font_size=14,
                showarrow=False,
                font=dict(color="#0f172a"),
            )
        ],
    )
    return fig


def create_financial_chart(data):
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=data["Month"],
            y=data["Revenue"],
            name="Revenue",
            marker=dict(color=COLORS["primary"], cornerradius=4),
            hovertemplate="<b>%{x}</b><br>Revenue: $%{y:,.0f}<extra></extra>",
        )
    )

    fig.add_trace(
        go.Bar(
            x=data["Month"],
            y=data["Expenses"],
            name="Expenses",
            marker=dict(color=COLORS["warning"], cornerradius=4),
            hovertemplate="<b>%{x}</b><br>Expenses: $%{y:,.0f}<extra></extra>",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=data["Month"],
            y=data["Profit"],
            name="Profit",
            mode="lines+markers",
            line=dict(color=COLORS["success"], width=3),
            marker=dict(size=10, symbol="diamond", line=dict(width=2, color="white")),
            yaxis="y2",
            hovertemplate="<b>%{x}</b><br>Profit: $%{y:,.0f}<extra></extra>",
        )
    )

    layout = get_chart_layout(height=380)
    layout.update(
        {
            "barmode": "group",
            "yaxis2": {
                "title": "Profit ($)",
                "overlaying": "y",
                "side": "right",
                "showgrid": False,
                "tickfont": {"size": 11, "color": "#64748b"},
            },
        }
    )
    fig.update_layout(**layout)
    return fig


# ============================================================================
# COMPONENT FUNCTIONS
# ============================================================================
def render_kpi_card(
    title, value, change, trend, value_type="number", icon="📊", delay=0
):
    icon_class = "success" if trend == "up" else "error" if trend == "down" else "info"
    change_class = "kpi-change-positive" if trend == "up" else "kpi-change-negative"
    change_icon = "↑" if trend == "up" else "↓"

    if value_type == "currency":
        display_value = f"${value:,.0f}" if value >= 1000 else f"${value}"
    elif value_type == "percentage":
        display_value = f"{value}%"
    elif value_type == "ratio":
        display_value = f"{value:.2f}"
    else:
        display_value = f"{value:,}" if isinstance(value, int) else str(value)

    st.markdown(
        f"""
    <div class="kpi-card" style="animation-delay: {delay}s;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div class="kpi-icon-wrapper {icon_class}">
                <span class="kpi-icon">{icon}</span>
            </div>
            <span class="{change_class} kpi-change">{change_icon} {abs(change)}%</span>
        </div>
        <div>
            <div class="kpi-value">{display_value}</div>
            <div class="kpi-label">{title}</div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


def render_chart_header(title, subtitle=""):
    st.markdown(
        f"""
    <div class="chart-card-header">
        <h4 class="chart-card-title">{title}</h4>
        {f'<p class="chart-card-subtitle">{subtitle}</p>' if subtitle else ""}
    </div>
    """,
        unsafe_allow_html=True,
    )


def render_summary_card(summary):
    st.markdown(
        f"""
    <div class="summary-card">
        <div class="summary-card-icon">{summary["icon"]}</div>
        <div class="summary-card-title">{summary["title"]}</div>
        <div class="summary-card-content">{summary["content"]}</div>
        <div class="summary-metric">
            <div>
                <div class="summary-metric-label">{summary["metric_label"]}</div>
                <div class="summary-metric-value">{summary["metric_value"]}</div>
            </div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


def generate_html_report():
    current_date = datetime.now().strftime("%B %d, %Y")
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>BizView Executive Report - {current_date}</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@700;800;900&display=swap" rel="stylesheet">
        <style>
            * {{ font-family: 'Inter', sans-serif; box-sizing: border-box; }}
            body {{ background: linear-gradient(180deg, #f8fafc, #f1f5f9); padding: 3rem; margin: 0; }}
            .container {{ max-width: 1200px; margin: 0 auto; background: white; border-radius: 24px; padding: 3rem; box-shadow: 0 20px 60px rgba(0,0,0,0.1); }}
            .header {{ border-bottom: 3px solid #0f172a; padding-bottom: 2rem; margin-bottom: 2rem; }}
            h1 {{ font-family: 'Outfit', sans-serif; font-size: 2.5rem; color: #0f172a; margin: 0; }}
            .kpi-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.5rem; margin: 2rem 0; }}
            .kpi-box {{ background: linear-gradient(145deg, #f8fafc, #ffffff); border-radius: 16px; padding: 1.5rem; border: 1px solid #e2e8f0; text-align: center; }}
            .kpi-value {{ font-family: 'Outfit', sans-serif; font-size: 2rem; font-weight: 800; color: #0f172a; }}
            .kpi-label {{ font-size: 0.75rem; color: #64748b; text-transform: uppercase; letter-spacing: 0.1em; margin-top: 0.5rem; }}
            .kpi-change {{ font-size: 0.875rem; font-weight: 700; margin-top: 0.5rem; }}
            .positive {{ color: #10b981; }}
            .negative {{ color: #ef4444; }}
            .footer {{ text-align: center; color: #94a3b8; font-size: 0.875rem; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e2e8f0; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>📊 BizView Executive Report</h1>
                <p style="color: #64748b; margin-top: 0.5rem;">Generated on {current_date}</p>
            </div>
            <div class="kpi-grid">
                <div class="kpi-box">
                    <div class="kpi-value">1,247</div>
                    <div class="kpi-label">Total Workflows</div>
                    <div class="kpi-change positive">↑ 12.5%</div>
                </div>
                <div class="kpi-box">
                    <div class="kpi-value">2.45</div>
                    <div class="kpi-label">Gearing Ratio</div>
                    <div class="kpi-change positive">↑ 8.3%</div>
                </div>
                <div class="kpi-box">
                    <div class="kpi-value">87.3%</div>
                    <div class="kpi-label">Productivity</div>
                    <div class="kpi-change positive">↑ 5.2%</div>
                </div>
                <div class="kpi-box">
                    <div class="kpi-value">76.8%</div>
                    <div class="kpi-label">Tech Adoption</div>
                    <div class="kpi-change negative">↓ 2.1%</div>
                </div>
            </div>
            <div class="footer">
                BizView Analytics Platform • Enterprise Edition • Confidential
            </div>
        </div>
    </body>
    </html>
    """


# ============================================================================
# SIDEBAR NAVIGATION
# ============================================================================
with st.sidebar:
    st.markdown(
        """
    <div style="padding: 1.5rem 0.5rem 1rem 0.5rem; margin-bottom: 1rem;">
        <div style="display: flex; align-items: center; gap: 0.875rem;">
            <div style="width: 48px; height: 48px; background: linear-gradient(145deg, #3b82f6, #8b5cf6); 
                        border-radius: 14px; display: flex; align-items: center; justify-content: center;
                        box-shadow: 0 8px 24px rgba(59, 130, 246, 0.4);">
                <span style="font-size: 1.5rem;">📊</span>
            </div>
            <div class="sidebar-text">
                <div style="font-family: 'Outfit', sans-serif; font-size: 1.375rem; font-weight: 800; color: white; 
                            letter-spacing: -0.03em; line-height: 1.1;">BizView</div>
                <div style="font-size: 0.6875rem; color: rgba(148, 163, 184, 0.9); text-transform: uppercase; 
                            letter-spacing: 0.1em; font-weight: 600;">Executive Dashboard</div>
            </div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div style="padding: 0 0.5rem; margin-bottom: 0.75rem;">
        <p style="font-size: 0.625rem; color: rgba(148, 163, 184, 0.6); text-transform: uppercase; 
                  letter-spacing: 0.15em; font-weight: 700; margin: 0;">Navigation</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    nav_items = [
        ("📊", "Dashboard"),
        ("📈", "Workflow Analytics"),
        ("👥", "Productivity"),
        ("💻", "Tech Adoption"),
        ("📋", "Executive Summary"),
        ("📥", "Reports & Export"),
    ]

    for icon, page in nav_items:
        button_type = (
            "primary" if st.session_state.current_page == page else "secondary"
        )
        if st.button(
            f"{icon}  {page}", key=page, type=button_type, use_container_width=True
        ):
            st.session_state.current_page = page
            st.rerun()

    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
    st.markdown(
        """
    <div style="padding: 1rem; background: rgba(59, 130, 246, 0.1); border-radius: 14px; 
                border: 1px solid rgba(59, 130, 246, 0.2); margin-top: 1rem;">
        <p style="font-size: 0.6875rem; color: rgba(255, 255, 255, 0.6); margin: 0 0 0.5rem 0;">Last Updated</p>
        <p style="font-size: 0.875rem; color: white; font-weight: 600; margin: 0;">
            """
        + datetime.now().strftime("%b %d, %Y %H:%M")
        + """
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

# ============================================================================
# PAGE CONTENT
# ============================================================================

# DASHBOARD PAGE
if st.session_state.current_page == "Dashboard":
    st.markdown("# 📊 Executive Dashboard")
    st.markdown(
        "<p style='color: #64748b; font-size: 1.0625rem; margin-bottom: 2rem; margin-top: -0.25rem;'>Real-time overview of key business metrics and performance indicators</p>",
        unsafe_allow_html=True,
    )

    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card(
            "Total Workflows",
            kpi_data["workflow_count"]["value"],
            kpi_data["workflow_count"]["change"],
            "up",
            "number",
            "📊",
            0,
        )
    with col2:
        render_kpi_card(
            "Gearing Ratio",
            kpi_data["volume_gearing_ratio"]["value"],
            kpi_data["volume_gearing_ratio"]["change"],
            "up",
            "ratio",
            "📈",
            0.1,
        )
    with col3:
        render_kpi_card(
            "Productivity",
            kpi_data["productivity"]["value"],
            kpi_data["productivity"]["change"],
            "up",
            "percentage",
            "👥",
            0.2,
        )
    with col4:
        render_kpi_card(
            "Tech Adoption",
            kpi_data["tech_adoption"]["value"],
            kpi_data["tech_adoption"]["change"],
            "down",
            "percentage",
            "💻",
            0.3,
        )

    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

    # Charts Row 1
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header(
            "WORKFLOW TRENDS", "Monthly workflow completion and status overview"
        )
        st.plotly_chart(
            create_workflow_trend_chart(workflow_trend_data),
            use_container_width=True,
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header(
            "DEPARTMENT PRODUCTIVITY", "Performance score vs target comparison"
        )
        st.plotly_chart(
            create_horizontal_bar_chart(productivity_data),
            use_container_width=True,
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # Charts Row 2
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("WORKFLOW DISTRIBUTION", "Status breakdown analysis")
        total_completed = workflow_trend_data["Completed"].sum()
        total_progress = workflow_trend_data["In Progress"].sum()
        total_pending = workflow_trend_data["Pending"].sum()
        st.plotly_chart(
            create_donut_chart(
                [total_completed, total_progress, total_pending],
                ["Completed", "In Progress", "Pending"],
                [COLORS["success"], COLORS["primary"], COLORS["warning"]],
                "Status",
            ),
            use_container_width=True,
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("FINANCIAL OVERVIEW", "Revenue, expenses and profit trends")
        st.plotly_chart(
            create_financial_chart(monthly_performance),
            use_container_width=True,
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # Recent Workflows Table
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_header("RECENT WORKFLOWS", "Latest workflow activities and status")
    st.dataframe(
        recent_workflows, use_container_width=True, hide_index=True, height=250
    )
    st.markdown("</div>", unsafe_allow_html=True)

# WORKFLOW ANALYTICS PAGE
elif st.session_state.current_page == "Workflow Analytics":
    st.markdown("# 📈 Workflow Analytics")
    st.markdown(
        "<p style='color: #64748b; font-size: 1.0625rem; margin-bottom: 2rem; margin-top: -0.25rem;'>Detailed analysis of workflow performance and trends</p>",
        unsafe_allow_html=True,
    )

    total_workflows = (
        workflow_trend_data["Completed"].sum()
        + workflow_trend_data["In Progress"].sum()
        + workflow_trend_data["Pending"].sum()
    )
    completion_rate = (workflow_trend_data["Completed"].sum() / total_workflows) * 100
    avg_monthly = workflow_trend_data["Completed"].mean()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card(
            "Total Processed", total_workflows, 15.3, "up", "number", "📊", 0
        )
    with col2:
        render_kpi_card(
            "Completion Rate",
            round(completion_rate, 1),
            3.2,
            "up",
            "percentage",
            "✅",
            0.1,
        )
    with col3:
        render_kpi_card(
            "Avg Monthly", round(avg_monthly), 8.7, "up", "number", "📈", 0.2
        )
    with col4:
        render_kpi_card(
            "Peak Month",
            workflow_trend_data["Completed"].max(),
            12.1,
            "up",
            "number",
            "🏆",
            0.3,
        )

    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_header(
        "WORKFLOW VOLUME TRENDS", "12-month workflow completion analysis"
    )
    st.plotly_chart(
        create_workflow_trend_chart(workflow_trend_data),
        use_container_width=True,
        config=get_chart_config(),
    )
    st.markdown("</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("STATUS DISTRIBUTION", "Current workflow status breakdown")
        st.plotly_chart(
            create_donut_chart(
                [
                    workflow_trend_data["Completed"].sum(),
                    workflow_trend_data["In Progress"].sum(),
                    workflow_trend_data["Pending"].sum(),
                ],
                ["Completed", "In Progress", "Pending"],
                [COLORS["success"], COLORS["primary"], COLORS["warning"]],
                "Total",
            ),
            use_container_width=True,
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("MONTHLY COMPLETION TREND", "Completed workflows per month")
        st.plotly_chart(
            create_line_chart(
                workflow_trend_data,
                "Month",
                "Completed",
                "Completed",
                COLORS["success"],
            ),
            use_container_width=True,
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

# PRODUCTIVITY PAGE
elif st.session_state.current_page == "Productivity":
    st.markdown("# 👥 Productivity Analysis")
    st.markdown(
        "<p style='color: #64748b; font-size: 1.0625rem; margin-bottom: 2rem; margin-top: -0.25rem;'>Team and department productivity metrics and insights</p>",
        unsafe_allow_html=True,
    )

    avg_score = productivity_data["Score"].mean()
    on_target = (productivity_data["Score"] >= productivity_data["Target"]).sum()
    total_employees = productivity_data["Employees"].sum()
    top_dept = productivity_data.loc[productivity_data["Score"].idxmax()]

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card(
            "Avg Productivity", round(avg_score, 1), 5.2, "up", "percentage", "📈", 0
        )
    with col2:
        render_kpi_card("Depts On Target", on_target, 16.7, "up", "number", "🎯", 0.1)
    with col3:
        render_kpi_card(
            "Total Employees", total_employees, 8.4, "up", "number", "👥", 0.2
        )
    with col4:
        render_kpi_card(
            "Top Score", top_dept["Score"], 3.1, "up", "percentage", "🏆", 0.3
        )

    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("DEPARTMENT PRODUCTIVITY", "Score vs Target comparison")
        st.plotly_chart(
            create_horizontal_bar_chart(productivity_data),
            use_container_width=True,
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("PRODUCTIVITY TREND", "Monthly output progression")
        st.plotly_chart(
            create_line_chart(
                workflow_trend_data, "Month", "Completed", "Output", COLORS["primary"]
            ),
            use_container_width=True,
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # Insight Cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            f"""
        <div class="insight-card">
            <h4>TOP PERFORMER</h4>
            <div class="insight-value" style="color: {COLORS["success"]};">{top_dept["Department"]}</div>
            <div class="insight-label">{top_dept["Score"]}% productivity score</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
        <div class="insight-card">
            <h4>ACHIEVEMENT RATE</h4>
            <div class="insight-value" style="color: {COLORS["primary"]};">{int((on_target / len(productivity_data)) * 100)}%</div>
            <div class="insight-label">{on_target} out of {len(productivity_data)} departments</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
        <div class="insight-card">
            <h4>TEAM SIZE</h4>
            <div class="insight-value" style="color: {COLORS["accent"]};">{total_employees}</div>
            <div class="insight-label">Across all departments</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

# TECH ADOPTION PAGE
elif st.session_state.current_page == "Tech Adoption":
    st.markdown("# 💻 Technology Adoption")
    st.markdown(
        "<p style='color: #64748b; font-size: 1.0625rem; margin-bottom: 2rem; margin-top: -0.25rem;'>Technology stack adoption rates and utilization metrics</p>",
        unsafe_allow_html=True,
    )

    avg_adoption = tech_adoption_data["Adoption"].mean()
    high_adoption = (tech_adoption_data["Adoption"] >= 80).sum()
    low_adoption = (tech_adoption_data["Adoption"] < 60).sum()
    emerging = (tech_adoption_data["Category"] == "Emerging").sum()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card(
            "Avg Adoption", round(avg_adoption, 1), -2.1, "down", "percentage", "💻", 0
        )
    with col2:
        render_kpi_card("High Adoption", high_adoption, 12.5, "up", "number", "✅", 0.1)
    with col3:
        render_kpi_card("Low Adoption", low_adoption, -25.0, "down", "number", "⚠️", 0.2)
    with col4:
        render_kpi_card("Emerging Tech", emerging, 100, "up", "number", "🚀", 0.3)

    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_header(
        "TECHNOLOGY ADOPTION ANALYSIS", "Adoption rates with performance thresholds"
    )
    st.plotly_chart(
        create_tech_adoption_chart(tech_adoption_data),
        use_container_width=True,
        config=get_chart_config(),
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_header(
        "TECHNOLOGY STACK DETAILS", "Complete tool inventory with adoption metrics"
    )
    styled_data = tech_adoption_data.copy()
    styled_data["Status"] = styled_data["Adoption"].apply(
        lambda x: "🟢 High" if x >= 80 else "🟡 Medium" if x >= 60 else "🔴 Low"
    )
    st.dataframe(styled_data, use_container_width=True, hide_index=True, height=400)
    st.markdown("</div>", unsafe_allow_html=True)

# EXECUTIVE SUMMARY PAGE
elif st.session_state.current_page == "Executive Summary":
    current_date = datetime.now().strftime("%A, %B %d, %Y")

    st.markdown(
        f"""
    <div style="background: linear-gradient(145deg, #050a14 0%, #0a1628 40%, #0f172a 70%, #1e293b 100%);
                color: white; border-radius: 26px; padding: 3rem; margin-bottom: 2.5rem;
                position: relative; overflow: hidden;
                box-shadow: 0 32px 72px rgba(0,0,0,0.35), 0 0 0 1px rgba(59, 130, 246, 0.15);">
        <div style="position: absolute; top: -50%; right: -20%; width: 60%; height: 200%;
                    background: radial-gradient(circle, rgba(59, 130, 246, 0.2) 0%, transparent 65%);
                    animation: rotateGlow 12s linear infinite;"></div>
        <div style="position: absolute; bottom: -50%; left: -20%; width: 60%; height: 200%;
                    background: radial-gradient(circle, rgba(139, 92, 246, 0.15) 0%, transparent 65%);
                    animation: rotateGlow 15s linear infinite reverse;"></div>
        <div style="position: relative; z-index: 1;">
            <p style="color: #fbbf24; font-size: 0.75rem; font-weight: 700; letter-spacing: 0.15em; margin-bottom: 1rem; text-transform: uppercase;">
                📅 {current_date}
            </p>
            <h1 style="color: white !important; margin-bottom: 1rem; font-size: 2.5rem; font-weight: 900; letter-spacing: -0.04em;">
                Executive Summary Report
            </h1>
            <p style="color: rgba(255,255,255,0.85); max-width: 800px; line-height: 1.8; font-size: 1.0625rem;">
                Comprehensive overview of organizational performance metrics, highlighting key achievements,
                strategic insights, and actionable recommendations for continued growth and excellence.
            </p>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Quick Stats
    col1, col2, col3, col4 = st.columns(4)
    stats = [
        (
            "📊",
            f"{kpi_data['workflow_count']['value']:,}",
            "Total Workflows",
            COLORS["navy"],
        ),
        (
            "📈",
            str(kpi_data["volume_gearing_ratio"]["value"]),
            "Gearing Ratio",
            COLORS["primary"],
        ),
        (
            "👥",
            f"{kpi_data['productivity']['value']}%",
            "Productivity",
            COLORS["success"],
        ),
        (
            "💻",
            f"{kpi_data['tech_adoption']['value']}%",
            "Tech Adoption",
            COLORS["warning"],
        ),
    ]

    for col, (icon, value, label, color) in zip([col1, col2, col3, col4], stats):
        with col:
            st.markdown(
                f"""
            <div class="insight-card" style="text-align: center; padding: 1.75rem;">
                <span style="font-size: 2.5rem; display: block; margin-bottom: 1rem;">{icon}</span>
                <div class="insight-value" style="color: {color};">{value}</div>
                <div class="insight-label">{label}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown(
        "<h2 style='margin: 3rem 0 2rem 0;'>📋 Strategic Insights & Analysis</h2>",
        unsafe_allow_html=True,
    )

    for i in range(0, 4, 2):
        col1, col2 = st.columns(2)
        with col1:
            render_summary_card(executive_summaries[i])
        with col2:
            if i + 1 < len(executive_summaries):
                render_summary_card(executive_summaries[i + 1])
        st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

# REPORTS & EXPORT PAGE
elif st.session_state.current_page == "Reports & Export":
    st.markdown("# 📥 Reports & Export")
    st.markdown(
        "<p style='color: #64748b; font-size: 1.0625rem; margin-bottom: 2.5rem; margin-top: -0.25rem;'>Download comprehensive reports and export data in multiple formats</p>",
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
        <div class="insight-card" style="padding: 1.75rem;">
            <div style="width: 60px; height: 60px; background: linear-gradient(145deg, {COLORS["navy"]}, {COLORS["primary"]});
                        border-radius: 18px; display: flex; align-items: center; justify-content: center;
                        margin-bottom: 1.5rem; box-shadow: 0 12px 32px rgba(15, 23, 42, 0.3);">
                <span style="font-size: 1.875rem;">📄</span>
            </div>
            <h3 style="margin: 0 0 0.5rem 0; font-size: 1.25rem;">Full Report</h3>
            <p style="color: {COLORS["gray"]}; font-size: 0.875rem; margin-bottom: 1.5rem;">
                Complete executive dashboard with all KPIs, charts, and insights in HTML format
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        st.download_button(
            "📥 Download HTML Report",
            data=generate_html_report(),
            file_name=f"BizView_Executive_Report_{datetime.now().strftime('%Y%m%d')}.html",
            mime="text/html",
            use_container_width=True,
        )

    with col2:
        st.markdown(
            f"""
        <div class="insight-card" style="padding: 1.75rem;">
            <div style="width: 60px; height: 60px; background: linear-gradient(145deg, {COLORS["success"]}, {COLORS["accent"]});
                        border-radius: 18px; display: flex; align-items: center; justify-content: center;
                        margin-bottom: 1.5rem; box-shadow: 0 12px 32px rgba(16, 185, 129, 0.3);">
                <span style="font-size: 1.875rem;">📊</span>
            </div>
            <h3 style="margin: 0 0 0.5rem 0; font-size: 1.25rem;">Excel Export</h3>
            <p style="color: {COLORS["gray"]}; font-size: 0.875rem; margin-bottom: 1.5rem;">
                All data tables in multi-sheet workbook for advanced analysis and custom reporting
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
            workflow_trend_data.to_excel(
                writer, sheet_name="Workflow Trends", index=False
            )
            productivity_data.to_excel(writer, sheet_name="Productivity", index=False)
            tech_adoption_data.to_excel(writer, sheet_name="Tech Adoption", index=False)
            monthly_performance.to_excel(writer, sheet_name="Financial", index=False)
            recent_workflows.to_excel(
                writer, sheet_name="Recent Workflows", index=False
            )

        st.download_button(
            "📥 Download Excel",
            data=buffer.getvalue(),
            file_name=f"BizView_Data_{datetime.now().strftime('%Y%m%d')}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True,
        )

    with col3:
        st.markdown(
            f"""
        <div class="insight-card" style="padding: 1.75rem;">
            <div style="width: 60px; height: 60px; background: linear-gradient(145deg, {COLORS["warning"]}, {COLORS["error"]});
                        border-radius: 18px; display: flex; align-items: center; justify-content: center;
                        margin-bottom: 1.5rem; box-shadow: 0 12px 32px rgba(245, 158, 11, 0.3);">
                <span style="font-size: 1.875rem;">📋</span>
            </div>
            <h3 style="margin: 0 0 0.5rem 0; font-size: 1.25rem;">CSV Export</h3>
            <p style="color: {COLORS["gray"]}; font-size: 0.875rem; margin-bottom: 1.5rem;">
                Raw data files for integration with external tools and systems
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        st.download_button(
            "📥 Download CSV",
            data=productivity_data.to_csv(index=False),
            file_name=f"BizView_Productivity_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv",
            use_container_width=True,
        )

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("<div style='height: 3rem;'></div>", unsafe_allow_html=True)
st.markdown(
    f"""
<div style="text-align: center; padding: 2rem; background: rgba(255,255,255,0.95); 
            backdrop-filter: blur(16px); border-radius: 20px; border: 1px solid #e2e8f0;
            box-shadow: 0 4px 16px rgba(0,0,0,0.04);">
    <p style="color: {COLORS["gray"]}; font-size: 0.875rem; margin-bottom: 0.5rem;">
        <strong>BizView Executive Dashboard</strong> • Ultra Premium Edition v7.0
    </p>
    <p style="color: {COLORS["gray"]}; font-size: 0.75rem;">
        Powered by Streamlit • {datetime.now().strftime("%Y")} • All Rights Reserved
    </p>
</div>
""",
    unsafe_allow_html=True,
)

print("BizView Dashboard v7.0 - Enhanced with premium animations & icon-only sidebar!")
