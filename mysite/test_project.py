from django.test import TestCase
from proj.models import Student
from proj.views import plswork, mygod, mygodtwo

class StudentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Student.objects.create(name='Fedor', surname='Ivanov', group='201-331')

    def test_name_label(self):
        student = Student.objects.get(id=1)
        field_label = student._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_surname_label(self):
        student = Student.objects.get(id=1)
        field_label = student._meta.get_field('surname').verbose_name
        self.assertEquals(field_label, 'surname')

    def test_group_label(self):
        student = Student.objects.get(id=1)
        field_label = student._meta.get_field('group').verbose_name
        self.assertEquals(field_label, 'group')
    def test_name_max_length(self):
        student = Student.objects.get(id=1)
        max_length = student._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_surname_max_length(self):
        student = Student.objects.get(id=1)
        max_length = student._meta.get_field('surname').max_length
        self.assertEquals(max_length, 50)

    def test_group_max_length(self):
        student = Student.objects.get(id=1)
        max_length = student._meta.get_field('group').max_length
        self.assertEquals(max_length, 50)

    def test_for_display(self):
        display = plswork("<WSGIRequest: GET '/'>").__str__()
        self.assertEquals(display, "<HttpResponse status_code=200, \"text/html; charset=utf-8\">")

    def test_for_records(self):
        expected_num = mygod()
        self.assertEquals(expected_num, 3)

    def test_for_records_false(self):
        expected_num = mygodtwo()
        self.assertEquals(expected_num, 3)
