"""
BizView Executive Dashboard - ULTRA PREMIUM EDITION
Enterprise-Grade Streamlit Application with:
- Glassmorphism UI & Premium Gradients
- D3-Style Smooth Animations
- 4K/HD Chart Rendering
- React-Like Component Architecture
- Optimized for 16" Displays
"""

import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from datetime import datetime
import io

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="BizView Executive Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",  # V10: Set back to expanded for user visibility
)

# ============================================================================
# PREMIUM CSS - ULTRA MODERN DESIGN SYSTEM
# ============================================================================
st.markdown(
    """
<style>
    /* ========== FONTS ========== */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Outfit:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

    /* ========== CSS VARIABLES - DESIGN TOKENS ========== */
    :root {
        /* Primary Colors */
        --navy-950: #020617;
        --navy-900: #0f172a;
        --navy-800: #1e293b;
        --navy-700: #334155;
        --navy-600: #475569;
        --navy-500: #64748b;
        
        /* Accent Colors */
        --blue-500: #3b82f6;
        --blue-600: #2563eb;
        --cyan-500: #06b6d4;
        --emerald-500: #10b981;
        --amber-500: #f59e0b;
        --rose-500: #f43f5e;
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
        
        /* Shadows - Layered Depth */
        --shadow-xs: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
        --shadow-sm: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1);
        --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
        --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
        --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
        --shadow-2xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
        --shadow-glow-blue: 0 0 40px rgba(59, 130, 246, 0.3);
        --shadow-glow-cyan: 0 0 40px rgba(6, 182, 212, 0.3);
        
        /* Gradients */
        --gradient-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --gradient-navy: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
        --gradient-blue: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        --gradient-cyan: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);
        --gradient-emerald: linear-gradient(135deg, #10b981 0%, #059669 100%);
        --gradient-amber: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        --gradient-rose: linear-gradient(135deg, #f43f5e 0%, #e11d48 100%);
        --gradient-violet: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);
        --gradient-glass: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
        --gradient-mesh: radial-gradient(at 0% 0%, rgba(59, 130, 246, 0.1) 0%, transparent 50%),
                         radial-gradient(at 100% 0%, rgba(139, 92, 246, 0.1) 0%, transparent 50%),
                         radial-gradient(at 100% 100%, rgba(6, 182, 212, 0.1) 0%, transparent 50%),
                         radial-gradient(at 0% 100%, rgba(16, 185, 129, 0.1) 0%, transparent 50%);
    }

    /* ========== V9: ULTRA PREMIUM GLOBAL RESETS ========== */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-rendering: optimizeLegibility;
        -webkit-font-feature-settings: "kern" 1;
        font-feature-settings: "kern" 1;
        font-kerning: normal;
        box-sizing: border-box;
    }

    /* Hide Streamlit Branding but keep Header for Toggle */
    #MainMenu, footer, .stDeployButton {visibility: hidden !important; height: 0 !important; margin: 0 !important; padding: 0 !important; overflow: hidden !important;}
    [data-testid="stToolbar"] {display: none !important;}
    [data-testid="stHeader"] {
        background: transparent !important;
        color: transparent !important;
        height: 1px !important;
        overflow: visible !important;
        pointer-events: none !important;
    }
    
    [data-testid="stHeader"] button {
        pointer-events: auto !important;
    }
    
    /* V10: Dark Sidebar Toggle Button - Forced Visibility */
    [data-testid="collapsedControl"],
    .st-emotion-cache-1dp5vir {
        position: fixed !important;
        top: 0.75rem !important;
        left: 0.75rem !important;
        z-index: 999999 !important;
        background: #0f172a !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        padding: 0.5rem !important;
        width: 2.75rem !important;
        height: 2.75rem !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        opacity: 1 !important;
        visibility: visible !important;
    }
    
    [data-testid="collapsedControl"]:hover {
        background: #1e293b !important;
        transform: scale(1.1) !important;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3) !important;
    }
    
    [data-testid="collapsedControl"] svg {
        color: #ffffff !important;
        width: 1.5rem !important;
        height: 1.5rem !important;
    }
    
    /* ========== MAIN APP BACKGROUND - STRICT WHITE ========== */
    .stApp {
        background: #ffffff !important;
    }
    
    /* Remove mesh overlay for clean look */
    .stApp::before {
        display: none !important;
    }

    /* ========== V9: MAIN CONTENT - REACT APP FEEL ========== */
    .main .block-container {
        padding-top: 0rem !important;
        padding-bottom: 2rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 1920px;
        margin: 0 auto;
        position: relative;
        z-index: 1;
        min-height: 100vh;
    }

    /* ========== V7: STREAMLIT COLUMN OVERRIDES - STRETCH ========== */
    /* Force st.columns containers to stretch children equally */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        align-items: stretch !important;
        gap: 1.5rem !important;
    }

    /* Each column inside st.columns should fill height */
    [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
        display: flex !important;
        flex-direction: column !important;
    }

    /* Direct children of columns fill available space */
    [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] > div:first-child {
        flex: 1 !important;
        display: flex !important;
        flex-direction: column !important;
    }

    /* ========== SIDEBAR - DEEP NAVY ========== */
    [data-testid="stSidebar"] {
        background: #0a1929 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        height: 100vh !important;
        overflow-y: auto;
        overflow-x: hidden;
        z-index: 100;
        backdrop-filter: blur(20px);
    }

    /* Subtle texture for premium feel, but keep it dark */
    [data-testid="stSidebar"]::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at top right, rgba(30, 41, 59, 0.3) 0%, transparent 60%);
        pointer-events: none;
    }

    /* V9: Sidebar Content - minimal top padding, no overflow */
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 0.5rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        padding-bottom: 1rem !important;
    }

    /* Remove Streamlit's default top spacing */
    [data-testid="stSidebarContent"] {
        padding-top: 0 !important;
    }

    /* V9: Sidebar Typography - Ultra Sharp */
    [data-testid="stSidebar"] .stMarkdown,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label {
        color: rgba(255, 255, 255, 0.9) !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 500 !important;
        letter-spacing: -0.01em !important;
    }

    /* V11: Sidebar Navigation Buttons - Linear SaaS Style */
    [data-testid="stSidebar"] .stButton > button {
        width: 100%;
        background: rgba(255, 255, 255, 0.03) !important;
        color: #94a3b8 !important; /* Slate-400 */
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        border-radius: 12px !important;
        padding: 0.75rem 1rem !important;
        margin: 0.25rem 0 !important;
        font-size: 0.875rem !important;
        font-weight: 500 !important;
        text-align: left !important;
        display: flex !important;
        justify-content: flex-start !important;
        align-items: center !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }

    /* Hover State */
    [data-testid="stSidebar"] .stButton > button:hover {
        background: rgba(255, 255, 255, 0.08) !important;
        color: #f8fafc !important;
        border-color: rgba(59, 130, 246, 0.3) !important;
        transform: translateX(4px) !important;
    }

    /* Active State - Premium Indicator */
    [data-testid="stSidebar"] .stButton > button[kind="primary"] {
        background: linear-gradient(90deg, rgba(59, 130, 246, 0.2) 0%, rgba(59, 130, 246, 0.05) 100%) !important;
        color: #ffffff !important;
        border-left: 4px solid #3b82f6 !important;
        border-radius: 4px 12px 12px 4px !important;
        padding-left: 1.25rem !important;
        box-shadow: 0 4px 20px rgba(59, 130, 246, 0.15) !important;
    }

    /* ========== TYPOGRAPHY ========== */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: -0.025em !important;
        color: var(--navy-900) !important;
    }

    h1 {
        font-size: 2.5rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, var(--navy-900) 0%, var(--navy-600) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    h2 { font-size: 1.875rem !important; }
    h3 { font-size: 1.5rem !important; }
    h4 { font-size: 1.125rem !important; }

    /* ========== V9: KPI CARDS - GLASSMORPHISM 2.0 ========== */
    .kpi-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.85) 100%);
        backdrop-filter: blur(30px) saturate(180%);
        -webkit-backdrop-filter: blur(30px) saturate(180%);
        border: 1px solid rgba(255, 255, 255, 0.6);
        border-radius: 20px;
        padding: 2rem;
        position: relative;
        overflow: hidden;
        transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08), 0 2px 8px rgba(0, 0, 0, 0.04), inset 0 1px 0 rgba(255, 255, 255, 0.8);
        animation: fadeInUp 0.6s cubic-bezier(0.34, 1.56, 0.64, 1) both;
        will-change: transform, box-shadow;
        /* V7: Flex-grow to fill column height */
        flex: 1 !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
        min-height: 0;
    }

    /* V9: Enhanced Glass Reflection */
    .kpi-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 60%;
        background: linear-gradient(180deg, rgba(255, 255, 255, 0.9) 0%, rgba(255, 255, 255, 0.1) 100%);
        opacity: 0.5;
        pointer-events: none;
        border-radius: 20px 20px 0 0;
    }

    /* V9: Animated Top Accent Bar */
    .kpi-card::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6, #06b6d4);
        background-size: 200% 100%;
        opacity: 0;
        transition: opacity 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        border-radius: 20px 20px 0 0;
    }

    .kpi-card:hover {
        transform: translateY(-16px) scale(1.03);
        box-shadow: 0 20px 60px rgba(59, 130, 246, 0.25), 0 8px 24px rgba(0, 0, 0, 0.12), inset 0 1px 0 rgba(255, 255, 255, 1);
        border-color: rgba(59, 130, 246, 0.4);
    }

    .kpi-card:hover::after {
        opacity: 1;
        animation: shimmer 2s linear infinite;
        animation: shimmer 2s infinite;
    }

    /* Icon Wrapper with Glow */
    .kpi-icon-wrapper {
        width: 64px;
        height: 64px;
        border-radius: 18px;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        transition: all 0.4s ease;
        box-shadow: var(--shadow-md);
        flex-shrink: 0;
    }

    .kpi-icon-wrapper::after {
        content: '';
        position: absolute;
        inset: -2px;
        border-radius: 20px;
        padding: 2px;
        background: linear-gradient(135deg, rgba(255,255,255,0.6), rgba(255,255,255,0.1));
        -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    .kpi-card:hover .kpi-icon-wrapper {
        transform: scale(1.1) rotate(5deg);
    }

    .kpi-card:hover .kpi-icon-wrapper::after {
        opacity: 1;
    }

    .kpi-icon-wrapper.success {
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        box-shadow: 0 8px 16px rgba(16, 185, 129, 0.3);
    }

    .kpi-icon-wrapper.warning {
        background: linear-gradient(135deg, #fed7aa 0%, #fdba74 100%);
        box-shadow: 0 8px 16px rgba(245, 158, 11, 0.3);
    }

    .kpi-icon-wrapper.error {
        background: linear-gradient(135deg, #fecaca 0%, #fca5a5 100%);
        box-shadow: 0 8px 16px rgba(239, 68, 68, 0.3);
    }

    .kpi-icon-wrapper.info {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        box-shadow: 0 8px 16px rgba(59, 130, 246, 0.3);
    }

    .kpi-icon {
        font-size: 2rem;
        filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.1));
        animation: iconFloat 3s ease-in-out infinite;
    }

    @keyframes iconFloat {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
    }

    /* V9: KPI Value - 8K Typography */
    .kpi-value {
        font-family: 'Outfit', sans-serif !important;
        font-size: 3rem !important;
        font-weight: 900 !important;
        line-height: 0.95 !important;
        letter-spacing: -0.05em !important;
        background: linear-gradient(135deg, #0f172a 0%, #334155 50%, #64748b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0.75rem 0;
        animation: countUp 1.2s cubic-bezier(0.34, 1.56, 0.64, 1);
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    }

    @keyframes countUp {
        0% { opacity: 0; transform: translateY(12px) scale(0.95); }
        60% { opacity: 1; transform: translateY(-2px) scale(1.02); }
        100% { opacity: 1; transform: translateY(0) scale(1); }
    }

    .kpi-label {
        font-size: 0.875rem;
        font-weight: 700;
        color: var(--gray-400);
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-top: 0.5rem;
        opacity: 0.9;
    }

    /* Change Indicator Badge */
    .kpi-change {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 1rem;
        border-radius: 100px;
        font-size: 0.85rem;
        font-weight: 700;
        margin-top: auto;
        transition: all 0.3s ease;
        animation: slideInRight 0.6s ease-out 0.3s backwards;
    }

    .kpi-change-positive {
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        color: #065f46;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.2);
    }

    .kpi-change-negative {
        background: linear-gradient(135deg, #fecaca 0%, #fca5a5 100%);
        color: #991b1b;
        box-shadow: 0 4px 12px rgba(239, 68, 68, 0.2);
    }

    .kpi-change:hover {
        transform: scale(1.05);
    }

    /* ========== V9: CHART CARDS - GLASSMORPHISM 2.0 ========== */
    .chart-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.88) 100%);
        backdrop-filter: blur(30px) saturate(180%);
        -webkit-backdrop-filter: blur(30px) saturate(180%);
        border: 1px solid rgba(255, 255, 255, 0.6);
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08), 0 2px 8px rgba(0, 0, 0, 0.04), inset 0 1px 0 rgba(255, 255, 255, 0.8);
        transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
        animation: fadeInUp 0.7s cubic-bezier(0.34, 1.56, 0.64, 1) both;
        margin-bottom: 2rem;
        will-change: transform, box-shadow;
    }

    .chart-card:hover {
        box-shadow: 0 16px 48px rgba(59, 130, 246, 0.15), 0 4px 16px rgba(0, 0, 0, 0.08), inset 0 1px 0 rgba(255, 255, 255, 1);
        transform: translateY(-8px);
        border-color: rgba(59, 130, 246, 0.3);
    }

    .chart-card-header {
        padding: 1.75rem 2rem;
        background: linear-gradient(180deg, rgba(248, 250, 252, 0.8) 0%, rgba(255, 255, 255, 0.4) 100%);
        border-bottom: 1px solid rgba(226, 232, 240, 0.5);
        position: relative;
    }

    .chart-card-header::after {
        content: '';
        position: absolute;
        bottom: -1px;
        left: 2rem;
        right: 2rem;
        height: 2px;
        background: linear-gradient(90deg, transparent, var(--blue-500), transparent);
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    .chart-card:hover .chart-card-header::after {
        opacity: 1;
    }

    /* V9: Chart Card Title - 8K Typography */
    .chart-card-title {
        font-family: 'Outfit', sans-serif !important;
        font-size: 0.875rem !important;
        font-weight: 800 !important;
        color: var(--navy-900) !important;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin: 0 !important;
        opacity: 0.95;
    }

    .chart-card-subtitle {
        font-size: 0.75rem;
        color: var(--gray-400);
        margin-top: 0.35rem;
        font-weight: 500;
        letter-spacing: 0.01em;
    }

    .chart-card-content {
        padding: 2rem;
    }

    /* ========== SUMMARY CARDS - PREMIUM DARK THEME ========== */
    .summary-card {
        background: var(--gradient-navy);
        border-radius: 24px;
        padding: 2.5rem;
        position: relative;
        overflow: hidden;
        box-shadow: var(--shadow-2xl);
        transition: all 0.4s ease;
        animation: fadeInUp 0.8s cubic-bezier(0.4, 0, 0.2, 1) both;
        height: 100%;
    }

    /* Animated Gradient Overlay */
    .summary-card::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 100%;
        height: 200%;
        background: radial-gradient(circle, rgba(59, 130, 246, 0.25) 0%, transparent 70%);
        animation: rotateGradient 10s linear infinite;
        pointer-events: none;
    }

    @keyframes rotateGradient {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    .summary-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: var(--shadow-2xl), 0 0 60px rgba(59, 130, 246, 0.3);
    }

    .summary-card-icon {
        width: 56px;
        height: 56px;
        border-radius: 16px;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.75rem;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }

    .summary-card:hover .summary-card-icon {
        transform: scale(1.15) rotate(5deg);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
    }

    .summary-card-title {
        color: #fbbf24 !important;
        font-family: 'Outfit', sans-serif !important;
        font-weight: 800 !important;
        font-size: 1.25rem !important;
        margin-bottom: 1rem !important;
        letter-spacing: -0.02em;
    }

    .summary-card-content {
        font-size: 0.95rem;
        line-height: 1.8;
        color: rgba(255, 255, 255, 0.85);
        margin-bottom: 1.5rem;
    }

    .summary-metric {
        padding-top: 1.5rem;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .summary-metric-value {
        font-family: 'Outfit', sans-serif !important;
        font-size: 2.25rem !important;
        font-weight: 900 !important;
        background: linear-gradient(135deg, #ffffff 0%, rgba(255,255,255,0.7) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .summary-metric-label {
        font-size: 0.75rem;
        color: rgba(255, 255, 255, 0.5);
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-weight: 600;
    }

    /* ========== INSIGHT CARDS ========== */
    .insight-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border: 1px solid var(--gray-200);
        border-radius: 20px;
        padding: 2rem;
        transition: all 0.3s ease;
        box-shadow: var(--shadow-md);
        animation: fadeIn 0.6s cubic-bezier(0.4, 0, 0.2, 1) both;
        height: 100%;
    }

    .insight-card:hover {
        box-shadow: var(--shadow-xl);
        transform: translateY(-6px);
        border-color: var(--blue-500);
    }

    .insight-card h4 {
        font-size: 0.8rem !important;
        font-weight: 700 !important;
        color: var(--gray-500) !important;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 1rem !important;
    }

    .insight-value {
        font-family: 'Outfit', sans-serif !important;
        font-size: 2.5rem !important;
        font-weight: 900 !important;
        letter-spacing: -0.03em;
        line-height: 1;
    }

    .insight-label {
        font-size: 0.9rem;
        color: var(--gray-500);
        margin-top: 0.5rem;
        font-weight: 500;
    }

    /* ========== V7: ENHANCED ANIMATIONS ========== */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    /* V7: KPI-specific entrance with subtle scale */
    @keyframes kpiEntrance {
        0% {
            opacity: 0;
            transform: translateY(16px) scale(0.97);
        }
        60% {
            opacity: 1;
            transform: translateY(-2px) scale(1.005);
        }
        100% {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(16px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeInLeft {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(12px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    @keyframes shimmer {
        0% {
            background-position: -200% 0;
        }
        100% {
            background-position: 200% 0;
        }
    }

    @keyframes pulse {
        0%, 100% {
            opacity: 1;
            transform: scale(1);
        }
        50% {
            opacity: 0.97;
            transform: scale(1.01);
        }
    }

    /* ========== BADGES ========== */
    .badge {
        display: inline-flex;
        align-items: center;
        padding: 0.5rem 1rem;
        border-radius: 100px;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 0.02em;
        transition: all 0.2s ease;
    }

    .badge:hover {
        transform: scale(1.05);
    }

    .badge-success {
        background: linear-gradient(135deg, #d1fae5, #a7f3d0);
        color: #065f46;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.2);
    }

    .badge-warning {
        background: linear-gradient(135deg, #fef3c7, #fde68a);
        color: #92400e;
        box-shadow: 0 4px 12px rgba(245, 158, 11, 0.2);
    }

    .badge-error {
        background: linear-gradient(135deg, #fee2e2, #fecaca);
        color: #991b1b;
        box-shadow: 0 4px 12px rgba(239, 68, 68, 0.2);
    }

    .badge-info {
        background: linear-gradient(135deg, #dbeafe, #bfdbfe);
        color: #1e40af;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.2);
    }

    /* ========== BUTTONS ========== */
    .stButton > button {
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        border-radius: 12px !important;
        padding: 0.75rem 1.5rem !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: var(--shadow-sm) !important;
    }

    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: var(--shadow-lg) !important;
    }

    .stDownloadButton > button {
        background: var(--gradient-navy) !important;
        color: white !important;
        border: none !important;
    }

    .stDownloadButton > button:hover {
        box-shadow: var(--shadow-xl), 0 0 40px rgba(15, 23, 42, 0.3) !important;
    }

    /* === V12: AESTHETIC TABLE ENHANCEMENTS === */
    .aesthetic-table-container {
        background: rgba(255, 255, 255, 0.7) !important;
        backdrop-filter: blur(20px) saturate(180%) !important;
        -webkit-backdrop-filter: blur(20px) saturate(180%) !important;
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
        border-radius: 20px !important;
        padding: 1rem !important;
        box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.05),
                    inset 0 0 0 1px rgba(255, 255, 255, 0.2) !important;
        margin-bottom: 2rem !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }

    .aesthetic-table-container:hover {
        transform: translateY(-4px);
        box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.1),
                    inset 0 0 0 1px rgba(255, 255, 255, 0.3) !important;
    }

    /* Refined Multi-Stop Gradient Badges */
    .status-badge-v12 {
        padding: 6px 14px;
        border-radius: 8px;
        font-size: 0.7rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        display: inline-flex;
        align-items: center;
        gap: 6px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        border: 1px solid rgba(255,255,255,0.5);
    }
    
    .status-completed-v12 {
        background: linear-gradient(135deg, #059669 0%, #10b981 100%);
        color: white;
    }
    .status-progress-v12 {
        background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%);
        color: white;
    }
    .status-risk-v12 {
        background: linear-gradient(135deg, #dc2626 0%, #ef4444 100%);
        color: white;
    }

    /* Filter Row Styling */
    .filter-row {
        display: flex;
        gap: 1rem;
        margin-bottom: 1rem;
        padding: 0.5rem;
        background: rgba(15, 23, 42, 0.03);
        border-radius: 12px;
        border: 1px solid rgba(15, 23, 42, 0.05);
    }

    .filter-input input {
        background: white !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px !important;
        font-size: 0.8rem !important;
        padding: 0.5rem 1rem !important;
    }

    /* === V11: PREMIUM GRADIENT TABLES (Inherited & Refined) === */
    .dataframe, [data-testid="stDataFrame"], [data-testid="stTable"] {
        font-family: 'Inter', sans-serif !important;
        font-size: 0.9rem !important;
        border-radius: 16px !important;
        overflow: hidden !important;
        box-shadow: var(--shadow-sm) !important;
        border: 1px solid var(--gray-200) !important;
    }

    /* Table Header Gradient */
    .dataframe thead tr, [data-testid="stDataFrame"] thead tr, [data-testid="stTable"] thead tr {
        background: linear-gradient(90deg, #f8fafc 0%, #ffffff 100%) !important;
        border-bottom: 2px solid #e2e8f0 !important;
    }

    .dataframe thead tr th, [data-testid="stDataFrame"] th, [data-testid="stTable"] th {
        font-family: 'Outfit', sans-serif !important;
        font-size: 0.75rem !important;
        font-weight: 800 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
        color: var(--gray-600) !important;
        padding: 1.25rem 1.5rem !important;
        border: none !important;
    }

    /* Row Styling */
    .dataframe tbody tr td, [data-testid="stDataFrame"] td, [data-testid="stTable"] td {
        padding: 1.25rem 1.5rem !important;
        color: var(--navy-900) !important;
        border-bottom: 1px solid var(--gray-100) !important;
        font-size: 0.875rem !important;
        transition: all 0.2s ease !important;
    }

    /* Row Hover Effect */
    .dataframe tbody tr:hover td, [data-testid="stDataFrame"] tr:hover td {
        background-color: var(--gray-50) !important;
        color: var(--blue-600) !important;
    }

    /* Custom Status Badges for Tables */
    .status-badge {
        padding: 4px 12px;
        border-radius: 100px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        display: inline-block;
    }
    .status-completed { background: #dcfce7; color: #166534; }
    .status-progress { background: #eff6ff; color: #1e40af; }
    .status-risk { background: #fee2e2; color: #991b1b; }

    /* ========== SCROLLBAR ========== */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }

    ::-webkit-scrollbar-track {
        background: var(--gray-100);
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, var(--blue-500), var(--violet-500));
        border-radius: 10px;
        border: 2px solid var(--gray-100);
    }

    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, var(--blue-600), var(--violet-500));
    }

    /* ========== 8px GRID SPACING UTILITIES ========== */
    .mt-1 { margin-top: 0.5rem; }  /* 8px */
    .mt-2 { margin-top: 1rem; }    /* 16px */
    .mt-3 { margin-top: 1.5rem; }  /* 24px */
    .mt-4 { margin-top: 2rem; }    /* 32px */
    .mb-1 { margin-bottom: 0.5rem; }
    .mb-2 { margin-bottom: 1rem; }
    .mb-3 { margin-bottom: 1.5rem; }
    .mb-4 { margin-bottom: 2rem; }
    .gap-1 { gap: 0.5rem; }
    .gap-2 { gap: 1rem; }
    .gap-3 { gap: 1.5rem; }
    .gap-4 { gap: 2rem; }
    .p-2 { padding: 1rem; }
    .p-3 { padding: 1.5rem; }
    .p-4 { padding: 2rem; }

    /* ========== RESPONSIVE OPTIMIZATIONS ========== */
    @media (max-width: 1920px) {
        .main .block-container {
            padding: 1.5rem 2rem !important;
        }
        .kpi-value {
            font-size: 2.5rem !important;
        }
    }

    @media (max-width: 1600px) {
        h1 { font-size: 2rem !important; }
        h2 { font-size: 1.5rem !important; }
        .kpi-value {
            font-size: 2rem !important;
        }
    }

    /* ========== PRINT STYLES ========== */
    @media print {
        [data-testid="stSidebar"] { display: none !important; }
        .no-print { display: none !important; }
        .stApp { background: white !important; }
        .chart-card, .kpi-card {
            box-shadow: none !important;
            break-inside: avoid;
        }
    }
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================================
# MOCK DATA - ENTERPRISE DATASET
# ============================================================================

# KPI Data
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

# Workflow Trend Data
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
        "Completed": [145, 162, 178, 195, 210, 225, 198, 235, 248, 262, 278, 290],
        "Pending": [23, 18, 25, 20, 15, 22, 28, 19, 16, 21, 17, 24],
        "Failed": [5, 8, 4, 6, 3, 7, 9, 4, 5, 6, 3, 8],
    }
)

# Volume Gearing Data
volume_gearing_data = pd.DataFrame(
    {
        "Quarter": ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"],
        "Ratio": [2.12, 2.28, 2.35, 2.45],
        "Volume": [485000, 512000, 548000, 592000],
        "Benchmark": [2.0, 2.1, 2.15, 2.2],
    }
)

# Productivity Data
productivity_data = pd.DataFrame(
    {
        "Department": [
            "Engineering",
            "Sales",
            "Marketing",
            "Operations",
            "Finance",
            "HR",
        ],
        "Score": [92.5, 88.2, 85.7, 91.3, 89.1, 83.4],
        "Target": [90, 85, 82, 88, 87, 80],
        "Employees": [45, 32, 18, 28, 15, 12],
    }
)

# Tech Adoption Data
tech_adoption_data = pd.DataFrame(
    {
        "Tool": [
            "CRM System",
            "Project Management",
            "Analytics Platform",
            "Collaboration Suite",
            "AI Assistant",
            "Automation Tools",
            "Cloud Storage",
            "Security Tools",
        ],
        "Adoption": [94, 89, 76, 92, 45, 68, 98, 85],
        "Category": [
            "Core",
            "Core",
            "Analytics",
            "Communication",
            "Emerging",
            "Process",
            "Core",
            "Security",
        ],
    }
)

# Department Breakdown
department_breakdown = pd.DataFrame(
    {
        "Department": ["Engineering", "Sales", "Marketing", "Operations", "Other"],
        "Value": [35, 25, 15, 15, 10],
    }
)

# Recent Workflows
recent_workflows = pd.DataFrame(
    {
        "ID": [
            "WF-001",
            "WF-002",
            "WF-003",
            "WF-004",
            "WF-005",
            "WF-006",
            "WF-007",
            "WF-008",
        ],
        "Workflow Name": [
            "Customer Onboarding",
            "Invoice Processing",
            "Lead Qualification",
            "Support Ticket Routing",
            "Employee Onboarding",
            "Report Generation",
            "Data Sync",
            "Contract Review",
        ],
        "Department": [
            "Sales",
            "Finance",
            "Marketing",
            "Operations",
            "HR",
            "Engineering",
            "Engineering",
            "Legal",
        ],
        "Status": [
            "Completed",
            "Completed",
            "Pending",
            "Completed",
            "Failed",
            "Completed",
            "Pending",
            "Completed",
        ],
        "Duration": [
            "2h 15m",
            "45m",
            "1h 30m",
            "15m",
            "3h 45m",
            "30m",
            "55m",
            "4h 20m",
        ],
        "Date": [
            "2024-12-15",
            "2024-12-15",
            "2024-12-14",
            "2024-12-14",
            "2024-12-13",
            "2024-12-13",
            "2024-12-12",
            "2024-12-12",
        ],
    }
)

# Executive Summaries
executive_summaries = [
    {
        "title": "Operational Excellence",
        "content": "Workflow completion rates have increased by 12.5% compared to last quarter, driven primarily by process automation initiatives in the Engineering and Operations departments.",
        "metric": "+12.5%",
        "metric_label": "Workflow Efficiency",
        "icon": "📈",
    },
    {
        "title": "Financial Performance",
        "content": "Volume gearing ratio has improved to 2.45, exceeding the industry benchmark of 2.2. This indicates optimal resource utilization and scalable growth patterns.",
        "metric": "2.45",
        "metric_label": "Gearing Ratio",
        "icon": "💰",
    },
    {
        "title": "Workforce Productivity",
        "content": "Overall productivity score stands at 87.3%, with Engineering leading at 92.5%. Cross-departmental collaboration initiatives have contributed to a 5.2% increase.",
        "metric": "87.3%",
        "metric_label": "Avg Productivity",
        "icon": "👥",
    },
    {
        "title": "Technology Transformation",
        "content": "Core technology adoption remains strong at 90%+, while emerging technologies like AI assistants show 45% adoption with significant growth potential.",
        "metric": "76.8%",
        "metric_label": "Tech Adoption",
        "icon": "💻",
    },
]

# Monthly Performance
monthly_performance = pd.DataFrame(
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
        "Revenue": [
            125000,
            132000,
            145000,
            152000,
            168000,
            175000,
            162000,
            185000,
            198000,
            210000,
            225000,
            242000,
        ],
        "Costs": [
            98000,
            102000,
            108000,
            112000,
            118000,
            122000,
            115000,
            128000,
            135000,
            142000,
            148000,
            155000,
        ],
        "Profit": [
            27000,
            30000,
            37000,
            40000,
            50000,
            53000,
            47000,
            57000,
            63000,
            68000,
            77000,
            87000,
        ],
    }
)

# ============================================================================
# CHART CONFIGURATION - 4K READY & D3-STYLE
# ============================================================================

# Premium Color Palette
COLORS = {
    "primary": "#3b82f6",
    "secondary": "#8b5cf6",
    "accent": "#06b6d4",
    "success": "#10b981",
    "warning": "#f59e0b",
    "error": "#ef4444",
    "navy": "#0f172a",
    "gray": "#64748b",
}


# V10: Plotly Template with D3.js-Style Animations
def get_chart_config():
    """Returns high-end chart configuration for interactive dashboards"""
    return {
        "displayModeBar": False,
        "responsive": True,
        "scrollZoom": False,
        "displaylogo": False,
        "toImageButtonOptions": {
            "format": "png",
            "filename": "bizview_chart",
            "height": 2160,  # 4K rendering
            "width": 3840,
            "scale": 1,
        },
    }


def get_chart_layout(title="", height=400):
    """Returns a premium chart layout with D3.js aesthetics"""
    return {
        "title": {
            "text": title,
            "font": {
                "family": "Outfit, sans-serif",
                "size": 14,
                "color": "#0f172a",
                "weight": 800,
            },
            "x": 0.05,
            "xanchor": "left",
            "y": 0.95,
        },
        "height": height,
        "margin": {"l": 50, "r": 30, "t": 60, "b": 60},
        "plot_bgcolor": "rgba(0,0,0,0)",
        "paper_bgcolor": "rgba(0,0,0,0)",
        "font": {"family": "Inter, sans-serif", "size": 11, "color": "#64748b"},
        "hovermode": "closest",
        "hoverlabel": {
            "bgcolor": "white",
            "font": {
                "size": 13,
                "family": "Inter, sans-serif",
            },
            "bordercolor": "#e2e8f0",
        },
        "xaxis": {
            "showgrid": False,
            "showline": True,
            "linecolor": "rgba(226, 232, 240, 0.5)",
            "linewidth": 1,
            "tickfont": {"size": 10, "color": "#94a3b8"},
            "zeroline": False,
        },
        "yaxis": {
            "showgrid": True,
            "gridcolor": "rgba(241, 245, 249, 0.5)",
            "gridwidth": 1,
            "showline": False,
            "tickfont": {"size": 10, "color": "#94a3b8"},
            "zeroline": False,
        },
        "legend": {
            "orientation": "h",
            "yanchor": "bottom",
            "y": -0.25,
            "xanchor": "center",
            "x": 0.5,
            "font": {"size": 10},
        },
        "transition": {"duration": 500, "easing": "cubic-in-out"},
    }


# V11: Ultimate Sankey 2.0 - Workflow Flow Visualization
def create_sankey_chart():
    """Creates a high-fidelity Sankey diagram showing workflow flow between departments and stages"""
    # Define nodes with hierarchical categories
    nodes = [
        "Sales Dept",
        "Marketing Dept",
        "Operations Dept",
        "Finance Dept",
        "Lead Inbound",
        "In Progress",
        "Quality Review",
        "Completed",
        "Archived",
    ]

    # Define flows (source, target, value)
    links = {
        "source": [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7],
        "target": [4, 5, 6, 4, 5, 6, 4, 5, 6, 5, 6, 5, 6, 6, 7, 7, 8, 8],
        "value": [
            45,
            30,
            25,
            38,
            42,
            20,
            55,
            35,
            30,
            48,
            22,
            95,
            85,
            102,
            195,
            220,
            45,
            130,
        ],
    }

    # Premium Node Colors (8K Clarity)
    node_colors = [
        "#3b82f6",
        "#8b5cf6",
        "#06b6d4",
        "#10b981",
        "#f59e0b",
        "#f97316",
        "#ef4444",
        "#10b981",
        "#64748b",
    ]

    # Link Colors with Dynamic Opacity
    link_colors = [
        "rgba(59,130,246,0.2)",
        "rgba(59,130,246,0.2)",
        "rgba(59,130,246,0.2)",
        "rgba(139,92,246,0.2)",
        "rgba(139,92,246,0.2)",
        "rgba(139,92,246,0.2)",
        "rgba(6,182,212,0.2)",
        "rgba(6,182,212,0.2)",
        "rgba(6,182,212,0.2)",
        "rgba(16,185,129,0.2)",
        "rgba(16,185,129,0.2)",
        "rgba(245,158,11,0.2)",
        "rgba(245,158,11,0.2)",
        "rgba(249,115,22,0.2)",
        "rgba(249,115,22,0.2)",
        "rgba(16,185,129,0.2)",
        "rgba(239,68,68,0.2)",
        "rgba(100,116,139,0.2)",
    ]

    fig = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    pad=15,
                    thickness=25,
                    line=dict(color="rgba(255,255,255,0.9)", width=2),
                    label=nodes,
                    color=node_colors,
                    hovertemplate="<b>%{label}</b><br>Volume: %{value}<extra></extra>",
                ),
                link=dict(
                    source=links["source"],
                    target=links["target"],
                    value=links["value"],
                    color=link_colors,
                    hovertemplate="%{source.label} → %{target.label}<br>Value: %{value}<extra></extra>",
                ),
                arrangement="perpendicular",
            )
        ]
    )

    fig.update_layout(
        height=500,
        margin=dict(l=10, r=10, t=40, b=40),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, sans-serif", size=12, color="#0f172a"),
        transition=dict(duration=1000, easing="cubic-in-out"),
    )
    return fig


# V11: Radar Chart for Departmental Balance
def create_radar_chart():
    """Creates a Radar chart showing balanced scorecard across departments"""
    categories = ["Efficiency", "Output", "Quality", "Tech Adoption", "Cost Control"]

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=[85, 92, 88, 76, 82],
            theta=categories,
            fill="toself",
            name="Sales",
            line_color="#3b82f6",
            fillcolor="rgba(59,130,246,0.2)",
        )
    )

    fig.add_trace(
        go.Scatterpolar(
            r=[78, 85, 92, 88, 75],
            theta=categories,
            fill="toself",
            name="Engineering",
            line_color="#8b5cf6",
            fillcolor="rgba(139,92,246,0.2)",
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True, range=[0, 100], gridcolor="#f1f5f9", tickfont_size=10
            ),
            angularaxis=dict(gridcolor="#f1f5f9", tickfont_size=11),
        ),
        showlegend=True,
        height=450,
        margin=dict(l=40, r=40, t=60, b=40),
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, sans-serif", size=12, color="#64748b"),
    )
    return fig


# V11: Sunburst Chart for Hierarchical Breakdown
def create_sunburst_chart():
    """Creates a Sunburst chart for Hierarchical Performance Breakdown"""
    labels = [
        "Enterprise",
        "Operations",
        "Commercial",
        "R&D",
        "Logistics",
        "Inventory",
        "Sales",
        "Marketing",
        "Engineering",
        "Design",
    ]
    parents = [
        "",
        "Enterprise",
        "Enterprise",
        "Enterprise",
        "Operations",
        "Operations",
        "Commercial",
        "Commercial",
        "R&D",
        "R&D",
    ]
    values = [1000, 400, 350, 250, 220, 180, 200, 150, 160, 90]

    colors = [
        "#0f172a",
        "#3b82f6",
        "#8b5cf6",
        "#06b6d4",
        "#60a5fa",
        "#93c5fd",
        "#a78bfa",
        "#c4b5fd",
        "#22d3ee",
        "#67e8f9",
    ]

    fig = go.Figure(
        go.Sunburst(
            labels=labels,
            parents=parents,
            values=values,
            branchvalues="total",
            marker=dict(colors=colors, line=dict(color="white", width=2)),
            hovertemplate="<b>%{label}</b><br>Share: %{percentParent:.1%}<extra></extra>",
        )
    )

    fig.update_layout(
        height=450,
        margin=dict(l=0, r=0, t=20, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        transition=dict(duration=800, easing="elastic-in-out"),
    )
    return fig


# ============================================================================
# REACT-LIKE COMPONENTS
# ============================================================================


def render_kpi_card(
    label, value, change, trend, format_type="number", icon="📊", animation_delay=0
):
    """Premium KPI Card Component with Glassmorphism"""

    # Format value
    if format_type == "percentage":
        display_value = f"{value}%"
    elif format_type == "ratio":
        display_value = f"{value:.2f}"
    elif format_type == "currency":
        display_value = f"${value:,.0f}"
    else:
        display_value = f"{value:,}"

    # Determine trend styling
    if trend == "up":
        trend_class = "kpi-change-positive"
        trend_icon = "↗"
        icon_class = "success"
    else:
        trend_class = "kpi-change-negative"
        trend_icon = "↘"
        icon_class = "warning"

    st.markdown(
        f"""
    <div class="kpi-card" style="animation-delay: {animation_delay}s;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div style="flex: 1;">
                <div class="kpi-label">{label}</div>
                <div class="kpi-value">{display_value}</div>
                <div class="kpi-change {trend_class}">
                    <span class="kpi-change-icon">{trend_icon}</span>
                    <span>{abs(change)}%</span>
                </div>
            </div>
            <div class="kpi-icon-wrapper {icon_class}">
                <div class="kpi-icon">{icon}</div>
            </div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


def render_chart_header(title, subtitle=""):
    """Chart Card Header Component"""
    st.markdown(
        f"""
    <div class="chart-card-header">
        <div class="chart-card-title">{title}</div>
        {f'<div class="chart-card-subtitle">{subtitle}</div>' if subtitle else ""}
    </div>
    """,
        unsafe_allow_html=True,
    )


def render_summary_card(summary):
    """Executive Summary Card Component"""
    st.markdown(
        f"""
    <div class="summary-card">
        <div class="summary-card-icon">{summary["icon"]}</div>
        <div class="summary-card-title">{summary["title"]}</div>
        <div class="summary-card-content">{summary["content"]}</div>
        <div class="summary-metric">
            <div>
                <div class="summary-metric-value">{summary["metric"]}</div>
                <div class="summary-metric-label">{summary["metric_label"]}</div>
            </div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


# V12: Aesthetic Table Component with Column Filtering
def render_aesthetic_table(df, key_prefix="table", height=400):
    """Renders a premium table with column-level filtering and V12 aesthetics"""
    st.markdown('<div class="aesthetic-table-container">', unsafe_allow_html=True)

    # Filter Row UI
    with st.container():
        cols = st.columns(len(df.columns))
        filters = {}
        for i, col_name in enumerate(df.columns):
            with cols[i]:
                # Small text input for filtering
                filters[col_name] = st.text_input(
                    f"Filter {col_name}",
                    key=f"{key_prefix}_filter_{col_name}",
                    placeholder=f"Search {col_name}...",
                    label_visibility="collapsed",
                )

    # Filtering Logic
    filtered_df = df.copy()
    for col_name, val in filters.items():
        if val:
            filtered_df = filtered_df[
                filtered_df[col_name]
                .astype(str)
                .str.contains(val, case=False, na=False)
            ]

    # Render the table
    st.dataframe(
        filtered_df,
        width="stretch",
        hide_index=True,
        height=height,
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ============================================================================
# CHART COMPONENTS - D3-STYLE WITH ANIMATIONS
# ============================================================================


def create_workflow_bar_chart(data):
    """Animated Stacked Bar Chart with D3.js Aesthetics"""
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            name="Completed",
            x=data["Month"],
            y=data["Completed"],
            marker=dict(
                color=COLORS["success"],
                line=dict(color="rgba(255,255,255,0.6)", width=1),
            ),
            width=0.4,
            hovertemplate="<b>%{x}</b><br>Completed: %{y}<extra></extra>",
        )
    )

    fig.add_trace(
        go.Bar(
            name="Pending",
            x=data["Month"],
            y=data["Pending"],
            marker=dict(
                color=COLORS["warning"],
                line=dict(color="rgba(255,255,255,0.6)", width=1),
            ),
            width=0.4,
            hovertemplate="<b>%{x}</b><br>Pending: %{y}<extra></extra>",
        )
    )

    fig.add_trace(
        go.Bar(
            name="Failed",
            x=data["Month"],
            y=data["Failed"],
            marker=dict(
                color=COLORS["error"], line=dict(color="rgba(255,255,255,0.6)", width=1)
            ),
            width=0.4,
            hovertemplate="<b>%{x}</b><br>Failed: %{y}<extra></extra>",
        )
    )

    layout = get_chart_layout(height=400)
    layout.update(
        {
            "barmode": "stack",
            "bargap": 0.4,
            "hovermode": "x unified",
        }
    )
    fig.update_layout(**layout)
    fig.update_yaxes(gridcolor="rgba(241, 245, 249, 0.4)")

    return fig


def create_donut_chart(data):
    """Premium Donut Chart with D3.js Aesthetics"""
    colors = [
        COLORS["primary"],
        "#6366f1",  # indigo
        "#8b5cf6",  # violet
        "#a855f7",  # purple
        "#d946ef",  # fuchsia
    ]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=data["Department"],
                values=data["Value"],
                hole=0.72,
                marker=dict(
                    colors=colors,
                    line=dict(color="white", width=4),
                ),
                textposition="outside",
                textinfo="label+percent",
                textfont=dict(size=11, family="Inter, sans-serif", color="#64748b"),
                hovertemplate="<b>%{label}</b><br>Usage: %{value}%<extra></extra>",
                rotation=90,
            )
        ]
    )

    layout = get_chart_layout(height=400)
    layout.update(
        {
            "showlegend": False,
            "margin": {"l": 40, "r": 40, "t": 40, "b": 40},
            "annotations": [
                {
                    "font": {
                        "family": "Outfit, sans-serif",
                        "size": 24,
                        "color": "#0f172a",
                        "weight": 900,
                    },
                    "showarrow": False,
                    "text": f"{data['Value'].sum()}%",
                    "x": 0.5,
                    "y": 0.5,
                },
                {
                    "font": {"size": 10, "color": "#94a3b8", "weight": 600},
                    "showarrow": False,
                    "text": "TOTAL FLOW",
                    "x": 0.5,
                    "y": 0.38,
                },
            ],
        }
    )
    fig.update_layout(**layout)

    return fig


def create_line_chart(data, x_col, y_col, name, color):
    """Smooth Line Chart with Area Fill and D3.js Aesthetics"""
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=data[x_col],
            y=data[y_col],
            mode="lines+markers",
            name=name,
            line=dict(color=color, width=3, shape="spline"),
            marker=dict(
                size=8, color="white", line=dict(color=color, width=2), opacity=1
            ),
            fill="tozeroy",
            fillcolor={
                "linear_gradient": {
                    "x0": 0,
                    "y0": 0,
                    "x1": 0,
                    "y1": 1,
                    "color_stops": [
                        {"offset": 0, "color": color},
                        {"offset": 1, "color": "rgba(255,255,255,0)"},
                    ],
                }
            }
            if hasattr(go.Scatter, "fillgradient")
            else f"rgba({int(color[1:3], 16)}, {int(color[3:5], 16)}, {int(color[5:7], 16)}, 0.15)",
            hovertemplate="<b>%{x}</b><br>" + name + ": %{y}<extra></extra>",
        )
    )

    layout = get_chart_layout(height=380)
    fig.update_layout(**layout)
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(gridcolor="rgba(241, 245, 249, 0.3)")

    return fig


def create_area_chart(data):
    """Multi-Series Area Chart with Premium Gradients"""
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=data["Quarter"],
            y=data["Ratio"],
            mode="lines+markers",
            name="Actual Ratio",
            line=dict(color=COLORS["primary"], width=4, shape="spline"),
            marker=dict(
                size=10, color="white", line=dict(color=COLORS["primary"], width=3)
            ),
            fill="tozeroy",
            fillcolor="rgba(59, 130, 246, 0.15)",
            hovertemplate="<b>%{x}</b><br>Ratio: %{y:.2f}<extra></extra>",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=data["Quarter"],
            y=data["Benchmark"],
            mode="lines",
            name="Benchmark",
            line=dict(color=COLORS["gray"], width=2, dash="dash"),
            hovertemplate="<b>%{x}</b><br>Benchmark: %{y:.2f}<extra></extra>",
        )
    )

    layout = get_chart_layout(height=380)
    fig.update_layout(**layout)

    return fig


def create_horizontal_bar_chart(data):
    """Horizontal Bar Chart with D3.js Aesthetics"""
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            y=data["Department"],
            x=data["Score"],
            name="Score",
            orientation="h",
            marker=dict(
                color=data["Score"],
                colorscale=[
                    [0, COLORS["error"]],
                    [0.5, COLORS["warning"]],
                    [1, COLORS["success"]],
                ],
                line=dict(color="rgba(255,255,255,0.4)", width=1),
            ),
            width=0.4,
            text=data["Score"].apply(lambda x: f"{x}%"),
            textposition="outside",
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
                size=12,
                color="#0f172a",
                symbol="diamond",
                line=dict(color="white", width=2),
                opacity=0.8,
            ),
            hovertemplate="<b>%{y}</b><br>Target: %{x}%<extra></extra>",
        )
    )

    layout = get_chart_layout(height=400)
    layout.update(
        {
            "bargap": 0.3,
            "margin": {"l": 100, "r": 50, "t": 60, "b": 60},
        }
    )
    fig.update_layout(**layout)
    fig.update_xaxes(showgrid=True, gridcolor="rgba(241, 245, 249, 0.4)")
    fig.update_yaxes(showgrid=False)

    return fig


def create_tech_adoption_chart(data):
    """Tech Adoption Chart with Threshold Lines and D3.js Aesthetics"""
    fig = go.Figure()

    colors = [
        COLORS["success"]
        if x >= 80
        else COLORS["warning"]
        if x >= 60
        else COLORS["error"]
        for x in data["Adoption"]
    ]

    fig.add_trace(
        go.Bar(
            x=data["Tool"],
            y=data["Adoption"],
            marker=dict(
                color=colors, line=dict(color="rgba(255,255,255,0.4)", width=1)
            ),
            width=0.5,
            text=data["Adoption"].apply(lambda x: f"{x}%"),
            textposition="outside",
            hovertemplate="<b>%{x}</b><br>Adoption: %{y}%<extra></extra>",
        )
    )

    # Add threshold lines
    fig.add_hline(
        y=80,
        line_dash="dash",
        line_color=COLORS["success"],
        line_width=1,
        opacity=0.5,
        annotation_text="HIGH (80%)",
        annotation_position="top right",
    )
    fig.add_hline(
        y=60,
        line_dash="dash",
        line_color=COLORS["warning"],
        line_width=1,
        opacity=0.5,
        annotation_text="MEDIUM (60%)",
        annotation_position="top right",
    )

    layout = get_chart_layout(height=400)
    fig.update_layout(**layout)

    return fig


def create_performance_chart(data):
    """Multi-Axis Performance Chart"""
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(
            x=data["Month"],
            y=data["Revenue"],
            name="Revenue",
            marker=dict(
                color=COLORS["primary"],
                line=dict(color="rgba(255,255,255,0.5)", width=2),
            ),
            hovertemplate="<b>%{x}</b><br>Revenue: $%{y:,.0f}<extra></extra>",
        ),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(
            x=data["Month"],
            y=data["Profit"],
            name="Profit",
            mode="lines+markers",
            line=dict(color=COLORS["success"], width=3),
            marker=dict(size=8, line=dict(color="white", width=2)),
            hovertemplate="<b>%{x}</b><br>Profit: $%{y:,.0f}<extra></extra>",
        ),
        secondary_y=True,
    )

    layout = get_chart_layout(height=380)
    fig.update_layout(**layout)
    fig.update_yaxes(title_text="Revenue ($)", secondary_y=False)
    fig.update_yaxes(title_text="Profit ($)", secondary_y=True)

    return fig


# ============================================================================
# EXPORT FUNCTIONALITY
# ============================================================================


def generate_html_report():
    """Generate HTML Report for Download"""
    current_date = datetime.now().strftime("%B %d, %Y")

    # Convert dataframe to HTML with styling
    workflows_html = recent_workflows.to_html(
        index=False, border=0, classes="styled-table"
    )

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>BizView Executive Report - {current_date}</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet">
        <style>
            :root {{
                --navy: #0f172a;
                --primary: #3b82f6;
                --slate: #64748b;
                --border: #e2e8f0;
                --bg: #f8fafc;
            }}
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ 
                font-family: 'Inter', sans-serif; 
                color: var(--navy); 
                background: #ffffff; 
                line-height: 1.6;
                padding: 0;
            }}
            .page {{
                width: 210mm;
                min-height: 297mm;
                padding: 20mm;
                margin: 10mm auto;
                background: white;
                box-shadow: 0 0 20px rgba(0,0,0,0.1);
                position: relative;
            }}
            .header {{ 
                border-bottom: 2px solid var(--navy); 
                padding-bottom: 30px; 
                margin-bottom: 40px; 
                display: flex; 
                justify-content: space-between; 
                align-items: center; 
            }}
            .brand h1 {{ 
                font-family: 'Outfit', sans-serif; 
                font-size: 32px; 
                font-weight: 800; 
                color: var(--navy); 
                letter-spacing: -1px;
            }}
            .brand p {{ color: var(--slate); font-size: 14px; font-weight: 500; text-transform: uppercase; letter-spacing: 1px; }}
            .report-meta {{ text-align: right; }}
            .report-meta .date {{ font-size: 18px; font-weight: 700; color: var(--navy); }}
            .report-meta .confidential {{ color: #ef4444; font-size: 12px; font-weight: 700; margin-top: 5px; }}

            .grid-executive {{ 
                display: grid; 
                grid-template-columns: repeat(4, 1fr); 
                gap: 20px; 
                margin-bottom: 40px; 
            }}
            .kpi-stat {{ 
                background: var(--bg); 
                border: 1px solid var(--border); 
                border-radius: 12px; 
                padding: 20px; 
                text-align: center; 
            }}
            .kpi-stat .label {{ color: var(--slate); font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px; }}
            .kpi-stat .value {{ font-family: 'Outfit', sans-serif; font-size: 28px; font-weight: 800; color: var(--navy); }}
            .kpi-stat .trend {{ font-size: 12px; font-weight: 700; margin-top: 5px; }}
            .trend.up {{ color: #10b981; }}
            .trend.down {{ color: #ef4444; }}

            .section {{ margin-bottom: 40px; }}
            .section-title {{ 
                font-family: 'Outfit', sans-serif; 
                font-size: 20px; 
                font-weight: 700; 
                margin-bottom: 20px; 
                color: var(--navy); 
                display: flex;
                align-items: center;
                gap: 10px;
            }}
            .section-title::after {{
                content: '';
                flex: 1;
                height: 1px;
                background: var(--border);
            }}

            .two-col {{ display: grid; grid-template-columns: 1fr 1fr; gap: 40px; }}

            .summary-box {{ 
                background: var(--bg); 
                padding: 24px; 
                border-radius: 12px; 
                border-left: 4px solid var(--primary);
            }}
            .summary-box h4 {{ margin-bottom: 10px; font-size: 16px; font-weight: 700; }}
            
            .styled-table {{ 
                width: 100%; 
                border-collapse: collapse; 
                font-size: 12px; 
                margin-top: 10px;
            }}
            .styled-table thead {{ background: #f1f5f9; }}
            .styled-table th {{ padding: 12px 15px; text-align: left; font-weight: 700; color: var(--slate); text-transform: uppercase; font-size: 10px; }}
            .styled-table td {{ padding: 12px 15px; border-bottom: 1px solid var(--border); }}
            .styled-table tbody tr:nth-child(even) {{ background: #fafafa; }}

            .footer {{ 
                position: absolute;
                bottom: 20mm;
                left: 20mm;
                right: 20mm;
                padding-top: 20px; 
                border-top: 1px solid var(--border); 
                text-align: center; 
                color: var(--slate); 
                font-size: 11px; 
            }}

            @media print {{
                body {{ background: white; }}
                .page {{ margin: 0; box-shadow: none; }}
                .no-print {{ display: none; }}
            }}
        </style>
    </head>
    <body>
        <div class="page">
            <div class="header">
                <div class="brand">
                    <h1>BIZVIEW</h1>
                    <p>Executive Analytics Platform</p>
                </div>
                <div class="report-meta">
                    <div class="date">{current_date}</div>
                    <div class="confidential">RESTRICTED ACCESS • CONFIDENTIAL</div>
                </div>
            </div>
            
            <div class="section">
                <h2 class="section-title">EXECUTIVE OVERVIEW</h2>
                <div class="grid-executive">
                    <div class="kpi-stat">
                        <div class="label">Total Workflows</div>
                        <div class="value">1,247</div>
                        <div class="trend up">▲ 12.5%</div>
                    </div>
                    <div class="kpi-stat">
                        <div class="label">Gearing Ratio</div>
                        <div class="value">2.45</div>
                        <div class="trend up">▲ 8.3%</div>
                    </div>
                    <div class="kpi-stat">
                        <div class="label">Productivity</div>
                        <div class="value">87.3%</div>
                        <div class="trend up">▲ 5.2%</div>
                    </div>
                    <div class="kpi-stat">
                        <div class="label">Tech Adoption</div>
                        <div class="value">76.8%</div>
                        <div class="trend down">▼ 2.1%</div>
                    </div>
                </div>
            </div>

            <div class="two-col section">
                <div>
                    <h2 class="section-title">OPERATIONAL INSIGHTS</h2>
                    <div class="summary-box">
                        <h4>Efficiency Gains</h4>
                        <p>Streamlined automated workflows have contributed to a 12.5% increase in operational velocity. The Engineering department remains the top performer with a 92.5% completion rate.</p>
                    </div>
                </div>
                <div>
                    <h2 class="section-title">STRATEGIC ALIGNMENT</h2>
                    <p style="font-size: 14px; color: var(--slate);">Current focus is on tech adoption in the Marketing sector, which has seen a slight decline. Mitigation strategies are in place for Q3.</p>
                </div>
            </div>
            
            <div class="section">
                <h2 class="section-title">RECENT ACTIVITY LOG</h2>
                {workflows_html}
            </div>

            <div class="footer">
                <p>Generated via BizView Enterprise • Confidential Intelligence Report • Page 1 of 1</p>
                <p style="margin-top: 5px;">© {datetime.now().strftime("%Y")} Analytics Corp. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html


# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================

if "current_page" not in st.session_state:
    st.session_state.current_page = "Dashboard"

# ============================================================================
# SIDEBAR NAVIGATION
# ============================================================================

with st.sidebar:
    st.markdown(
        """
    <div style="text-align: center; padding: 1.5rem 0 2rem 0; background: linear-gradient(180deg, rgba(255,255,255,0.05) 0%, transparent 100%); border-radius: 16px; margin: 0 0.5rem;">
        <div style="position: relative; display: inline-block;">
            <div style="font-size: 3.5rem; filter: drop-shadow(0 0 20px rgba(59, 130, 246, 0.4)); animation: pulse 4s infinite;">📊</div>
        </div>
        <h2 style="color: white !important; font-size: 1.75rem !important; font-weight: 800; margin: 1rem 0 0 0; letter-spacing: -0.02em;">BizView</h2>
        <p style="color: rgba(255,255,255,0.5); font-size: 0.8rem; margin: 0.25rem 0 0 0; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 600;">Enterprise Suite</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("<hr style='margin: 2rem 0; opacity: 0.1;'>", unsafe_allow_html=True)

    st.markdown("##### 📌 NAVIGATION")

    pages = [
        ("Dashboard", "🏠"),
        ("Workflow Analytics", "📊"),
        ("Financial Metrics", "💰"),
        ("Productivity", "👥"),
        ("Tech Adoption", "💻"),
        ("Executive Summary", "📋"),
        ("Reports & Export", "📥"),
    ]

    for page_name, icon in pages:
        button_type = (
            "primary" if st.session_state.current_page == page_name else "secondary"
        )
        if st.button(f"{icon}  {page_name}", key=f"nav_{page_name}", type=button_type):
            st.session_state.current_page = page_name
            st.rerun()

    st.markdown("<hr style='margin: 2rem 0; opacity: 0.1;'>", unsafe_allow_html=True)

    st.markdown("##### ⚙️ SETTINGS")
    theme = st.selectbox("Theme", ["Light", "Dark", "Auto"], key="theme_select")
    export_format = st.selectbox(
        "Export Format", ["PDF", "Excel", "CSV"], key="export_select"
    )

    st.markdown("<hr style='margin: 2rem 0; opacity: 0.1;'>", unsafe_allow_html=True)

    st.markdown(
        """
    <div style="text-align: center; padding: 1.5rem 1rem; background: rgba(255,255,255,0.03); border-radius: 12px; margin-bottom: 1rem;">
        <div style="font-size: 0.75rem; color: rgba(255,255,255,0.5); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.5rem;">Global Action</div>
        <div style="color: white; font-size: 0.85rem; margin-bottom: 1rem;">Export current view data</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.download_button(
        "📥 Download Full Report",
        data=generate_html_report(),
        file_name=f"BizView_Global_Report_{datetime.now().strftime('%Y%m%d')}.html",
        mime="text/html",
        type="primary",
        key="global_export_btn",
        width="stretch",
    )

    st.markdown(
        f"""
    <div style="margin-top: 2rem; padding: 1.25rem; background: rgba(255,255,255,0.03); border-radius: 16px; border: 1px solid rgba(255,255,255,0.05);">
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
            <div style="width: 40px; height: 40px; border-radius: 10px; background: var(--gradient-primary); display: flex; align-items: center; justify-content: center; font-weight: 700; color: white;">JD</div>
            <div style="text-align: left;">
                <div style="color: white; font-size: 0.85rem; font-weight: 600;">John Doe</div>
                <div style="color: rgba(255,255,255,0.4); font-size: 0.7rem;">Executive Director</div>
            </div>
        </div>
        <div style="font-size: 0.7rem; color: rgba(255,255,255,0.3); border-top: 1px solid rgba(255,255,255,0.05); padding-top: 10px; display: flex; justify-content: space-between;">
            <span>BizView v2.0.4</span>
            <span style="color: #10b981;">● Online</span>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

# ============================================================================
# MAIN CONTENT AREA
# ============================================================================

# Dashboard Page
if st.session_state.current_page == "Dashboard":
    st.markdown("# 🏠 Executive Dashboard")
    st.markdown(
        "<p style='color: #64748b; font-size: 1.125rem; margin-bottom: 2rem;'>Comprehensive overview of all key metrics and performance indicators</p>",
        unsafe_allow_html=True,
    )

    # KPI Cards Row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card(
            kpi_data["workflow_count"]["label"],
            kpi_data["workflow_count"]["value"],
            kpi_data["workflow_count"]["change"],
            kpi_data["workflow_count"]["trend"],
            "number",
            kpi_data["workflow_count"]["icon"],
            0,
        )
    with col2:
        render_kpi_card(
            kpi_data["volume_gearing_ratio"]["label"],
            kpi_data["volume_gearing_ratio"]["value"],
            kpi_data["volume_gearing_ratio"]["change"],
            kpi_data["volume_gearing_ratio"]["trend"],
            "ratio",
            kpi_data["volume_gearing_ratio"]["icon"],
            0.1,
        )
    with col3:
        render_kpi_card(
            kpi_data["productivity"]["label"],
            kpi_data["productivity"]["value"],
            kpi_data["productivity"]["change"],
            kpi_data["productivity"]["trend"],
            "percentage",
            kpi_data["productivity"]["icon"],
            0.2,
        )
    with col4:
        render_kpi_card(
            kpi_data["tech_adoption"]["label"],
            kpi_data["tech_adoption"]["value"],
            kpi_data["tech_adoption"]["change"],
            kpi_data["tech_adoption"]["trend"],
            "percentage",
            kpi_data["tech_adoption"]["icon"],
            0.3,
        )

    st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

    # Charts Row 1
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("WORKFLOW TRENDS", "Monthly completion rates by status")
        st.plotly_chart(
            create_workflow_bar_chart(workflow_trend_data),
            width="stretch",
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("DEPARTMENT SPLIT", "Workflow distribution")
        st.plotly_chart(
            create_donut_chart(department_breakdown),
            width="stretch",
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # Charts Row 2
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("FINANCIAL PERFORMANCE", "Revenue & Profit Analysis")
        st.plotly_chart(
            create_performance_chart(monthly_performance),
            width="stretch",
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("GEARING RATIO TREND", "Quarterly progression vs benchmark")
        st.plotly_chart(
            create_area_chart(volume_gearing_data),
            width="stretch",
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # Executive Summaries
    st.markdown(
        "<h3 style='margin: 2.5rem 0 1.5rem 0;'>📋 Executive Insights</h3>",
        unsafe_allow_html=True,
    )
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            '<div class="chart-card" style="padding:0;">', unsafe_allow_html=True
        )
        render_chart_header(
            "HIERARCHICAL BREAKDOWN", "Share of operations by department"
        )
        st.plotly_chart(
            create_sunburst_chart(),
            width="stretch",
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div style='height:2rem;'></div>", unsafe_allow_html=True)
        render_summary_card(executive_summaries[0])
        st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)
        render_summary_card(executive_summaries[2])
    with col2:
        st.markdown(
            '<div class="chart-card" style="padding:0;">', unsafe_allow_html=True
        )
        render_chart_header("DEPARTMENTAL PERFORMANCE", "Comparative efficiency radar")
        st.plotly_chart(
            create_radar_chart(),
            width="stretch",
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div style='height:2rem;'></div>", unsafe_allow_html=True)
        render_summary_card(executive_summaries[1])
        st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)
        render_summary_card(executive_summaries[3])

    # Recent Workflows Table
    st.markdown(
        "<h3 style='margin: 2.5rem 0 1.5rem 0;'>📝 Recent Workflows</h3>",
        unsafe_allow_html=True,
    )
    render_aesthetic_table(recent_workflows, "dash_workflows", height=400)

# Workflow Analytics Page
elif st.session_state.current_page == "Workflow Analytics":
    st.markdown("# 📊 Workflow Analytics")
    st.markdown(
        "<p style='color: #64748b; font-size: 1.125rem; margin-bottom: 2rem;'>Detailed analysis of workflow performance and efficiency</p>",
        unsafe_allow_html=True,
    )

    # KPI Summary
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card("Total Workflows", 1247, 12.5, "up", "number", "📊", 0)
    with col2:
        render_kpi_card("Completed", 1098, 15.2, "up", "number", "✅", 0.1)
    with col3:
        render_kpi_card("Pending", 89, -8.3, "down", "number", "⏳", 0.2)
    with col4:
        render_kpi_card("Failed", 60, -12.1, "down", "number", "❌", 0.3)

    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

    # V11: New Visualization Grid
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("DEPT PERFORMANCE RADAR", "Balanced scorecard metrics")
        st.plotly_chart(
            create_radar_chart(),
            width="stretch",
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header(
            "WORKFLOW FLOW (SANKEY 2.0)", "Department to Status distribution"
        )
        st.plotly_chart(
            create_sankey_chart(),
            width="stretch",
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header(
            "MONTHLY WORKFLOW DISTRIBUTION", "Status breakdown over time"
        )
        st.plotly_chart(
            create_workflow_bar_chart(workflow_trend_data),
            width="stretch",
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("COMPLETION TREND", "Success rate progression")
        st.plotly_chart(
            create_line_chart(
                workflow_trend_data,
                "Month",
                "Completed",
                "Completed",
                COLORS["success"],
            ),
            width="stretch",
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_header("WORKFLOW EXECUTION LOG", "Detailed activity history")

    # V12: Aesthetic Filtered Table
    render_aesthetic_table(recent_workflows, "work_log_v12", height=400)
    st.markdown("</div>", unsafe_allow_html=True)

# Financial Metrics Page
elif st.session_state.current_page == "Financial Metrics":
    st.markdown("# 💰 Financial Metrics")
    st.markdown(
        "<p style='color: #64748b; font-size: 1.125rem; margin-bottom: 2rem;'>Financial performance analysis and volume gearing metrics</p>",
        unsafe_allow_html=True,
    )

    total_revenue = monthly_performance["Revenue"].sum()
    total_profit = monthly_performance["Profit"].sum()
    profit_margin = (total_profit / total_revenue) * 100

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card("Gearing Ratio", 2.45, 8.3, "up", "ratio", "📈", 0)
    with col2:
        render_kpi_card(
            "Total Revenue", total_revenue, 18.5, "up", "currency", "💰", 0.1
        )
    with col3:
        render_kpi_card("Total Profit", total_profit, 24.2, "up", "currency", "💵", 0.2)
    with col4:
        render_kpi_card(
            "Profit Margin", round(profit_margin, 1), 5.8, "up", "percentage", "📊", 0.3
        )

    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header(
            "VOLUME GEARING ANALYSIS", "Quarterly performance vs benchmark"
        )
        st.plotly_chart(
            create_area_chart(volume_gearing_data),
            width="stretch",
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("REVENUE DISTRIBUTION", "By department")
        st.plotly_chart(
            create_donut_chart(department_breakdown),
            width="stretch",
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_header(
        "FINANCIAL PERFORMANCE OVERVIEW", "Monthly revenue and profit trends"
    )
    st.plotly_chart(
        create_performance_chart(monthly_performance),
        width="stretch",
        config=get_chart_config(),
    )
    st.markdown("</div>", unsafe_allow_html=True)

# Productivity Page
elif st.session_state.current_page == "Productivity":
    st.markdown("# 👥 Productivity Metrics")
    st.markdown(
        "<p style='color: #64748b; font-size: 1.125rem; margin-bottom: 2rem;'>Department-wise productivity analysis and performance tracking</p>",
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
            width="stretch",
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
            width="stretch",
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

# Tech Adoption Page
elif st.session_state.current_page == "Tech Adoption":
    st.markdown("# 💻 Technology Adoption")
    st.markdown(
        "<p style='color: #64748b; font-size: 1.125rem; margin-bottom: 2rem;'>Technology stack adoption rates and utilization metrics</p>",
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
        width="stretch",
        config=get_chart_config(),
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_header(
        "TECHNOLOGY STACK DETAILS", "Complete tool inventory with adoption metrics"
    )

    # Style the dataframe with colored badges
    styled_data = tech_adoption_data.copy()
    styled_data["Status"] = styled_data["Adoption"].apply(
        lambda x: "🟢 High" if x >= 80 else "🟡 Medium" if x >= 60 else "🔴 Low"
    )
    st.dataframe(styled_data, width="stretch", hide_index=True, height=400)
    st.markdown("</div>", unsafe_allow_html=True)

    # Action Items
    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        low_tools = tech_adoption_data[tech_adoption_data["Adoption"] < 60]
        st.markdown(
            f"""
        <div class="summary-card">
            <div class="summary-card-icon">⚠️</div>
            <div class="summary-card-title">Focus Areas</div>
            <div class="summary-card-content">
                {"".join(f'<p style="margin: 8px 0;">• {row["Tool"]} - {row["Adoption"]}% adoption</p>' for _, row in low_tools.iterrows())}
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        high_tools = tech_adoption_data[tech_adoption_data["Adoption"] >= 90]
        st.markdown(
            f"""
        <div class="insight-card">
            <h4>TOP PERFORMERS</h4>
            <div style="margin-top: 1rem;">
                {"".join(f'<p style="margin: 12px 0; color: {COLORS["success"]}; font-weight: 600;">✅ {row["Tool"]} - {row["Adoption"]}%</p>' for _, row in high_tools.iterrows())}
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

# Executive Summary Page
elif st.session_state.current_page == "Executive Summary":
    current_date = datetime.now().strftime("%A, %B %d, %Y")

    st.markdown(
        f"""
    <div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #475569 100%); 
                color: white; 
                border-radius: 28px; 
                padding: 3rem; 
                margin-bottom: 2.5rem; 
                position: relative; 
                overflow: hidden;
                box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25);">
        <div style="position: absolute; top: -50%; right: -20%; width: 60%; height: 200%; 
                    background: radial-gradient(circle, rgba(59, 130, 246, 0.2) 0%, transparent 70%);
                    animation: rotateGradient 15s linear infinite;"></div>
        <div style="position: relative; z-index: 1;">
            <p style="color: #fbbf24; font-size: 14px; font-weight: 700; letter-spacing: 0.15em; margin-bottom: 16px; text-transform: uppercase;">
                📅 {current_date}
            </p>
            <h1 style="color: white !important; margin-bottom: 20px; font-size: 2.5rem; font-weight: 900; letter-spacing: -0.04em;">
                Executive Summary Report
            </h1>
            <p style="color: rgba(255,255,255,0.8); max-width: 800px; line-height: 1.8; font-size: 1.125rem;">
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
            <div class="insight-card" style="text-align: center; padding: 2rem;">
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

    # Action Items
    st.markdown(
        "<h2 style='margin: 3rem 0 2rem 0;'>🎯 Strategic Action Items</h2>",
        unsafe_allow_html=True,
    )
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
        <div class="insight-card">
            <h4>🚀 PRIORITIES</h4>
            <div style="margin-top: 1.5rem;">
                <div style="display: flex; gap: 1rem; padding: 1.25rem; background: linear-gradient(135deg, {COLORS["primary"]}15, {COLORS["accent"]}10); border-radius: 12px; margin-bottom: 1rem; border-left: 4px solid {COLORS["primary"]};">
                    <div style="font-size: 1.5rem; font-weight: 900; color: {COLORS["primary"]};">1</div>
                    <div>
                        <div style="font-weight: 700; margin-bottom: 0.5rem; color: {COLORS["navy"]};">Accelerate AI Adoption</div>
                        <div style="font-size: 0.875rem; color: {COLORS["gray"]};">Implement training programs to increase AI assistant adoption from 45% to 70%</div>
                    </div>
                </div>
                <div style="display: flex; gap: 1rem; padding: 1.25rem; background: linear-gradient(135deg, {COLORS["success"]}15, {COLORS["accent"]}10); border-radius: 12px; margin-bottom: 1rem; border-left: 4px solid {COLORS["success"]};">
                    <div style="font-size: 1.5rem; font-weight: 900; color: {COLORS["success"]};">2</div>
                    <div>
                        <div style="font-weight: 700; margin-bottom: 0.5rem; color: {COLORS["navy"]};">Scale Automation</div>
                        <div style="font-size: 0.875rem; color: {COLORS["gray"]};">Expand workflow automation to reduce manual processing by 30%</div>
                    </div>
                </div>
                <div style="display: flex; gap: 1rem; padding: 1.25rem; background: linear-gradient(135deg, {COLORS["warning"]}15, {COLORS["accent"]}10); border-radius: 12px; border-left: 4px solid {COLORS["warning"]};">
                    <div style="font-size: 1.5rem; font-weight: 900; color: {COLORS["warning"]};">3</div>
                    <div>
                        <div style="font-weight: 700; margin-bottom: 0.5rem; color: {COLORS["navy"]};">Department Alignment</div>
                        <div style="font-size: 0.875rem; color: {COLORS["gray"]};">Focus on HR and Marketing to bring productivity above target</div>
                    </div>
                </div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
        <div class="insight-card">
            <h4>🏆 KEY ACHIEVEMENTS</h4>
            <div style="margin-top: 1.5rem;">
                <div style="padding: 1.25rem; background: linear-gradient(135deg, {COLORS["success"]}15, {COLORS["success"]}05); border-radius: 12px; margin-bottom: 1rem; border: 2px solid {COLORS["success"]}30;">
                    <div style="font-weight: 700; margin-bottom: 0.5rem; color: {COLORS["success"]};">✅ 12.5% Workflow Growth</div>
                    <div style="font-size: 0.875rem; color: {COLORS["gray"]};">Exceeded quarterly targets with significant efficiency gains</div>
                </div>
                <div style="padding: 1.25rem; background: linear-gradient(135deg, {COLORS["primary"]}15, {COLORS["primary"]}05); border-radius: 12px; margin-bottom: 1rem; border: 2px solid {COLORS["primary"]}30;">
                    <div style="font-weight: 700; margin-bottom: 0.5rem; color: {COLORS["primary"]};">✅ Gearing Ratio Above Benchmark</div>
                    <div style="font-size: 0.875rem; color: {COLORS["gray"]};">Achieved 2.45 vs 2.2 industry standard</div>
                </div>
                <div style="padding: 1.25rem; background: linear-gradient(135deg, {COLORS["accent"]}15, {COLORS["accent"]}05); border-radius: 12px; border: 2px solid {COLORS["accent"]}30;">
                    <div style="font-weight: 700; margin-bottom: 0.5rem; color: {COLORS["accent"]};">✅ Engineering Excellence</div>
                    <div style="font-size: 0.875rem; color: {COLORS["gray"]};">Engineering department achieved 92.5% productivity score</div>
                </div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

# Reports & Export Page
elif st.session_state.current_page == "Reports & Export":
    st.markdown("# 📥 Reports & Export")
    st.markdown(
        "<p style='color: #64748b; font-size: 1.125rem; margin-bottom: 2.5rem;'>Download comprehensive reports and export data in multiple formats</p>",
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
        <div class="insight-card" style="padding: 2rem;">
            <div style="width: 64px; height: 64px; background: linear-gradient(135deg, {COLORS["navy"]}, {COLORS["primary"]}); 
                        border-radius: 18px; display: flex; align-items: center; justify-content: center; 
                        margin-bottom: 1.5rem; box-shadow: 0 8px 24px rgba(15, 23, 42, 0.25);">
                <span style="font-size: 2rem;">📄</span>
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
            width="stretch",
        )

    with col2:
        st.markdown(
            f"""
        <div class="insight-card" style="padding: 2rem;">
            <div style="width: 64px; height: 64px; background: linear-gradient(135deg, {COLORS["success"]}, {COLORS["accent"]}); 
                        border-radius: 18px; display: flex; align-items: center; justify-content: center; 
                        margin-bottom: 1.5rem; box-shadow: 0 8px 24px rgba(16, 185, 129, 0.25);">
                <span style="font-size: 2rem;">📊</span>
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
            width="stretch",
        )

    with col3:
        st.markdown(
            f"""
        <div class="insight-card" style="padding: 2rem;">
            <div style="width: 64px; height: 64px; background: linear-gradient(135deg, {COLORS["warning"]}, {COLORS["error"]}); 
                        border-radius: 18px; display: flex; align-items: center; justify-content: center; 
                        margin-bottom: 1.5rem; box-shadow: 0 8px 24px rgba(245, 158, 11, 0.25);">
                <span style="font-size: 2rem;">📋</span>
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
            width="stretch",
        )

    # Report Preview
    st.markdown(
        "<hr style='margin: 3rem 0; border: none; height: 1px; background: linear-gradient(90deg, transparent, #e2e8f0, transparent);'>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h2 style='margin-bottom: 2rem;'>📄 Report Preview</h2>",
        unsafe_allow_html=True,
    )

    current_date = datetime.now().strftime("%B %d, %Y")

    st.markdown(
        f"""
    <div style="background: white; border: 2px solid #e2e8f0; border-radius: 20px; padding: 3rem; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 3px solid {COLORS["navy"]}; padding-bottom: 2rem; margin-bottom: 2.5rem;">
            <div>
                <h1 style="margin: 0; font-size: 2rem; color: {COLORS["navy"]} !important;">📊 BizView Executive Report</h1>
                <p style="color: {COLORS["gray"]}; margin-top: 0.75rem; font-size: 1rem;">Enterprise Analytics Platform</p>
            </div>
            <div style="text-align: right; background: linear-gradient(135deg, {COLORS["primary"]}15, {COLORS["accent"]}10); padding: 1rem 1.5rem; border-radius: 12px;">
                <p style="color: {COLORS["gray"]}; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.5rem;">Generated</p>
                <p style="color: {COLORS["navy"]}; font-weight: 700; font-size: 1.125rem; margin: 0;">{current_date}</p>
            </div>
        </div>

        <h3 style="color: {COLORS["navy"]}; font-size: 1.25rem; margin-bottom: 1.5rem;">Key Performance Indicators</h3>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.5rem; margin-bottom: 2.5rem;">
            <div style="background: linear-gradient(135deg, #f8fafc, #ffffff); padding: 1.5rem; border-radius: 16px; text-align: center; border: 1px solid #e2e8f0;">
                <p style="font-family: 'Outfit', sans-serif; font-size: 2rem; font-weight: 800; color: {COLORS["navy"]}; margin: 0;">1,247</p>
                <p style="color: {COLORS["gray"]}; font-size: 0.75rem; font-weight: 600; margin: 0.5rem 0 0 0; text-transform: uppercase; letter-spacing: 0.05em;">Total Workflows</p>
                <p style="color: {COLORS["success"]}; font-size: 0.875rem; margin: 0.5rem 0 0 0; font-weight: 700;">↗ 12.5%</p>
            </div>
            <div style="background: linear-gradient(135deg, #f8fafc, #ffffff); padding: 1.5rem; border-radius: 16px; text-align: center; border: 1px solid #e2e8f0;">
                <p style="font-family: 'Outfit', sans-serif; font-size: 2rem; font-weight: 800; color: {COLORS["navy"]}; margin: 0;">2.45</p>
                <p style="color: {COLORS["gray"]}; font-size: 0.75rem; font-weight: 600; margin: 0.5rem 0 0 0; text-transform: uppercase; letter-spacing: 0.05em;">Gearing Ratio</p>
                <p style="color: {COLORS["success"]}; font-size: 0.875rem; margin: 0.5rem 0 0 0; font-weight: 700;">↗ 8.3%</p>
            </div>
            <div style="background: linear-gradient(135deg, #f8fafc, #ffffff); padding: 1.5rem; border-radius: 16px; text-align: center; border: 1px solid #e2e8f0;">
                <p style="font-family: 'Outfit', sans-serif; font-size: 2rem; font-weight: 800; color: {COLORS["navy"]}; margin: 0;">87.3%</p>
                <p style="color: {COLORS["gray"]}; font-size: 0.75rem; font-weight: 600; margin: 0.5rem 0 0 0; text-transform: uppercase; letter-spacing: 0.05em;">Productivity</p>
                <p style="color: {COLORS["success"]}; font-size: 0.875rem; margin: 0.5rem 0 0 0; font-weight: 700;">↗ 5.2%</p>
            </div>
            <div style="background: linear-gradient(135deg, #f8fafc, #ffffff); padding: 1.5rem; border-radius: 16px; text-align: center; border: 1px solid #e2e8f0;">
                <p style="font-family: 'Outfit', sans-serif; font-size: 2rem; font-weight: 800; color: {COLORS["navy"]}; margin: 0;">76.8%</p>
                <p style="color: {COLORS["gray"]}; font-size: 0.75rem; font-weight: 600; margin: 0.5rem 0 0 0; text-transform: uppercase; letter-spacing: 0.05em;">Tech Adoption</p>
                <p style="color: {COLORS["error"]}; font-size: 0.875rem; margin: 0.5rem 0 0 0; font-weight: 700;">↘ 2.1%</p>
            </div>
        </div>

        <p style="text-align: center; color: {COLORS["gray"]}; font-size: 0.875rem; margin-top: 2.5rem; padding-top: 2rem; border-top: 1px solid #e2e8f0;">
            BizView Analytics Platform • Enterprise Edition • Confidential
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("<div style='height: 3rem;'></div>", unsafe_allow_html=True)
st.markdown(
    f"""
<div style="text-align: center; padding: 2rem; background: rgba(255,255,255,0.8); backdrop-filter: blur(10px); border-radius: 20px; border: 1px solid #e2e8f0;">
    <p style="color: {COLORS["gray"]}; font-size: 0.875rem; margin-bottom: 0.5rem;">
        <strong>BizView Executive Dashboard</strong> • Ultra Premium Edition
    </p>
    <p style="color: {COLORS["gray"]}; font-size: 0.75rem;">
        Powered by Streamlit • {datetime.now().strftime("%Y")} • All Rights Reserved
    </p>
</div>
""",
    unsafe_allow_html=True,
)
