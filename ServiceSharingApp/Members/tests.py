from django.test import TestCase, Client,TransactionTestCase
from django.contrib.auth import get_user_model
from ServicEventPool.models import Service, Event, Location, Notification, Activity, Media, User_Service_Status, User_Event_Status,Comment
from django.db.utils import IntegrityError



class ServiceCreateTest(TestCase):
    def setUp(self):
        User1 = get_user_model().objects.create_user(username='testuset1', email='test@test.com',
                                                         password='testpassword')
        Location.objects.create(name='Bogazici University', geoLocation='41.083556 29.050598')
        get_user_model().objects.create_user(username='testuset', email='test@test.com', password='testpassword')

        Service.objects.create(name="Service Test Name", description="Service Test Description",
                               service_date = "2022-12-12", service_time = "00:00",
                               service_provider=User1,
                               location=Location.objects.get(name='Bogazici University'),
                               duration_credit=2, slug="ServiceTestSlug")

        Service.objects.create(name="Service Test2 Name", description="Service Test2 Description",
                               service_date="2022-12-12", service_time="00:00",
                               service_provider=User1,
                               location=Location.objects.get(name='Bogazici University'),
                               duration_credit=1, slug="ServiceTest2Slug")

    def test_service_object_created_properly(self):
        service = Service.objects.get(name="Service Test Name")
        self.assertEqual(service.name, 'Service Test Name')
        self.assertEqual(service.description, 'Service Test Description')
        self.assertEqual(service.duration_credit, 2)

    def test_service_object_creation_not_same(self):
        with self.assertRaises(IntegrityError):
            User2 = get_user_model().objects.create_user(username='testuset2', email='test@test.com',
                                                             password='testpassword')
            Location.objects.create(name='Bogazici University2', geoLocation='41.083556 29.050598')
            self.user = get_user_model().objects.create_user(username='testuset1', email='test@test.com',
                                                             password='testpassword')
            Service.objects.create(name="Service Test Name", description="Service Test Description",
                                   service_date="2022-12-12", service_time="00:00",
                                   service_provider=User2,
                                   location=Location.objects.get(name='Bogazici University2'),
                                   duration_credit=2, slug="ServiceTestSlug")


class EventCreateTest(TestCase):
    def setUp(self):
        User = get_user_model().objects.create_user(username='testuset3', email='test@test.com', password='testpassword')
        Location.objects.create(name='Bogazici University3', geoLocation='41.083556 29.050598')
        Event.objects.create(name="Event Test Name", description="Event Test Description",
                             event_date="2022-12-12", event_time="00:00",
                             event_provider=User,duration=2,
                             location=Location.objects.get(name='Bogazici University3'),
                                slug="EventTestSlug")

        Event.objects.create(name="Event Test2 Name", description="Event Test2 Description",
                             event_date="2022-12-12", event_time="00:00",
                             event_provider=User,duration=2,
                             location=Location.objects.get(name='Bogazici University3'),
                                slug="EventTest2Slug")

    def test_event_object_created_properly(self):
        event = Event.objects.get(name='Event Test Name')
        self.assertEqual(event.name, 'Event Test Name')
        self.assertEqual(event.description, 'Event Test Description')



class UserTestCase(TestCase):

    User = get_user_model()

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuset', email='test@test.com', password='testpassword')

    def test_user(self):
        self.assertEqual(self.user.email, 'test@test.com' )

    def test_login_url(self):
        login_url = "/members/login_user"
        data = {"username":"testuset", "password":"testpassword"}
        response = self.client.post(login_url, data, follow=True)
        status_code = response.status_code
        self.assertEqual(status_code, 200)