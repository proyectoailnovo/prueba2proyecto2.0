from django.test import TestCase
from django.test import SimpleTestCase
from django.test import Client
from django.db import models
import unittest
from datetime import datetime
from http import HTTPStatus
from blog.forms import CreateBlogPostForm, UpdateBlogPostForm
from soporte.forms import FormularioContacto
from blog.models import BlogPost, Imggal
from account.forms import Registrarseform, AccountAuthenticationForm, AccountUpdateForm
from account.models import AccountManager


#Test FormularioContacto

class TestForms(SimpleTestCase):

    def test_form_contacto_validdata(self):
        form = FormularioContacto(data={
            'asunto':'problema comprar',
            'mensaje': 'no funciona nada'
        })

        self.assertTrue(form.is_valid())

    def test_form_contacto_nodata(self):
        form = FormularioContacto(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

#Test blog

class TestForms2(SimpleTestCase):

    def test_form_blog_nodata(self):
        form = CreateBlogPostForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)


class TestModel2(TestCase):
    def test_correct_data(self):
        self.data=Imggal.objects.create(imgtitle='fff')
        self.assertEqual(str(self.data),'fff')


class TestCreateBlogPostFormblank(TestCase):
    def test_form_validation_for_blank_items(self):
        form = CreateBlogPostForm(data={'title': '','body': '','image': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
        form.errors['title','body','image'],["este campo es obligatorio"]
        )


# Test account

class TestForms3(TestCase):

    def test_form_registro_validdata(self):
        form = Registrarseform(data={'email': 'sad@gmail.com',
        'username':'ffffff','password1':'1234asds',
        'password2':"1234asds"})

        self.assertTrue(form.is_valid())

    def test_form_registro_nodata(self):
        form = Registrarseform(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)


class Testblank2(TestCase):
    def test_form_validation_for_blank_items(self):
        form = AccountAuthenticationForm(data={'password': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
        form.errors['password'],["este campo es obligatorio"]
        )


#esto no funciona...

class Testblank(TestCase):
    def UpdateBlogPostForm(self):
        form = AccountUpdateForm(data={'title': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
        form.errors['title'],["esto no puede estar vacio"]
        )


class CommentFormTest(TestCase):

    def setUp(self):
        user = get_user_model().objects.create_user('zoidberg')
        self.entry = Entry.objects.create(author=user, title="My entry title")

    def test_valid_data(self):
        form = CreateBlogPostForm({
            'title': "asddsadasd",
            'body': "asdasdasdas",
            'image': "../static/img/2080ti.jpg",
        }, entry=self.entry)
        self.assertTrue(form.is_valid())
        fields = form.save()
        self.assertEqual(fields.title, "asddsadasd")
        self.assertEqual(fields.body, "asdasdasdas")
        self.assertEqual(fields.image, "../static/img/2080ti.jpg")
        self.assertEqual(fields.entry, self.entry)