from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("API_KEY")
HEADERS = {
    "x-apisports-key": API_KEY
}
BASE_URL = "https://v3.football.api-sports.io"

# عرض الفرق حسب الليجا
@app.route("/league-teams")
def league_teams():
    league = request.args.get("league")
    season = request.args.get("season", "2023")
    if not league:
        return jsonify({"error": "League ID is required"}), 400
    url = f"{BASE_URL}/teams?league={league}&season={season}"
    response = requests.get(url, headers=HEADERS)
    return jsonify(response.json())

# عرض المباريات حسب الليجا
@app.route("/league-matches")
def league_matches():
    league = request.args.get("league")
    season = request.args.get("season", "2023")
    date_filter = request.args.get("date")  # اختياري، YYYY-MM-DD
    if not league:
        return jsonify({"error": "League ID is required"}), 400
    
    url = f"{BASE_URL}/fixtures?league={league}&season={season}"
    if date_filter:
        url += f"&date={date_filter}"
    response = requests.get(url, headers=HEADERS)
    return jsonify(response.json())

# عرض معلومات عن الليجا
@app.route("/league-info")
def league_info():
    league = request.args.get("league")
    if not league:
        return jsonify({"error": "League ID is required"}), 400
    url = f"{BASE_URL}/leagues?id={league}"
    response = requests.get(url, headers=HEADERS)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True, port=7000)
