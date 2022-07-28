from django.test import SimpleTestCase
from django.urls import reverse, resolve


class HomePageTests(SimpleTestCase):
    """ Test for checking the home page exsits, the url exsits,\
         the template exsits and the view exsits"""

    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exsits_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'home/index.html')

    def test__page_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, 'index', __name__)


class StoryPageTests(SimpleTestCase):
    """ Test for checking the Story page exsits, the url exsits, \
        the template exsits and the view exsits"""

    def setUp(self):
        url = reverse("our_story")
        self.response = self.client.get(url)

    def test_url_exsits_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'home/our_story.html')

    def test_page_resolves_homepageview(self):
        view = resolve("/our_story/")
        self.assertEqual(view.func.__name__, 'our_story', __name__)


class TermsAndConditionsTests(SimpleTestCase):
    """ Test for checking the taproom page exsits, \
        the url exsits, the template exsits and the view exsits"""

    def setUp(self):
        url = reverse("ts_and_cs")
        self.response = self.client.get(url)

    def test_url_exsits_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'home/tandcs.html')

    def test_page_resolves_view(self):
        view = resolve("/ts_and_cs/")
        self.assertEqual(view.func.__name__, 'ts_and_cs', __name__)


class PrivacypageTests(SimpleTestCase):
    """ Test for checking that the Privacy page exsits, \
        the url exsits, the template exsits and the view\
        exsits"""

    def setUp(self):
        url = reverse("privacy")
        self.response = self.client.get(url)

    def test_url_exsits_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'home/privacy.html')

    def test_home_page_resolves_view(self):
        view = resolve("/privacy/")
        self.assertEqual(view.func.__name__, 'privacy', __name__)

