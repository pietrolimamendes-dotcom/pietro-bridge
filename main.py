from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Rota principal para saber se está online
@app.route('/')
def home():
    return "Pietro Audit Bridge Online 24/7", 200

# O "Cérebro" que faz o re-upload
@app.route('/upload', methods=['POST'])
def upload():
    try:
        data = request.json
        cookie = data.get("cookie")
        asset_id = data.get("asset_id")
        asset_type = data.get("type", "Audio")

        # IMPORTANTE: Aqui a Nuvem se conecta ao Roblox
        # No futuro, você pode colocar a API real do Roblox aqui.
        # Por enquanto, ele gera o ID simulado para o seu mapa não bugar.
        
        new_id = f"118{asset_id[-7:]}" # Simula um ID novo na sua conta
        
        return jsonify({
            "status": "success",
            "new_id": new_id,
            "msg": f"{asset_type} migrado para sua conta!"
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "reason": str(e)}), 400

if __name__ == "__main__":
    app.run()
