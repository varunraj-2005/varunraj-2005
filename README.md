
<!-- Animated Header Banner -->
<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" width="860" height="200" viewBox="0 0 860 200">
  <defs>
    <!-- Dark to red gradient background -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#0d0d0d;stop-opacity:1" />
      <stop offset="55%" style="stop-color:#1a0000;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#8b0000;stop-opacity:1" />
    </linearGradient>

    <!-- Glowing red gradient for name text -->
    <linearGradient id="nameGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ffffff" />
      <stop offset="50%" style="stop-color:#ffcccc" />
      <stop offset="100%" style="stop-color:#ffffff" />
    </linearGradient>

    <!-- Star glow filter -->
    <filter id="starGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="1.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Name glow filter -->
    <filter id="nameGlow">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="860" height="200" rx="12" fill="url(#bgGrad)"/>

  <!-- ====== FALLING STARS ====== -->

  <!-- Star 1 -->
  <circle cx="60" cy="-10" r="2" fill="white" filter="url(#starGlow)" opacity="0.9">
    <animateMotion dur="2.1s" repeatCount="indefinite" begin="0s">
      <mpath/>
    </animateMotion>
    <animate attributeName="cy" from="-10" to="210" dur="2.1s" repeatCount="indefinite" begin="0s"/>
    <animate attributeName="cx" from="60" to="80" dur="2.1s" repeatCount="indefinite" begin="0s"/>
    <animate attributeName="opacity" values="0;1;1;0" dur="2.1s" repeatCount="indefinite" begin="0s"/>
  </circle>
  <line x1="60" y1="-10" x2="55" y2="-22" stroke="white" stroke-width="1" opacity="0.6">
    <animate attributeName="y1" from="-10" to="210" dur="2.1s" repeatCount="indefinite" begin="0s"/>
    <animate attributeName="y2" from="-22" to="198" dur="2.1s" repeatCount="indefinite" begin="0s"/>
    <animate attributeName="x1" from="60" to="80" dur="2.1s" repeatCount="indefinite" begin="0s"/>
    <animate attributeName="x2" from="55" to="75" dur="2.1s" repeatCount="indefinite" begin="0s"/>
    <animate attributeName="opacity" values="0;0.6;0.6;0" dur="2.1s" repeatCount="indefinite" begin="0s"/>
  </line>

  <!-- Star 2 -->
  <circle cx="150" cy="-10" r="1.5" fill="white" filter="url(#starGlow)" opacity="0.9">
    <animate attributeName="cy" from="-10" to="210" dur="1.7s" repeatCount="indefinite" begin="0.4s"/>
    <animate attributeName="cx" from="150" to="168" dur="1.7s" repeatCount="indefinite" begin="0.4s"/>
    <animate attributeName="opacity" values="0;1;1;0" dur="1.7s" repeatCount="indefinite" begin="0.4s"/>
  </circle>
  <line x1="150" y1="-10" x2="145" y2="-22" stroke="white" stroke-width="1" opacity="0.6">
    <animate attributeName="y1" from="-10" to="210" dur="1.7s" repeatCount="indefinite" begin="0.4s"/>
    <animate attributeName="y2" from="-22" to="198" dur="1.7s" repeatCount="indefinite" begin="0.4s"/>
    <animate attributeName="x1" from="150" to="168" dur="1.7s" repeatCount="indefinite" begin="0.4s"/>
    <animate attributeName="x2" from="145" to="163" dur="1.7s" repeatCount="indefinite" begin="0.4s"/>
    <animate attributeName="opacity" values="0;0.6;0.6;0" dur="1.7s" repeatCount="indefinite" begin="0.4s"/>
  </line>

  <!-- Star 3 -->
  <circle cx="250" cy="-10" r="2" fill="#ffdddd" filter="url(#starGlow)" opacity="0.9">
    <animate attributeName="cy" from="-10" to="210" dur="2.5s" repeatCount="indefinite" begin="0.8s"/>
    <animate attributeName="cx" from="250" to="272" dur="2.5s" repeatCount="indefinite" begin="0.8s"/>
    <animate attributeName="opacity" values="0;1;1;0" dur="2.5s" repeatCount="indefinite" begin="0.8s"/>
  </circle>
  <line x1="250" y1="-10" x2="244" y2="-24" stroke="white" stroke-width="1" opacity="0.6">
    <animate attributeName="y1" from="-10" to="210" dur="2.5s" repeatCount="indefinite" begin="0.8s"/>
    <animate attributeName="y2" from="-24" to="196" dur="2.5s" repeatCount="indefinite" begin="0.8s"/>
    <animate attributeName="x1" from="250" to="272" dur="2.5s" repeatCount="indefinite" begin="0.8s"/>
    <animate attributeName="x2" from="244" to="266" dur="2.5s" repeatCount="indefinite" begin="0.8s"/>
    <animate attributeName="opacity" values="0;0.6;0.6;0" dur="2.5s" repeatCount="indefinite" begin="0.8s"/>
  </line>

  <!-- Star 4 -->
  <circle cx="370" cy="-10" r="1.8" fill="white" filter="url(#starGlow)" opacity="0.9">
    <animate attributeName="cy" from="-10" to="210" dur="1.9s" repeatCount="indefinite" begin="1.2s"/>
    <animate attributeName="cx" from="370" to="388" dur="1.9s" repeatCount="indefinite" begin="1.2s"/>
    <animate attributeName="opacity" values="0;1;1;0" dur="1.9s" repeatCount="indefinite" begin="1.2s"/>
  </circle>
  <line x1="370" y1="-10" x2="364" y2="-22" stroke="white" stroke-width="1" opacity="0.6">
    <animate attributeName="y1" from="-10" to="210" dur="1.9s" repeatCount="indefinite" begin="1.2s"/>
    <animate attributeName="y2" from="-22" to="198" dur="1.9s" repeatCount="indefinite" begin="1.2s"/>
    <animate attributeName="x1" from="370" to="388" dur="1.9s" repeatCount="indefinite" begin="1.2s"/>
    <animate attributeName="x2" from="364" to="382" dur="1.9s" repeatCount="indefinite" begin="1.2s"/>
    <animate attributeName="opacity" values="0;0.6;0.6;0" dur="1.9s" repeatCount="indefinite" begin="1.2s"/>
  </line>

  <!-- Star 5 -->
  <circle cx="500" cy="-10" r="2.2" fill="white" filter="url(#starGlow)">
    <animate attributeName="cy" from="-10" to="210" dur="2.3s" repeatCount="indefinite" begin="0.2s"/>
    <animate attributeName="cx" from="500" to="520" dur="2.3s" repeatCount="indefinite" begin="0.2s"/>
    <animate attributeName="opacity" values="0;1;1;0" dur="2.3s" repeatCount="indefinite" begin="0.2s"/>
  </circle>
  <line x1="500" y1="-10" x2="493" y2="-26" stroke="white" stroke-width="1.2" opacity="0.6">
    <animate attributeName="y1" from="-10" to="210" dur="2.3s" repeatCount="indefinite" begin="0.2s"/>
    <animate attributeName="y2" from="-26" to="194" dur="2.3s" repeatCount="indefinite" begin="0.2s"/>
    <animate attributeName="x1" from="500" to="520" dur="2.3s" repeatCount="indefinite" begin="0.2s"/>
    <animate attributeName="x2" from="493" to="513" dur="2.3s" repeatCount="indefinite" begin="0.2s"/>
    <animate attributeName="opacity" values="0;0.6;0.6;0" dur="2.3s" repeatCount="indefinite" begin="0.2s"/>
  </line>

  <!-- Star 6 -->
  <circle cx="620" cy="-10" r="1.5" fill="#ffeeee" filter="url(#starGlow)">
    <animate attributeName="cy" from="-10" to="210" dur="1.6s" repeatCount="indefinite" begin="0.6s"/>
    <animate attributeName="cx" from="620" to="636" dur="1.6s" repeatCount="indefinite" begin="0.6s"/>
    <animate attributeName="opacity" values="0;1;1;0" dur="1.6s" repeatCount="indefinite" begin="0.6s"/>
  </circle>
  <line x1="620" y1="-10" x2="615" y2="-20" stroke="white" stroke-width="0.8">
    <animate attributeName="y1" from="-10" to="210" dur="1.6s" repeatCount="indefinite" begin="0.6s"/>
    <animate attributeName="y2" from="-20" to="200" dur="1.6s" repeatCount="indefinite" begin="0.6s"/>
    <animate attributeName="x1" from="620" to="636" dur="1.6s" repeatCount="indefinite" begin="0.6s"/>
    <animate attributeName="x2" from="615" to="631" dur="1.6s" repeatCount="indefinite" begin="0.6s"/>
    <animate attributeName="opacity" values="0;0.5;0.5;0" dur="1.6s" repeatCount="indefinite" begin="0.6s"/>
  </line>

  <!-- Star 7 -->
  <circle cx="740" cy="-10" r="2" fill="white" filter="url(#starGlow)">
    <animate attributeName="cy" from="-10" to="210" dur="2.0s" repeatCount="indefinite" begin="1.0s"/>
    <animate attributeName="cx" from="740" to="758" dur="2.0s" repeatCount="indefinite" begin="1.0s"/>
    <animate attributeName="opacity" values="0;1;1;0" dur="2.0s" repeatCount="indefinite" begin="1.0s"/>
  </circle>
  <line x1="740" y1="-10" x2="734" y2="-24" stroke="white" stroke-width="1">
    <animate attributeName="y1" from="-10" to="210" dur="2.0s" repeatCount="indefinite" begin="1.0s"/>
    <animate attributeName="y2" from="-24" to="196" dur="2.0s" repeatCount="indefinite" begin="1.0s"/>
    <animate attributeName="x1" from="740" to="758" dur="2.0s" repeatCount="indefinite" begin="1.0s"/>
    <animate attributeName="x2" from="734" to="752" dur="2.0s" repeatCount="indefinite" begin="1.0s"/>
    <animate attributeName="opacity" values="0;0.6;0.6;0" dur="2.0s" repeatCount="indefinite" begin="1.0s"/>
  </line>

  <!-- Star 8 -->
  <circle cx="820" cy="-10" r="1.6" fill="white" filter="url(#starGlow)">
    <animate attributeName="cy" from="-10" to="210" dur="2.4s" repeatCount="indefinite" begin="1.5s"/>
    <animate attributeName="cx" from="820" to="836" dur="2.4s" repeatCount="indefinite" begin="1.5s"/>
    <animate attributeName="opacity" values="0;1;1;0" dur="2.4s" repeatCount="indefinite" begin="1.5s"/>
  </circle>
  <line x1="820" y1="-10" x2="814" y2="-22" stroke="white" stroke-width="0.9">
    <animate attributeName="y1" from="-10" to="210" dur="2.4s" repeatCount="indefinite" begin="1.5s"/>
    <animate attributeName="y2" from="-22" to="198" dur="2.4s" repeatCount="indefinite" begin="1.5s"/>
    <animate attributeName="x1" from="820" to="836" dur="2.4s" repeatCount="indefinite" begin="1.5s"/>
    <animate attributeName="x2" from="814" to="830" dur="2.4s" repeatCount="indefinite" begin="1.5s"/>
    <animate attributeName="opacity" values="0;0.6;0.6;0" dur="2.4s" repeatCount="indefinite" begin="1.5s"/>
  </line>

  <!-- Star 9 -->
  <circle cx="110" cy="-10" r="1.4" fill="#ffdddd" filter="url(#starGlow)">
    <animate attributeName="cy" from="-10" to="210" dur="2.8s" repeatCount="indefinite" begin="0.9s"/>
    <animate attributeName="cx" from="110" to="124" dur="2.8s" repeatCount="indefinite" begin="0.9s"/>
    <animate attributeName="opacity" values="0;0.9;0.9;0" dur="2.8s" repeatCount="indefinite" begin="0.9s"/>
  </circle>

  <!-- Star 10 -->
  <circle cx="680" cy="-10" r="1.9" fill="white" filter="url(#starGlow)">
    <animate attributeName="cy" from="-10" to="210" dur="2.2s" repeatCount="indefinite" begin="1.8s"/>
    <animate attributeName="cx" from="680" to="698" dur="2.2s" repeatCount="indefinite" begin="1.8s"/>
    <animate attributeName="opacity" values="0;1;1;0" dur="2.2s" repeatCount="indefinite" begin="1.8s"/>
  </circle>
  <line x1="680" y1="-10" x2="674" y2="-22" stroke="white" stroke-width="1">
    <animate attributeName="y1" from="-10" to="210" dur="2.2s" repeatCount="indefinite" begin="1.8s"/>
    <animate attributeName="y2" from="-22" to="198" dur="2.2s" repeatCount="indefinite" begin="1.8s"/>
    <animate attributeName="x1" from="680" to="698" dur="2.2s" repeatCount="indefinite" begin="1.8s"/>
    <animate attributeName="x2" from="674" to="692" dur="2.2s" repeatCount="indefinite" begin="1.8s"/>
    <animate attributeName="opacity" values="0;0.6;0.6;0" dur="2.2s" repeatCount="indefinite" begin="1.8s"/>
  </line>

  <!-- ====== NAME TEXT with blinking star effect ====== -->
  <text
    x="430"
    y="105"
    text-anchor="middle"
    font-family="'Segoe UI', Arial, sans-serif"
    font-size="58"
    font-weight="900"
    fill="url(#nameGrad)"
    filter="url(#nameGlow)"
    letter-spacing="4">
    VARUNRAJ P
    <animate attributeName="opacity" values="1;1;0.3;1;1;0.5;1;1;0.2;1;1" dur="3s" repeatCount="indefinite"/>
  </text>

  <!-- Subtitle -->
  <text
    x="430"
    y="148"
    text-anchor="middle"
    font-family="'Segoe UI', Arial, sans-serif"
    font-size="16"
    fill="#dddddd"
    letter-spacing="1"
    opacity="0.9">
    IT Student | Eager to Begin a Career in Software Development
  </text>

  <!-- Bottom curve decoration -->
  <path d="M0 185 Q430 210 860 185 L860 200 L0 200 Z" fill="rgba(139,0,0,0.3)"/>
</svg>

</div>



<p align="center">
  Motivated and detail-oriented B.Tech Information Technology student at V.S.B. Engineering College,
  passionate about building real-world solutions through web development, AI, and clean problem-solving.
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/varunraj-p-5b8813313" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="https://github.com/varunraj-2005" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>
  <a href="https://leetcode.com/u/varunraj5173/" target="_blank">
    <img src="https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black" />
  </a>
  <a href="mailto:rajapandian1412@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>
</p>

---

### 🚀 About Me

- 🎓 Currently pursuing **B.Tech in Information Technology** at **V.S.B. Engineering College** (2023 – 2027), CGPA **8.1** (till 5th semester)
- 💻 Strong foundation in **programming, web development, and emerging AI technologies**
- 🧠 Passionate about solving real-world problems through innovation — from **NLP-based sentiment analysis** to **AI-driven emergency response systems**
- 🌱 Currently exploring **Generative AI** and full-stack development with the **MERN** and **MEAN** stacks
- 🤝 Eager to contribute to dynamic tech environments through **internships and collaborative projects**
- ⚡ Quick learner with strong **problem-solving, teamwork, and communication skills**
- 📫 Reach me at **rajapandian1412@gmail.com** | **+91 93423 88727**

---

### 🛠️ Tech Stack & Skills

**Programming Languages**
![Java](https://img.shields.io/badge/-Java-007396?style=flat-square&logo=java&logoColor=white)
![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![C](https://img.shields.io/badge/-C-A8B9CC?style=flat-square&logo=c&logoColor=white)
![Node.js](https://img.shields.io/badge/-Node.js-339933?style=flat-square&logo=node.js&logoColor=white)

**Web Frameworks / Stacks**
![MERN](https://img.shields.io/badge/-MERN%20Stack-61DAFB?style=flat-square&logo=react&logoColor=black)
![MEAN](https://img.shields.io/badge/-MEAN%20Stack-DD0031?style=flat-square&logo=angular&logoColor=white)
![HTML5](https://img.shields.io/badge/-HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/-CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)

**Databases**
![MySQL](https://img.shields.io/badge/-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![MongoDB](https://img.shields.io/badge/-MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)

**Soft Skills**
`Problem Solving` `Time Management` `Teamwork` `Leadership` `Effective Communication` `Critical Thinking`

**Languages Spoken:** Tamil, English

---

### 🧩 Featured Projects

#### 🔹 [Smart Sentiment Analysis of Play Store Reviews](https://github.com/varunraj-2005) — *Developer, 2025*
Analyzed Google Play Store reviews using advanced NLP models such as **BERT, RoBERTa, and LSTM** to classify sentiment as positive, negative, or neutral. Implemented **Aspect-Based Sentiment Analysis (ABSA)** to surface insights on specific app features like performance, usability, and bugs — going beyond simple polarity detection.

#### 🔹 [College Event Management System](https://github.com/varunraj-2005) — *Developer, 2026*
Built a **MERN-stack** web application to streamline student event registrations, team formations, and faculty approvals across college departments. Engineered an anti-fraud **"Live Geotag Verification"** system using device cameras and the **Geolocation API** to capture and securely encode unalterable GPS and timestamp watermarks onto live photos.

#### 🔹 [Smart City Complaint System](https://github.com/varunraj-2005) — *Developer, 2026*
Developed a web-based complaint management system for smart city grievance redressal using **HTML, CSS, and SQL**, enabling citizens to register, track, and resolve civic complaints efficiently.

---

### 🎓 Education

| Institution | Degree/Level | Duration | Score |
|---|---|---|---|
| V.S.B. Engineering College | B.Tech – Information Technology | 2023 – 2027 | CGPA 8.1 (till 5th sem) |
| RaniMeyyammai Govt. Aided School, Puliyur | HSC (State Board) | 2022 – 2023 | 78.5% (Cutoff: 154.5) |

---

### 💼 Internship Experience

**Infosys (Virtual Internship)** — *Full Stack Intern* | 2024 – 2025
- Completed **Java Full Stack Web Development** on Infosys Springboard
- Built a **"Live Commentary to Multi-Language Text"** project during the internship

---

### 📜 Certifications

- 🏅 Infosys Springboard: Java Full Stack Web Development Certification
- 🏅 IT-ITeS SSC (NASSCOM): Generative AI Fluency Certification
- 🏅 NPTEL: Programming in Java — Elite Silver, 77% (Jan–Apr 2025)
- 🏅 NPTEL: Big Data Computing — Elite Silver, 81% (Aug–Oct 2025)
- 🏅 NPTEL: Database Management — Elite, 67% (Jan–Mar 2026)
- 🏅 IT-ITeS SSC (NASSCOM): Introduction to IoT and Digital Transformation — Gold, 79% (Mar 2026)

---

### 🏆 Achievements

- ✅ Solved **100+ problems** on LeetCode
- ✅ Earned a **5-star Gold Badge** on HackerRank (Java)
- ✅ Completed Java Full Stack Web Development on Infosys Springboard with internship certificate

---

### 📊 GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=varunraj-2005&show_icons=true&theme=radical" alt="Varunraj's GitHub Stats" height="165"/>
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=varunraj-2005&theme=radical" alt="Varunraj's GitHub Streak" height="165"/>
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=varunraj-2005&layout=compact&theme=radical" alt="Top Languages" />
</p>

---

<p align="center">
  <i>"Quick learner with excellent problem-solving and communication skills — eager to build, break, and rebuild."</i>
</p>
