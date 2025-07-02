
# 📘 Django REST API for Subjects, Courses & Comments

Bu loyiha **Django** va **Django REST Framework** asosida yaratilgan bo‘lib, quyidagi modellarni boshqarish imkonini beradi:

- `Subject` (Fanlar)
- `Course` (Kurslar)
- `Comment` (Izohlar / Reytinglar)

---

## 🚀 API Imkoniyatlari

### 📚 Subject API

| Method | URL | Tavsif |
|--------|-----|--------|
| `GET` | `/api/subjects/` | Barcha subjectlarni ro'yxatini ko'rsatadi (`course_count` va kurslar bilan) |
| `GET` | `/api/subjects/<id>/` | Bitta subject tafsilotlarini ko'rsatadi |
| `POST` | `/api/subjects/` | Yangi subject yaratadi |
| `PUT` / `PATCH` | `/api/subjects/<id>/` | Subjectni o'zgartiradi |
| `DELETE` | `/api/subjects/<id>/` | Subjectni o'chiradi |

---

### 🎓 Course API

| Method | URL | Tavsif |
|--------|-----|--------|
| `GET` | `/api/courses/` | Barcha kurslarni `average_rating` bo‘yicha kamayish tartibida ko'rsatadi |
| `GET` | `/api/courses/<id>/` | Bitta kurs tafsilotlarini ko'rsatadi |
| `POST` | `/api/courses/` | Yangi kurs yaratadi |
| `PUT` / `PATCH` | `/api/courses/<id>/` | Kursni o'zgartiradi |
| `DELETE` | `/api/courses/<id>/` | Kursni o'chiradi |

---

### 💬 Comment API

| Method | URL | Tavsif |
|--------|-----|--------|
| `GET` | `/api/comments/` | Barcha izohlarni ko'rsatadi |
| `POST` | `/api/comments/` | Kursga yangi izoh va reyting qo'shadi |
| `GET` | `/api/comments/<id>/` | Izoh tafsilotlarini ko'rsatadi |
| `PUT` / `PATCH` | `/api/comments/<id>/` | Izohni o'zgartiradi |
| `DELETE` | `/api/comments/<id>/` | Izohni o'chiradi |

---

## 📊 Qo‘shimcha imkoniyatlar

- Har bir `Course` obyektida `average_rating` (o‘rtacha baho) maydoni mavjud.
- `Course` ro‘yxati avtomatik `average_rating` bo‘yicha kamayish tartibida chiqadi.
- Har bir `Subject` uchun `course_count` (kurslar soni) va kurslar ro‘yxati mavjud.

---

## ⚙️ Ishga tushirish

### 1️⃣ Virtual environment yaratish

```bash
python -m venv venv
```

> Aktivlashtirish:

- **Linux / Mac:**

  ```bash
  source venv/bin/activate
  ```

- **Windows:**

  ```bash
  venv\Scripts\activate
  ```

---

### 2️⃣ Kerakli kutubxonalarni o‘rnatish

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Ma'lumotlar bazasini tayyorlash

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 4️⃣ Superuser yaratish (ixtiyoriy)

```bash
python manage.py createsuperuser
```

---

### 5️⃣ Serverni ishga tushirish

```bash
python manage.py runserver
```

> Endi siz `http://127.0.0.1:8000/api/` orqali API ni test qilishingiz mumkin.

---

## 📦 Namuna ma'lumotlar

### ➕ Yangi Subject yaratish

```json
{
  "title": "Backend Development"
}
```

---

### ➕ Yangi Course yaratish

```json
{
  "title": "Django Rest Framework",
  "overview": "Learn DRF",
  "duration": "12:00:00",
  "price": "99.99",
  "subject_id": 1
}
```

---

### ➕ Yangi Comment yaratish

```json
{
  "topic": "Zo'r kurs!",
  "content": "Men ko'p narsani o'rgandim.",
  "rating": 5,
  "course": 1,
  "user": 2
}
```

---

## 🔍 Test qilish

Postman, Insomnia yoki brauzer orqali quyidagi URL orqali test qilishingiz mumkin:

👉 `http://127.0.0.1:8000/api/`

---

## 👨‍💻 Beka_cr

Loyiha `Django` + `DRF` asosida o‘rgatish va test qilish maqsadida yaratilgan.
