import streamlit as st

st.set_page_config(
    page_title="Sahu Borewell Services | Lucknow",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

#MainMenu, header, footer, [data-testid="stToolbar"], [data-testid="stDecoration"] {
    display: none !important;
}

[data-testid="stAppViewContainer"] {
    background: #ffffff !important;
}

[data-testid="stMainBlockContainer"] {
    padding: 0 !important;
    max-width: 100% !important;
}

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

body, [data-testid="stAppViewContainer"] {
    font-family: 'Inter', sans-serif;
    color: #1e293b;
    background: #ffffff;
}

a {
    text-decoration: none;
}

.navbar {
    position: sticky;
    top: 0;
    z-index: 1000;
    background: #ffffff;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    padding: 0 5vw;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 70px;
}

.nav-logo {
    font-weight: 800;
    font-size: 1.35rem;
    color: #0f3b5c;
}

.nav-logo span {
    color: #2c7da0;
}

.nav-info {
    display: flex;
    align-items: center;
    gap: 32px;
}

.nav-contact {
    font-size: 0.85rem;
    color: #5a6e7c;
}

.nav-cta {
    background: #2c7da0;
    color: white;
    font-weight: 600;
    font-size: 0.85rem;
    padding: 8px 20px;
    border-radius: 30px;
    transition: all 0.2s;
    display: inline-block;
}

.nav-cta:hover {
    background: #1f5e7a;
    transform: translateY(-1px);
}

.hero {
    background: linear-gradient(135deg, #e8f0f5 0%, #ffffff 100%);
    padding: 60px 5vw;
}

.hero-content {
    max-width: 1300px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: center;
}

.hero-tag {
    display: inline-block;
    background: #e2e8f0;
    padding: 6px 14px;
    border-radius: 30px;
    font-size: 0.75rem;
    font-weight: 500;
    color: #2c7da0;
    margin-bottom: 24px;
}

.hero-headline {
    font-size: clamp(2.5rem, 5vw, 3.8rem);
    font-weight: 800;
    line-height: 1.2;
    color: #0f3b5c;
    margin-bottom: 20px;
}

.hero-headline .hl-blue {
    color: #2c7da0;
}

.hero-sub {
    font-size: 1rem;
    line-height: 1.6;
    color: #5a6e7c;
    margin-bottom: 32px;
}

.hero-actions {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
    margin-bottom: 48px;
}

.btn-primary {
    background: #2c7da0;
    color: white;
    font-weight: 600;
    padding: 14px 32px;
    border-radius: 40px;
    transition: all 0.2s;
    display: inline-block;
}

.btn-primary:hover {
    background: #1f5e7a;
    transform: translateY(-2px);
}

.btn-outline {
    border: 2px solid #2c7da0;
    color: #2c7da0;
    font-weight: 600;
    padding: 12px 30px;
    border-radius: 40px;
    transition: all 0.2s;
    display: inline-block;
}

.btn-outline:hover {
    background: #2c7da0;
    color: white;
}

.stats-grid {
    display: flex;
    gap: 40px;
    flex-wrap: wrap;
}

.stat-item {
    text-align: left;
}

.stat-number {
    font-size: 2rem;
    font-weight: 800;
    color: #0f3b5c;
    display: block;
}

.stat-label {
    font-size: 0.8rem;
    color: #5a6e7c;
}

.emergency-card {
    background: #ffffff;
    border-radius: 20px;
    padding: 32px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.05);
    border: 1px solid #eef2f6;
}

.emergency-badge {
    display: inline-block;
    background: #dc2626;
    color: white;
    font-size: 0.7rem;
    font-weight: 600;
    padding: 4px 12px;
    border-radius: 30px;
    margin-bottom: 20px;
}

.emergency-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: #0f3b5c;
    margin-bottom: 16px;
}

.emergency-phone {
    font-size: 1.8rem;
    font-weight: 800;
    color: #2c7da0;
    margin: 20px 0;
}

.emergency-phone a {
    color: #2c7da0;
    text-decoration: none;
}

.trust-strip {
    background: #0f3b5c;
    padding: 40px 5vw;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 30px;
    text-align: center;
}

.trust-card {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(10px);
    padding: 30px 20px;
    border-radius: 16px;
    transition: transform 0.3s;
}

.trust-card:hover {
    transform: translateY(-5px);
    background: rgba(255,255,255,0.15);
}

.trust-icon {
    font-size: 2.5rem;
    display: block;
    margin-bottom: 15px;
}

.trust-text {
    color: white;
    font-weight: 600;
    font-size: 1rem;
}

.trust-text small {
    display: block;
    font-size: 0.8rem;
    font-weight: 400;
    opacity: 0.8;
    margin-top: 5px;
}

.section {
    padding: 80px 5vw;
}

.section-light {
    background: #ffffff;
}

.section-gray {
    background: #f8fafc;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
}

.section-header {
    text-align: center;
    max-width: 700px;
    margin: 0 auto 60px;
}

.section-tag {
    display: inline-block;
    background: #e2e8f0;
    padding: 4px 12px;
    border-radius: 30px;
    font-size: 0.7rem;
    font-weight: 600;
    color: #2c7da0;
    margin-bottom: 16px;
}

.section-title {
    font-size: clamp(1.8rem, 4vw, 2.5rem);
    font-weight: 800;
    color: #0f3b5c;
    margin-bottom: 20px;
}

.section-subtitle {
    color: #5a6e7c;
    line-height: 1.6;
}

.services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 30px;
}

.service-card {
    background: white;
    border-radius: 20px;
    padding: 35px;
    transition: all 0.3s;
    border: 1px solid #eef2f6;
    box-shadow: 0 4px 12px rgba(0,0,0,0.02);
}

.service-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    border-color: #2c7da0;
}

.service-icon {
    font-size: 2.8rem;
    margin-bottom: 20px;
}

.service-title {
    font-size: 1.35rem;
    font-weight: 700;
    color: #0f3b5c;
    margin-bottom: 12px;
}

.service-desc {
    color: #5a6e7c;
    line-height: 1.6;
    font-size: 0.9rem;
}

.about-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: center;
}

.about-stats {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-top: 30px;
}

.about-stat {
    text-align: center;
    padding: 24px;
    background: #f8fafc;
    border-radius: 16px;
}

.about-stat-number {
    font-size: 2rem;
    font-weight: 800;
    color: #2c7da0;
}

.about-stat-label {
    font-size: 0.8rem;
    color: #5a6e7c;
}

.feature-list {
    list-style: none;
    margin-top: 20px;
}

.feature-list li {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 10px 0;
    color: #5a6e7c;
}

.feature-list .check {
    color: #2c7da0;
    font-weight: bold;
    font-size: 1.1rem;
}

.contact-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 50px;
}

.contact-info {
    background: #f8fafc;
    border-radius: 20px;
    padding: 40px;
}

.contact-item {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 16px 0;
    border-bottom: 1px solid #eef2f6;
}

.contact-item:last-child {
    border-bottom: none;
}

.contact-icon {
    width: 48px;
    height: 48px;
    background: white;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
}

.contact-detail {
    flex: 1;
}

.contact-label {
    font-size: 0.7rem;
    font-weight: 600;
    color: #2c7da0;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.contact-value {
    font-weight: 500;
    color: #0f3b5c;
    margin-top: 4px;
}

.contact-value a {
    color: #0f3b5c;
    text-decoration: none;
}

.contact-value a:hover {
    color: #2c7da0;
}

.cta-box {
    background: #0f3b5c;
    border-radius: 20px;
    padding: 48px;
    color: white;
    text-align: center;
}

.cta-box h3 {
    font-size: 1.8rem;
    margin-bottom: 16px;
}

.cta-box p {
    margin-bottom: 32px;
    opacity: 0.9;
}

.cta-button {
    display: inline-block;
    background: #2c7da0;
    color: white;
    padding: 14px 32px;
    border-radius: 40px;
    font-weight: 600;
    transition: all 0.2s;
}

.cta-button:hover {
    background: #1f5e7a;
    transform: translateY(-2px);
}

.footer {
    background: #0f3b5c;
    color: white;
    padding: 48px 5vw 24px;
}

.footer-content {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 40px;
    margin-bottom: 40px;
}

.footer-logo {
    font-size: 1.5rem;
    font-weight: 800;
}

.footer-logo span {
    color: #2c7da0;
}

.footer-links h4, .footer-contact h4 {
    margin-bottom: 20px;
    font-size: 1rem;
}

.footer-links a {
    display: block;
    color: rgba(255,255,255,0.8);
    margin-bottom: 12px;
    font-size: 0.85rem;
    text-decoration: none;
}

.footer-links a:hover {
    color: white;
}

.footer-contact p {
    color: rgba(255,255,255,0.8);
    margin-bottom: 8px;
    font-size: 0.85rem;
}

.footer-bottom {
    text-align: center;
    padding-top: 24px;
    border-top: 1px solid rgba(255,255,255,0.1);
    font-size: 0.75rem;
    color: rgba(255,255,255,0.6);
}

@media (max-width: 768px) {
    .hero-content, .about-grid, .contact-grid {
        grid-template-columns: 1fr;
    }
    
    .trust-strip {
        grid-template-columns: repeat(2, 1fr);
    }
    
    .navbar {
        padding: 0 5vw;
    }
    
    .nav-info .nav-contact {
        display: none;
    }
    
    .section {
        padding: 50px 5vw;
    }
}

@media (max-width: 480px) {
    .trust-strip {
        grid-template-columns: 1fr;
    }
    
    .services-grid {
        grid-template-columns: 1fr;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<nav class="navbar">
    <div class="nav-logo">
        Sahu <span>Borewell</span>
    </div>
    <div class="nav-info">
        <span class="nav-contact">📍 Lucknow, Uttar Pradesh</span>
        <span class="nav-contact">📧 parmodsahu.pv270@gmail.com</span>
        <a class="nav-cta" href="tel:7844883040">📞 24/7: 7844883040</a>
    </div>
</nav>
""", unsafe_allow_html=True)

st.markdown("""
<section class="hero">
    <div class="hero-content">
        <div>
            <div class="hero-tag">🚨 24/7 Emergency Service Available</div>
            <h1 class="hero-headline">
                Professional <span class="hl-blue">Borewell</span><br>
                Water Solutions
            </h1>
            <p class="hero-sub">
                Expert borewell drilling, maintenance, and pump installations. We deliver reliable water solutions 
                for residential, commercial, and agricultural needs with state-of-the-art machinery.
            </p>
            <div class="hero-actions">
                <a class="btn-primary" href="tel:7844883040">📞 Call Now: 7844883040</a>
                <a class="btn-outline" href="#contact">Get Free Quote</a>
            </div>
            <div class="stats-grid">
                <div class="stat-item">
                    <span class="stat-number">16+</span>
                    <span class="stat-label">Years Experience</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">500+</span>
                    <span class="stat-label">Projects Completed</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">24/7</span>
                    <span class="stat-label">Emergency Support</span>
                </div>
            </div>
        </div>
        <div>
            <div class="emergency-card">
                <div class="emergency-badge">⚡ EMERGENCY SERVICE</div>
                <div class="emergency-title">Need Immediate Help?</div>
                <p>24/7 support for broken pumps, collapsed borewells, and urgent water scarcity issues.</p>
                <div class="emergency-phone">
                    <a href="tel:7844883040">📞 7844883040</a>
                </div>
                <p style="font-size: 0.8rem; color: #5a6e7c;">Call now for rapid response</p>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

st.markdown("""
<div class="trust-strip">
    <div class="trust-card">
        <div class="trust-icon">🏆</div>
        <div class="trust-text">16+ Years Experience <small>Since 2008</small></div>
    </div>
    <div class="trust-card">
        <div class="trust-icon">✅</div>
        <div class="trust-text">Licensed & Insured <small>Certified Professionals</small></div>
    </div>
    <div class="trust-card">
        <div class="trust-icon">⚙️</div>
        <div class="trust-text">Advanced Technology <small>Modern DTH Drilling</small></div>
    </div>
    <div class="trust-card">
        <div class="trust-icon">⭐</div>
        <div class="trust-text">100% Satisfaction <small>Happy Customers</small></div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<section class="section section-light">
    <div class="container">
        <div class="section-header">
            <div class="section-tag">What We Do</div>
            <h2 class="section-title">Comprehensive Water Solutions</h2>
            <p class="section-subtitle">We use modern machinery and scientifically backed methods to provide the highest quality borewell services in Lucknow.</p>
        </div>
        <div class="services-grid">
            <div class="service-card">
                <div class="service-icon">⚙️</div>
                <h3 class="service-title">Borewell Drilling</h3>
                <p class="service-desc">High-power DTH and rotary drilling for residential, commercial, and agricultural properties up to 1500+ feet. Expert drilling in all terrain types with proper site survey.</p>
            </div>
            <div class="service-card">
                <div class="service-icon">🧪</div>
                <h3 class="service-title">Water Quality Testing</h3>
                <p class="service-desc">Comprehensive water quality analysis to ensure safety, checking for minerals, pH, TDS, bacteria, and contaminants with certified lab reports.</p>
            </div>
            <div class="service-card">
                <div class="service-icon">🔧</div>
                <h3 class="service-title">Pump Installation</h3>
                <p class="service-desc">Expert installation of submersible, jet, and surface pumps tailored to your specific depth and water yield. All major brands like Kirloskar, CRI, Grundfos supported.</p>
            </div>
            <div class="service-card">
                <div class="service-icon">🛠️</div>
                <h3 class="service-title">Borewell Maintenance</h3>
                <p class="service-desc">Flushing, cleaning, casing repair, and repairing existing borewells to restore optimal water flow and pressure. Preventive maintenance services available.</p>
            </div>
            <div class="service-card">
                <div class="service-icon">📍</div>
                <h3 class="service-title">Site Survey & Analysis</h3>
                <p class="service-desc">Scientific groundwater exploration and geophysical surveys to identify the perfect drilling point for maximum water yield and long-term sustainability.</p>
            </div>
            <div class="service-card">
                <div class="service-icon">🚨</div>
                <h3 class="service-title">24/7 Emergency Service</h3>
                <p class="service-desc">Round-the-clock support for broken pumps, collapsed borewells, and immediate water scarcity issues. Quick response within 2 hours in Lucknow city.</p>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

st.markdown("""
<section class="section section-gray">
    <div class="container">
        <div class="about-grid">
            <div>
                <div class="section-tag">About Our Company</div>
                <h2 class="section-title">Your Trusted Partner for Groundwater Solutions</h2>
                <p class="section-subtitle" style="margin-bottom: 20px;">
                    Sahu Borewell Services is a premier water drilling contractor dedicated to providing reliable, 
                    efficient, and cost-effective groundwater solutions in Lucknow and surrounding areas.
                </p>
                <p class="section-subtitle">
                    Led by Pramod Sahu ji with 16+ years of hands-on experience, we have successfully completed 
                    hundreds of projects across residential, commercial, and agricultural sectors.
                </p>
                <ul class="feature-list">
                    <li><span class="check">✓</span> State-of-the-art hydraulic DTH drilling rigs</li>
                    <li><span class="check">✓</span> Expert team with decades of combined experience</li>
                    <li><span class="check">✓</span> Transparent pricing with no hidden costs</li>
                    <li><span class="check">✓</span> Fast, efficient, and clean execution</li>
                    <li><span class="check">✓</span> Post-service support and maintenance</li>
                </ul>
            </div>
            <div>
                <div class="about-stats">
                    <div class="about-stat">
                        <div class="about-stat-number">500+</div>
                        <div class="about-stat-label">Successful Projects</div>
                    </div>
                    <div class="about-stat">
                        <div class="about-stat-number">100%</div>
                        <div class="about-stat-label">Customer Satisfaction</div>
                    </div>
                    <div class="about-stat">
                        <div class="about-stat-number">24/7</div>
                        <div class="about-stat-label">Emergency Support</div>
                    </div>
                    <div class="about-stat">
                        <div class="about-stat-number">16+</div>
                        <div class="about-stat-label">Years Experience</div>
                    </div>
                </div>
                <div class="emergency-card" style="margin-top: 30px;">
                    <div class="emergency-title" style="font-size: 1.2rem;">📍 Our Location</div>
                    <p>Gahru, Sarojini Nagar<br>Piparsand Road, Near Naher<br>Lucknow, Uttar Pradesh - 226008</p>
                    <p style="margin-top: 15px;">👤 Proprietor: Pramod Sahu</p>
                </div>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

st.markdown("""
<section class="section section-light" id="contact">
    <div class="container">
        <div class="section-header">
            <div class="section-tag">Contact Us</div>
            <h2 class="section-title">Get In Touch</h2>
            <p class="section-subtitle">Need a quote or facing an emergency? Reach out to us directly. Our team is ready to assist you 24/7.</p>
        </div>
        <div class="contact-grid">
            <div class="contact-info">
                <div class="contact-item">
                    <div class="contact-icon">📞</div>
                    <div class="contact-detail">
                        <div class="contact-label">Call Us 24/7</div>
                        <div class="contact-value"><a href="tel:7844883040">7844883040</a></div>
                    </div>
                </div>
                <div class="contact-item">
                    <div class="contact-icon">✉️</div>
                    <div class="contact-detail">
                        <div class="contact-label">Email Us</div>
                        <div class="contact-value"><a href="mailto:parmodsahu.pv270@gmail.com">parmodsahu.pv270@gmail.com</a></div>
                    </div>
                </div>
                <div class="contact-item">
                    <div class="contact-icon">📍</div>
                    <div class="contact-detail">
                        <div class="contact-label">Location</div>
                        <div class="contact-value">Gahru, Sarojini Nagar<br>Piparsand Road, Near Naher<br>Lucknow, Uttar Pradesh</div>
                    </div>
                </div>
                <div class="contact-item">
                    <div class="contact-icon">🕐</div>
                    <div class="contact-detail">
                        <div class="contact-label">Working Hours</div>
                        <div class="contact-value">Mon - Sat: 8:00 AM - 6:00 PM<br>Sunday: Emergency Services Only</div>
                    </div>
                </div>
            </div>
            <div class="cta-box">
                <h3>Need Immediate Assistance?</h3>
                <p>Call us now for emergency service or free consultation. We're available 24/7 to help with your water needs.</p>
                <a class="cta-button" href="tel:7844883040">📞 Call 7844883040 Now</a>
                <p style="margin-top: 24px; font-size: 0.8rem;">Free site visit and quote available</p>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

st.markdown("""
<footer class="footer">
    <div class="footer-content">
        <div>
            <div class="footer-logo">Sahu <span>Borewell</span></div>
            <p style="margin-top: 16px; font-size: 0.85rem; opacity: 0.8;">Professional borewell services in Lucknow since 2008.</p>
        </div>
        <div class="footer-links">
            <h4>Quick Links</h4>
            <a href="#">Borewell Drilling</a>
            <a href="#">Water Testing</a>
            <a href="#">Pump Installation</a>
            <a href="#">Maintenance Services</a>
            <a href="#">Emergency Support</a>
        </div>
        <div class="footer-contact">
            <h4>Contact Info</h4>
            <p>📞 7844883040</p>
            <p>✉ parmodsahu.pv270@gmail.com</p>
            <p>📍 Lucknow, Uttar Pradesh</p>
            <p>👤 Pramod Sahu (Proprietor)</p>
        </div>
    </div>
    <div class="footer-bottom">
        <p>© 2025 Sahu Borewell Services | All Rights Reserved | Serving Lucknow Since 2008</p>
    </div>
</footer>
""", unsafe_allow_html=True)
