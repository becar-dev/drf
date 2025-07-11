<div align="center">
<h1 align="center">📘 Django REST API for Educational Platform</h1>
<p align="center">
A high-performance, scalable, and secure RESTful API for managing subjects, courses, and user interactions.
<br />
<a href="#-api-dokumentatsiyasi-swagger"><strong>API Hujjatlarini ko'rish »</strong></a>
·
<a href="https://www.google.com/search?q=https://github.com/your-username/your-repo/issues">Xatolik haqida xabar berish</a>
·
<a href="https://www.google.com/search?q=https://github.com/your-username/your-repo/pulls">Yangi imkoniyat taklif qilish</a>
</p>
</div>

<div align="center">

</div>

<details open>
<summary><h2>Mundarija</h2></summary>
<ol>
<li><a href="#-loyiha-haqida">Loyiha haqida</a></li>
<li><a href="#-texnologiyalar-steki">Texnologiyalar Steki</a></li>
<li><a href="#-arxitektura-va-optimizatsiya">Arxitektura va Optimizatsiya</a></li>
<li><a href="#-api-endpointlar">API Endpointlar</a></li>
<li><a href="#-oʻrnatish-va-ishga-tushirish">Oʻrnatish va Ishga Tushirish</a></li>
<li><a href="#-infografika">Infografika</a></li>
<li><a href="#-muallif">Muallif</a></li>
<li><a href="#-litsenziya">Litsenziya</a></li>
</ol>
</details>

🎯 Loyiha haqida
Ushbu loyiha Fanlar, Kurslar va Izohlar kabi o'quv platformasining asosiy komponentlarini boshqarish uchun mo'ljallangan yuqori unumdorlikka ega RESTful API tizimidir. Tizim kengaytiriluvchanlik (scalability), xavfsizlik va tezkorlikni birinchi o'ringa qo'yadi.

Asosiy yutuqlar:

N+1 muammosi to'liq hal qilingan: Ma'lumotlar bazasiga so'rovlar soni prefetch_related, select_related va annotate orqali minimallashtirilgan.

Pagination: Katta hajmdagi ma'lumotlar to'plamlari sahifalarga bo'lib uzatiladi, bu esa API javob vaqtini keskin qisqartiradi.

Moslashuvchan autentifikatsiya: JWT, Token va Session kabi bir nechta autentifikatsiya usullarini qo'llab-quvvatlaydi.

🛠️ Texnologiyalar Steki
Kategoriya

Texnologiya

Izoh

Backend

Django, Django REST Framework

Asosiy framework va API yaratish uchun kutubxona.

Ma'lumotlar bazasi

PostgreSQL / SQLite3

Ishlab chiqarish (production) uchun PostgreSQL tavsiya etiladi.

Autentifikatsiya

Simple JWT, TokenAuthentication

Xavfsiz va zamonaviy autentifikatsiya mexanizmlari.

API Dokumentatsiya

drf-yasg (Swagger UI)

Interaktiv API hujjatlari va testlash uchun.

Development & Test

Django Debug Toolbar

API ishlashini tahlil qilish va optimallashtirish uchun.

Asinxron vazifalar

Celery, Redis (Ixtiyoriy)

Katta hajmli vazifalarni fonda bajarish uchun.

🏗️ Arxitektura va Optimizatsiya
Loyiha arxitekturasi DRY (Don't Repeat Yourself) va KISS (Keep It Simple, Stupid) tamoyillariga asoslangan.

ViewSet va Routerlar: Kodni tartibli saqlash va standart CRUD operatsiyalarini osonlashtirish uchun viewsets.ModelViewSet va DefaultRouterdan foydalanilgan.

Serialayzerlarni ixtisoslashtirish: List va Detail amallari uchun alohida serialayzerlar (CourseListSerializer, CourseDetailSerializer) ishlatilgan. Bu keraksiz ma'lumotlarni uzatishni oldini oladi.

Maxsus Permissionlar: course/permission.py faylida biznes mantiqqa asoslangan maxsus ruxsatnomalar (IsEvenYear, IsSuperUserOnly) yaratilgan.

🔗 API Endpointlar
Barcha endpointlar /api/ prefiksi bilan boshlanadi.

<details>
<summary><strong>Autentifikatsiya Endpointlari (/api/auth/...)</strong></summary>

Method

URL

Tavsif

POST

auth/register/

Yangi foydalanuvchini ro‘yxatdan o‘tkazish.

POST

auth/login/

Tizimga kirish va token olish.

POST

auth/logout/

Tizimdan chiqish (JWT tokenini qora ro'yxatga kiritish).

POST

auth/token/refresh/

refresh token orqali yangi access token olish.

</details>

<details>
<summary><strong>Asosiy resurslar (/api/...)</strong></summary>

Resurs

URL

Qo'llab-quvvatlanadigan metodlar

Subjects

subjects/

GET, POST, PUT, PATCH, DELETE

Courses

courses/

GET, POST, PUT, PATCH, DELETE

Modules

modules/

GET, POST, PUT, PATCH, DELETE

Comments

comments/

GET, POST, PUT, PATCH, DELETE

</details>

🚀 Oʻrnatish va Ishga Tushirish
Loyiha bilan ishlashni boshlash uchun quyidagi qadamlarni bajaring.

1. Talablar
Python 3.8+

PostgreSQL (tavsiya etiladi) yoki SQLite3

Git

2. O'rnatish
# 1. Repozitoriyni klonlash
git clone [https://github.com/your-username/your-repo.git](https://github.com/your-username/your-repo.git)
cd your-repo

# 2. Virtual muhit yaratish va faollashtirish
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows

# 3. Kerakli kutubxonalarni o'rnatish
pip install -r requirements.txt

# 4. .env faylini sozlash (agar mavjud bo'lsa)
# .env.example faylidan nusxa oling va kerakli o'zgaruvchilarni kiriting

# 5. Ma'lumotlar bazasi migratsiyalarini qo'llash
python manage.py migrate

# 6. Superuser yaratish
python manage.py createsuperuser

3. Ishga tushirish
# Development serverni ishga tushirish
python manage.py runserver

Endi loyiha http://127.0.0.1:8000/ manzilida ishlaydi.

4. API Dokumentatsiyasi (Swagger)
API bilan tanishish va uni test qilish uchun quyidagi manzilga o'ting:

Swagger UI: http://127.0.0.1:8000/swagger/

📊 Infografika
<div align="center">
<h2>
<a href="link-to-your-infographic.html">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/SOON...-Click%2520to%2520view%2520interactive%2520infographic-blue%3Fstyle%3Dfor-the-badge%26logo%3Ddata:image/svg%2Bxml%3Bbase64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyQzYuNDg2IDIgMiA2LjQ4NiAyIDEyczQuNDg2IDEwIDEwIDEwIDEwLTQuNDg2IDEwLTEwUzE3LjUxNCAyIDEyIDJ6bTAgMThjLTQuNDEgMC04LTMuNTktOC04czMuNTktOCA4IDggOCAzLjU5IDggOC0zLjU5IDgtOCA4eiIvPjxwYXRoIGQ9Ik0xMSAxNmgydjJoLTJ6bTAtOGgydjZoLTJ6Ii8%2BPC9zdmc+" alt="SOON..."/>
</a>
</h2>
<p>Loyiha arxitekturasi, optimizatsiya yutuqlari va asosiy ko'rsatkichlarni namoyish etuvchi interaktiv infografika tez orada tayyor bo'ladi.</p>
</div>

👨‍💻 Muallif
Beka_dev

GitHub: @your-username

Telegram: @your-telegram

📝 Litsenziya
Ushbu loyiha MIT litsenziyasi ostida tarqatiladi. Batafsil ma'lumot uchun LICENSE fayliga qarang.