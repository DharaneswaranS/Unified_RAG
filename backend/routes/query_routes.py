from flask import Blueprint, request, jsonify
from backend.services.retrieval_service import retrieve_context
from backend.services.reasoning_service import generate_answer
query_bp = Blueprint("query", __name__)
@query_bp.route("/query", methods=["POST"])
def query():
    data = request.get_json()
    question = data.get("question")
    if not question:
        return jsonify({"error": "Question missing"}), 400
    context = retrieve_context(question)
    answer = generate_answer(question, context)
    return jsonify({"answer": answer})
