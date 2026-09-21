import os
import re
import json
import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="MCQ Generator", page_icon="📝")
st.title("📝 MCQ Generator")

MODEL = "Qwen/Qwen2.5-72B-Instruct"  # any chat model available on HF Inference
client = InferenceClient(model=MODEL, token=os.getenv("HF_TOKEN"))

text = st.text_area("Topic / paste text", height=200)
c1, c2 = st.columns(2)
n = c1.slider("Questions", 1, 20, 5)
level = c2.selectbox("Difficulty", ["Easy", "Medium", "Hard"])

PROMPT = """Generate {n} {level} multiple-choice questions from the content below.
Return ONLY a JSON list, no markdown, no extra text. Each item:
{{"question": str, "options": [4 strings], "answer": index 0-3, "explanation": str}}

Content:
{text}"""

if st.button("Generate") and text.strip():
    with st.spinner("Generating..."):
        try:
            r = client.chat_completion(
                messages=[{"role": "user", "content": PROMPT.format(n=n, level=level, text=text)}],
                max_tokens=3000,
                temperature=0.5,
            )
            raw = r.choices[0].message.content
            st.session_state.mcqs = json.loads(re.search(r"\[.*\]", raw, re.S).group())
        except Exception as e:
            st.error(f"Failed: {e}")

mcqs = st.session_state.get("mcqs")
if mcqs:
    with st.form("quiz"):
        picks = [
            st.radio(f"{i+1}. {q['question']}", q["options"], index=None, key=f"q{i}")
            for i, q in enumerate(mcqs)
        ]
        submitted = st.form_submit_button("Submit")

    if submitted:
        score = 0
        for i, (q, p) in enumerate(zip(mcqs, picks)):
            correct = q["options"][q["answer"]]
            if p == correct:
                score += 1
                st.success(f"Q{i+1}: ✅ {correct}")
            else:
                st.error(f"Q{i+1}: ❌ Correct answer: {correct}")
            st.caption(q["explanation"])
        st.subheader(f"Score: {score}/{len(mcqs)}")
