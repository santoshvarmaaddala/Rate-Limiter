from flask import Flask, request, jsonify
from limiter.factory import LimiterFactory

app = Flask(__name__)

rateLimiter = LimiterFactory.create_limiter()

@app.route('/')
def home():
    return "✅ Rate Limiter is Running 🚀"

@app.route('/check', methods=["GET"])
def check_rate_limit():
    user_id = request.args.get("user_id")

    if not user_id:
        return jsonify({"error" : "Missing user_id parameter"}), 400
    
    allowed = rateLimiter.allow_request(user_id)

    if allowed:
        return jsonify({
            "user_id": user_id,
            "allowed": True,
            "message": "✅ request allowed"
        }), 200
    else:
        return jsonify({
            "user_id": user_id,
            "allowed": False,
            "message": "❌ Rate limit exceeded"
        }), 429



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
