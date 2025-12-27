
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime
st.set_page_config(
    page_title="Raghavendra Pratap Singh - Growth Portfolio",
    page_icon="😎",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&family=Exo+2:wght@100;200;300;400;500;600;700;800;900&display=swap');
    
    .cyber-main-header {
        font-family: 'Orbitron', sans-serif;
        font-size: 4rem;
        background: linear-gradient(90deg, #00F260, #0575E6, #00B4DB, #0083B0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 900;
        margin-bottom: 0;
        text-shadow: 0 0 30px rgba(0,242,96,0.5);
        animation: cyberGlow 3s ease-in-out infinite;
        letter-spacing: 2px;
    }
    
    @keyframes cyberGlow {
        0% { text-shadow: 0 0 20px rgba(0,242,96,0.5); }
        50% { text-shadow: 0 0 40px rgba(5,117,230,0.8); }
        100% { text-shadow: 0 0 20px rgba(0,242,96,0.5); }
    }
    
    .cyber-sub-header {
        font-family: 'Rajdhani', sans-serif;
        text-align: center;
        color: #00FFFF;
        font-size: 1.4rem;
        font-weight: 600;
        letter-spacing: 2px;
        margin-bottom: 2rem;
        text-shadow: 0 0 10px rgba(0,255,255,0.7);
    }
    
    .security-card {
        background: linear-gradient(135deg, rgba(20,30,50,0.95) 0%, rgba(10,15,30,0.95) 100%);
        border: 1px solid #00F260;
        border-radius: 20px;
        padding: 2rem;
        color: white;
        box-shadow: 0 8px 40px rgba(0,242,96,0.4);
        backdrop-filter: blur(15px);
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }
    
    .security-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0,242,96,0.2), transparent);
        transition: 0.5s;
    }
    
    .security-card:hover::before {
        left: 100%;
    }
    
    .security-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 50px rgba(0,242,96,0.6);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 1.5rem;
        color: white;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 6px 20px rgba(102,126,234,0.4);
        margin-bottom: 1rem;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(102,126,234,0.6);
    }
    
    .hacker-card {
        background: linear-gradient(135deg, #FF416C 0%, #FF4B2B 100%);
        border: 2px solid #FF416C;
        border-radius: 20px;
        padding: 2rem;
        color: white;
        animation: hackerPulse 2s infinite;
        box-shadow: 0 0 40px rgba(255,65,108,0.6);
    }
    
    @keyframes hackerPulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }
    
    .skill-meter {
        background: linear-gradient(90deg, #00F260, #0575E6);
        border-radius: 10px;
        padding: 0.8rem;
        margin: 0.8rem 0;
        color: white;
        font-family: 'Exo 2', sans-serif;
        font-weight: 600;
        font-size: 1rem;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,242,96,0.3);
        transition: all 0.3s ease;
    }
    
    .skill-meter:hover {
        transform: translateX(5px);
        box-shadow: 0 6px 20px rgba(0,242,96,0.5);
    }
    
    .cyber-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border: none;
        border-radius: 25px;
        padding: 12px 30px;
        color: white;
        font-family: 'Exo 2', sans-serif;
        font-weight: 700;
        font-size: 1rem;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 6px 20px rgba(102,126,234,0.4);
    }
    
    .cyber-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(102,126,234,0.6);
    }
    
    .matrix-bg {
        background: linear-gradient(180deg, #0a0f1a 0%, #1a1f2b 50%, #0a0f1a 100%);
    }
    
    .stat-number {
        font-family: 'Orbitron', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(90deg, #00F260, #00FFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .project-shield {
        background: linear-gradient(135deg, #00B4DB 0%, #0083B0 100%);
        border-radius: 20px;
        padding: 2rem;
        color: white;
        box-shadow: 0 8px 40px rgba(0,180,219,0.5);
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .project-shield:hover {
        transform: translateY(-5px) rotate(1deg);
        box-shadow: 0 12px 50px rgba(0,180,219,0.7);
    }
    
    .contact-shield {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 1.5rem;
        color: white;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .contact-shield:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 30px rgba(102,126,234,0.6);
    }
    
    .thm-card {
        background: linear-gradient(135deg, #00F260 0%, #0575E6 100%);
        border-radius: 15px;
        padding: 1.5rem;
        color: white;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 6px 20px rgba(0,242,96,0.4);
    }
    
    .thm-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,242,96,0.6);
    }
    
    .clickable-card {
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .clickable-card:hover {
        transform: translateY(-3px);
    }
</style>
""", unsafe_allow_html=True)

if 'visit_count' not in st.session_state:
    st.session_state.visit_count = 0
st.session_state.visit_count += 98291

st.markdown('<div class="matrix-bg">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    try:
        photo_url = "data:image/jpeg;base64,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"
        st.image(photo_url, 
                 width=280, 
                 caption="🛡️ Raghavendra - Youth Skill Promoter")
    except:
        st.image("https://via.placeholder.com/300x300/0083B0/FFFFFF?text=RAM+MISHRA", 
                 width=280, 
                 caption="🛡️ Raghavendra - Youth Skill Promoter")

with col2:
    st.markdown('<h1 class="cyber-main-header">🛡️ RAGHAVENDRA PRATAP SINGH</h1>', unsafe_allow_html=True)
    st.markdown('<p class="cyber-sub-header">YOUTH SKILL PROMOTER | DEVELOPER | HACKING ELITE</p>', unsafe_allow_html=True)

    stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)
    
    with stats_col1:
        st.markdown("""
        <div class="metric-card">
            <h3>🔒 Projects</h3>
            <div class="stat-number">3</div>
            <p>2 Live</p>
        </div>
        """, unsafe_allow_html=True)
    
    with stats_col2:
        st.markdown("""
        <div class="metric-card">
            <h3>🛡️ Developer Level</h3>
            <div class="stat-number">Intermediate</div>
        </div>
        """, unsafe_allow_html=True)
    
    with stats_col3:
        st.markdown("""
        <div class="metric-card">
            <h3>⛷️ Skiing</h3>
            <div class="stat-number">Back hobby</div>
            <p></p>
        </div>
        """, unsafe_allow_html=True)
    
    with stats_col4:
        st.markdown(f"""
        <div class="metric-card">
            <h3>👁️ Views</h3>
            <div class="stat-number">{st.session_state.visit_count}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div class="hacker-card">
<h3>🎯  MISSION STATEMENT</h3>
<p style='font-size: 1.2rem; font-style: italic;'>"To grow India through continuous learning, technological development, and education-first approach while actively pursuing cybersecurity knowledge and maintaining a balanced life through sports and reading."</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("## 🛡️ ABOUT THE INFLUENCER")

about_col1, about_col2 = st.columns(2)

with about_col1:
    st.markdown("""
    <div class="security-card">
    <h3>👨‍💻 THE JOURNEY BEGINS</h3>
    <p>My journey began with a simple belief: education first. While others chased trends, I built habits—waking up early to read, hitting the badminton court in the afternoon, coding into the evening.</p>
    
    <h4>🎓 LEARNING PHILOSOPHY</h4>
    <p><strong>DISCOVER → EXPLORE → IMPLEMENT → SHARE</strong></p>
    <p>I believe in hands-on learning through real-world projects, CTF challenges, and continuous 
    skill development. Every day is an opportunity to learn something new and strengthen my cyber defenses.</p>
    </div>
    """, unsafe_allow_html=True)

with about_col2:
    st.markdown("""
    <div class="security-card">
    <h3>📊  PROFILE</h3>
    
    <div class="skill-meter" style="width: 100%">✅ A-Grade Academic Record</div>
    <div class="skill-meter" style="width: 95%">🛡️ 50+ TryHackMe Labs Completed</div>
    <div class="skill-meter" style="width: 90%">🐍 Multiple Python Projects Live</div>
    <div class="skill-meter" style="width: 85%">🌐 Active Tech Blogger</div>
    <div class="skill-meter" style="width: 100%">🚀 Continuous Skill Development</div>
    
    <h4>🎯 CURRENT FOCUS AREAS</h4>
    <p>• Advanced Python & Automation</p>
    <p>• Web Application Security</p>
    <p>• Network Defense Strategies</p>
    <p>• Cybersecurity Fundamentals</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("## 💡  SKILL MATRIX")

skills_data = {
    'Skill': ['Python Programming', 'Ethical Hacking', 'Linux Fundamentals', 'Web Security', 
              'Network Security', 'Bash Scripting', 'HTML/CSS', 'Documentation'],
    'Level': [60, 40, 50, 35, 45, 30, 55, 50],
    'Category': ['Programming', 'Security', 'OS', 'Security', 'Networking', 'Scripting', 'Web', 'Soft Skills']
}

skills_df = pd.DataFrame(skills_data)

fig_radar = go.Figure()
fig_radar.add_trace(go.Scatterpolar(
    r=skills_df['Level'],
    theta=skills_df['Skill'],
    fill='toself',
    name='Skill Level',
    line=dict(color='#00F260'),
    fillcolor='rgba(0, 242, 96, 0.3)'
))

fig_radar.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
    showlegend=False,
    title="🛡️ Cybersecurity Skills Radar",
    font=dict(color='white'),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    height=500
)

st.plotly_chart(fig_radar, use_container_width=True)

st.markdown("### 🔧 CYBER TECH ARSENAL")
tech_cols = st.columns(6)
tech_stack = ["🐍 Python", "🐧 Linux", "🌐 Global Independence", "💻 HTML/CSS/JS", "🔗 Git & GitHub", "⚡ Highly Concious"]

for i, tech in enumerate(tech_stack):
    with tech_cols[i]:
        st.markdown(f"""
        <div class="contact-shield">
            <strong>{tech}</strong>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("## 🚀  PROJECTS SHOWCASE")

project_col1, project_col2, project_col3 = st.columns(3)

with project_col1:
    st.markdown("""
    <a href="https://eco-ai.streamlit.app" target="_blank" style="text-decoration: none;">
    <div class="project-shield">
        <h3>🔥 EcoGuardian AI</h3>
        <p><strong>AI-Powered Forest Fire Detection</strong></p>
        <p>🛡️ Advanced neural network system</p>
        <p>🌐 Real-time threat monitoring</p>
        <p>🚀 Emergency response protocols</p>
        <p>📊 Live data visualization</p>
        <p>🎯 <strong>Status:</strong> 🟢 LIVE DEPLOYMENT</p>
        <p><small>🔗 Click to view live project</small></p>
    </div>
    </a>
    """, unsafe_allow_html=True)

with project_col2:
    st.markdown("""
    <a href="https://snap-login.com" target="_blank" style="text-decoration: none;">
    <div class="project-shield">
        <h3>🛡️ TryHackMe Journey</h3>
        <p><strong>50+ Security Labs Mastered</strong></p>
        <p>🔐 Network security fundamentals</p>
        <p>🌐 Web vulnerability assessment</p>
        <p>⚡ Hands-on hacking simulations</p>
        <p>📈 Progressive skill development</p>
        <p>🎯 <strong>Status:</strong> 🔵 ACTIVE LEARNING</p>
        <p><small>🔗 Click to view THM profile</small></p>
    </div>
    </a>
    """, unsafe_allow_html=True)

with project_col3:
    st.markdown("""
    <a href="https://snap-login.com" target="_blank" style="text-decoration: none;">
    <div class="project-shield">
        <h3>📝 Tech Blog</h3>
        <p><strong>Knowledge Sharing Platform</strong></p>
        <p>✍️ Cybersecurity concepts</p>
        <p>🐍 Python tutorials</p>
        <p>🎯 Project documentation</p>
        <p>🌟 Learning journey stories</p>
        <p>🎯 <strong>Status:</strong> 🟡 REGULAR UPDATES</p>
        <p><small>🔗 Click to visit blog</small></p>
    </div>
    </a>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("## 🛡️ TRYHACKME CYBER DOJO")

thm_col1, thm_col2, thm_col3, thm_col4 = st.columns(4)

with thm_col1:
    st.markdown("""
    <div class="thm-card">
        <h3>🏆 Labs Completed</h3>
        <div class="stat-number">50+</div>
        <p>25 this month</p>
    </div>
    """, unsafe_allow_html=True)

with thm_col2:
    st.markdown("""
    <div class="thm-card">
        <h3>📚 Learning Paths</h3>
        <div class="stat-number">3</div>
        <p>Active</p>
        <p><small>Web Fundamentals</small></p>
    </div>
    """, unsafe_allow_html=True)

with thm_col3:
    st.markdown("""
    <div class="thm-card">
        <h3>⚡ Hacker Rank</h3>
        <div class="stat-number">Pentester</div>
        <p>Climbing Fast</p>
    </div>
    """, unsafe_allow_html=True)

with thm_col4:
    st.markdown("""
    <div class="thm-card">
        <h3>🎯 Streak</h3>
        <div class="stat-number">15</div>
        <p>Days</p>
        <p><small>Consistent</small></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("## 🎯 CYBER ROADMAP 2026-2027")

goal_col1, goal_col2, goal_col3 = st.columns(3)

with goal_col1:
    st.markdown("""
    <div class="metric-card">
        <h4>🎓 EDUCATION PATH</h4>
        <p>• Computer Science Degree</p>
        <p>• Cybersecurity Certifications</p>
        <p>• Advanced Programming</p>
        <p>• Network Security Courses</p>
    </div>
    """, unsafe_allow_html=True)

with goal_col2:
    st.markdown("""
    <div class="metric-card">
        <h4>💼 CAREER ASPIRATIONS</h4>
        <p>• Cybersecurity Analyst</p>
        <p>• Ethical Hacker</p>
        <p>• Security Researcher</p>
        <p>• Open Source Contributor</p>
    </div>
    """, unsafe_allow_html=True)

with goal_col3:
    st.markdown("""
    <div class="metric-card">
        <h4>🚀 PROJECT GOALS</h4>
        <p>• Advanced Security Tools</p>
        <p>• AI Cybersecurity Solutions</p>
        <p>• Community Learning Platforms</p>
        <p>• Bug Bounty Participation</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("## 📞 CYBER COMMAND CENTER")

contact_col1, contact_col2, contact_col3, contact_col4 = st.columns(4)


st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #00FFFF; font-family: "Orbitron", sans-serif;'>
    <h3>🛡️ SECURING THE DIGITAL FUTURE</h3>
    <p><em>"The only truly secure system is one that is powered off, cast in a block of concrete, 
    and sealed in a lead-lined room with armed guards - and even then I have my doubts." - Gene Spafford</em></p>
    <p style='color: #666; margin-top: 2rem;'>Built with  Excellence & Passion | Raghavendra © 2026</p>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)