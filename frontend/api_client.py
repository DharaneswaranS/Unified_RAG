import requests
BASE_URL = "http://127.0.0.1:5000"
def upload_file(file):
    try:
        files = {"file": (file.name, file.getvalue())}
        res = requests.post(f"{BASE_URL}/upload", files=files)

        if res.status_code == 200:
            return f"{file.name} uploaded successfully"
        else:
            return f"Upload failed: {res.text}"
    except Exception as e:
        return f"Connection error: {e}"
def ask_question(question):
    try:
        res = requests.post(
            f"{BASE_URL}/query",
            json={"question": question}
        )

        if res.status_code == 200:
            return res.json()["answer"]
        else:
            return f"Error: {res.text}"
    except Exception as e:
        return f"Backend not running: {e}"
