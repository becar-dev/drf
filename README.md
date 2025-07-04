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

## 🛡️ Permission Tizimi (Yangi)

### 🔐 CompositePermission orqali xavfsizlik

Quyidagi qat’iy ruxsatlar joriy etildi:

| Nomi | Tavsif |
|------|--------|
| `IsEvenYear` | Faqat **juft yillarda** (2024, 2026, ...) ruxsat |
| `IsSuperUserOnly` | Faqat `is_superuser=True` foydalanuvchilarga ruxsat |
| `OnlyPutPatchAllowed` | Faqat `PUT` va `PATCH` methodlariga ruxsat |
| `AdminPremiumCourseAccess` | Premium kurslarga faqat `admin` kirishi mumkin |

Ushbu permissionlar `utils/permission.py` ichida `CompositePermission` sinfi orqali **markazlashtirilgan** va ixcham holatda boshqariladi.

---

## 📊 Qo‘shimcha imkoniyatlar

- Har bir `Course` obyektida `average_rating` (o‘rtacha baho) maydoni mavjud.
- `Course` ro‘yxati avtomatik `average_rating` bo‘yicha kamayish tartibida chiqadi.
- Har bir `Subject` uchun `course_count` (kurslar soni) va kurslar ro‘yxati mavjud.
- **Premium kurslar** faqat `admin` foydalanuvchilarga ko‘rinadi (filter darajasida cheklangan).
- Permission xatolari foydalanuvchiga **aniq va tushunarli message** bilan qaytadi.
- Har bir permission mustaqil modulda joylashgan (`course/permission.py`), servis qatlamdan mustaqil.

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

### 2️⃣ Kutubxonalarni o‘rnatish

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

> API-ni tekshirish uchun:  
👉 `http://127.0.0.1:8000/api/`

---

## 📦 Namuna ma'lumotlar

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

## 🔍 Test qilish

Postman, Insomnia yoki browser orqali quyidagi URL orqali test qilishingiz mumkin:  
👉 `http://127.0.0.1:8000/api/`

---

## 👨‍💻 Muallif

**Beka_dev** — Django & DRF asosidagi REST API loyihasi.

---

## 📝 Litsenziya

Ushbu loyiha faqat o‘quv va ichki test maqsadlarida foydalanish uchun mo‘ljallangan.