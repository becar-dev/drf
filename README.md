# Django REST API for Subjects & Courses

Bu loyiha Django + Django REST Framework asosida qilingan.  
U Subject va Course modellarini to'liq CRUD API orqali boshqarish imkonini beradi.

---

## 🚀 **API imkoniyatlari**

### Subject API

| Method | URL | Description |
|---------|-----------------------------|-------------------------|
| GET | `/api/subjects/` | Barcha subjectlarni ro'yxatini ko'rsatadi (course_count va kurslar ro'yxati bilan) |
| GET | `/api/subjects/<id>/` | Bitta subject tafsilotlarini ko'rsatadi |
| POST | `/api/subjects/create/` | Yangi subject yaratadi |
| PUT / PATCH | `/api/subjects/<id>/update/` | Subjectni o'zgartiradi |
| DELETE | `/api/subjects/<id>/delete/` | Subjectni o'chiradi |

---

### Course API

| Method | URL | Description |
|---------|-----------------------------|-------------------------|
| GET | `/api/courses/` | Barcha kurslarni ro'yxatini ko'rsatadi |
| GET | `/api/courses/<id>/` | Bitta kurs tafsilotlarini ko'rsatadi |
| POST | `/api/courses/create/` | Yangi kurs yaratadi |
| PUT / PATCH | `/api/courses/<id>/update/` | Kursni o'zgartiradi |
| DELETE | `/api/courses/<id>/delete/` | Kursni o'chiradi |

---

## ⚙ **Ishga tushirish**

1️⃣ Virtual environment yarating:
```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

 Superuser yarating (agar admin kerak bo'lsa):
python manage.py createsuperuser


python manage.py runserver


Yangi Subject
{
  "title": "Backend Development"
}


Yangi Course
{
  "title": "Django Rest Framework",
  "overview": "Learn DRF",
  "duration": "12:00:00",
  "price": "99.99",
  "subject_id": 1
}

API test qilish
Siz Postman yoki brauzer orqali http://127.0.0.1:8000/api/ dan foydalanishingiz mumkin.



