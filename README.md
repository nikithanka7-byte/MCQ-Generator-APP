# MCQ Generator APP

## Project Overview

**MCQ Generator APP** is a Streamlit-based web application that uses Artificial Intelligence to automatically generate Multiple Choice Questions (MCQs) from a given topic or text.

The application allows users to select the **number of questions** and **difficulty level**. It generates questions with four answer options, correct answers, and explanations.

The generated questions can be answered interactively, and the application automatically calculates the final score.

---

## Features

- Generate MCQs from a topic or pasted text
- Select the number of questions from **1 to 20**
- Select difficulty level:
  - Easy
  - Medium
  - Hard
- Generate four options for each question
- Automatic answer evaluation
- Display correct answers
- Provide explanations for questions
- Automatic score calculation
- Interactive quiz interface
- AI-powered question generation
- Structured JSON-based MCQ generation

---

## AI Model

The application uses the following AI model:

**Qwen/Qwen2.5-72B-Instruct**

The model is accessed using the **Hugging Face Inference API**.

The model generates structured multiple-choice questions based on the topic or text provided by the user.

---

## Technologies Used

- **Python**
- **Streamlit**
- **Hugging Face Hub**
- **Qwen2.5-72B-Instruct**
- **JSON**
- **Regular Expressions**

---

## Project Structure

```text
MCQ-Generator/
│
├── app.py
├── requirements.txt
└── README.md
```

### File Description

| File | Description |
|------|-------------|
| `app.py` | Main Streamlit application |
| `requirements.txt` | Required Python dependencies |
| `README.md` | Project documentation |

---

## Requirements

The project requires the following Python libraries:

```text
streamlit
huggingface_hub
```

The complete dependencies are available in the `requirements.txt` file.

---

## Installation

### 1. Clone the Repository

```bash
https://github.com/nikithanka7-byte/MCQ-Generator-APP
```

### 2. Open the Project Folder

```bash
cd MCQ-Generator
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell execution policy prevents activation, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate the virtual environment again:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Hugging Face Token

The application requires a **Hugging Face Access Token** to access the AI model through the Hugging Face Inference API.

Set the token as an environment variable.

### Windows PowerShell

```powershell
$env:HF_TOKEN="your_huggingface_token"
```

Replace:

```text
your_huggingface_token
```

with your actual Hugging Face token.

**Important:** Do not upload your Hugging Face token to GitHub.

For better security, use environment variables or a secrets management method instead of writing the token directly inside `app.py`.

---

## Run the Application

After installing the required dependencies, run:

```bash
streamlit run app.py
```

The Streamlit application will start and open in the browser.

---

## How to Use

### Step 1: Enter Content

Enter a topic or paste text into the input field.

### Step 2: Select Number of Questions

Choose the required number of questions.

The application supports:

```text
1 to 20 questions
```

### Step 3: Select Difficulty

Choose one of the following difficulty levels:

```text
Easy
Medium
Hard
```

### Step 4: Generate Questions

Click the **Generate** button.

The AI model generates MCQs based on the provided topic or text.

### Step 5: Answer Questions

Select one answer for each generated question.

### Step 6: Submit the Quiz

Click the **Submit** button.

The application evaluates the selected answers automatically.

### Step 7: View Results

The application displays:

- Score
- Correct answers
- Explanations
- Quiz results

---

## MCQ Output

Each generated question contains:

```text
Question

Option A
Option B
Option C
Option D

Correct Answer

Explanation
```

The questions are generated using the AI model and processed as structured JSON data.

---

## Example - Application Preview

[streamlit-app-2026-09-21-12-15-19.webm](https://github.com/user-attachments/assets/0d5a89fa-e20c-454b-bdf3-b2a861e75f82)
<img width="1366" height="768" alt="Screenshot (12)" src="https://github.com/user-attachments/assets/46acb6f2-e9c8-4c66-a080-db222e0c1fcc" />
<img width="1366" height="768" alt="Screenshot (13)" src="https://github.com/user-attachments/assets/1b290bf8-20d8-4aeb-bdc4-5ff674d192a2" />
<img width="1366" height="768" alt="Screenshot (14)" src="https://github.com/user-attachments/assets/f6ba04dd-dfeb-40e7-9c65-5ffee035d0aa" />
<img width="1366" height="768" alt="Screenshot (15)" src="https://github.com/user-attachments/assets/6c37becd-ee4a-45ad-89fa-39f9f13e1051" />





```text





```

---

## Score Calculation

After submitting the quiz, the application compares the user's selected answers with the correct answers.

The score is calculated based on the number of correct answers.

### Example

```text
Total Questions: 10
Correct Answers: 8

Score: 8/10
```

---

## Learning Outcomes

Through this project, we learn:

- How to build an AI application using **Streamlit**
- How to use the **Hugging Face Inference API**
- How to work with an **instruction-tuned language model**
- How to integrate an AI model into a Python application
- How to generate structured **JSON output**
- How to create an interactive quiz application
- How to process AI-generated content
- How to calculate quiz scores using Python
- How to create a user-friendly web interface

---

## Future Enhancements

The project can be further improved by adding:

- Different question types
- Timer functionality
- Downloadable quiz results
- User login system
- Previous quiz score history
- Support for additional AI models
- PDF input
- Document input
- Image-based question generation
- Database integration
- Leaderboard functionality

---

## Applications

The AI MCQ Generator can be useful for:

- Student self-assessment
- Online learning
- Educational platforms
- Practice tests
- Exam preparation
- Classroom activities
- AI-based education systems

---

## Conclusion

The **AI MCQ Generator** demonstrates how Generative AI can be integrated with a **Streamlit application** to automatically create interactive multiple-choice quizzes.

By combining **Python, Streamlit, Hugging Face Inference API, and Qwen2.5-72B-Instruct**, the application provides an easy way to generate questions, answer quizzes, evaluate responses, and calculate scores automatically.

This project also provides practical experience in **Generative AI, API integration, structured JSON generation, and Streamlit application development**.
