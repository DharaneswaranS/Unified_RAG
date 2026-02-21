from flask import Blueprint, request, jsonify
import os
from backend.services.ingestion_service import ingest_file
from backend.config import UPLOAD_FOLDER
upload_bp = Blueprint("upload", __name__)
@upload_bp.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)
    result = ingest_file(path)
    return jsonify({"message": result})
