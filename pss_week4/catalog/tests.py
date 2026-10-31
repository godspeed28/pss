from django.test import TestCase
from django.db import connection
from django.test.utils import CaptureQueriesContext

from users.models import User
from catalog.models import (
    Course,
    Lesson,
    Enrollment,
    Assignment,
    Submission,
)


class LMSModelTest(TestCase):
    def test_all_models_can_be_queried(self):
        """Memastikan semua model LMS dapat di-query."""
        models = [
            User,
            Course,
            Lesson,
            Enrollment,
            Assignment,
            Submission,
        ]

        for model in models:
            with self.subTest(model=model.__name__):
                self.assertIsNotNone(model.objects.count())

    def test_course_query_works(self):
        """Memastikan query Course berjalan."""
        self.assertIsNotNone(Course.objects.all().count())

    def test_course_lecturer_optimization(self):
        """Membandingkan query Course sebelum dan sesudah optimasi."""
        # Lewati pengujian jika belum ada data Course.
        if not Course.objects.filter(lecturer__isnull=False).exists():
            self.skipTest("Belum ada Course dengan Lecturer.")

        # BEFORE: tanpa select_related()
        with CaptureQueriesContext(connection) as before_ctx:
            courses = list(
                Course.objects.filter(lecturer__isnull=False).order_by("code")[:100]
            )
            for course in courses:
                _ = course.lecturer.username

        before_queries = len(before_ctx.captured_queries)

        # AFTER: menggunakan select_related()
        with CaptureQueriesContext(connection) as after_ctx:
            courses = list(
                Course.objects.filter(lecturer__isnull=False)
                .select_related("lecturer")
                .order_by("code")[:100]
            )
            for course in courses:
                _ = course.lecturer.username

        after_queries = len(after_ctx.captured_queries)

        print(f"\nCourse-Lecturer BEFORE: {before_queries} query")
        print(f"Course-Lecturer AFTER: {after_queries} query")

        self.assertLess(
            after_queries,
            before_queries,
            "Optimasi tidak mengurangi jumlah query. "
            "Pastikan tersedia cukup data Course dan Lecturer.",
        )
