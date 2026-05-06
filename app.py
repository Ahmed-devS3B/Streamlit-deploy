import streamlit as st

st.set_page_config(
    page_title="Ahmed Ibrahim • Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Outfit:wght@300;400;500;600;700;800&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, .stApp {
    background: #060608;
    color: #c9d1d9;
    font-family: 'Outfit', sans-serif;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 2.5rem 5rem 2.5rem; max-width: 1280px; }

/* ── HERO ── */
.hero {
    min-height: 90vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 6rem 0 4rem;
    position: relative;
}
.hero-grid {
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(rgba(6,182,212,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(6,182,212,0.03) 1px, transparent 1px);
    background-size: 60px 60px;
    mask-image: radial-gradient(ellipse at center, black 30%, transparent 80%);
}
.hero-glow {
    position: absolute;
    top: 20%; left: -10%;
    width: 500px; height: 500px;
    background: radial-gradient(circle, rgba(6,182,212,0.08) 0%, transparent 70%);
    pointer-events: none;
    animation: pulse 4s ease-in-out infinite;
}
.hero-glow-2 {
    position: absolute;
    bottom: 10%; right: -5%;
    width: 400px; height: 400px;
    background: radial-gradient(circle, rgba(139,92,246,0.07) 0%, transparent 70%);
    pointer-events: none;
    animation: pulse 4s ease-in-out infinite 2s;
}
@keyframes pulse {
    0%, 100% { opacity: 0.6; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.1); }
}
.hero-eyebrow {
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    color: #06b6d4;
    letter-spacing: 0.2em;
    margin-bottom: 1.25rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
}
.hero-eyebrow::before {
    content: '';
    display: inline-block;
    width: 2rem;
    height: 1px;
    background: #06b6d4;
}
.hero-name {
    font-family: 'Outfit', sans-serif;
    font-size: clamp(3.5rem, 8vw, 7rem);
    font-weight: 800;
    line-height: 0.95;
    letter-spacing: -0.04em;
    color: #f0f6fc;
    margin-bottom: 1.25rem;
}
.hero-name .accent { color: #06b6d4; }
.hero-roles {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    margin-bottom: 2rem;
}
.role-tag {
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 0.4rem 0.9rem;
    border-radius: 4px;
    border: 1px solid;
}
.role-cyan { color: #06b6d4; border-color: rgba(6,182,212,0.3); background: rgba(6,182,212,0.06); }
.role-violet { color: #8b5cf6; border-color: rgba(139,92,246,0.3); background: rgba(139,92,246,0.06); }
.role-green { color: #10b981; border-color: rgba(16,185,129,0.3); background: rgba(16,185,129,0.06); }
.hero-desc {
    max-width: 520px;
    font-size: 1.05rem;
    line-height: 1.8;
    color: #6b7280;
    margin-bottom: 2.5rem;
    font-weight: 300;
}
.hero-desc strong { color: #9ca3af; font-weight: 500; }
.hero-links { display: flex; gap: 1rem; flex-wrap: wrap; }
.hero-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-family: 'Space Mono', monospace;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    padding: 0.85rem 1.75rem;
    border-radius: 6px;
    text-decoration: none;
    transition: all 0.2s;
}
.btn-primary { background: #06b6d4; color: #060608; box-shadow: 0 0 30px rgba(6,182,212,0.3); }
.btn-primary:hover { box-shadow: 0 0 50px rgba(6,182,212,0.5); transform: translateY(-2px); }
.btn-ghost { background: transparent; color: #6b7280; border: 1px solid rgba(255,255,255,0.08); }
.btn-ghost:hover { border-color: rgba(6,182,212,0.3); color: #06b6d4; }

/* ── SECTION ── */
.sec-header { margin-bottom: 2.5rem; position: relative; padding-left: 1.25rem; }
.sec-header::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 3px;
    background: linear-gradient(180deg, #06b6d4, #8b5cf6);
    border-radius: 2px;
}
.sec-label { font-family: 'Space Mono', monospace; font-size: 0.68rem; letter-spacing: 0.2em; text-transform: uppercase; color: #06b6d4; margin-bottom: 0.4rem; }
.sec-title { font-family: 'Outfit', sans-serif; font-size: clamp(1.6rem, 3vw, 2.2rem); font-weight: 800; color: #f0f6fc; letter-spacing: -0.03em; }

/* ── DIVIDER ── */
.hr { height: 1px; background: linear-gradient(90deg, transparent, rgba(6,182,212,0.2), rgba(139,92,246,0.2), transparent); margin: 4rem 0; }

/* ── STATS ── */
.stat-row { display: flex; gap: 1px; background: rgba(255,255,255,0.04); border-radius: 12px; overflow: hidden; border: 1px solid rgba(255,255,255,0.05); }
.stat-cell { flex: 1; padding: 2rem 1.5rem; background: #0d0d12; text-align: center; }
.stat-val { font-family: 'Space Mono', monospace; font-size: 2.5rem; font-weight: 700; color: #06b6d4; line-height: 1; margin-bottom: 0.4rem; }
.stat-lbl { font-size: 0.78rem; color: #4b5563; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 600; }

/* ── SKILLS ── */
.skill-category { background: #0d0d12; border: 1px solid rgba(255,255,255,0.05); border-radius: 12px; padding: 1.75rem; height: 100%; }
.skill-cat-title { font-family: 'Space Mono', monospace; font-size: 0.72rem; letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 1.25rem; display: flex; align-items: center; gap: 0.5rem; }
.cat-cyan { color: #06b6d4; }
.cat-violet { color: #8b5cf6; }
.cat-green { color: #10b981; }
.cat-orange { color: #f59e0b; }
.badges { display: flex; flex-wrap: wrap; gap: 0.5rem; }
.badge-img { height: 26px; border-radius: 4px; }

/* ── PROJECTS ── */
.proj { background: #0d0d12; border: 1px solid rgba(255,255,255,0.05); border-radius: 12px; padding: 2rem; position: relative; overflow: hidden; transition: border-color 0.3s, transform 0.3s; height: 100%; }
.proj::after { content: ''; position: absolute; inset: 0; background: linear-gradient(135deg, rgba(6,182,212,0.03) 0%, transparent 60%); pointer-events: none; }
.proj:hover { border-color: rgba(6,182,212,0.25); transform: translateY(-4px); }
.proj-num { font-family: 'Space Mono', monospace; font-size: 0.65rem; color: #374151; letter-spacing: 0.1em; margin-bottom: 1rem; }
.proj-title { font-family: 'Outfit', sans-serif; font-size: 1.2rem; font-weight: 700; color: #f0f6fc; margin-bottom: 0.6rem; letter-spacing: -0.02em; }
.proj-desc { font-size: 0.875rem; color: #6b7280; line-height: 1.7; margin-bottom: 1.25rem; font-weight: 300; }
.tech-row { display: flex; flex-wrap: wrap; gap: 0.4rem; }
.tech { font-family: 'Space Mono', monospace; font-size: 0.68rem; color: #4b5563; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); padding: 0.25rem 0.6rem; border-radius: 4px; }

/* ── GITHUB ── */
.gh-img { width: 100%; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05); }

/* ── CONTACT ── */
.contact-wrap { background: linear-gradient(135deg, rgba(6,182,212,0.06), rgba(139,92,246,0.04)); border: 1px solid rgba(6,182,212,0.15); border-radius: 16px; padding: 3.5rem 2.5rem; text-align: center; }
.contact-title { font-family: 'Outfit', sans-serif; font-size: 2.5rem; font-weight: 800; color: #f0f6fc; letter-spacing: -0.03em; margin-bottom: 0.75rem; }
.contact-sub { color: #4b5563; font-size: 0.95rem; margin-bottom: 2rem; font-weight: 300; }
.contact-btns { display: flex; justify-content: center; flex-wrap: wrap; gap: 0.75rem; }
.c-btn { display: inline-flex; align-items: center; gap: 0.5rem; font-family: 'Space Mono', monospace; font-size: 0.75rem; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; padding: 0.75rem 1.5rem; border-radius: 6px; text-decoration: none; border: 1px solid; transition: all 0.2s; }
.c-linkedin { color: #0a66c2; border-color: rgba(10,102,194,0.3); background: rgba(10,102,194,0.07); }
.c-github { color: #f0f6fc; border-color: rgba(240,246,252,0.15); background: rgba(240,246,252,0.04); }
.footer { text-align: center; color: #1f2937; font-family: 'Space Mono', monospace; font-size: 0.7rem; letter-spacing: 0.1em; margin-top: 3rem; }
</style>
""", unsafe_allow_html=True)

# HERO
st.markdown("""
<div class="hero">
    <div class="hero-grid"></div>
    <div class="hero-glow"></div>
    <div class="hero-glow-2"></div>
    <div class="hero-eyebrow">PORTFOLIO · 2026</div>
    <div class="hero-name">Ahmed<br><span class="accent">Ibrahim</span></div>
    <div class="hero-roles">
        <span class="role-tag role-cyan">⚡ Big Data Engineer</span>
        <span class="role-tag role-violet">⚛️ React Developer</span>
        <span class="role-tag role-green">🌐 Next.js Developer</span>
    </div>
    <p class="hero-desc">
        I speak both the language of <strong>data</strong> and the <strong>web</strong>.<br>
        Building scalable pipelines with Spark & Hadoop, and crafting
        clean, fast interfaces with React & Next.js.
    </p>
    <div class="hero-links">
        <a class="hero-btn btn-primary" href="https://www.linkedin.com/in/ahmeedibrahim" target="_blank">🔗 LinkedIn</a>
        <a class="hero-btn btn-ghost" href="https://github.com/Ahmed-devS3B" target="_blank">⭐ GitHub</a>
    </div>
</div>
""", unsafe_allow_html=True)

# STATS
st.markdown("""
<div class="stat-row">
    <div class="stat-cell"><div class="stat-val">15+</div><div class="stat-lbl">Projects</div></div>
    <div class="stat-cell"><div class="stat-val">10+</div><div class="stat-lbl">Technologies</div></div>
    <div class="stat-cell"><div class="stat-val">2+</div><div class="stat-lbl">Years Exp.</div></div>
    <div class="stat-cell"><div class="stat-val">2</div><div class="stat-lbl">Domains</div></div>
</div>
""", unsafe_allow_html=True)

# ABOUT
st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="sec-header">
    <div class="sec-label">// who i am</div>
    <div class="sec-title">About Me</div>
</div>
""", unsafe_allow_html=True)

a1, a2 = st.columns([1.2, 1])
with a1:
    st.markdown("""
    <div style="font-size:1rem; line-height:1.9; color:#6b7280; font-weight:300;">
        I'm a <span style="color:#06b6d4; font-weight:600;">Big Data Engineer</span> and
        <span style="color:#8b5cf6; font-weight:600;">React Developer</span> passionate about
        building systems that handle data at scale and interfaces that delight users.<br><br>
        Currently working on <strong style="color:#9ca3af;">Big Data pipelines</strong> and
        <strong style="color:#9ca3af;">React applications</strong>, always exploring the intersection
        of data engineering and modern frontend development.<br><br>
        💬 Ask me about <strong style="color:#9ca3af;">Python, SQL, React, Next.js</strong><br>
        ⚡ Fun fact: I speak both the language of data and the web.
    </div>
    """, unsafe_allow_html=True)

with a2:
    st.markdown("""
    <div style="background:#0d0d12; border:1px solid rgba(255,255,255,0.05); border-radius:12px; padding:1.75rem;">
        <div style="font-family:'Space Mono',monospace; font-size:0.68rem; color:#06b6d4; letter-spacing:0.15em; text-transform:uppercase; margin-bottom:1.25rem;">CURRENTLY</div>
        <div style="display:flex; flex-direction:column; gap:1rem;">
            <div style="display:flex; gap:0.75rem;">
                <span>🔭</span>
                <div><div style="font-size:0.8rem; color:#9ca3af; font-weight:500;">Working on</div><div style="font-size:0.85rem; color:#6b7280;">Big Data pipelines & React apps</div></div>
            </div>
            <div style="display:flex; gap:0.75rem;">
                <span>🌱</span>
                <div><div style="font-size:0.8rem; color:#9ca3af; font-weight:500;">Exploring</div><div style="font-size:0.85rem; color:#6b7280;">Data engineering & modern frontend</div></div>
            </div>
            <div style="display:flex; gap:0.75rem;">
                <span>🎯</span>
                <div><div style="font-size:0.8rem; color:#9ca3af; font-weight:500;">Goal</div><div style="font-size:0.85rem; color:#6b7280;">Turning data into insights & clean UIs</div></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# TECH STACK
st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="sec-header">
    <div class="sec-label">// what i use</div>
    <div class="sec-title">Tech Stack</div>
</div>
""", unsafe_allow_html=True)

t1, t2 = st.columns(2)
with t1:
    st.markdown("""
    <div class="skill-category">
        <div class="skill-cat-title cat-cyan">📊 Data Engineering</div>
        <div class="badges">
            <img class="badge-img" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
            <img class="badge-img" src="https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white"/>
            <img class="badge-img" src="https://img.shields.io/badge/Hadoop-66CCFF?style=for-the-badge&logo=apachehadoop&logoColor=black"/>
            <img class="badge-img" src="https://img.shields.io/badge/Apache_Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white"/>
        </div>
    </div>
    """, unsafe_allow_html=True)

with t2:
    st.markdown("""
    <div class="skill-category">
        <div class="skill-cat-title cat-violet">⚛️ Frontend</div>
        <div class="badges">
            <img class="badge-img" src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB"/>
            <img class="badge-img" src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white"/>
            <img class="badge-img" src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white"/>
            <img class="badge-img" src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/>
            <img class="badge-img" src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white"/>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
t3, t4 = st.columns(2)

with t3:
    st.markdown("""
    <div class="skill-category">
        <div class="skill-cat-title cat-green">🗄️ Databases & APIs</div>
        <div class="badges">
            <img class="badge-img" src="https://img.shields.io/badge/SQL_Server-CC2927?style=for-the-badge&logo=microsoftsqlserver&logoColor=white"/>
            <img class="badge-img" src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white"/>
            <img class="badge-img" src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white"/>
            <img class="badge-img" src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"/>
            <img class="badge-img" src="https://img.shields.io/badge/REST_API-005571?style=for-the-badge&logo=fastapi&logoColor=white"/>
        </div>
    </div>
    """, unsafe_allow_html=True)

with t4:
    st.markdown("""
    <div class="skill-category">
        <div class="skill-cat-title cat-orange">💻 Tools & IDEs</div>
        <div class="badges">
            <img class="badge-img" src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
            <img class="badge-img" src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white"/>
            <img class="badge-img" src="https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white"/>
            <img class="badge-img" src="https://img.shields.io/badge/Visual_Studio-5C2D91?style=for-the-badge&logo=visualstudio&logoColor=white"/>
            <img class="badge-img" src="https://img.shields.io/badge/PyCharm-000000?style=for-the-badge&logo=pycharm&logoColor=white"/>
            <img class="badge-img" src="https://img.shields.io/badge/MATLAB-0076A8?style=for-the-badge&logo=mathworks&logoColor=white"/>
        </div>
    </div>
    """, unsafe_allow_html=True)

# PROJECTS
st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="sec-header">
    <div class="sec-label">// what i've built</div>
    <div class="sec-title">Featured Projects</div>
</div>
""", unsafe_allow_html=True)

p1, p2 = st.columns(2)
with p1:
    st.markdown("""
    <div class="proj">
        <div class="proj-num">PROJECT_01</div>
        <div class="proj-title">🛒 FreshCart Marketplace</div>
        <p class="proj-desc">Full-stack multi-vendor e-commerce platform with role-based access for Customers, Vendors & Admins. Features real-time notifications via SignalR, JWT auth, and a PostgreSQL backend deployed on Railway.</p>
        <div class="tech-row">
            <span class="tech">React</span><span class="tech">.NET 8</span><span class="tech">PostgreSQL</span><span class="tech">SignalR</span><span class="tech">Tailwind</span><span class="tech">Vercel</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown("""
    <div class="proj">
        <div class="proj-num">PROJECT_02</div>
        <div class="proj-title">🗄️ Big Data Pipeline</div>
        <p class="proj-desc">Scalable distributed data engineering pipeline for processing and analyzing large-scale datasets. Built with a Hadoop/Spark stack with ETL jobs, Airflow scheduling, and SQL reporting.</p>
        <div class="tech-row">
            <span class="tech">Python</span><span class="tech">Apache Spark</span><span class="tech">Hadoop</span><span class="tech">Airflow</span><span class="tech">SQL</span><span class="tech">MongoDB</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
p3, p4 = st.columns(2)

with p3:
    st.markdown("""
    <div class="proj">
        <div class="proj-num">PROJECT_03</div>
        <div class="proj-title">📊 Analytics Dashboard</div>
        <p class="proj-desc">Modern admin dashboard with interactive charts, real-time metrics, and a clean dark UI. Built with React and Recharts for dynamic data visualization.</p>
        <div class="tech-row">
            <span class="tech">React.js</span><span class="tech">Next.js</span><span class="tech">Tailwind CSS</span><span class="tech">Recharts</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with p4:
    st.markdown("""
    <div class="proj">
        <div class="proj-num">PROJECT_04</div>
        <div class="proj-title">⚡ Developer Portfolio</div>
        <p class="proj-desc">This interactive portfolio built with Streamlit — showcasing projects, skills, and GitHub stats with a premium dark terminal-inspired aesthetic and smooth animations.</p>
        <div class="tech-row">
            <span class="tech">Python</span><span class="tech">Streamlit</span><span class="tech">CSS</span><span class="tech">HTML</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# GITHUB STATS
st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="sec-header">
    <div class="sec-label">// activity</div>
    <div class="sec-title">GitHub Stats</div>
</div>
""", unsafe_allow_html=True)

g1, g2 = st.columns(2)
with g1:
    st.markdown('<img class="gh-img" src="https://github-readme-streak-stats.herokuapp.com/?user=Ahmed-devS3B&theme=tokyonight&hide_border=true&background=0d0d12&ring=06b6d4&fire=8b5cf6&currStreakLabel=06b6d4"/>', unsafe_allow_html=True)
with g2:
    st.markdown('<img class="gh-img" src="https://github-readme-stats.vercel.app/api?username=Ahmed-devS3B&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0d0d12&title_color=06b6d4&icon_color=8b5cf6&text_color=6b7280"/>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<img class="gh-img" src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=Ahmed-devS3B&theme=tokyonight"/>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div style="text-align:center;"><img src="https://raw.githubusercontent.com/Ahmed-devS3B/Ahmed-devS3B/output/github-contribution-grid-snake.svg" style="max-width:100%; border-radius:12px;"/></div>', unsafe_allow_html=True)

# CONTACT
st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="contact-wrap">
    <div class="contact-title">Let's Build Together</div>
    <p class="contact-sub">Open to data engineering roles, frontend projects, and interesting collaborations.</p>
    <div class="contact-btns">
        <a class="c-btn c-linkedin" href="https://www.linkedin.com/in/ahmeedibrahim" target="_blank">🔗 LinkedIn</a>
        <a class="c-btn c-github" href="https://github.com/Ahmed-devS3B" target="_blank">⭐ GitHub</a>
    </div>
</div>
<div class="footer" style="margin-top:2.5rem;">AHMED IBRAHIM · BUILT WITH STREAMLIT · 2026</div>
""", unsafe_allow_html=True)