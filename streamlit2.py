"""
BizView Executive Dashboard - Enterprise Edition
Premium Streamlit Application with HD Visuals & Modern Aesthetics
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from datetime import datetime, timedelta
import io
import base64
import numpy as np

# ============ PAGE CONFIGURATION ============
st.set_page_config(
    page_title="BizView Executive Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============ PREMIUM CSS - ENTERPRISE GRADE ============
st.markdown(
    """
<style>
    /* Import Premium Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');
    
    /* CSS Variables - Premium Color Palette */
    :root {
        --navy-900: #0F172A;
        --navy-800: #1E293B;
        --navy-700: #334155;
        --navy-600: #475569;
        --blue-500: #3B82F6;
        --blue-400: #60A5FA;
        --cyan-500: #06B6D4;
        --cyan-400: #22D3EE;
        --amber-500: #F59E0B;
        --amber-400: #FBBF24;
        --emerald-500: #10B981;
        --emerald-400: #34D399;
        --rose-500: #F43F5E;
        --rose-400: #FB7185;
        --violet-500: #8B5CF6;
        --slate-50: #F8FAFC;
        --slate-100: #F1F5F9;
        --slate-200: #E2E8F0;
        --slate-300: #CBD5E1;
        --slate-400: #94A3B8;
        --slate-500: #64748B;
        --white: #FFFFFF;
        
        /* Shadows */
        --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
        --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
        --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
        --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
        --shadow-glow: 0 0 40px rgba(59, 130, 246, 0.15);
        
        /* Gradients */
        --gradient-navy: linear-gradient(135deg, #0F172A 0%, #1E293B 50%, #334155 100%);
        --gradient-blue: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%);
        --gradient-emerald: linear-gradient(135deg, #10B981 0%, #059669 100%);
        --gradient-amber: linear-gradient(135deg, #F59E0B 0%, #D97706 100%);
        --gradient-rose: linear-gradient(135deg, #F43F5E 0%, #E11D48 100%);
    }
    
    /* Hide Streamlit Defaults */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    header {visibility: hidden;}
    [data-testid="stToolbar"] {display: none;}
    
    /* Main App Background */
    .stApp {
        background: linear-gradient(180deg, var(--slate-50) 0%, var(--white) 100%) !important;
    }
    
    .main .block-container {
        padding: 1rem 2rem 2rem 2rem;
        max-width: 100%;
    }
    
    /* ==================== SIDEBAR - PREMIUM DARK THEME ==================== */
    [data-testid="stSidebar"] {
        background: var(--gradient-navy) !important;
        border-right: 1px solid rgba(255,255,255,0.05);
    }
    
    [data-testid="stSidebar"]::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.02'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
        pointer-events: none;
        z-index: 0;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 0;
        position: relative;
        z-index: 1;
    }
    
    [data-testid="stSidebar"] .stMarkdown,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label {
        color: rgba(255, 255, 255, 0.9) !important;
    }
    
    [data-testid="stSidebar"] hr {
        border-color: rgba(255, 255, 255, 0.08) !important;
        margin: 1.5rem 0 !important;
    }
    
    /* Sidebar Navigation Buttons */
    [data-testid="stSidebar"] .stButton > button {
        width: 100%;
        text-align: left !important;
        justify-content: flex-start !important;
        background: transparent !important;
        color: rgba(255, 255, 255, 0.7) !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.875rem 1.25rem !important;
        margin: 0.25rem 0 !important;
        font-size: 0.875rem !important;
        font-weight: 500 !important;
        font-family: 'Inter', sans-serif !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        position: relative;
        overflow: hidden;
    }
    
    [data-testid="stSidebar"] .stButton > button:hover {
        background: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        transform: translateX(4px);
    }
    
    [data-testid="stSidebar"] .stButton > button[kind="primary"] {
        background: linear-gradient(90deg, rgba(59, 130, 246, 0.2) 0%, rgba(59, 130, 246, 0.1) 100%) !important;
        color: white !important;
        border-left: 3px solid var(--amber-500) !important;
        border-radius: 0 12px 12px 0 !important;
    }
    
    /* Sidebar Select Boxes */
    [data-testid="stSidebar"] .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 10px !important;
        color: white !important;
        transition: all 0.2s ease !important;
    }
    
    [data-testid="stSidebar"] .stSelectbox > div > div:hover {
        border-color: rgba(255, 255, 255, 0.25) !important;
        background: rgba(255, 255, 255, 0.12) !important;
    }
    
    [data-testid="stSidebar"] .stSelectbox label {
        color: rgba(255, 255, 255, 0.5) !important;
        font-size: 0.7rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
        font-weight: 600 !important;
    }
    
    /* ==================== TYPOGRAPHY ==================== */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Outfit', sans-serif !important;
        color: var(--navy-900) !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em !important;
    }
    
    h1 { font-size: 2rem !important; font-weight: 800 !important; }
    h2 { font-size: 1.5rem !important; }
    h3 { font-size: 1.125rem !important; }
    
    p, span, div, label {
        font-family: 'Inter', sans-serif !important;
    }
    
    /* ==================== KPI CARDS - PREMIUM GLASS EFFECT ==================== */
    .kpi-card {
        background: var(--white);
        border: 1px solid rgba(226, 232, 240, 0.8);
        border-radius: 20px;
        padding: 1.75rem;
        position: relative;
        overflow: hidden;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: var(--shadow-md);
    }
    
    .kpi-card::before {
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
        transform: translateY(-8px);
        box-shadow: var(--shadow-xl), var(--shadow-glow);
        border-color: rgba(59, 130, 246, 0.2);
    }
    
    .kpi-card:hover::before {
        opacity: 1;
    }
    
    .kpi-icon-wrapper {
        width: 56px;
        height: 56px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1.25rem;
        position: relative;
        overflow: hidden;
    }
    
    .kpi-icon-wrapper::after {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, rgba(255,255,255,0.4) 0%, transparent 100%);
    }
    
    .kpi-icon-wrapper.up {
        background: linear-gradient(135deg, #DCFCE7 0%, #BBF7D0 100%);
    }
    
    .kpi-icon-wrapper.down {
        background: linear-gradient(135deg, #FEE2E2 0%, #FECACA 100%);
    }
    
    .kpi-icon {
        font-size: 1.5rem;
        position: relative;
        z-index: 1;
    }
    
    .kpi-value {
        font-family: 'Outfit', sans-serif !important;
        font-size: 2.5rem !important;
        font-weight: 800 !important;
        color: var(--navy-900) !important;
        line-height: 1;
        letter-spacing: -0.03em;
        background: linear-gradient(135deg, var(--navy-900) 0%, var(--navy-700) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .kpi-label {
        font-size: 0.875rem;
        font-weight: 500;
        color: var(--slate-500);
        margin-top: 0.5rem;
        letter-spacing: 0.01em;
    }
    
    .kpi-change {
        display: inline-flex;
        align-items: center;
        gap: 0.375rem;
        font-size: 0.8rem;
        font-weight: 600;
        margin-top: 1rem;
        padding: 0.5rem 0.875rem;
        border-radius: 100px;
        transition: all 0.2s ease;
    }
    
    .kpi-change-positive {
        background: linear-gradient(135deg, #DCFCE7 0%, #D1FAE5 100%);
        color: #166534;
    }
    
    .kpi-change-negative {
        background: linear-gradient(135deg, #FEE2E2 0%, #FECACA 100%);
        color: #991B1B;
    }
    
    .kpi-change-icon {
        font-size: 0.75rem;
    }
    
    /* ==================== CHART CARDS - MODERN DESIGN ==================== */
    .chart-card {
        background: var(--white);
        border: 1px solid var(--slate-200);
        border-radius: 20px;
        overflow: hidden;
        box-shadow: var(--shadow-md);
        transition: all 0.3s ease;
    }
    
    .chart-card:hover {
        box-shadow: var(--shadow-lg);
    }
    
    .chart-card-header {
        padding: 1.25rem 1.5rem;
        border-bottom: 1px solid var(--slate-100);
        background: linear-gradient(180deg, var(--white) 0%, var(--slate-50) 100%);
    }
    
    .chart-card-title {
        font-family: 'Outfit', sans-serif !important;
        font-size: 0.8rem !important;
        font-weight: 700 !important;
        color: var(--navy-900) !important;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin: 0 !important;
    }
    
    .chart-card-subtitle {
        font-size: 0.75rem;
        color: var(--slate-500);
        margin-top: 0.25rem;
        font-weight: 400;
    }
    
    .chart-card-content {
        padding: 1.5rem;
    }
    
    /* ==================== SUMMARY CARDS - PREMIUM DARK ==================== */
    .summary-card {
        background: var(--gradient-navy);
        color: white;
        border-radius: 20px;
        padding: 2rem;
        position: relative;
        overflow: hidden;
        box-shadow: var(--shadow-xl);
        transition: all 0.3s ease;
    }
    
    .summary-card::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 100%;
        height: 100%;
        background: radial-gradient(circle, rgba(59, 130, 246, 0.15) 0%, transparent 70%);
        pointer-events: none;
    }
    
    .summary-card::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
    }
    
    .summary-card:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-xl), 0 0 60px rgba(15, 23, 42, 0.3);
    }
    
    .summary-card-icon {
        width: 48px;
        height: 48px;
        border-radius: 14px;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        margin-bottom: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .summary-card-title {
        color: var(--amber-400) !important;
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700 !important;
        font-size: 1.125rem !important;
        margin-bottom: 0.75rem;
        letter-spacing: -0.01em;
    }
    
    .summary-card-content {
        font-size: 0.9rem;
        line-height: 1.8;
        color: rgba(255, 255, 255, 0.85);
    }
    
    .summary-metric {
        margin-top: 1.5rem;
        padding-top: 1.25rem;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .summary-metric-value {
        font-family: 'Outfit', sans-serif !important;
        font-size: 2rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, #FFFFFF 0%, rgba(255,255,255,0.8) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .summary-metric-label {
        font-size: 0.75rem;
        color: rgba(255, 255, 255, 0.5);
        margin-top: 0.25rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* ==================== INSIGHT CARDS ==================== */
    .insight-card {
        background: var(--white);
        border: 1px solid var(--slate-200);
        border-radius: 16px;
        padding: 1.5rem;
        transition: all 0.3s ease;
        box-shadow: var(--shadow-sm);
    }
    
    .insight-card:hover {
        box-shadow: var(--shadow-md);
        border-color: var(--blue-400);
    }
    
    .insight-card h4 {
        font-size: 0.75rem !important;
        font-weight: 600 !important;
        color: var(--slate-500) !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.75rem !important;
    }
    
    .insight-value {
        font-family: 'Outfit', sans-serif !important;
        font-size: 2rem !important;
        font-weight: 800 !important;
        letter-spacing: -0.02em;
    }
    
    .insight-label {
        font-size: 0.875rem;
        color: var(--slate-500);
        margin-top: 0.25rem;
    }
    
    /* ==================== DATA TABLES ==================== */
    .dataframe {
        font-family: 'Inter', sans-serif !important;
        font-size: 0.875rem !important;
        border-radius: 12px !important;
        overflow: hidden !important;
    }
    
    .dataframe th {
        font-family: 'Outfit', sans-serif !important;
        font-size: 0.7rem !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.08em !important;
        color: var(--slate-500) !important;
        background: var(--slate-50) !important;
        padding: 1rem 1.25rem !important;
    }
    
    .dataframe td {
        padding: 1rem 1.25rem !important;
        border-bottom: 1px solid var(--slate-100) !important;
    }
    
    /* ==================== BADGES ==================== */
    .badge {
        display: inline-flex;
        align-items: center;
        padding: 0.375rem 0.875rem;
        font-size: 0.75rem;
        font-weight: 600;
        border-radius: 100px;
        letter-spacing: 0.02em;
    }
    
    .badge-success { 
        background: linear-gradient(135deg, #DCFCE7 0%, #D1FAE5 100%); 
        color: #166534; 
    }
    .badge-warning { 
        background: linear-gradient(135deg, #FEF3C7 0%, #FDE68A 100%); 
        color: #92400E; 
    }
    .badge-error { 
        background: linear-gradient(135deg, #FEE2E2 0%, #FECACA 100%); 
        color: #991B1B; 
    }
    .badge-navy { 
        background: var(--gradient-navy); 
        color: white; 
    }
    .badge-blue { 
        background: var(--gradient-blue); 
        color: white; 
    }
    
    /* ==================== BUTTONS ==================== */
    .stButton > button {
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        border-radius: 12px !important;
        padding: 0.625rem 1.25rem !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: var(--shadow-sm) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: var(--shadow-md) !important;
    }
    
    .stDownloadButton > button {
        background: var(--gradient-navy) !important;
        color: white !important;
        border: none !important;
    }
    
    .stDownloadButton > button:hover {
        box-shadow: var(--shadow-lg), 0 0 30px rgba(15, 23, 42, 0.2) !important;
    }
    
    /* ==================== ANIMATIONS ==================== */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes fadeInLeft {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    
    @keyframes shimmer {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }
    
    .animate-fade-in-up {
        animation: fadeInUp 0.5s ease-out forwards;
    }
    
    .animate-fade-in-left {
        animation: fadeInLeft 0.5s ease-out forwards;
    }
    
    /* Staggered animations */
    .stagger-1 { animation-delay: 0.1s; }
    .stagger-2 { animation-delay: 0.2s; }
    .stagger-3 { animation-delay: 0.3s; }
    .stagger-4 { animation-delay: 0.4s; }
    
    /* ==================== SCROLLBAR ==================== */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--slate-100);
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, var(--slate-300) 0%, var(--slate-400) 100%);
        border-radius: 5px;
        border: 2px solid var(--slate-100);
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, var(--slate-400) 0%, var(--slate-500) 100%);
    }
    
    /* ==================== HEADER BAR ==================== */
    .header-bar {
        background: var(--white);
        border-radius: 16px;
        padding: 1rem 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: var(--shadow-sm);
        border: 1px solid var(--slate-200);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .header-title {
        font-family: 'Outfit', sans-serif !important;
        font-size: 1.75rem !important;
        font-weight: 800 !important;
        color: var(--navy-900) !important;
        letter-spacing: -0.03em !important;
        margin: 0 !important;
    }
    
    .header-subtitle {
        font-size: 0.875rem;
        color: var(--slate-500);
        margin-top: 0.25rem;
    }
    
    /* ==================== PRIORITY CARDS ==================== */
    .priority-card {
        display: flex;
        gap: 1rem;
        padding: 1.25rem;
        background: var(--slate-50);
        border-radius: 14px;
        margin-bottom: 0.75rem;
        transition: all 0.3s ease;
        border: 1px solid transparent;
    }
    
    .priority-card:hover {
        background: var(--white);
        border-color: var(--slate-200);
        box-shadow: var(--shadow-md);
        transform: translateX(8px);
    }
    
    .priority-number {
        width: 36px;
        height: 36px;
        background: var(--gradient-navy);
        color: white;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 0.875rem;
        flex-shrink: 0;
    }
    
    .priority-content h5 {
        font-family: 'Outfit', sans-serif;
        font-weight: 600;
        color: var(--navy-900);
        font-size: 0.9375rem;
        margin: 0 0 0.25rem 0;
    }
    
    .priority-content p {
        color: var(--slate-500);
        font-size: 0.8125rem;
        margin: 0;
        line-height: 1.5;
    }
    
    /* ==================== ACHIEVEMENT CARDS ==================== */
    .achievement-card {
        display: flex;
        gap: 1rem;
        padding: 1.25rem;
        background: linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%);
        border: 1px solid #BBF7D0;
        border-radius: 14px;
        margin-bottom: 0.75rem;
        transition: all 0.3s ease;
    }
    
    .achievement-card:hover {
        box-shadow: var(--shadow-md);
        transform: translateX(8px);
    }
    
    .achievement-dot {
        width: 10px;
        height: 10px;
        background: var(--emerald-500);
        border-radius: 50%;
        margin-top: 5px;
        flex-shrink: 0;
        box-shadow: 0 0 10px rgba(16, 185, 129, 0.4);
    }
    
    .achievement-content h5 {
        font-family: 'Outfit', sans-serif;
        font-weight: 600;
        color: var(--navy-900);
        font-size: 0.9375rem;
        margin: 0 0 0.25rem 0;
    }
    
    .achievement-content p {
        color: var(--slate-600);
        font-size: 0.8125rem;
        margin: 0;
    }
    
    /* ==================== EXPORT CARDS ==================== */
    .export-card {
        background: var(--white);
        border: 1px solid var(--slate-200);
        border-radius: 20px;
        padding: 1.75rem;
        transition: all 0.3s ease;
        box-shadow: var(--shadow-sm);
    }
    
    .export-card:hover {
        border-color: var(--blue-400);
        box-shadow: var(--shadow-lg), var(--shadow-glow);
        transform: translateY(-4px);
    }
    
    .export-icon {
        width: 56px;
        height: 56px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .export-icon.navy { background: var(--gradient-navy); }
    .export-icon.blue { background: var(--gradient-blue); }
    .export-icon.emerald { background: var(--gradient-emerald); }
    
    .export-title {
        font-family: 'Outfit', sans-serif;
        font-weight: 700;
        font-size: 1.125rem;
        color: var(--navy-900);
        margin-bottom: 0.25rem;
    }
    
    .export-subtitle {
        font-size: 0.8125rem;
        color: var(--slate-500);
        margin-bottom: 1rem;
    }
    
    .export-description {
        font-size: 0.875rem;
        color: var(--slate-600);
        line-height: 1.6;
    }
    
    /* ==================== PRINT STYLES ==================== */
    @media print {
        [data-testid="stSidebar"] { display: none !important; }
        .no-print { display: none !important; }
        .stApp { background: white !important; }
        .kpi-card, .chart-card, .summary-card { box-shadow: none !important; }
    }
</style>
""",
    unsafe_allow_html=True,
)

# ============ SVG ICONS (HD Quality) ============
ICONS = {
    "workflow": """<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>""",
    "trending": """<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline><polyline points="17 6 23 6 23 12"></polyline></svg>""",
    "users": """<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>""",
    "cpu": """<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect><rect x="9" y="9" width="6" height="6"></rect><line x1="9" y1="1" x2="9" y2="4"></line><line x1="15" y1="1" x2="15" y2="4"></line><line x1="9" y1="20" x2="9" y2="23"></line><line x1="15" y1="20" x2="15" y2="23"></line><line x1="20" y1="9" x2="23" y2="9"></line><line x1="20" y1="14" x2="23" y2="14"></line><line x1="1" y1="9" x2="4" y2="9"></line><line x1="1" y1="14" x2="4" y2="14"></line></svg>""",
    "check": """<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>""",
    "clock": """<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>""",
    "x": """<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line><line x1="9" y1="9" x2="15" y2="15"></line></svg>""",
    "dollar": """<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>""",
    "target": """<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle></svg>""",
    "award": """<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>""",
    "zap": """<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>""",
    "alert": """<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>""",
}

# ============ MOCK DATA ============
kpi_data = {
    "workflow_count": {
        "value": 1247,
        "change": 12.5,
        "trend": "up",
        "label": "Total Workflows",
    },
    "volume_gearing_ratio": {
        "value": 2.45,
        "change": 8.3,
        "trend": "up",
        "label": "Volume Gearing Ratio",
    },
    "productivity": {
        "value": 87.3,
        "change": 5.2,
        "trend": "up",
        "label": "Productivity Score",
    },
    "tech_adoption": {
        "value": 76.8,
        "change": -2.1,
        "trend": "down",
        "label": "Tech Adoption Rate",
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
        "Completed": [145, 162, 178, 195, 210, 225, 198, 235, 248, 262, 278, 290],
        "Pending": [23, 18, 25, 20, 15, 22, 28, 19, 16, 21, 17, 24],
        "Failed": [5, 8, 4, 6, 3, 7, 9, 4, 5, 6, 3, 8],
    }
)

volume_gearing_data = pd.DataFrame(
    {
        "Quarter": ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"],
        "Ratio": [2.12, 2.28, 2.35, 2.45],
        "Volume": [485000, 512000, 548000, 592000],
        "Benchmark": [2.0, 2.1, 2.15, 2.2],
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
        ],
        "Score": [92.5, 88.2, 85.7, 91.3, 89.1, 83.4],
        "Target": [90, 85, 82, 88, 87, 80],
        "Employees": [45, 32, 18, 28, 15, 12],
    }
)

tech_adoption_data = pd.DataFrame(
    {
        "Tool": [
            "CRM System",
            "Project Mgmt",
            "Analytics",
            "Collaboration",
            "AI Assistant",
            "Automation",
            "Cloud Storage",
            "Security",
        ],
        "Adoption": [94, 89, 76, 92, 45, 68, 98, 85],
        "Category": [
            "Core",
            "Core",
            "Analytics",
            "Comms",
            "Emerging",
            "Process",
            "Core",
            "Security",
        ],
    }
)

department_breakdown = pd.DataFrame(
    {
        "Department": ["Engineering", "Sales", "Marketing", "Operations", "Other"],
        "Value": [35, 25, 15, 15, 10],
    }
)

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
        "Workflow": [
            "Customer Onboarding",
            "Invoice Processing",
            "Lead Qualification",
            "Support Routing",
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
            "✅ Completed",
            "✅ Completed",
            "⏳ Pending",
            "✅ Completed",
            "❌ Failed",
            "✅ Completed",
            "⏳ Pending",
            "✅ Completed",
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
            "Dec 15",
            "Dec 15",
            "Dec 14",
            "Dec 14",
            "Dec 13",
            "Dec 13",
            "Dec 12",
            "Dec 12",
        ],
    }
)

executive_summaries = [
    {
        "title": "Operational Excellence",
        "content": "Workflow completion rates have increased by 12.5% compared to last quarter, driven by automation initiatives.",
        "metric": "+12.5%",
        "metric_label": "Workflow Efficiency",
        "icon": "📈",
    },
    {
        "title": "Financial Performance",
        "content": "Volume gearing ratio improved to 2.45, exceeding the industry benchmark of 2.2.",
        "metric": "2.45",
        "metric_label": "Gearing Ratio",
        "icon": "💰",
    },
    {
        "title": "Workforce Productivity",
        "content": "Overall productivity at 87.3%, with Engineering leading at 92.5%.",
        "metric": "87.3%",
        "metric_label": "Avg Productivity",
        "icon": "👥",
    },
    {
        "title": "Tech Transformation",
        "content": "Core tech adoption at 90%+, AI assistant adoption at 45%.",
        "metric": "76.8%",
        "metric_label": "Tech Adoption",
        "icon": "💻",
    },
]

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

# ============ PREMIUM CHART COLORS ============
COLORS = {
    "navy": "#0F172A",
    "navy_light": "#1E293B",
    "blue": "#3B82F6",
    "blue_light": "#60A5FA",
    "cyan": "#06B6D4",
    "emerald": "#10B981",
    "amber": "#F59E0B",
    "rose": "#F43F5E",
    "violet": "#8B5CF6",
    "slate": "#64748B",
}

# ============ COMPONENT FUNCTIONS ============


def render_premium_kpi(
    label, value, change, trend, format_type="number", icon="📊", delay=0
):
    """Render premium KPI card with animations"""
    if format_type == "percentage":
        display_value = f"{value}%"
    elif format_type == "ratio":
        display_value = f"{value:.2f}"
    elif format_type == "currency":
        display_value = f"${value:,.0f}"
    else:
        display_value = f"{value:,}"

    wrapper_class = "up" if trend == "up" else "down"
    change_class = "kpi-change-positive" if trend == "up" else "kpi-change-negative"
    arrow = "↑" if trend == "up" else "↓"

    st.markdown(
        f"""
    <div class="kpi-card animate-fade-in-up stagger-{delay}">
        <div class="kpi-icon-wrapper {wrapper_class}">
            <span class="kpi-icon">{icon}</span>
        </div>
        <div class="kpi-value">{display_value}</div>
        <div class="kpi-label">{label}</div>
        <div class="kpi-change {change_class}">
            <span class="kpi-change-icon">{arrow}</span>
            {abs(change)}%
            <span style="font-weight: 400; opacity: 0.8; margin-left: 4px;">vs last period</span>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


def render_chart_header(title, subtitle=""):
    st.markdown(
        f"""
    <div class="chart-card-header">
        <div class="chart-card-title">{title}</div>
        <div class="chart-card-subtitle">{subtitle}</div>
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
        <p class="summary-card-content">{summary["content"]}</p>
        <div class="summary-metric">
            <div class="summary-metric-value">{summary["metric"]}</div>
            <div class="summary-metric-label">{summary["metric_label"]}</div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


# ============ PREMIUM CHART FUNCTIONS ============


def create_premium_bar_chart(data):
    """Create stunning bar chart with gradients"""
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            name="Completed",
            x=data["Month"],
            y=data["Completed"],
            marker=dict(
                color=data["Completed"],
                colorscale=[[0, "#1E293B"], [1, "#3B82F6"]],
                line=dict(width=0),
            ),
            hovertemplate="<b>%{x}</b><br>Completed: %{y}<extra></extra>",
        )
    )
    fig.add_trace(
        go.Bar(
            name="Pending",
            x=data["Month"],
            y=data["Pending"],
            marker=dict(color="#06B6D4"),
            hovertemplate="<b>%{x}</b><br>Pending: %{y}<extra></extra>",
        )
    )
    fig.add_trace(
        go.Bar(
            name="Failed",
            x=data["Month"],
            y=data["Failed"],
            marker=dict(color="#F43F5E"),
            hovertemplate="<b>%{x}</b><br>Failed: %{y}<extra></extra>",
        )
    )

    fig.update_layout(
        barmode="group",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, sans-serif", size=12, color="#64748B"),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
            font=dict(size=11),
            bgcolor="rgba(0,0,0,0)",
        ),
        margin=dict(l=40, r=20, t=60, b=40),
        xaxis=dict(
            gridcolor="rgba(226, 232, 240, 0.5)",
            showgrid=False,
            tickfont=dict(size=11, color="#64748B"),
        ),
        yaxis=dict(
            gridcolor="rgba(226, 232, 240, 0.5)",
            gridwidth=1,
            tickfont=dict(size=11, color="#64748B"),
        ),
        bargap=0.2,
        bargroupgap=0.1,
        hoverlabel=dict(
            bgcolor="#0F172A", font_size=13, font_family="Inter", bordercolor="#0F172A"
        ),
    )
    return fig


def create_premium_donut_chart(data):
    """Create beautiful donut chart"""
    colors = ["#0F172A", "#3B82F6", "#06B6D4", "#8B5CF6", "#F59E0B"]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=data["Department"],
                values=data["Value"],
                hole=0.65,
                marker=dict(colors=colors, line=dict(color="#FFFFFF", width=3)),
                textposition="outside",
                textinfo="label+percent",
                textfont=dict(size=12, family="Inter", color="#64748B"),
                hovertemplate="<b>%{label}</b><br>%{value}%<br>(%{percent})<extra></extra>",
                pull=[0.02, 0, 0, 0, 0],
            )
        ]
    )

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", size=12),
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=False,
        annotations=[
            dict(
                text="<b>Distribution</b>",
                x=0.5,
                y=0.5,
                font_size=14,
                font_family="Outfit",
                font_color="#0F172A",
                showarrow=False,
            )
        ],
        hoverlabel=dict(bgcolor="#0F172A", font_size=13, font_family="Inter"),
    )
    return fig


def create_premium_area_chart(data):
    """Create gradient area chart"""
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=data["Quarter"],
            y=data["Ratio"],
            name="Gearing Ratio",
            mode="lines+markers",
            fill="tozeroy",
            fillcolor="rgba(59, 130, 246, 0.15)",
            line=dict(color="#3B82F6", width=3, shape="spline"),
            marker=dict(size=10, color="#3B82F6", line=dict(width=3, color="#FFFFFF")),
            hovertemplate="<b>%{x}</b><br>Ratio: %{y:.2f}<extra></extra>",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=data["Quarter"],
            y=data["Benchmark"],
            name="Benchmark",
            mode="lines+markers",
            line=dict(color="#F59E0B", width=2, dash="dot"),
            marker=dict(size=8, color="#F59E0B", symbol="diamond"),
            hovertemplate="<b>%{x}</b><br>Benchmark: %{y:.2f}<extra></extra>",
        )
    )

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", size=12, color="#64748B"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
        margin=dict(l=40, r=20, t=60, b=40),
        xaxis=dict(gridcolor="rgba(226, 232, 240, 0.5)", showgrid=False),
        yaxis=dict(gridcolor="rgba(226, 232, 240, 0.5)", range=[0, 3]),
        hoverlabel=dict(bgcolor="#0F172A", font_size=13),
    )
    return fig


def create_premium_horizontal_bar(data):
    """Create horizontal bar chart"""
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            name="Score",
            y=data["Department"],
            x=data["Score"],
            orientation="h",
            marker=dict(
                color=data["Score"],
                colorscale=[[0, "#1E293B"], [0.5, "#3B82F6"], [1, "#10B981"]],
                line=dict(width=0),
                cornerradius=6,
            ),
            text=data["Score"].astype(str) + "%",
            textposition="inside",
            textfont=dict(color="white", size=11, family="Inter"),
            hovertemplate="<b>%{y}</b><br>Score: %{x}%<extra></extra>",
        )
    )

    fig.add_trace(
        go.Scatter(
            name="Target",
            y=data["Department"],
            x=data["Target"],
            mode="markers",
            marker=dict(
                size=12,
                color="#F59E0B",
                symbol="line-ns",
                line=dict(width=3, color="#F59E0B"),
            ),
            hovertemplate="<b>%{y}</b><br>Target: %{x}%<extra></extra>",
        )
    )

    fig.update_layout(
        barmode="overlay",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", size=12, color="#64748B"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
        margin=dict(l=100, r=40, t=60, b=40),
        xaxis=dict(
            gridcolor="rgba(226, 232, 240, 0.5)", range=[0, 100], ticksuffix="%"
        ),
        yaxis=dict(gridcolor="rgba(226, 232, 240, 0)", showgrid=False),
        bargap=0.4,
        hoverlabel=dict(bgcolor="#0F172A", font_size=13),
    )
    return fig


def create_premium_tech_chart(data):
    """Create tech adoption chart with color coding"""
    colors = [
        "#10B981" if a >= 80 else "#3B82F6" if a >= 60 else "#F43F5E"
        for a in data["Adoption"]
    ]

    fig = go.Figure(
        go.Bar(
            x=data["Tool"],
            y=data["Adoption"],
            marker=dict(color=colors, line=dict(width=0), cornerradius=8),
            text=data["Adoption"].astype(str) + "%",
            textposition="outside",
            textfont=dict(size=11, family="Inter", color="#64748B"),
            hovertemplate="<b>%{x}</b><br>Adoption: %{y}%<extra></extra>",
        )
    )

    # Add threshold lines
    fig.add_hline(
        y=80,
        line_dash="dash",
        line_color="#10B981",
        opacity=0.5,
        annotation_text="High",
        annotation_position="right",
    )
    fig.add_hline(
        y=60,
        line_dash="dash",
        line_color="#F59E0B",
        opacity=0.5,
        annotation_text="Medium",
        annotation_position="right",
    )

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", size=12, color="#64748B"),
        margin=dict(l=40, r=60, t=40, b=100),
        xaxis=dict(gridcolor="rgba(226, 232, 240, 0)", tickangle=-45, showgrid=False),
        yaxis=dict(gridcolor="rgba(226, 232, 240, 0.5)", range=[0, 115]),
        hoverlabel=dict(bgcolor="#0F172A", font_size=13),
    )
    return fig


def create_premium_performance_chart(data):
    """Create performance area chart"""
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=data["Month"],
            y=data["Revenue"],
            name="Revenue",
            mode="lines",
            fill="tonexty",
            fillcolor="rgba(15, 23, 42, 0.1)",
            line=dict(color="#0F172A", width=3, shape="spline"),
            hovertemplate="<b>%{x}</b><br>Revenue: $%{y:,.0f}<extra></extra>",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=data["Month"],
            y=data["Profit"],
            name="Profit",
            mode="lines",
            fill="tozeroy",
            fillcolor="rgba(16, 185, 129, 0.2)",
            line=dict(color="#10B981", width=3, shape="spline"),
            hovertemplate="<b>%{x}</b><br>Profit: $%{y:,.0f}<extra></extra>",
        )
    )

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", size=12, color="#64748B"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
        margin=dict(l=60, r=20, t=60, b=40),
        xaxis=dict(gridcolor="rgba(226, 232, 240, 0)", showgrid=False),
        yaxis=dict(gridcolor="rgba(226, 232, 240, 0.5)", tickformat="$,.0f"),
        hoverlabel=dict(bgcolor="#0F172A", font_size=13),
    )
    return fig


def create_premium_line_chart(data, x_col, y_col, name, color="#3B82F6"):
    """Create premium line chart"""
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=data[x_col],
            y=data[y_col],
            name=name,
            mode="lines+markers",
            fill="tozeroy",
            fillcolor=f"rgba{tuple(int(color.lstrip('#')[i : i + 2], 16) for i in (0, 2, 4)) + (0.1,)}",
            line=dict(color=color, width=3, shape="spline"),
            marker=dict(size=8, color=color, line=dict(width=2, color="white")),
            hovertemplate="<b>%{x}</b><br>Value: %{y}<extra></extra>",
        )
    )

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", size=12, color="#64748B"),
        margin=dict(l=40, r=20, t=20, b=40),
        xaxis=dict(gridcolor="rgba(226, 232, 240, 0)", showgrid=False),
        yaxis=dict(gridcolor="rgba(226, 232, 240, 0.5)"),
        hoverlabel=dict(bgcolor="#0F172A", font_size=13),
    )
    return fig


# ============ PDF REPORT GENERATOR ============
def generate_premium_report():
    """Generate premium HTML report"""
    current_date = datetime.now().strftime("%B %d, %Y")

    prod_rows = "".join(
        f"""
    <tr>
        <td style="font-weight: 600;">{row["Department"]}</td>
        <td style="font-family: 'JetBrains Mono'; font-weight: 600;">{row["Score"]}%</td>
        <td style="color: #64748B;">{row["Target"]}%</td>
        <td><span style="background: {"linear-gradient(135deg, #DCFCE7, #D1FAE5)" if row["Score"] >= row["Target"] else "linear-gradient(135deg, #FEF3C7, #FDE68A)"}; color: {"#166534" if row["Score"] >= row["Target"] else "#92400E"}; padding: 6px 14px; border-radius: 100px; font-size: 11px; font-weight: 600;">{"On Target" if row["Score"] >= row["Target"] else "Below"}</span></td>
    </tr>
    """
        for _, row in productivity_data.iterrows()
    )

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>BizView Executive Report</title>
        <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Inter:wght@400;500;600&family=JetBrains+Mono&display=swap" rel="stylesheet">
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ font-family: 'Inter', sans-serif; color: #0F172A; background: linear-gradient(180deg, #F8FAFC, #FFFFFF); }}
            .container {{ max-width: 1000px; margin: 0 auto; padding: 48px; background: white; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }}
            h1, h2, h3 {{ font-family: 'Outfit', sans-serif; letter-spacing: -0.02em; }}
            h1 {{ font-size: 32px; font-weight: 800; }}
            h2 {{ font-size: 18px; font-weight: 700; margin: 40px 0 20px 0; color: #0F172A; text-transform: uppercase; letter-spacing: 0.05em; }}
            
            .header {{ border-bottom: 3px solid #0F172A; padding-bottom: 24px; margin-bottom: 40px; display: flex; justify-content: space-between; }}
            .header-left p {{ color: #64748B; margin-top: 8px; font-size: 14px; }}
            .header-right {{ text-align: right; }}
            .header-right p {{ color: #64748B; font-size: 13px; }}
            .header-right strong {{ color: #0F172A; font-weight: 600; }}
            
            .kpi-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-bottom: 48px; }}
            .kpi-box {{ background: linear-gradient(135deg, #F8FAFC, #FFFFFF); border: 1px solid #E2E8F0; padding: 24px; border-radius: 16px; text-align: center; }}
            .kpi-value {{ font-family: 'Outfit'; font-size: 32px; font-weight: 800; background: linear-gradient(135deg, #0F172A, #334155); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
            .kpi-label {{ color: #64748B; font-size: 13px; margin-top: 8px; font-weight: 500; }}
            .kpi-change {{ font-size: 12px; margin-top: 12px; font-weight: 600; }}
            .kpi-change.positive {{ color: #166534; }}
            .kpi-change.negative {{ color: #991B1B; }}
            
            table {{ width: 100%; border-collapse: collapse; margin: 20px 0 40px 0; }}
            th {{ background: #F8FAFC; text-align: left; padding: 14px 18px; border-bottom: 2px solid #E2E8F0; font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; color: #64748B; font-weight: 700; }}
            td {{ padding: 16px 18px; border-bottom: 1px solid #F1F5F9; font-size: 14px; }}
            
            .footer {{ text-align: center; color: #94A3B8; font-size: 12px; margin-top: 48px; padding-top: 24px; border-top: 1px solid #E2E8F0; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="header-left">
                    <h1>📊 Executive Dashboard Report</h1>
                    <p>BizView Analytics Platform • Enterprise Edition</p>
                </div>
                <div class="header-right">
                    <p>Generated</p>
                    <p><strong>{current_date}</strong></p>
                </div>
            </div>
            
            <h2>Key Performance Indicators</h2>
            <div class="kpi-grid">
                <div class="kpi-box">
                    <div class="kpi-value">{kpi_data["workflow_count"]["value"]:,}</div>
                    <div class="kpi-label">Total Workflows</div>
                    <div class="kpi-change positive">↑ {kpi_data["workflow_count"]["change"]}%</div>
                </div>
                <div class="kpi-box">
                    <div class="kpi-value">{kpi_data["volume_gearing_ratio"]["value"]}</div>
                    <div class="kpi-label">Gearing Ratio</div>
                    <div class="kpi-change positive">↑ {kpi_data["volume_gearing_ratio"]["change"]}%</div>
                </div>
                <div class="kpi-box">
                    <div class="kpi-value">{kpi_data["productivity"]["value"]}%</div>
                    <div class="kpi-label">Productivity</div>
                    <div class="kpi-change positive">↑ {kpi_data["productivity"]["change"]}%</div>
                </div>
                <div class="kpi-box">
                    <div class="kpi-value">{kpi_data["tech_adoption"]["value"]}%</div>
                    <div class="kpi-label">Tech Adoption</div>
                    <div class="kpi-change negative">↓ {abs(kpi_data["tech_adoption"]["change"])}%</div>
                </div>
            </div>
            
            <h2>Department Productivity</h2>
            <table>
                <thead><tr><th>Department</th><th>Score</th><th>Target</th><th>Status</th></tr></thead>
                <tbody>{prod_rows}</tbody>
            </table>
            
            <div class="footer">
                <p>Generated by BizView Analytics Platform • Enterprise Edition • Confidential</p>
            </div>
        </div>
    </body>
    </html>
    """


# ============ SESSION STATE ============
if "current_page" not in st.session_state:
    st.session_state.current_page = "Dashboard"

# ============ SIDEBAR ============
with st.sidebar:
    st.markdown(
        """
    <div style="padding: 2rem 1.5rem 1.5rem 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.08);">
        <div style="display: flex; align-items: center; gap: 14px;">
            <div style="width: 42px; height: 42px; background: linear-gradient(135deg, #3B82F6, #06B6D4); border-radius: 12px; display: flex; align-items: center; justify-content: center;">
                <span style="font-size: 20px;">📊</span>
            </div>
            <div>
                <span style="font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 1.25rem; color: white; letter-spacing: -0.02em;">BizView</span>
                <p style="font-size: 11px; color: rgba(255,255,255,0.5); margin: 2px 0 0 0; letter-spacing: 0.05em;">EXECUTIVE ANALYTICS</p>
            </div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

    nav_items = [
        ("📊", "Dashboard"),
        ("🔄", "Workflow Analytics"),
        ("💰", "Financial Metrics"),
        ("👥", "Productivity"),
        ("💻", "Tech Adoption"),
        ("📋", "Executive Summary"),
        ("📥", "Reports & Export"),
    ]

    for icon, name in nav_items:
        btn_type = "primary" if st.session_state.current_page == name else "secondary"
        if st.button(
            f"{icon}  {name}",
            key=f"nav_{name}",
            type=btn_type,
            use_container_width=True,
        ):
            st.session_state.current_page = name
            st.rerun()

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown(
        "<p style='font-size: 10px; text-transform: uppercase; letter-spacing: 0.15em; color: rgba(255,255,255,0.4); margin-bottom: 1rem; padding: 0 0.5rem;'>Filters</p>",
        unsafe_allow_html=True,
    )

    department = st.selectbox(
        "Department",
        [
            "All Departments",
            "Engineering",
            "Sales",
            "Marketing",
            "Operations",
            "Finance",
            "HR",
        ],
    )
    date_range = st.selectbox(
        "Date Range", ["Last 30 Days", "Last 7 Days", "Last 90 Days", "Year to Date"]
    )
    status = st.selectbox("Status", ["All Status", "Completed", "Pending", "Failed"])

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown(
        """
    <div style="padding: 0 0.5rem; color: rgba(255,255,255,0.35); font-size: 11px;">
        <p style="margin-bottom: 0.5rem;">⚙️ Settings</p>
        <p style="font-size: 10px; letter-spacing: 0.05em;">Enterprise Edition v2.0</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

# ============ MAIN CONTENT ============
col_header, col_actions = st.columns([3, 1])
with col_header:
    st.markdown(
        f"""
    <div>
        <h1 style='margin: 0; font-size: 2rem;'>{st.session_state.current_page}</h1>
        <p style='color: #64748B; font-size: 0.875rem; margin-top: 0.25rem;'>Real-time analytics and insights</p>
    </div>
    """,
        unsafe_allow_html=True,
    )
with col_actions:
    col_print, col_download = st.columns(2)
    with col_print:
        if st.button("🖨️ Print", use_container_width=True):
            st.toast("Use Ctrl+P / Cmd+P to print", icon="🖨️")
    with col_download:
        st.download_button(
            "📥 Export",
            data=generate_premium_report(),
            file_name=f"BizView_Report_{datetime.now().strftime('%Y%m%d')}.html",
            mime="text/html",
            use_container_width=True,
        )

st.markdown(
    "<hr style='margin: 1.25rem 0 2rem 0; border-color: #E2E8F0;'>",
    unsafe_allow_html=True,
)

# ============ PAGES ============
if st.session_state.current_page == "Dashboard":
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_premium_kpi(
            kpi_data["workflow_count"]["label"],
            kpi_data["workflow_count"]["value"],
            kpi_data["workflow_count"]["change"],
            "up",
            "number",
            "📊",
            1,
        )
    with col2:
        render_premium_kpi(
            kpi_data["volume_gearing_ratio"]["label"],
            kpi_data["volume_gearing_ratio"]["value"],
            kpi_data["volume_gearing_ratio"]["change"],
            "up",
            "ratio",
            "📈",
            2,
        )
    with col3:
        render_premium_kpi(
            kpi_data["productivity"]["label"],
            kpi_data["productivity"]["value"],
            kpi_data["productivity"]["change"],
            "up",
            "percentage",
            "👥",
            3,
        )
    with col4:
        render_premium_kpi(
            kpi_data["tech_adoption"]["label"],
            kpi_data["tech_adoption"]["value"],
            kpi_data["tech_adoption"]["change"],
            "down",
            "percentage",
            "💻",
            4,
        )

    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

    col_chart1, col_chart2 = st.columns([2, 1])
    with col_chart1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("WORKFLOW TRENDS", "Monthly completion rates by status")
        st.plotly_chart(
            create_premium_bar_chart(workflow_trend_data),
            use_container_width=True,
            config={"displayModeBar": False},
        )
        st.markdown("</div>", unsafe_allow_html=True)
    with col_chart2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("DEPARTMENT SPLIT", "Workflow allocation")
        st.plotly_chart(
            create_premium_donut_chart(department_breakdown),
            use_container_width=True,
            config={"displayModeBar": False},
        )
        st.markdown("</div>", unsafe_allow_html=True)

    col_chart3, col_chart4 = st.columns(2)
    with col_chart3:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("FINANCIAL PERFORMANCE", "Revenue vs Profit")
        st.plotly_chart(
            create_premium_performance_chart(monthly_performance),
            use_container_width=True,
            config={"displayModeBar": False},
        )
        st.markdown("</div>", unsafe_allow_html=True)
    with col_chart4:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("COMPLETION TREND", "Monthly workflow output")
        st.plotly_chart(
            create_premium_line_chart(
                workflow_trend_data, "Month", "Completed", "Completed", "#10B981"
            ),
            use_container_width=True,
            config={"displayModeBar": False},
        )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        "<h3 style='margin: 2rem 0 1.5rem 0;'>Executive Summaries</h3>",
        unsafe_allow_html=True,
    )
    col_sum1, col_sum2 = st.columns(2)
    with col_sum1:
        render_summary_card(executive_summaries[0])
    with col_sum2:
        render_summary_card(executive_summaries[1])

    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_header("RECENT WORKFLOWS", "Latest executions")
    st.dataframe(
        recent_workflows, use_container_width=True, hide_index=True, height=350
    )
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.current_page == "Workflow Analytics":
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_premium_kpi("Total Workflows", 1247, 12.5, "up", "number", "📊", 1)
    with col2:
        render_premium_kpi("Completed", 1098, 15.2, "up", "number", "✅", 2)
    with col3:
        render_premium_kpi("Pending", 89, -8.3, "up", "number", "⏳", 3)
    with col4:
        render_premium_kpi("Failed", 60, -12.1, "up", "number", "❌", 4)

    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("STATUS BREAKDOWN", "Monthly distribution")
        st.plotly_chart(
            create_premium_bar_chart(workflow_trend_data),
            use_container_width=True,
            config={"displayModeBar": False},
        )
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("COMPLETION TREND", "Growth over time")
        st.plotly_chart(
            create_premium_line_chart(
                workflow_trend_data, "Month", "Completed", "Completed", "#10B981"
            ),
            use_container_width=True,
            config={"displayModeBar": False},
        )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_header("WORKFLOW LOG", "Detailed execution history")
    st.dataframe(recent_workflows, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.current_page == "Financial Metrics":
    total_revenue = monthly_performance["Revenue"].sum()
    total_profit = monthly_performance["Profit"].sum()
    profit_margin = total_profit / total_revenue * 100

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_premium_kpi("Gearing Ratio", 2.45, 8.3, "up", "ratio", "📈", 1)
    with col2:
        render_premium_kpi(
            "Annual Revenue", total_revenue, 18.5, "up", "currency", "💰", 2
        )
    with col3:
        render_premium_kpi(
            "Annual Profit", total_profit, 24.2, "up", "currency", "📊", 3
        )
    with col4:
        render_premium_kpi(
            "Profit Margin", round(profit_margin, 1), 5.8, "up", "percentage", "📉", 4
        )

    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("GEARING RATIO TREND", "Quarterly vs Benchmark")
        st.plotly_chart(
            create_premium_area_chart(volume_gearing_data),
            use_container_width=True,
            config={"displayModeBar": False},
        )
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("REVENUE MIX", "By department")
        st.plotly_chart(
            create_premium_donut_chart(department_breakdown),
            use_container_width=True,
            config={"displayModeBar": False},
        )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_header("PERFORMANCE OVERVIEW", "Revenue and Profit trend")
    st.plotly_chart(
        create_premium_performance_chart(monthly_performance),
        use_container_width=True,
        config={"displayModeBar": False},
    )
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.current_page == "Productivity":
    avg_score = productivity_data["Score"].mean()
    on_target = (productivity_data["Score"] >= productivity_data["Target"]).sum()
    total_employees = productivity_data["Employees"].sum()
    top = productivity_data.loc[productivity_data["Score"].idxmax()]

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_premium_kpi(
            "Avg Score", round(avg_score, 1), 5.2, "up", "percentage", "📈", 1
        )
    with col2:
        render_premium_kpi("On Target", on_target, 16.7, "up", "number", "🎯", 2)
    with col3:
        render_premium_kpi("Employees", total_employees, 8.4, "up", "number", "👥", 3)
    with col4:
        render_premium_kpi("Top Score", top["Score"], 3.1, "up", "percentage", "🏆", 4)

    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("DEPARTMENT SCORES", "Performance vs Target")
        st.plotly_chart(
            create_premium_horizontal_bar(productivity_data),
            use_container_width=True,
            config={"displayModeBar": False},
        )
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("OUTPUT TREND", "Monthly progression")
        st.plotly_chart(
            create_premium_line_chart(
                workflow_trend_data, "Month", "Completed", "Output", "#3B82F6"
            ),
            use_container_width=True,
            config={"displayModeBar": False},
        )
        st.markdown("</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            f"""
        <div class="insight-card">
            <h4>Top Team</h4>
            <div class="insight-value" style="color: #0F172A;">{top["Department"]}</div>
            <div class="insight-label">{top["Score"]}% productivity</div>
        </div>
        """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            f"""
        <div class="insight-card">
            <h4>Achievement Rate</h4>
            <div class="insight-value" style="color: #10B981;">{int(on_target / len(productivity_data) * 100)}%</div>
            <div class="insight-label">{on_target}/{len(productivity_data)} teams on target</div>
        </div>
        """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            f"""
        <div class="insight-card">
            <h4>Total Workforce</h4>
            <div class="insight-value" style="color: #3B82F6;">{total_employees}</div>
            <div class="insight-label">Across all departments</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

elif st.session_state.current_page == "Tech Adoption":
    avg_adoption = tech_adoption_data["Adoption"].mean()
    high = (tech_adoption_data["Adoption"] >= 80).sum()
    low = (tech_adoption_data["Adoption"] < 60).sum()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_premium_kpi(
            "Avg Adoption", round(avg_adoption, 1), -2.1, "down", "percentage", "💻", 1
        )
    with col2:
        render_premium_kpi("High Adoption", high, 12.5, "up", "number", "✅", 2)
    with col3:
        render_premium_kpi("Low Adoption", low, -25.0, "up", "number", "⚠️", 3)
    with col4:
        render_premium_kpi("Emerging Tech", 1, 100, "up", "number", "🚀", 4)

    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_header("ADOPTION BY TOOL", "With performance thresholds")
    st.plotly_chart(
        create_premium_tech_chart(tech_adoption_data),
        use_container_width=True,
        config={"displayModeBar": False},
    )
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.current_page == "Executive Summary":
    current_date = datetime.now().strftime("%A, %B %d, %Y")

    st.markdown(
        f"""
    <div style="background: linear-gradient(135deg, #0F172A 0%, #1E293B 50%, #334155 100%); color: white; border-radius: 24px; padding: 2.5rem; margin-bottom: 2rem; position: relative; overflow: hidden; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25);">
        <div style="position: absolute; top: -50%; right: -20%; width: 60%; height: 200%; background: radial-gradient(circle, rgba(59, 130, 246, 0.15) 0%, transparent 70%);"></div>
        <p style="color: #FBBF24; font-size: 13px; font-weight: 600; letter-spacing: 0.1em; margin-bottom: 12px;">📅 {current_date}</p>
        <h2 style="color: white; margin-bottom: 16px; font-size: 2rem; font-weight: 800; letter-spacing: -0.03em;">Monthly Executive Report</h2>
        <p style="color: rgba(255,255,255,0.7); max-width: 700px; line-height: 1.7; font-size: 1rem;">
            Comprehensive overview of organizational performance metrics, highlighting key achievements and strategic recommendations.
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)
    stats = [
        ("📊", f"{kpi_data['workflow_count']['value']:,}", "Workflows", "#0F172A"),
        ("📈", str(kpi_data["volume_gearing_ratio"]["value"]), "Gearing", "#3B82F6"),
        ("👥", f"{kpi_data['productivity']['value']}%", "Productivity", "#10B981"),
        ("💻", f"{kpi_data['tech_adoption']['value']}%", "Tech Adoption", "#F59E0B"),
    ]
    for col, (icon, value, label, color) in zip([col1, col2, col3, col4], stats):
        with col:
            st.markdown(
                f"""
            <div class="insight-card" style="text-align: center; padding: 1.75rem;">
                <span style="font-size: 2rem;">{icon}</span>
                <div class="insight-value" style="color: {color}; margin-top: 0.75rem;">{value}</div>
                <div class="insight-label">{label}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown(
        "<h3 style='margin: 2.5rem 0 1.5rem 0;'>Key Insights</h3>",
        unsafe_allow_html=True,
    )
    for i in range(0, 4, 2):
        col1, col2 = st.columns(2)
        with col1:
            render_summary_card(executive_summaries[i])
        with col2:
            if i + 1 < len(executive_summaries):
                render_summary_card(executive_summaries[i + 1])
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

elif st.session_state.current_page == "Reports & Export":
    st.markdown(
        "<h3 style='margin-bottom: 1.5rem;'>Export Options</h3>", unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
        <div class="export-card">
            <div class="export-icon navy">📄</div>
            <div class="export-title">Full Report</div>
            <div class="export-subtitle">Complete dashboard PDF</div>
            <p class="export-description">Export all KPIs, charts, and data tables in a comprehensive report format.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        st.download_button(
            "📥 Download Report",
            data=generate_premium_report(),
            file_name=f"BizView_Report_{datetime.now().strftime('%Y%m%d')}.html",
            mime="text/html",
            use_container_width=True,
        )

    with col2:
        st.markdown(
            f"""
        <div class="export-card">
            <div class="export-icon blue">📊</div>
            <div class="export-title">Excel Export</div>
            <div class="export-subtitle">Multi-sheet workbook</div>
            <p class="export-description">All datasets in separate sheets for analysis and custom reporting.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
            workflow_trend_data.to_excel(writer, sheet_name="Workflows", index=False)
            productivity_data.to_excel(writer, sheet_name="Productivity", index=False)
            tech_adoption_data.to_excel(writer, sheet_name="Tech", index=False)
            monthly_performance.to_excel(writer, sheet_name="Financial", index=False)

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
        <div class="export-card">
            <div class="export-icon emerald">📋</div>
            <div class="export-title">CSV Export</div>
            <div class="export-subtitle">Raw data files</div>
            <p class="export-description">Individual CSV files for integration with other tools and systems.</p>
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
