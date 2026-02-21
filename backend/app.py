from flask import Flask
from backend.routes.upload_routes import upload_bp
from backend.routes.query_routes import query_bp
app = Flask(__name__)
app.register_blueprint(upload_bp)
app.register_blueprint(query_bp)
if __name__ == "__main__":
    app.run(debug=False, port=5000,use_reloader=False)
