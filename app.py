from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="AIzaSyBCKUS1KoCWpQGkjkCMQ-8k668y4uvJObk")

MODEL_NAME = "models/gemini-2.0-flash-lite"

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    user_input = ""
    selected_mode = "explain"

    if request.method == "POST":
        user_input = request.form["question"]
        selected_mode = request.form["mode"]

        if selected_mode == "explain":
            prompt = f"Explain this clearly for a student in simple words:\n{user_input}"
        elif selected_mode == "summarize":
            prompt = f"Summarize this in short bullet points:\n{user_input}"
        else:
            prompt = f"Create 5 quiz questions with answers based on this topic:\n{user_input}"

        try:
            model = genai.GenerativeModel(MODEL_NAME)
            response = model.generate_content(prompt)
            response_text = response.text
        except Exception:
            if selected_mode == "explain":
                response_text = f"[Demo Mode] Simple explanation for: {user_input}"
            elif selected_mode == "summarize":
                response_text = f"[Demo Mode]\n- Main idea of {user_input}\n- Key points\n- Quick revision summary"
            else:
                response_text = (
                    f"[Demo Mode]\n"
                    f"1. What is {user_input}?\nAnswer: Basic definition.\n\n"
                    f"2. Why is {user_input} important?\nAnswer: It helps in understanding the topic.\n\n"
                    f"3. Give one example of {user_input}.\nAnswer: Example-based response.\n\n"
                    f"4. What are the main features of {user_input}?\nAnswer: Key features here.\n\n"
                    f"5. Where is {user_input} used?\nAnswer: Common applications here."
                )

    return render_template(
        "index.html",
        response=response_text,
        question=user_input,
        mode=selected_mode
    )

if __name__ == "__main__":
    app.run(debug=True)