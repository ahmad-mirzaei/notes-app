برنامه یادداشت‌برداری با جنگو

یک برنامه یادداشت‌ برداری ساده، تمیز و قابل توسعه که با استفاده از Django و Class-Based Views (CBVs) و بر اساس شیوه‌های استاندارد توسعه در جنگو پیاده‌ سازی شده است.


---

✨ امکانات

- ایجاد یادداشت جدید
- نمایش لیست یادداشت‌ ها
- مشاهده جزئیات هر یادداشت
- ویرایش یادداشت‌ ها
- حذف یادداشت همراه با صفحه تأیید
- جستجو در یادداشت‌ها بر اساس عنوان
- ثبت خودکار زمان ایجاد و آخرین ویرایش
- اعتبار سنجی فرم‌ها با استفاده از ModelForm
- محافظت از فرم‌ها با CSRF
- استفاده از Class-Based Views برای پیاده‌ سازی CRUD

---

🛠️ فناوری‌ های استفاده شده

- Python 3
- Django
- SQLite
- HTML5
- Django Template Language (DTL)

---

📂 ساختار پروژه

notes-app/
├── config/
├── notes/
│   ├── migrations/
│   ├── templates/
│   │   └── notes/
│   ├── templatetags/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
└── README.md

---

📌 قابلیت‌ های پیاده‌ سازی شده

عملیات CRUD

- ✅ ایجاد یادداشت (Create)
- ✅ نمایش لیست یادداشت‌ ها (List)
- ✅ مشاهده جزئیات یادداشت (Detail)
- ✅ ویرایش یادداشت (Update)
- ✅ حذف یادداشت (Delete)

جستجو

امکان جستجوی یادداشت‌ ها بر اساس عنوان با استفاده از Django ORM.

فرم‌ها

- استفاده از ModelForm
- ویجت‌های سفارشی
- Placeholder برای فیلدها
- اعتبارسنجی سمت سرور

امنیت

- محافظت در برابر حملات CSRF
- صفحه تأیید حذف برای جلوگیری از حذف ناخواسته
- اعتبارسنجی داخلی فرم‌های Django

---

🚀 راه‌اندازی پروژه

دریافت پروژه

git clone https://github.com/<your-username>/notes-app.git

ساخت محیط مجازی

python -m venv .venv

فعال‌ سازی محیط مجازی

ویندوز

.venv\Scripts\activate

لینوکس / مک

source .venv/bin/activate

نصب وابستگی‌ ها

pip install -r requirements.txt

اعمال Migrationها

python manage.py migrate

اجرای سرور توسعه

python manage.py runserver

---

🎯 اهداف آموزشی پروژه

این پروژه با هدف تمرین و یادگیری مفاهیم زیر توسعه داده شده است:

- مدل‌ها (Models)
- ORM جنگو
- Class-Based Views
- ModelForm
- مدیریت مسیرها (URL Routing)
- قالب‌های جنگو (Templates)
- عملیات CRUD
- پیاده‌ سازی جستجو
- کار با Git و GitHub

---

🔮 برنامه‌ های توسعه آینده

- سیستم احراز هویت کاربران
- رابط کاربری با Bootstrap
- صفحه‌ بندی (Pagination)
- دسته ‌بندی و برچسب‌ گذاری یادداشت‌ ها
- ویرایشگر متن پیشرفته
- توسعه REST API با Django REST Framework
- Docker
- تست‌ های خودکار
- استقرار (Deployment)

---

📄 مجوز

این پروژه با هدف آموزش و یادگیری توسعه داده شده است و استفاده آموزشی از آن آزاد است.