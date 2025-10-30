from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  # 🆕 Import CORS

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)  # 🆕 Enable CORS

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    soil = data.get("soil")
    location = data.get("location")

    # Simple logic (you can replace this with AI later)
    recommendations = {
        "Alluvial": "Rice, Wheat, Sugarcane, Maize",
        "Black": "Cotton, Soybean, Sunflower, Groundnut",
        "Red": "Millets, Pulses, Oilseeds, Rice",
        "Laterite": "Tea, Coffee, Cashew, Rubber",
        "Arid": "Bajra, Jowar, Pulses, Cactus crops",
        "Saline": "Barley, Sugar Beet, Date Palm, Rice (with treatment)",
        "Mountain": "Apples, Barley, Tea, Spices",
        "Peaty": "Paddy, Jute, Coconut, Vegetables"
    }

    recommendation = recommendations.get(soil, "No data available")
    return jsonify({"recommendation": f"For {soil} soil in {location}, suitable crops are: {recommendation}."})

if __name__ == "__main__":
    app.run(debug=True)
