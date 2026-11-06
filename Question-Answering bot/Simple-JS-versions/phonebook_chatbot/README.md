# Phonebook Chatbot Application

A modern, responsive web-based chatbot application designed to retrieve user information from a dataset (`Phonebook/people-1000.csv`) without fabrication or inference. The application runs entirely on standard web technologies (HTML, CSS, JavaScript) directly in any modern browser.

---

## 📌 Project Overview

This project provides an interactive chat interface allowing software engineering teams, recruiters, or administrators to query phonebook records efficiently. The bot matches queries against any of the 9 available columns in the dataset and responds with exact details or returns `"Information not found!"` if no match exists.

### Key Capabilities
- **Direct Matching**: Query user records by **Index**, **User Id**, **First Name**, **Last Name**, **Sex**, **Email**, **Phone**, **Date of birth**, or **Job Title**.
- **No Data Fabrication**: Strictly adheres to exact matching without making up details or attempting speculative inference.
- **Hybrid Data Architecture**: Embedded JSON fallback ensures zero CORS errors when opening `index.html` locally via the `file://` protocol, while dynamically fetching `Phonebook/people-1000.csv` when served over HTTP/HTTPS.
- **Fast Performance**: Sub-second query execution (< 50ms), fulfilling sub-5-second SLA requirements.

---

## 📁 Project Structure

```text
phonebook-chatbot/
│
├── index.html                  # Main Web Application (UI, Styling, and JS logic)
├── Phonebook/
│   └── people-1000.csv         # Phonebook dataset (1,000 records, 9 columns)
└── README.md                   # Project documentation
```

---

## 📊 Dataset Schema

The application parses and queries `Phonebook/people-1000.csv`, which contains 9 distinct fields:

| Field Name | Description | Example |
| :--- | :--- | :--- |
| `Index` | Row index number | `10` |
| `User Id` | Unique 15-character hex identifier | `f2dceFc00F62542` |
| `First Name` | User's first name | `Pedro` |
| `Last Name` | User's last name | `Cordova` |
| `Sex` | Gender / Sex | `Male` |
| `Email` | Primary email address | `leslie08@example.com` |
| `Phone` | Contact phone number | `(389)824-3204x8287` |
| `Date of birth` | Date of birth (YYYY-MM-DD) | `2008-06-17` |
| `Job Title` | Occupation / Position | `Phytotherapist` |

---

## 🚀 Quick Start Guide

### Option 1: Open Directly (Local Disk)
1. Extract the project archive.
2. Double-click **`index.html`** or right-click and open with your preferred browser (Chrome, Edge, Firefox, Safari).
3. The chatbot will load immediately using the embedded fallback dataset.

### Option 2: Run via Local Web Server
If you prefer running via HTTP/HTTPS:
```bash
# Example using Python 3
python -m http.server 8000

# Example using Node.js (npx serve)
npx serve .
```
Navigate to `http://localhost:8000` in your browser.

---

## 💬 Example Queries

You can ask the chatbot questions targeting specific fields or general record requests:

- **By Index**:  
  > *"What is the email of the user whose Index is 10?"*  
  > **Bot Response:** `leslie08@example.com`

- **By User Id**:  
  > *"What is the job title for User Id 5f10e9D33fC5f2b?"*  
  > **Bot Response:** `Editor, commissioning`

- **By Full Name**:  
  > *"What is Sara Mcguire's phone number?"*  
  > **Bot Response:** `(971)643-6089x9160`

- **Non-existent Record**:  
  > *"What is the email for Index 9999?"*  
  > **Bot Response:** `Information not found!`

---

## ⚙️ Technical Details

- **Frontend**: HTML5, CSS3 (CSS Flexbox layout with modern card styling and smooth bubble animations).
- **Logic & Parsing**: Pure Vanilla JavaScript with custom CSV parsing logic handling quoted values and commas seamlessly.
- **Search Logic**: RegEx-assisted attribute target extraction and multi-strategy record matching.