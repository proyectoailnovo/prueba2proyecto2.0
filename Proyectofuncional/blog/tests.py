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

#Test account

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
        form.errors['password'],["no debe estar vacio"]
        )
