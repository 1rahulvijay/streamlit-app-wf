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
import numpy as np
from datetime import datetime, timedelta
import io

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

    /* ========== GLOBAL RESETS ========== */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }

    /* Hide Streamlit Branding */
    #MainMenu, footer, header, .stDeployButton {visibility: hidden !important;}
    [data-testid="stToolbar"] {display: none !important;}
    
    /* ========== MAIN APP BACKGROUND ========== */
    .stApp {
        background: linear-gradient(180deg, #f8fafc 0%, #ffffff 50%, #f8fafc 100%);
        background-attachment: fixed;
    }
    
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: var(--gradient-mesh);
        opacity: 0.5;
        pointer-events: none;
        z-index: 0;
    }

    .main .block-container {
        padding: 2rem 3rem;
        max-width: 1920px;
        margin: 0 auto;
        position: relative;
        z-index: 1;
    }

    /* ========== SIDEBAR - PREMIUM GLASSMORPHISM ========== */
    [data-testid="stSidebar"] {
        background: var(--gradient-navy) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08);
        position: relative;
        overflow: hidden;
    }

    /* Animated Background Pattern */
    [data-testid="stSidebar"]::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: 
            radial-gradient(circle at 20% 50%, rgba(59, 130, 246, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 80% 80%, rgba(139, 92, 246, 0.15) 0%, transparent 50%);
        animation: gradientShift 10s ease infinite;
        pointer-events: none;
    }

    @keyframes gradientShift {
        0%, 100% { opacity: 0.5; transform: scale(1); }
        50% { opacity: 0.8; transform: scale(1.1); }
    }

    /* Sidebar Content */
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1rem;
        position: relative;
        z-index: 1;
    }

    [data-testid="stSidebar"] .stMarkdown,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label {
        color: rgba(255, 255, 255, 0.9) !important;
    }

    /* Sidebar Navigation Buttons - React Style */
    [data-testid="stSidebar"] .stButton > button {
        width: 100%;
        background: transparent !important;
        color: rgba(255, 255, 255, 0.7) !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.875rem 1.25rem !important;
        margin: 0.35rem 0 !important;
        font-size: 0.9rem !important;
        font-weight: 500 !important;
        text-align: left !important;
        justify-content: flex-start !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        position: relative;
        overflow: hidden;
    }

    [data-testid="stSidebar"] .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 0;
        height: 100%;
        background: linear-gradient(90deg, rgba(59, 130, 246, 0.2), rgba(139, 92, 246, 0.2));
        transition: width 0.3s ease;
        z-index: -1;
    }

    [data-testid="stSidebar"] .stButton > button:hover {
        color: white !important;
        transform: translateX(6px);
        background: rgba(255, 255, 255, 0.08) !important;
    }

    [data-testid="stSidebar"] .stButton > button:hover::before {
        width: 100%;
    }

    /* Active Navigation Button */
    [data-testid="stSidebar"] .stButton > button[kind="primary"] {
        background: linear-gradient(90deg, rgba(59, 130, 246, 0.25), rgba(139, 92, 246, 0.15)) !important;
        color: white !important;
        border-left: 3px solid #f59e0b !important;
        border-radius: 0 12px 12px 0 !important;
        font-weight: 600 !important;
        box-shadow: var(--shadow-md);
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

    /* ========== KPI CARDS - ULTRA PREMIUM GLASSMORPHISM ========== */
    .kpi-card {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.5);
        border-radius: 24px;
        padding: 2rem;
        position: relative;
        overflow: hidden;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: var(--shadow-lg);
        animation: fadeInUp 0.6s ease-out backwards;
    }

    /* Glass Reflection Effect */
    .kpi-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 50%;
        background: linear-gradient(180deg, rgba(255, 255, 255, 0.8) 0%, transparent 100%);
        opacity: 0.4;
        pointer-events: none;
    }

    /* Top Accent Bar */
    .kpi-card::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: var(--gradient-blue);
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    .kpi-card:hover {
        transform: translateY(-12px) scale(1.02);
        box-shadow: var(--shadow-2xl), var(--shadow-glow-blue);
        border-color: rgba(59, 130, 246, 0.3);
    }

    .kpi-card:hover::after {
        opacity: 1;
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
        margin-bottom: 1.5rem;
        position: relative;
        transition: all 0.4s ease;
        box-shadow: var(--shadow-md);
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

    /* KPI Value - Premium Typography */
    .kpi-value {
        font-family: 'Outfit', sans-serif !important;
        font-size: 3rem !important;
        font-weight: 900 !important;
        line-height: 1 !important;
        letter-spacing: -0.04em !important;
        background: linear-gradient(135deg, var(--navy-900) 0%, var(--navy-600) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0.75rem 0;
        animation: countUp 1s ease-out;
    }

    @keyframes countUp {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .kpi-label {
        font-size: 0.95rem;
        font-weight: 600;
        color: var(--gray-500);
        letter-spacing: 0.02em;
        margin-top: 0.5rem;
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
        margin-top: 1.25rem;
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

    /* ========== CHART CARDS - MODERN & CLEAN ========== */
    .chart-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(226, 232, 240, 0.6);
        border-radius: 24px;
        overflow: hidden;
        box-shadow: var(--shadow-lg);
        transition: all 0.3s ease;
        animation: fadeInUp 0.7s ease-out backwards;
        margin-bottom: 2rem;
    }

    .chart-card:hover {
        box-shadow: var(--shadow-xl);
        transform: translateY(-4px);
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

    .chart-card-title {
        font-family: 'Outfit', sans-serif !important;
        font-size: 0.875rem !important;
        font-weight: 800 !important;
        color: var(--navy-900) !important;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin: 0 !important;
    }

    .chart-card-subtitle {
        font-size: 0.8rem;
        color: var(--gray-500);
        margin-top: 0.35rem;
        font-weight: 500;
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
        animation: fadeInUp 0.8s ease-out backwards;
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
        animation: fadeIn 0.6s ease-out backwards;
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

    /* ========== ANIMATIONS ========== */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeInLeft {
        from {
            opacity: 0;
            transform: translateX(-30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(20px);
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
            opacity: 0.9;
            transform: scale(1.02);
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

    /* ========== DATAFRAMES ========== */
    .dataframe {
        font-family: 'Inter', sans-serif !important;
        font-size: 0.9rem !important;
        border-radius: 16px !important;
        overflow: hidden !important;
        box-shadow: var(--shadow-sm) !important;
    }

    .dataframe thead tr th {
        font-family: 'Outfit', sans-serif !important;
        font-size: 0.75rem !important;
        font-weight: 800 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
        color: var(--gray-600) !important;
        background: linear-gradient(180deg, var(--gray-50), var(--white)) !important;
        padding: 1.25rem 1.5rem !important;
    }

    .dataframe tbody tr td {
        padding: 1.25rem 1.5rem !important;
        border-bottom: 1px solid var(--gray-100) !important;
    }

    .dataframe tbody tr:hover {
        background: var(--gray-50) !important;
    }

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

    /* ========== SPACING UTILITIES ========== */
    .mt-1 { margin-top: 0.5rem; }
    .mt-2 { margin-top: 1rem; }
    .mt-3 { margin-top: 1.5rem; }
    .mt-4 { margin-top: 2rem; }
    .mb-1 { margin-bottom: 0.5rem; }
    .mb-2 { margin-bottom: 1rem; }
    .mb-3 { margin-bottom: 1.5rem; }
    .mb-4 { margin-bottom: 2rem; }

    /* ========== RESPONSIVE OPTIMIZATIONS ========== */
    @media (max-width: 1920px) {
        .main .block-container {
            padding: 1.5rem 2rem;
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


# Plotly Template for 4K Rendering
def get_chart_config():
    return {
        "displayModeBar": False,
        "responsive": True,
    }


def get_chart_layout(title="", height=400):
    return {
        "title": {
            "text": title,
            "font": {
                "family": "Outfit, sans-serif",
                "size": 16,
                "color": "#0f172a",
                "weight": 700,
            },
            "x": 0,
            "xanchor": "left",
        },
        "height": height,
        "margin": {"l": 20, "r": 20, "t": 60, "b": 60},
        "plot_bgcolor": "rgba(0,0,0,0)",
        "paper_bgcolor": "rgba(0,0,0,0)",
        "font": {"family": "Inter, sans-serif", "size": 12, "color": "#64748b"},
        "hoverlabel": {
            "bgcolor": "white",
            "font_size": 13,
            "font_family": "Inter, sans-serif",
            "bordercolor": "#e2e8f0",
        },
        "xaxis": {
            "showgrid": False,
            "showline": True,
            "linecolor": "#e2e8f0",
            "linewidth": 2,
            "tickfont": {"size": 11, "color": "#94a3b8"},
        },
        "yaxis": {
            "showgrid": True,
            "gridcolor": "#f1f5f9",
            "gridwidth": 1,
            "showline": False,
            "tickfont": {"size": 11, "color": "#94a3b8"},
        },
        "legend": {
            "orientation": "h",
            "yanchor": "bottom",
            "y": -0.3,
            "xanchor": "center",
            "x": 0.5,
            "font": {"size": 11},
        },
    }


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


# ============================================================================
# CHART COMPONENTS - D3-STYLE WITH ANIMATIONS
# ============================================================================


def create_workflow_bar_chart(data):
    """Animated Stacked Bar Chart"""
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            name="Completed",
            x=data["Month"],
            y=data["Completed"],
            marker=dict(
                color=COLORS["success"],
                line=dict(color="rgba(255,255,255,0.5)", width=2),
            ),
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
                line=dict(color="rgba(255,255,255,0.5)", width=2),
            ),
            hovertemplate="<b>%{x}</b><br>Pending: %{y}<extra></extra>",
        )
    )

    fig.add_trace(
        go.Bar(
            name="Failed",
            x=data["Month"],
            y=data["Failed"],
            marker=dict(
                color=COLORS["error"], line=dict(color="rgba(255,255,255,0.5)", width=2)
            ),
            hovertemplate="<b>%{x}</b><br>Failed: %{y}<extra></extra>",
        )
    )

    layout = get_chart_layout(height=380)
    layout.update(
        {
            "barmode": "stack",
            "bargap": 0.2,
        }
    )
    fig.update_layout(**layout)

    return fig


def create_donut_chart(data):
    """Premium Donut Chart with Gradient Effect"""
    colors = [
        COLORS["primary"],
        COLORS["accent"],
        COLORS["success"],
        COLORS["warning"],
        COLORS["secondary"],
    ]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=data["Department"],
                values=data["Value"],
                hole=0.65,
                marker=dict(colors=colors, line=dict(color="white", width=3)),
                textposition="outside",
                textinfo="label+percent",
                textfont=dict(size=12, family="Inter, sans-serif"),
                hovertemplate="<b>%{label}</b><br>%{value}%<br>%{percent}<extra></extra>",
            )
        ]
    )

    layout = get_chart_layout(height=380)
    layout.update(
        {
            "showlegend": False,
            "annotations": [
                {
                    "text": f"<b>{data['Value'].sum()}%</b><br><span style='font-size:11px; color:#94a3b8;'>Total</span>",
                    "x": 0.5,
                    "y": 0.5,
                    "font": {
                        "size": 24,
                        "family": "Outfit, sans-serif",
                        "color": "#0f172a",
                    },
                    "showarrow": False,
                }
            ],
        }
    )
    fig.update_layout(**layout)

    return fig


def create_line_chart(data, x_col, y_col, name, color):
    """Smooth Line Chart with Area Fill"""
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=data[x_col],
            y=data[y_col],
            mode="lines+markers",
            name=name,
            line=dict(color=color, width=3, shape="spline"),
            marker=dict(size=8, color=color, line=dict(color="white", width=2)),
            fill="tozeroy",
            fillcolor=f"rgba({int(color[1:3], 16)}, {int(color[3:5], 16)}, {int(color[5:7], 16)}, 0.1)",
            hovertemplate="<b>%{x}</b><br>" + name + ": %{y}<extra></extra>",
        )
    )

    layout = get_chart_layout(height=380)
    fig.update_layout(**layout)

    return fig


def create_area_chart(data):
    """Multi-Series Area Chart"""
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=data["Quarter"],
            y=data["Ratio"],
            mode="lines+markers",
            name="Actual Ratio",
            line=dict(color=COLORS["primary"], width=3),
            marker=dict(size=10, symbol="circle"),
            fill="tozeroy",
            fillcolor="rgba(59, 130, 246, 0.2)",
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
    """Horizontal Bar Chart with Target Comparison"""
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
                line=dict(color="rgba(255,255,255,0.5)", width=2),
            ),
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
                color=COLORS["navy"],
                symbol="diamond",
                line=dict(color="white", width=2),
            ),
            hovertemplate="<b>%{y}</b><br>Target: %{x}%<extra></extra>",
        )
    )

    layout = get_chart_layout(height=380)
    fig.update_layout(**layout)

    return fig


def create_tech_adoption_chart(data):
    """Tech Adoption Chart with Threshold Lines"""
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
                color=colors, line=dict(color="rgba(255,255,255,0.5)", width=2)
            ),
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
        line_width=2,
        annotation_text="High (80%)",
        annotation_position="right",
    )
    fig.add_hline(
        y=60,
        line_dash="dash",
        line_color=COLORS["warning"],
        line_width=2,
        annotation_text="Medium (60%)",
        annotation_position="right",
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

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>BizView Executive Report - {current_date}</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet">
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ font-family: 'Inter', sans-serif; color: #0f172a; background: #ffffff; padding: 3rem; }}
            .header {{ border-bottom: 4px solid #0f172a; padding-bottom: 2rem; margin-bottom: 3rem; }}
            .header h1 {{ font-family: 'Outfit', sans-serif; font-size: 2.5rem; font-weight: 800; margin-bottom: 0.5rem; }}
            .header .subtitle {{ color: #64748b; font-size: 1.125rem; }}
            .kpi-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; margin-bottom: 3rem; }}
            .kpi-card {{ background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 16px; padding: 2rem; text-align: center; }}
            .kpi-card .value {{ font-family: 'Outfit', sans-serif; font-size: 2.5rem; font-weight: 800; color: #0f172a; margin: 0.5rem 0; }}
            .kpi-card .label {{ color: #64748b; font-size: 0.875rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }}
            .kpi-card .change {{ display: inline-block; margin-top: 0.75rem; padding: 0.5rem 1rem; border-radius: 100px; font-size: 0.875rem; font-weight: 700; }}
            .kpi-card .change.positive {{ background: #d1fae5; color: #065f46; }}
            .kpi-card .change.negative {{ background: #fee2e2; color: #991b1b; }}
            .section {{ margin-bottom: 3rem; }}
            .section h2 {{ font-family: 'Outfit', sans-serif; font-size: 1.5rem; font-weight: 700; margin-bottom: 1rem; }}
            .footer {{ margin-top: 4rem; padding-top: 2rem; border-top: 1px solid #e2e8f0; text-align: center; color: #94a3b8; font-size: 0.875rem; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>📊 BizView Executive Dashboard Report</h1>
            <div class="subtitle">Generated on {current_date}</div>
        </div>
        
        <div class="section">
            <h2>Key Performance Indicators</h2>
            <div class="kpi-grid">
                <div class="kpi-card">
                    <div class="label">Total Workflows</div>
                    <div class="value">1,247</div>
                    <div class="change positive">↗ 12.5%</div>
                </div>
                <div class="kpi-card">
                    <div class="label">Gearing Ratio</div>
                    <div class="value">2.45</div>
                    <div class="change positive">↗ 8.3%</div>
                </div>
                <div class="kpi-card">
                    <div class="label">Productivity</div>
                    <div class="value">87.3%</div>
                    <div class="change positive">↗ 5.2%</div>
                </div>
                <div class="kpi-card">
                    <div class="label">Tech Adoption</div>
                    <div class="value">76.8%</div>
                    <div class="change negative">↘ 2.1%</div>
                </div>
            </div>
        </div>
        
        <div class="footer">
            <p>BizView Analytics Platform | Enterprise Edition | Confidential</p>
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
    <div style="text-align: center; padding: 2rem 0 3rem 0;">
        <div style="font-size: 3rem; margin-bottom: 1rem;">📊</div>
        <h2 style="color: white; font-size: 1.5rem; font-weight: 800; margin: 0;">BizView</h2>
        <p style="color: rgba(255,255,255,0.6); font-size: 0.875rem; margin-top: 0.5rem;">Executive Dashboard</p>
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
        f"""
    <div style="text-align: center; padding: 1rem; background: rgba(255,255,255,0.05); border-radius: 12px;">
        <div style="font-size: 0.75rem; color: rgba(255,255,255,0.5); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.5rem;">Last Updated</div>
        <div style="font-size: 0.875rem; color: rgba(255,255,255,0.9); font-weight: 600;">{datetime.now().strftime("%B %d, %Y")}</div>
        <div style="font-size: 0.75rem; color: rgba(255,255,255,0.7); margin-top: 0.25rem;">{datetime.now().strftime("%I:%M %p")}</div>
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

    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

    # Charts Row 1
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("WORKFLOW TRENDS", "Monthly completion rates by status")
        st.plotly_chart(
            create_workflow_bar_chart(workflow_trend_data),
            use_container_width=True,
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("DEPARTMENT SPLIT", "Workflow distribution")
        st.plotly_chart(
            create_donut_chart(department_breakdown),
            use_container_width=True,
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
            use_container_width=True,
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("GEARING RATIO TREND", "Quarterly progression vs benchmark")
        st.plotly_chart(
            create_area_chart(volume_gearing_data),
            use_container_width=True,
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
        render_summary_card(executive_summaries[0])
        st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)
        render_summary_card(executive_summaries[2])
    with col2:
        render_summary_card(executive_summaries[1])
        st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)
        render_summary_card(executive_summaries[3])

    # Recent Workflows Table
    st.markdown(
        "<h3 style='margin: 2.5rem 0 1.5rem 0;'>📝 Recent Workflows</h3>",
        unsafe_allow_html=True,
    )
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.dataframe(
        recent_workflows, use_container_width=True, hide_index=True, height=400
    )
    st.markdown("</div>", unsafe_allow_html=True)

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

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header(
            "MONTHLY WORKFLOW DISTRIBUTION", "Status breakdown over time"
        )
        st.plotly_chart(
            create_workflow_bar_chart(workflow_trend_data),
            use_container_width=True,
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
            use_container_width=True,
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_header("WORKFLOW EXECUTION LOG", "Detailed activity history")
    st.dataframe(
        recent_workflows, use_container_width=True, hide_index=True, height=400
    )
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
            use_container_width=True,
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("REVENUE DISTRIBUTION", "By department")
        st.plotly_chart(
            create_donut_chart(department_breakdown),
            use_container_width=True,
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_header(
        "FINANCIAL PERFORMANCE OVERVIEW", "Monthly revenue and profit trends"
    )
    st.plotly_chart(
        create_performance_chart(monthly_performance),
        use_container_width=True,
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
        use_container_width=True,
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
    st.dataframe(styled_data, use_container_width=True, hide_index=True, height=400)
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
            use_container_width=True,
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
            use_container_width=True,
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
            use_container_width=True,
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
