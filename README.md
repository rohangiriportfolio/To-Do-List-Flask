# **To-Do List App**

Modern Flask Web application implementing **CRUD operations** (Create, Read, Update, Delete)

## ✨ **Features**
- 3-section navigation (Home/Add/Show)
- Update and delete functionality
- Responsive design

## 🛠 **Tech Stack**
- **Backend**: Flask + MongoDB
- **Frontend**: HTML/CSS

## 🚀 **Requirements**
```bash
pip install -r requirements.txt
python app.py
```

## 📁 **Structure**
├── app.py
├── templates/
│ ├── index.html
│ └── edit.html
├── static/
│ └── style.css
├── requirements.txt
└── README.md

text

## 📱 **Routes**
| Method | URL | Description |
|--------|-----|-------------|
| GET | `/` | Homepage (Home/Add/Show) |
| POST | `/add` | Add new task |
| POST | `/edit` | Load edit form (hidden task_id) |
| POST | `/update` | Save task changes |
| POST | `/delete` | Delete task |

## 💾 **Database Schema**
```json
{
    "_id": ObjectId,
    "task": "string",
    "deadline": "YYYY-MM-DD",
    "status": "active\|inactive"
}
```
