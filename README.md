<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>🎬 Movie Recommender System — README (HTML)</title>
  <style>
    :root{
      --bg:#0b0f14;          /* page background */
      --card:#0f1520;        /* card background */
      --muted:#97a3b6;       /* secondary text */
      --text:#e6edf3;        /* primary text */
      --accent:#7aa2f7;      /* links & accents */
      --accent-2:#22c55e;    /* badges/ok */
      --border:#1f2a37;      /* outlines */
      --code-bg:#0a0f15;     /* code block */
      --kbd-bg:#0b1220;      /* inline code */
      --shadow: 0 10px 30px rgba(0,0,0,.35);
      --radius: 18px;
    }
    *{box-sizing:border-box}
    html,body{height:100%}
    body{
      margin:0; background:radial-gradient(1200px 800px at 80% -10%, #162237 0%, transparent 60%),
                 radial-gradient(1000px 700px at -10% 20%, #13202f 0%, transparent 60%),
                 var(--bg);
      color:var(--text);
      font:16px/1.6 system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, "Helvetica Neue", Arial, "Apple Color Emoji", "Segoe UI Emoji";
    }
    .container{max-width:1100px; margin:auto; padding:40px 20px}
    .card{background:linear-gradient(180deg, rgba(255,255,255,.03), rgba(255,255,255,.01)); border:1px solid var(--border); border-radius:var(--radius); box-shadow:var(--shadow);}
    .hero{padding:36px 28px 24px}
    .title{display:flex; align-items:center; gap:14px; flex-wrap:wrap;}
    .title h1{margin:0; font-size: clamp(26px, 3vw, 38px); letter-spacing:.3px}
    .subtitle{margin:.4rem 0 0; color:var(--muted)}

    .badges{display:flex; gap:10px; flex-wrap:wrap; margin:18px 0 6px}
    .badges a img{height:22px; display:block; filter:drop-shadow(0 1px 1px rgba(0,0,0,.4))}

    .grid{display:grid; gap:16px; grid-template-columns:repeat(12,1fr)}
    .section{grid-column:1/-1; background:var(--card); border:1px solid var(--border); border-radius:var(--radius); padding:22px}
    .section h2{margin:0 0 10px; font-size: clamp(20px, 2.3vw, 26px)}
    .section p{margin:8px 0}
    .muted{color:var(--muted)}

    .list{margin:0; padding-left:18px}
    .list li{margin:.35rem 0}

    .code, pre{background:var(--code-bg); border:1px solid var(--border); border-radius:14px; padding:14px; overflow:auto; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; font-size:.95rem}
    code{background:var(--kbd-bg); padding:.15rem .4rem; border:1px solid var(--border); border-radius:8px; font-size:.95em}

    .structure{white-space:pre; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace}

    .two-col{display:grid; grid-template-columns: repeat(12, 1fr); gap:16px}
    .two-col .section{grid-column: span 12}
    @media (min-width: 860px){ .two-col .left{grid-column: span 7} .two-col .right{grid-column: span 5} }

    .footer{color:var(--muted); text-align:center; margin:26px 0 6px}
    a{color:var(--accent); text-decoration:none}
    a:hover{text-decoration:underline}
    .pill{display:inline-block; padding:.2rem .6rem; border:1px solid var(--border); border-radius:999px; background:rgba(122,162,247,.08)}
  </style>
</head>
<body>
  <main class="container">
    <!-- HERO -->
    <section class="card hero">
      <div class="title">
        <span style="font-size:1.8rem">🎬</span>
        <h1>Movie Recommender System</h1>
        <span class="pill">Content‑Based • Cosine Similarity</span>
      </div>
      <p class="subtitle">A machine learning–powered recommender that suggests movies by computing similarity on curated features. Built with <strong>Python</strong>, <strong>Pandas</strong>, and <strong>Scikit‑learn</strong>. Deployable on <strong>Render</strong> or <strong>Hugging Face Spaces</strong>.</p>

      <div class="badges">
        <a href="https://www.python.org/" target="_blank" rel="noopener"><img alt="Python" src="https://img.shields.io/badge/Python-3.x-blue?logo=python"></a>
        <a href="https://streamlit.io/" target="_blank" rel="noopener"><img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-App-red?logo=streamlit"></a>
        <a href="https://scikit-learn.org/" target="_blank" rel="noopener"><img alt="Scikit-Learn" src="https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn"></a>
        <a href="https://render.com/" target="_blank" rel="noopener"><img alt="Deployment" src="https://img.shields.io/badge/Deployed%20on-Render-46a2f1?logo=render"></a>
        <a href="#license"><img alt="License" src="https://img.shields.io/badge/License-MIT-green.svg"></a>
      </div>
    </section>

    <!-- FEATURES & STACK -->
    <section class="grid" style="margin-top:16px">
      <div class="section">
        <h2>🚀 Features</h2>
        <ul class="list">
          <li><strong>Content‑based filtering</strong> using cosine similarity on engineered movie features</li>
          <li><strong>Fast recommendations</strong> via pre‑computed similarity matrix</li>
          <li>Simple web UI using <strong>Streamlit</strong> or <strong>Flask</strong></li>
          <li>Handles thousands of titles efficiently</li>
          <li><strong>Deploy anywhere</strong>: Render or Hugging Face Spaces</li>
        </ul>
      </div>
      <div class="section">
        <h2>🛠️ Tech Stack</h2>
        <ul class="list">
          <li><strong>Python 3</strong></li>
          <li><strong>Pandas</strong> — data handling</li>
          <li><strong>Scikit‑learn</strong> — vectorization & similarity</li>
          <li><strong>Pickle</strong> — serialize pre‑computed models</li>
          <li><strong>Streamlit / Flask</strong> — front‑end</li>
          <li><strong>Render</strong> — deployment</li>
        </ul>
      </div>
    </section>

    <!-- STRUCTURE -->
    <section class="section">
      <h2>📂 Project Structure</h2>
      <pre class="structure">movie-recommender/
│── app.py             # Main application file
│── movies.pkl         # Movie metadata (compressed dataset)
│── similarity.pkl     # Pre-computed similarity matrix
│── requirements.txt   # Dependencies
│── setup.sh           # Setup script (for Render deployment)
│── README.md          # Project documentation</pre>
    </section>

    <!-- QUICK START (two column on wide) -->
    <section class="two-col" style="margin-top:16px">
      <div class="section left">
        <h2>⚡ Quick Start</h2>
        <h3>1️⃣ Clone the repository</h3>
        <pre class="code">git clone https://github.com/&lt;your-username&gt;/movie-recommender.git
cd movie-recommender</pre>
        <h3>2️⃣ Install dependencies</h3>
        <pre class="code">pip install -r requirements.txt</pre>
        <h3>3️⃣ Run the app</h3>
        <p><strong>Streamlit</strong></p>
        <pre class="code">streamlit run app.py</pre>
        <p><strong>Flask</strong></p>
        <pre class="code">python app.py</pre>
      </div>
      <div class="section right">
        <h2>🌍 Deployment on Render</h2>
        <ol class="list">
          <li>Push your code to <strong>GitHub</strong>.</li>
          <li>Connect your repository to <strong>Render</strong>.</li>
          <li>Add a <code>setup.sh</code> to download <code>.pkl</code> files if hosted externally.</li>
          <li>Deploy and share your <strong>public URL</strong> 🎉</li>
        </ol>
        <p class="muted">Tip: For a <em>free</em> alternative, deploy on <a href="https://huggingface.co/spaces" target="_blank" rel="noopener">Hugging Face Spaces</a> with Streamlit/Gradio.</p>
      </div>
    </section>

    <!-- SCREENSHOTS -->
    <section class="section">
      <h2>📸 Screenshots</h2>
      <p class="muted">Add screenshots or GIFs of the UI (homepage and recommendation results) after deployment.</p>
    </section>

    <!-- FUTURE -->
    <section class="section">
      <h2>💡 Future Improvements</h2>
      <ul class="list">
        <li>Collaborative filtering (user‑based/implicit feedback)</li>
        <li>Integrate <strong>TMDB API</strong> for posters & rich metadata</li>
        <li>Dockerize for reproducible, scalable deployments</li>
      </ul>
    </section>

    <!-- CONTRIBUTING -->
    <section class="section">
      <h2>🤝 Contributing</h2>
      <ol class="list">
        <li>Fork the repository</li>
        <li>Create a new branch</li>
        <li>Commit your changes</li>
        <li>Open a Pull Request 🎯</li>
      </ol>
    </section>

    <!-- SUPPORT -->
    <section class="section">
      <h2>⭐ Show Your Support</h2>
      <p>If you find this useful, give the project a star on GitHub — it helps others discover it!</p>
    </section>

    <!-- AUTHOR -->
    <section class="section" id="license">
      <h2>👨‍💻 Author</h2>
      <p><strong>Mubasir Anwar</strong></p>
      <p>📧 <a href="mailto:mubasiranwar70@gmail.com">mubasiranwar70@gmail.com</a><br>
         💼 <a href="https://www.linkedin.com/in/mubasir-anwar-013628316/" target="_blank" rel="noopener">LinkedIn Profile</a></p>
      <p class="muted">License: MIT</p>
    </section>

    <p class="footer">© <span id="year"></span> Movie Recommender System — README (HTML). All rights reserved.</p>
  </main>

  <script>
    // tiny enhancement: current year in footer
    document.getElementById('year').textContent = new Date().getFullYear();
  </script>
</body>
</html>

