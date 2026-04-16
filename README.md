# 📄 AI Document Scanner with OCR and Smart Data Extraction

---

## 📌 Overview

This project is an AI-powered document processing system that extracts text from images and converts it into structured data.

It combines:

* OCR (Optical Character Recognition) for text extraction
* LLM (Large Language Model) for intelligent data parsing

The system can process receipts, invoices, and documents to extract key information automatically.

---

## ✨ Features

* 🖼️ Upload document images (receipt, invoice, etc.)
* 🔍 Extract text using OCR (Tesseract)
* 🧠 Convert raw text into structured JSON using LLM
* 📊 Display extracted fields (name, date, amount, items)
* ⚡ Simple and interactive UI (Streamlit)

---

## 🧠 Tech Stack

* **Python**
* **Streamlit**
* **Tesseract OCR**
* **OpenAI API (LLM)**
* **Pillow**

---

## 🏗️ Architecture

```id="a7l2bz"
Image Upload
   ↓
OCR (Tesseract)
   ↓
Raw Text Extraction
   ↓
LLM Processing
   ↓
Structured Data (JSON)
   ↓
Streamlit UI Display
```

---

## 📂 Project Structure

```id="w3d0qn"
ai-document-scanner/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils/
│   ├── ocr.py
│   └── extractor.py
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone Repository

```bash id="5bhqk2"
git clone https://github.com/your-username/ai-document-scanner.git
cd ai-document-scanner
```

---

### 2️⃣ Install Dependencies

```bash id="hw3m0s"
pip install -r requirements.txt
```

---

### 3️⃣ Install Tesseract OCR

#### 🔹 Windows:

Download and install from:
https://github.com/tesseract-ocr/tesseract

#### 🔹 Mac:

```bash id="1y8kzq"
brew install tesseract
```

#### 🔹 Linux:

```bash id="vjqh0p"
sudo apt install tesseract-ocr
```

---

### 4️⃣ Set OpenAI API Key

```bash id="f3h9yn"
export OPENAI_API_KEY=your_api_key
```

(Windows)

```bash id="m9kt4r"
set OPENAI_API_KEY=your_api_key
```

---

### 5️⃣ Run Application

```bash id="2xv8ql"
streamlit run app.py
```

---

## 💡 Example Output

### Extracted JSON:

```json id="p9z4ml"
{
  "name": "ABC Store",
  "date": "12 Jan 2024",
  "amount": "450",
  "items": ["Milk", "Bread"]
}
```

---

## 🎯 Use Cases

* Expense tracking apps
* Invoice processing systems
* Document digitization
* Financial automation

---

## Author

**Joncy Keda - AI Developer**

