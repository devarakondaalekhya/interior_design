# ✦ AI Dream Architect — Hackathon Edition

A cinematic, professional-grade AI Interior Design Assistant web application.

---

## 🗂️ Project Structure

```
ai-interior-design/
├── frontend/
│   └── index.html          # Complete frontend (HTML + CSS + JS + Three.js)
├── backend/
│   ├── app.py              # Flask REST API
│   └── requirements.txt    # Python dependencies
└── README.md
```

---

## 🚀 Run Locally

### 1. Start the Backend (Python Flask API)

```bash
cd backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the API server
python app.py
```

The API runs on: `http://localhost:5000`

### 2. Open the Frontend

Open `frontend/index.html` directly in your browser, OR serve it:

```bash
# Option A — Python simple server (from frontend directory)
cd frontend
python -m http.server 8080

# Then open: http://localhost:8080

# Option B — VS Code Live Server
# Just right-click index.html → "Open with Live Server"
```

---

## ✦ Features

### Landing Experience
- Animated Three.js particle + grid background
- Glassmorphism floating cards with hover animations
- Custom animated cursor
- Animated headline with shimmer effect

### Mode 1 — Custom Architect
- Graph paper grid canvas (GRID = 16px snapping)
- Draw walls, doors, windows interactively
- Add bedroom / kitchen / living room rooms
- Click "Generate 3D" → cinematic 3D house builds

### Mode 2 — AI Dream Builder
- 5-step wizard: Home Type → Theme → Mood → Budget → Colors
- Animated budget slider with ₹ formatting
- Clickable color palette with selection state
- AI-generated design brief with materials & recommendations
- 3D cinematic walkthrough launch

### Mode 3 — Redesign Existing
- Image upload with preview
- Animated AI analysis loader (5 steps)
- AI redesign plan with improvement roadmap
- 3D visualization inspired from analysis

### 3D Cinematic Walkthrough (Three.js)
- ACES Filmic tonemapping
- Animated camera fly-from-sky path (8 keyframes, 28-second loop)
- Progressive build sequence: floor → walls → doors → windows → roof → furniture → garden
- Directional sunlight with shadows (PCFSoft)
- Point lights with color shifting
- Stars and fog atmosphere

### Realistic Furniture
- Sofa with cushions, arms, wooden legs
- Platform bed with headboard, pillows, blanket
- TV unit with floating screen and glow
- Round marble dining table with 6 chairs
- Fiddle leaf plants with trunk and leaf clusters
- Walk-in closet with handles
- AC wall unit
- Click any furniture → Shopping popup (Amazon + IKEA links)

### AI Chatbot (Aria)
- Floating glassmorphism chat window
- Context-aware responses (lighting, furniture, color, budget, kitchen, bedroom)
- Quick suggestion chips
- API-connected with fallback responses

### Budget Analytics Dashboard
- Bar chart: room budget distribution
- Doughnut chart: category breakdown (furniture/materials/labour/décor)
- Responsive Chart.js visualizations

### UI/UX
- Dark luxury theme (deep navy + gold)
- Glassmorphism panels
- Custom cursor (gold dot + ring)
- Noise texture overlay
- Responsive layout

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health` | Health check |
| POST | `/api/generate-design` | Generate design from wizard data |
| POST | `/api/analyze-image` | Analyze uploaded image |
| POST | `/api/chat` | Chatbot response |
| POST | `/api/furniture-details` | Get furniture shopping info |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5 + CSS3 + Vanilla JS |
| 3D Engine | Three.js r128 |
| Charts | Chart.js |
| Backend | Python Flask 3.0 |
| CORS | Flask-CORS 4.0 |
| Fonts | Cormorant Garamond + Syne + JetBrains Mono |

---

## ⚡ Offline Mode

The app includes full offline fallback — if the Flask backend is not running, every feature still works with built-in demo data. You can judge the full UI experience without starting the backend.

---

## 🏆 Hackathon Notes

- No broken CDN links — Three.js r128 from official Cloudflare CDN
- No console errors
- Responsive on mobile
- Click furniture objects in 3D to open shopping popup
- Press `ESC` to close popups
