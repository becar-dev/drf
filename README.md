# 📘 Django REST API for Subjects, Courses & Comments

Ushbu loyiha **Django** va **Django REST Framework** asosida yaratilgan bo‘lib, `Fanlar`, `Kurslar` va `Izohlar` bilan ishlovchi mustahkam RESTful API tizimini o‘z ichiga oladi.

---

## 🛠️ Texnologiyalar Steki

- **Backend:** Django, Django REST Framework
- **Ma'lumotlar bazasi:** PostgreSQL (yoki SQLite3)
- **Autentifikatsiya:** Simple JWT (JSON Web Tokens), TokenAuthentication
- **API Dokumentatsiya:** drf-yasg (Swagger)
- **Kod formati:** Black, isort

---

## 🚀 API Imkoniyatlari

### 📚 Subject API

| Method | URL | Tavsif |
|--------|-----|--------|
| `GET` | `/api/subjects/` | Barcha fanlar ro‘yxati (`course_count` va kurslar bilan) |
| `GET` | `/api/subjects/<id>/` | Bitta fanga oid ma’lumot |
| `POST` | `/api/subjects/` | Yangi fan yaratish |
| `PUT` / `PATCH` | `/api/subjects/<id>/` | Fan ma’lumotini o‘zgartirish |
| `DELETE` | `/api/subjects/<id>/` | Fan ma’lumotini o‘chirish |

---

### 🎓 Course API

| Method | URL | Tavsif |
|--------|-----|--------|
| `GET` | `/api/courses/` | Kurslar ro‘yxati `average_rating` bo‘yicha kamayish tartibida |
| `GET` | `/api/courses/<id>/` | Bitta kurs tafsilotlari |
| `POST` | `/api/courses/` | Yangi kurs yaratish |
| `PUT` / `PATCH` | `/api/courses/<id>/` | Kursni yangilash |
| `DELETE` | `/api/courses/<id>/` | Kursni o‘chirish |

---

### 💬 Comment API

| Method | URL | Tavsif |
|--------|-----|--------|
| `GET` | `/api/comments/` | Barcha izohlar ro‘yxati |
| `POST` | `/api/comments/` | Yangi izoh va reyting qo‘shish |
| `GET` | `/api/comments/<id>/` | Izoh tafsilotlari |
| `PUT` / `PATCH` | `/api/comments/<id>/` | Izohni o‘zgartirish |
| `DELETE` | `/api/comments/<id>/` | Izohni o‘chirish |

---

## 🔐 Autentifikatsiya

API bir nechta autentifikatsiya usulini qo'llab-quvvatlaydi. 
So'rov yuborayotganda,`Authorization` sarlavhasini to'g'ri formatda yuborish kerak.


| Usul | Sarlavha Formati | Izoh |
| :--- | :--- | :--- |
| **JWT** | `Authorization: Bearer <access_token>` | Eng tavsiya etilgan usul. |
| **Token** | `Authorization: Token <token>` | Oddiy servislar uchun. |
| **Basic** | `Authorization: Basic <base64_encoded>` | Faqat test uchun. |

### 🧾 Endpointlar

| Method | URL | Tavsif | `auth_type` parametri |
| :--- | :--- | :--- | :--- |
| `POST` | `/api/register/` | Yangi foydalanuvchi ro‘yxatdan o‘tadi | `jwt`, `token`, `session` |
| `POST` | `/api/login/` | Tizimga kirish | `jwt`, `token`, `session` |
| `POST` | `/api/logout/` | Tizimdan chiqish | `jwt`, `token`, `session` |
| `POST` | `/api/token/refresh/` | `refresh` token orqali yangi `access` token olish | - |

**Token yuborish formati:**

```
Authorization: Token <sizning_token>
```

---

## 🧠 Permission Tizimi (Custom)

| Permission nomi | Tavsif |
|-----------------|--------|
| `IsEvenYear` | Faqat **juft yillarda** (2024, 2026, ...) ruxsat |
| `IsSuperUserOnly` | Faqat `superuser` lar uchun ruxsat |
| `OnlyPutPatchAllowed` | Faqat `PUT` va `PATCH` methodlari ruxsat etiladi |
| `AdminPremiumCourseAccess` | `is_premium=True` kurslar faqat `admin` foydalanuvchilarga ko‘rinadi |

---

## 📊 Qo‘shimcha Imkoniyatlar

- Har bir `Course` obyektida `average_rating` maydoni mavjud
- `Course` ro‘yxati reyting bo‘yicha tartiblangan
- Har bir `Subject`:
  - `courses` ro‘yxatini
  - `course_count` qiymatini oladi
- Premium kurslar oddiy foydalanuvchilardan yashirilgan
- Har bir permission aniq xatolik xabari bilan qaytadi
- Barcha permissionlar `course/permission.py` faylida modullar orqali boshqariladi

---

## 📘 Swagger API Dokumentatsiyasi

**URL:** [`/swagger/`](http://127.0.0.1:8000/swagger/)

- Swagger orqali to‘g‘ridan-to‘g‘ri API test qilish mumkin
- `Token` yoki `Bearer` orqali `Authorize` qilish qo‘llab-quvvatlanadi

---

## ⚙️ O‘rnatish

### 1️⃣ Virtual environment yaratish

```bash
python -m venv venv
```

> Faollashtirish:

- **Windows:** `venv\Scripts\activate`
- **Linux/macOS:** `source venv/bin/activate`

### 2️⃣ Kutubxonalarni o‘rnatish

```bash
pip install -r requirements.txt
```

### 3️⃣ Ma’lumotlar bazasini sozlash

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4️⃣ Superuser yaratish (admin panel uchun)

```bash
python manage.py createsuperuser
```

### 5️⃣ Serverni ishga tushirish

```bash
python manage.py runserver
```

👉 [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

---

## 🧪 Test Ma'lumotlari

### ➕ Yangi Subject

```json
{
  "title": "Backend Development"
}
```

### ➕ Yangi Course

```json
{
  "title": "Django Rest Framework",
  "overview": "Learn DRF",
  "duration": "12:00:00",
  "price": "99.99",
  "subject_id": 1
}
```

### ➕ Yangi Comment

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

## 👨‍💻 Muallif

**Beka_dev**  

---

## 📝 Litsenziya

Ushbu loyiha faqat o‘quv va ichki test maqsadlarida foydalanish uchun mo‘ljallangan. Tijorat maqsadlarida foydalanish uchun muallif ruxsati talab qilinadi.