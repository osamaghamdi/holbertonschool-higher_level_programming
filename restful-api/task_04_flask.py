from flask import Flask, jsonify, request


app = Flask(__name__)

users = {}

@app.route("/")
def home():
    """Root endpoint returns a welcome message."""
    return "Welcome to the Flask API!"

@app.route("/status")
def status():
    """Health check endpoint."""
    return "OK"

@app.route("/data")
def get_usernames():
    """Return list of all usernames."""
    return jsonify(list(users.keys()))

@app.route("/users/<username>")
def get_user(username):
    """Return full data of the given user, or error if not found."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user via POST request."""
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return (
        jsonify({
            "message": "User added",
            "user": users[username]
        }),
        201
    )

if __name__ == "__main__":
    app.run()
