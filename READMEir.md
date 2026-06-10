برنامه یادداشت‌ها (Notes App)

یک برنامه ساده مدیریت یادداشت که با Django و با رعایت اصول معماری ماژولار و قابل توسعه ساخته شده است.

امکانات

- ایجاد یادداشت
- نمایش لیست یادداشت‌ها
- ویرایش یادداشت‌ها (در حال توسعه)
- حذف یادداشت‌ها (در حال توسعه)

تکنولوژی‌های استفاده شده

- Python
- Django
- SQLite
- Class-Based Views (CBV)
- Django Forms

ساختار پروژه

notes_app/
├── config/
├── notes/
├── manage.py
├── requirements.txt
└── README.md

راه‌اندازی پروژه

کلون کردن مخزن

git clone <repository-url>
cd notes_app

ساخت و فعال‌سازی محیط مجازی

python -m venv venv

ویندوز:

venv\Scripts\activate

لینوکس / مک:

source venv/bin/activate

نصب وابستگی‌ها

pip install -r requirements.txt

اعمال مایگریشن‌ها

python manage.py migrate

اجرای سرور توسعه

python manage.py runserver

سپس مرورگر را باز کرده و به آدرس زیر بروید:

http://127.0.0.1:8000/notes/

وضعیت فعلی پروژه

- [x] راه‌اندازی اولیه پروژه Django
- [x] ساخت اپلیکیشن Notes
- [x] ساخت مدل Note
- [x] ایجاد و اعمال Migrationها
- [x] پیاده‌سازی List View
- [x] پیاده‌سازی فرم ایجاد یادداشت
- [ ] ویرایش یادداشت
- [ ] حذف یادداشت
- [ ] احراز هویت کاربران
- [ ] استقرار (Deployment)

اهداف آموزشی

این پروژه با هدف تمرین و یادگیری موارد زیر توسعه داده می‌شود:

- معماری Django
- ORM
- Class-Based Views
- فرم‌ها و اعتبارسنجی
- عملیات CRUD
- ساختاردهی صحیح پروژه

مجوز

این پروژه صرفاً با اهداف آموزشی توسعه داده شده است.