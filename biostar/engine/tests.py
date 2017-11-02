import logging
from django.test import TestCase
from django.test import Client

from django.urls import reverse

logger = logging.getLogger('engine')


class TestLogin(TestCase):
    def setUp(self):
        return



class UserNavigation(TestCase):

    def test_account_pages(self):
        'Tests general account pages for users'

        params = dict(id=1)

        urls = [
            (reverse('signup'), dict(info=dict(email="test1@lvh.me", password="test1@lvh.me"),code=200)),
            (reverse('login'),dict(info=dict(email="test1@lvh.me", password="test1@lvh.me"),code=200)),
            (reverse('profile', kwargs=params),dict(info={},code=200))
        ]

        c = Client()

        for url, info in urls:
            resp = c.post(url, info["info"])
            self.assertEqual(resp.status_code, info["code"])


class SiteNavigation(TestCase):


    def visit_urls(self, urls, code):
        c = Client()
        for url in urls:
            resp = c.get(url)
            if resp.status_code != code:
                # print (resp.content)
                # We already know it is an error.
                # Use this to prints the url and the code.
                self.assertEqual(url, code)

    def test_public_pages(self):
        "Checking public pages"

        params = dict(id=1)


        urls = [
            reverse('index'), reverse('info'),
            reverse('login'), reverse('signup'),
            reverse('project_list'),
            reverse('project_view', kwargs=params),
            reverse('data_list', kwargs=params),
            reverse('analysis_list', kwargs=params),
            reverse('job_list', kwargs=params),
        ]

        self.visit_urls(urls, 200)


    def test_page_redirect(self):
        "Testing that a redirect occurs for some pages"

        params = dict(id=1)
        urls = [
            reverse('data_upload', kwargs=params),
        ]

        self.visit_urls(urls, 302)



