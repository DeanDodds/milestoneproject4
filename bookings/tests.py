from django.test import SimpleTestCase
from django.urls import reverse


class BookingTaproomPageTests(SimpleTestCase):
    """ Test for checking the taproom booking page exsits, the url exsits,\
         the template exsits """

    def setUp(self):
        url = reverse("booking_taproom")
        self.response = self.client.get(url)

    def test_url_exsits_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'bookings/taproom_booking.html')


class BreweryTourBookingPageTests(SimpleTestCase):
    """ Test for checking the brewery tour booking page exsits, the url exsits,\
         the template exsits """

    def setUp(self):
        url = reverse("book_brew_tour")
        self.response = self.client.get(url)

    def test_url_exsits_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 
                                'bookings/brew_tour_booking.html')
