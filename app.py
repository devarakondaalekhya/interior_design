from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import json
import time

app = Flask(__name__)
CORS(app)

DESIGN_THEMES = {
    "modern": {
        "colors": ["#1a1a2e", "#16213e", "#0f3460", "#e94560"],
        "materials": ["Brushed Steel", "Glass", "Concrete", "Marble"],
        "furniture_style": "Sleek minimalist with clean lines",
        "lighting": "Recessed LED with accent strips"
    },
    "classic": {
        "colors": ["#8B7355", "#D4AF37", "#F5F5DC", "#4A3728"],
        "materials": ["Mahogany Wood", "Velvet", "Brass", "Marble"],
        "furniture_style": "Ornate with carved details and rich fabrics",
        "lighting": "Chandelier with warm Edison bulbs"
    },
    "indo_western": {
        "colors": ["#800020", "#DAA520", "#228B22", "#FF7F50"],
        "materials": ["Teak Wood", "Silk", "Jali Work", "Terracotta"],
        "furniture_style": "Fusion of traditional motifs with modern comfort",
        "lighting": "Jali lanterns with warm ambient glow"
    },
    "tech_futuristic": {
        "colors": ["#00FFFF", "#0D0D0D", "#1A1A2E", "#00FF41"],
        "materials": ["Carbon Fiber", "Acrylic", "LED Panels", "Smart Glass"],
        "furniture_style": "Modular smart furniture with embedded tech",
        "lighting": "RGB programmable strips and smart panels"
    }
}

ROOM_BUDGETS = {
    "villa": {"living": 0.25, "bedroom": 0.20, "kitchen": 0.15, "bathroom": 0.10, "garden": 0.15, "misc": 0.15},
    "apartment": {"living": 0.30, "bedroom": 0.25, "kitchen": 0.20, "bathroom": 0.15, "misc": 0.10},
    "flat": {"living": 0.35, "bedroom": 0.30, "kitchen": 0.20, "bathroom": 0.15}
}

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "message": "AI Interior Design API Running"})

@app.route('/api/generate-design', methods=['POST'])
def generate_design():
    data = request.get_json()
    home_type = data.get('home_type', 'apartment').lower()
    theme = data.get('theme', 'modern').lower().replace(' ', '_')
    mood = data.get('mood', 'luxury').lower()
    budget = data.get('budget', 500000)
    colors = data.get('colors', ['#2C3E50', '#E8D5B7'])

    theme_data = DESIGN_THEMES.get(theme, DESIGN_THEMES['modern'])
    budget_dist = ROOM_BUDGETS.get(home_type, ROOM_BUDGETS['apartment'])

    room_budgets = {room: int(budget * pct) for room, pct in budget_dist.items()}

    design_plan = {
        "summary": f"Your {mood} {theme.replace('_',' ').title()} {home_type.title()} has been crafted with precision. "
                   f"We selected {', '.join(theme_data['materials'][:2])} as primary materials to achieve that "
                   f"authentic {theme.replace('_',' ')} aesthetic. The {theme_data['lighting']} will set the perfect ambiance.",
        "theme": theme,
        "mood": mood,
        "home_type": home_type,
        "total_budget": budget,
        "room_budgets": room_budgets,
        "colors": theme_data['colors'],
        "materials": theme_data['materials'],
        "furniture_style": theme_data['furniture_style'],
        "lighting": theme_data['lighting'],
        "ai_recommendations": [
            f"Install {theme_data['lighting']} for maximum {mood} ambiance",
            f"Use {theme_data['materials'][0]} flooring throughout for cohesion",
            f"Place statement {theme_data['materials'][1]} pieces as focal points",
            "Maximize natural light with strategically placed mirrors",
            f"The {mood} theme calls for {theme_data['furniture_style']}"
        ],
        "furniture_list": generate_furniture_list(theme, mood, budget),
        "shopping_links": generate_shopping_links(theme)
    }

    return jsonify(design_plan)

@app.route('/api/analyze-image', methods=['POST'])
def analyze_image():
    # Simulate AI image analysis
    time.sleep(0.5)
    styles = ['Modern Minimalist', 'Scandinavian', 'Industrial Chic', 'Bohemian', 'Contemporary Luxury']
    materials = ['Oak Wood', 'Marble', 'Brushed Brass', 'Linen', 'Concrete']
    colors = ['Warm Neutrals', 'Cool Grays', 'Earth Tones', 'Monochromatic']

    return jsonify({
        "detected_style": random.choice(styles),
        "detected_materials": random.sample(materials, 3),
        "dominant_colors": random.choice(colors),
        "brightness": random.choice(['Bright and Airy', 'Moody and Dark', 'Warm and Inviting']),
        "layout_type": random.choice(['Open Plan', 'Traditional Rooms', 'Studio']),
        "ai_redesign_plan": "Based on your uploaded image, I've detected a sophisticated design language. I'll preserve the spatial flow while elevating the materials and introducing carefully curated statement pieces. The redesign will amplify what works — the proportions and light — while modernizing the surface treatments.",
        "improvements": [
            "Elevate ceiling materials with coffered or stretched fabric detail",
            "Replace standard lighting with architectural fixtures",
            "Introduce layered textiles for depth and warmth",
            "Add biophilic elements — large statement plants",
            "Upgrade hardware and fixtures to brushed brass"
        ],
        "estimated_cost": random.randint(150000, 800000)
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '').lower()
    context = data.get('context', {})

    responses = {
        'lighting': "Great question! For your space, I recommend a three-layer lighting approach: ambient (recessed ceiling lights), task (pendant or under-cabinet), and accent (LED strips or wall sconces). This creates depth and allows mood adjustment throughout the day.",
        'furniture': "Your furniture selection should follow the 60-30-10 rule: 60% dominant color pieces, 30% secondary, 10% accent. For your chosen theme, I'd suggest anchoring the room with a statement sofa, then building outward.",
        'color': "Color psychology is key here. Your palette suggests a desire for balance between energy and calm. I'd recommend cool tones for productivity spaces and warm amber accents for relaxation zones.",
        'budget': "Smart budgeting tip: allocate 35% to statement pieces you'll live with daily (sofa, bed), 40% to quality materials (flooring, kitchen surfaces), and 25% to décor that can be refreshed seasonally.",
        'kitchen': "For your kitchen, the triangle principle (sink-stove-refrigerator) should guide layout. With your budget, I'd prioritize quality countertops and cabinetry hardware — these affect daily experience most.",
        'bedroom': "The bedroom is your sanctuary. Layer your lighting, invest in a quality mattress base, and use curtains that can block light fully. Position the bed with a solid wall behind for psychological comfort.",
        'default': "That's an excellent design consideration. Based on your chosen theme and preferences, I'd recommend exploring how texture and material contrast can elevate the space. Would you like specific product recommendations or spatial layout advice?"
    }

    response_text = responses['default']
    for key in responses:
        if key in message:
            response_text = responses[key]
            break

    return jsonify({
        "response": response_text,
        "suggestions": ["Tell me about lighting", "Furniture recommendations", "Budget breakdown", "Color palette advice"]
    })

@app.route('/api/furniture-details', methods=['POST'])
def furniture_details():
    data = request.get_json()
    furniture_id = data.get('furniture_id', 'sofa')

    furniture_db = {
        'sofa': {
            'name': 'Designer Sectional Sofa',
            'description': 'Premium L-shaped sectional with deep-seated cushions and solid wood legs',
            'price': '₹85,000 - ₹2,40,000',
            'amazon_link': 'https://www.amazon.in/s?k=luxury+sectional+sofa',
            'ikea_link': 'https://www.ikea.com/in/en/cat/sofas-fu003/',
            'image_emoji': '🛋️',
            'material': 'Premium Fabric / Leather',
            'dimensions': '280cm × 160cm × 85cm'
        },
        'bed': {
            'name': 'King Platform Bed with Storage',
            'description': 'Upholstered headboard with hydraulic storage and oak frame',
            'price': '₹45,000 - ₹1,80,000',
            'amazon_link': 'https://www.amazon.in/s?k=king+size+luxury+bed',
            'ikea_link': 'https://www.ikea.com/in/en/cat/beds-bm003/',
            'image_emoji': '🛏️',
            'material': 'Solid Oak + Velvet Upholstery',
            'dimensions': '200cm × 180cm × 120cm'
        },
        'tv_unit': {
            'name': 'Floating Media Console',
            'description': 'Wall-mounted TV unit with ambient LED backlight and hidden cable management',
            'price': '₹25,000 - ₹95,000',
            'amazon_link': 'https://www.amazon.in/s?k=wall+mounted+tv+unit',
            'ikea_link': 'https://www.ikea.com/in/en/cat/tv-media-furniture-fu007/',
            'image_emoji': '📺',
            'material': 'High-gloss MDF + Tempered Glass',
            'dimensions': '180cm × 40cm × 45cm'
        },
        'dining': {
            'name': 'Marble Top Dining Table',
            'description': 'Six-seater with Carrara marble top and solid brass legs',
            'price': '₹60,000 - ₹3,50,000',
            'amazon_link': 'https://www.amazon.in/s?k=marble+dining+table+6+seater',
            'ikea_link': 'https://www.ikea.com/in/en/cat/dining-tables-fu004/',
            'image_emoji': '🍽️',
            'material': 'Carrara Marble + Brass',
            'dimensions': '180cm × 90cm × 76cm'
        },
        'plant': {
            'name': 'Large Fiddle Leaf Fig',
            'description': 'Statement indoor tree with designer ceramic pot — purifies air and adds drama',
            'price': '₹2,500 - ₹15,000',
            'amazon_link': 'https://www.amazon.in/s?k=fiddle+leaf+fig+large',
            'ikea_link': 'https://www.ikea.com/in/en/cat/plants-pots-ph001/',
            'image_emoji': '🪴',
            'material': 'Natural Plant + Ceramic Pot',
            'dimensions': '60cm × 60cm × 180cm'
        }
    }

    item = furniture_db.get(furniture_id, furniture_db['sofa'])
    return jsonify(item)

def generate_furniture_list(theme, mood, budget):
    items = [
        {"id": "sofa", "name": "Sectional Sofa", "room": "Living Room", "cost": int(budget * 0.08)},
        {"id": "bed", "name": "Platform Bed", "room": "Bedroom", "cost": int(budget * 0.07)},
        {"id": "tv_unit", "name": "Media Console", "room": "Living Room", "cost": int(budget * 0.04)},
        {"id": "dining", "name": "Dining Table Set", "room": "Kitchen/Dining", "cost": int(budget * 0.06)},
        {"id": "plant", "name": "Statement Plants", "room": "All Rooms", "cost": int(budget * 0.02)},
    ]
    return items

def generate_shopping_links(theme):
    return {
        "amazon": "https://www.amazon.in/s?k=luxury+furniture+" + theme.replace('_', '+'),
        "ikea": "https://www.ikea.com/in/en/",
        "pepperfry": "https://www.pepperfry.com/"
    }

if __name__ == '__main__':
    app.run(debug=True, port=5000)
