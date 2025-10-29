# ram_cybersecurity_portfolio_final.py
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime

# Page Configuration - Ultimate Cyber Theme
st.set_page_config(
    page_title="Ram Lalit Mishra - Cybersecurity Portfolio",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ultimate Cyber Security CSS
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

# Initialize session state
if 'visit_count' not in st.session_state:
    st.session_state.visit_count = 0
st.session_state.visit_count += 98291

# MAIN HEADER - ULTIMATE CYBER THEME
st.markdown('<div class="matrix-bg">', unsafe_allow_html=True)

# Hero Section
col1, col2 = st.columns([1, 2])

with col1:
    # Profile Image Section
    try:
        st.image("Ram.jpg", 
                 width=280, 
                 caption="🛡️ Ram Lalit Mishra - Cybersecurity Protector")
  except:
    # Fallback
    st.image("https://via.placeholder.com/300x300/0083B0/FFFFFF?text=RAM+MISHRA", 
             width=280, 
             caption="🛡️ Ram Lalit Mishra - Cybersecurity Protector")

with col2:
    st.markdown('<h1 class="cyber-main-header">🛡️ RAM LALIT MISHRA</h1>', unsafe_allow_html=True)
    st.markdown('<p class="cyber-sub-header">CYBERSECURITY ENTHUSIAST | PYTHON DEVELOPER | ETHICAL HACKER</p>', unsafe_allow_html=True)
    
    # Cyber Stats Row
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
            <h3>🛡️ Try Hackme Labs</h3>
            <div class="stat-number">50+</div>
        </div>
        """, unsafe_allow_html=True)
    
    with stats_col3:
        st.markdown("""
        <div class="metric-card">
            <h3>🐍 Python</h3>
            <div class="stat-number">60%</div>
            <p>+10%</p>
        </div>
        """, unsafe_allow_html=True)
    
    with stats_col4:
        st.markdown(f"""
        <div class="metric-card">
            <h3>👁️ Views</h3>
            <div class="stat-number">{st.session_state.visit_count}</div>
        </div>
        """, unsafe_allow_html=True)

# Mission Statement
st.markdown("""
<div class="hacker-card">
<h3>🎯 CYBER MISSION STATEMENT</h3>
<p style='font-size: 1.2rem; font-style: italic;'>"Security is not a product, but a process. My mission is to make the digital world safer, 
one vulnerability at a time. I believe in ethical hacking, continuous learning, and building secure systems that protect people's data and privacy."</p>
</div>
""", unsafe_allow_html=True)

# ABOUT ME SECTION
st.markdown("---")
st.markdown("## 🛡️ ABOUT THE CYBER PROTECTOR")

about_col1, about_col2 = st.columns(2)

with about_col1:
    st.markdown("""
    <div class="security-card">
    <h3>👨‍💻 THE JOURNEY BEGINS</h3>
    <p>I am a highly enthusiastic student with a burning passion for cybersecurity and technology. 
    While maintaining A-grade academic performance, I've embarked on a self-directed journey into 
    the world of ethical hacking, Python development, and cybersecurity fundamentals.</p>
    
    <h4>🎓 LEARNING PHILOSOPHY</h4>
    <p><strong>DISCOVER → EXPLORE → IMPLEMENT → SHARE</strong></p>
    <p>I believe in hands-on learning through real-world projects, CTF challenges, and continuous 
    skill development. Every day is an opportunity to learn something new and strengthen my cyber defenses.</p>
    </div>
    """, unsafe_allow_html=True)

with about_col2:
    st.markdown("""
    <div class="security-card">
    <h3>📊 CYBER PROFILE</h3>
    
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

# SKILLS & EXPERTISE
st.markdown("---")
st.markdown("## 💡 CYBERSECURITY SKILL MATRIX")

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

# TECH STACK
st.markdown("### 🔧 CYBER TECH ARSENAL")
tech_cols = st.columns(6)
tech_stack = ["🐍 Python", "🐧 Linux", "🌐 Streamlit", "💻 HTML/CSS/JS", "🔗 Git & GitHub", "⚡ VS Code"]

for i, tech in enumerate(tech_stack):
    with tech_cols[i]:
        st.markdown(f"""
        <div class="contact-shield">
            <strong>{tech}</strong>
        </div>
        """, unsafe_allow_html=True)

# PROJECTS SHOWCASE WITH LINKS
st.markdown("---")
st.markdown("## 🚀 CYBER PROJECTS SHOWCASE")

project_col1, project_col2, project_col3 = st.columns(3)

with project_col1:
    st.markdown("""
    <a href="https://theram6788-forest-ai-app.streamlit.app" target="_blank" style="text-decoration: none;">
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
    <a href="https://tryhackme.com/p/theram6788" target="_blank" style="text-decoration: none;">
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
    <a href="https://theram6788.blogspot.com" target="_blank" style="text-decoration: none;">
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

# TRYHACKME PROGRESS
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

# FUTURE GOALS
st.markdown("---")
st.markdown("## 🎯 CYBER ROADMAP 2024-2025")

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

# CONTACT SECTION WITH LINKS
st.markdown("---")
st.markdown("## 📞 CYBER COMMAND CENTER")

contact_col1, contact_col2, contact_col3, contact_col4 = st.columns(4)

with contact_col1:
    st.markdown("""
    <a href="https://linkedin.com/in/ram-lalit-mishra-a0139838b" target="_blank" style="text-decoration: none;">
    <div class="contact-shield">
        <h4>💼 LinkedIn</h4>
        <p>Ram Lalit Mishra</p>
        <p><em>Professional Network</em></p>
        <p><small>🔗 Click to connect</small></p>
    </div>
    </a>
    """, unsafe_allow_html=True)

with contact_col2:
    st.markdown("""
    <a href="https://github.com/theram6788" target="_blank" style="text-decoration: none;">
    <div class="contact-shield">
        <h4>🐙 GitHub</h4>
        <p>@theram6788</p>
        <p><em>Code Repository</em></p>
        <p><small>🔗 Click to view projects</small></p>
    </div>
    </a>
    """, unsafe_allow_html=True)

with contact_col3:
    st.markdown("""
    <a href="https://theram6788.blogspot.com" target="_blank" style="text-decoration: none;">
    <div class="contact-shield">
        <h4>📝 Blog</h4>
        <p>theram6788.blogspot.com</p>
        <p><em>Knowledge Sharing</em></p>
        <p><small>🔗 Click to read articles</small></p>
    </div>
    </a>
    """, unsafe_allow_html=True)

with contact_col4:
    st.markdown("""
    <a href="https://drive.google.com/your-resume-link" target="_blank" style="text-decoration: none;">
    <div class="contact-shield">
        <h4>📄 Resume</h4>
        <p>Google Drive</p>
        <p><em>Detailed CV</em></p>
        <p><small>🔗 Click to download</small></p>
    </div>
    </a>
    """, unsafe_allow_html=True)

# FINAL FOOTER
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #00FFFF; font-family: "Orbitron", sans-serif;'>
    <h3>🛡️ SECURING THE DIGITAL FUTURE</h3>
    <p><em>"The only truly secure system is one that is powered off, cast in a block of concrete, 
    and sealed in a lead-lined room with armed guards - and even then I have my doubts." - Gene Spafford</em></p>
    <p style='color: #666; margin-top: 2rem;'>Built with 🐍 Python & ❤️ Passion | Ram Lalit Mishra © 2024</p>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
