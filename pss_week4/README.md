# Simple LMS

Backend aplikasi Learning Management System menggunakan Django dan PostgreSQL.

## Teknologi

- Python
- Django
- PostgreSQL
- Docker Compose

## Cara Menjalankan Project

1. Clone repository:

```bash
git clone https://github.com/username/simple-lms.git
```

2. Masuk ke folder project:

```bash
cd simple-lms
```

3. Jalankan Docker:

```bash
docker compose up -d --build
```

4. Jalankan migrasi:

```bash
docker compose exec app python manage.py migrate
```

5. Periksa container:

```bash
docker compose ps
```

6. Jalankan pengujian:

```bash
docker compose exec app python manage.py test
```

## Pengujian Django Shell

```bash
docker compose exec app python manage.py shell
```

## Fitur

- Manajemen User
- Manajemen Course
- Manajemen Lesson
- Enrollment mahasiswa
- Assignment
- Submission
