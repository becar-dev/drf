# populate_db.py

import os
import django
import random
from faker import Faker

def setup_django():
    """
    Django muhitini sozlaydi. Skriptni loyiha tashqarisidan ishga tushirish uchun kerak.
    'root.settings' o'rniga o'zingizning settings faylingiz nomini yozing.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')
    django.setup()

def populate():
    """
    Ma'lumotlar bazasini avtomatik to'ldiradi.
    """
    # Faker kutubxonasidan soxta ma'lumotlar yaratish uchun foydalanamiz
    fake = Faker()

    # Modellarni django sozlangandan keyin import qilamiz
    from course.models import Subject, Course, Module, Comment
    from django.contrib.auth.models import User

    print("Eski ma'lumotlar tozalanmoqda...")
    Comment.objects.all().delete()
    Module.objects.all().delete()
    Course.objects.all().delete()
    Subject.objects.all().delete()
    print("Tozalandi.")

    # Test uchun bitta foydalanuvchi yaratamiz
    try:
        user = User.objects.get(username='testuser')
    except User.DoesNotExist:
        user = User.objects.create_user(username='testuser', password='strongpassword123')
        print(f"'{user.username}' nomli test foydalanuvchisi yaratildi.")

    # Qancha ma'lumot yaratishni belgilaymiz
    NUM_SUBJECTS = 10
    NUM_COURSES_PER_SUBJECT = 100  # Jami: 10 * 100 = 1000 ta kurs
    NUM_MODULES_PER_COURSE = 15    # Jami: 1000 * 15 = 15,000 ta modul
    NUM_COMMENTS_PER_COURSE = 20   # Jami: 1000 * 20 = 20,000 ta izoh

    # --- 1. Fanlarni (Subjects) yaratish ---
    print(f"{NUM_SUBJECTS} ta fan yaratilmoqda...")
    subjects = []
    for _ in range(NUM_SUBJECTS):
        subjects.append(Subject(title=fake.catch_phrase(), slug=fake.slug()))
    # bulk_create bir nechta obyektni bitta so'rovda yaratadi (juda samarali)
    Subject.objects.bulk_create(subjects)
    print("Fanlar yaratildi.")

    # --- 2. Kurslarni (Courses) yaratish ---
    print(f"{NUM_COURSES_PER_SUBJECT * NUM_SUBJECTS} ta kurs yaratilmoqda...")
    all_subjects = list(Subject.objects.all())
    courses = []
    for subject in all_subjects:
        for _ in range(NUM_COURSES_PER_SUBJECT):
            # TUZATISH: `user=user` o'rniga `owner=user` ishlatildi (`models.py` ga mos ravishda)
            courses.append(Course(
                subject=subject,
                owner=user,
                title=fake.bs().title(),
                overview=fake.text(max_nb_chars=250),
                is_premium=random.choice([True, False]),
                price=round(random.uniform(10.99, 299.99), 2)
            ))
    Course.objects.bulk_create(courses)
    print("Kurslar yaratildi.")

    # --- 3. Modullarni (Modules) yaratish ---
    print(f"{NUM_MODULES_PER_COURSE * len(courses)} ta modul yaratilmoqda...")
    all_courses = list(Course.objects.all())
    modules = []
    for course in all_courses:
        for i in range(NUM_MODULES_PER_COURSE):
            modules.append(Module(
                course=course,
                title=f"Modul {i + 1}: {fake.sentence(nb_words=5)}"
            ))
    Module.objects.bulk_create(modules, batch_size=1000) # Ko'p ma'lumot uchun batch_size
    print("Modullar yaratildi.")

    # --- 4. Izohlarni (Comments) yaratish ---
    print(f"{NUM_COMMENTS_PER_COURSE * len(courses)} ta izoh yaratilmoqda...")
    comments = []
    for course in all_courses:
        for _ in range(NUM_COMMENTS_PER_COURSE):
            # TUZATISH: `body` o'rniga `content` ishlatildi va `topic` qo'shildi (`models.py` ga mos ravishda)
            comments.append(Comment(
                course=course,
                user=user,
                rating=random.choice(Comment.RatingChoices.values),
                topic=fake.sentence(nb_words=4),
                content=fake.paragraph(nb_sentences=4)
            ))
    Comment.objects.bulk_create(comments, batch_size=1000)
    print("Izohlar yaratildi.")

    print("\n✅ Ma'lumotlar bazasi muvaffaqiyatli to'ldirildi!")

if __name__ == '__main__':
    print("Django muhiti sozlanmoqda...")
    setup_django()
    populate()
