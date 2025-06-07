# 📄 AI Resume Screening & Candidate Ranking System

An intelligent web-based system that automatically screens and ranks resumes based on a given job description. Built using **Python**, **NLP**, **machine learning**, and deployed via an interactive **Streamlit interface**, it helps recruiters instantly identify the most relevant candidates.

---

## 🧠 Project Summary

Modern recruitment involves sifting through dozens or hundreds of resumes, often manually. This system uses **TF-IDF vectorization** and **cosine similarity** to automate the resume shortlisting process.

You simply:

* Paste a job description
* Upload one or more resume PDFs
* View ranked resumes by their **match score**

All processing happens **locally** — no resume data is sent to any server.

---

## 🔧 Technologies Used

| Technology    | Purpose                                  |
| ------------- | ---------------------------------------- |
| Python 3.11+  | Core programming language                |
| Streamlit     | Web application interface                |
| PyPDF2        | Resume (PDF) text extraction             |
| scikit-learn  | TF-IDF and cosine similarity computation |
| pandas        | Result display in tables                 |
| VS Code + Git | Local development and version control    |

---
## 🧩 System Design

The system architecture is composed of several key components that work together to automate the resume screening and ranking process.

### Architecture Diagram
![pic](https://github.com/user-attachments/assets/f6a89341-f9f2-4854-a53d-95bc7e1e8153)


### Component Breakdown

#### 🔹 User Input and Frontend

* **Enter Job Description**: A text area to input a job role's description.
* **Upload Resumes**: Upload one or more resume PDFs through the interface.

#### 🔹 Backend Processing

* **Resume Parsing**: Converts uploaded PDF resumes into raw text using `PyPDF2`.
* **Text Extraction**: Cleans and prepares the text for vectorization.

#### 🔹 Feature Engineering

* **TF-IDF Vectorization**: Converts textual data into numeric form using term frequency–inverse document frequency.

#### 🔹 Similarity Computation

* **Cosine Similarity**: Measures the similarity between the job description and each resume vector.

#### 🔹 Ranking and Output Display

* **Store Results**: Combines resume names and similarity scores in a `DataFrame`.
* **Sort Resumes**: Orders candidates based on their match score.
* **Display Ranked Resumes**: Shows the results in a sortable, tabular format on the Streamlit frontend.

---







## 🌐 Live Preview (Streamlit UI)
![Screenshot 2025-05-11 133225](https://github.com/user-attachments/assets/bbb4bb35-69d2-47c9-80c2-d70343a0b078)



Shows:

* Job description input box
* PDF file uploader
* Ranked resume match table

---

## 📁 Folder Structure

```
Resume-Screening-and-Ranking-System/
│
├── app.py                  # Streamlit frontend application
├── resume_ranking.ipynb   # Jupyter notebook for logic testing
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore              # Files/folders to exclude from Git tracking
```

---

## 🛠️ How to Set Up Locally

> Tested on Windows 11 (PowerShell, VS Code)

### ✅ Step 1: Clone the Repository

```powershell
git clone https://github.com/Alpha-Soumen/Resume-Screening-and-Ranking-System.git
cd Resume-Screening-and-Ranking-System
```

### ✅ Step 2: Create Virtual Environment

```powershell
python -m venv venv
.\venv\Scripts\Activate
```

### ✅ Step 3: Install Dependencies

```powershell
pip install -r requirements.txt
```

### ✅ Step 4: Run the Streamlit App

```powershell
streamlit run app.py
```

> App will open in your default browser at [http://localhost:8501](http://localhost:8501)

---

## 🧪 Features

* Upload multiple resumes (PDF)
* Paste any job description
* Rank resumes using cosine similarity
* View results as a sortable table
* Supports unicode-rich resumes (with encoding fix)

---

## 🧠 How It Works (Under the Hood)

1. **Text Extraction**: Each uploaded PDF is parsed using `PyPDF2`, skipping bad characters.
2. **Vectorization**: The job description and resume texts are converted using `TfidfVectorizer`.
3. **Similarity Comparison**: Cosine similarity scores each resume against the job description.
4. **Ranking**: A DataFrame shows resume names and scores in descending order.

---


## 💡 Future Enhancements

* BERT-based semantic similarity for better understanding
* Admin login via Firebase
* Resume keyword visualizations (charts)
* Export matched resumes to PDF or CSV
* Deployment on Streamlit Cloud

---

## 👨‍💻 Developed by

* **Soumen Bhunia**
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/soumen-bhunia/)



