from django.test import TestCase, Client
from myapp.models import Profile
import json

class ProfileViewJsonTestCase(TestCase):
    def setUp(self):
        self.profile1 = Profile.objects.create(name="Robin", address="ydf square", mobile_number="6423389144", email="robinhood@sype.org")
        self.profile2 = Profile.objects.create(name="Meg", address="blk. no. 12", mobile_number="2466626518", email="megclark@redbox.com")
    
    # tests (GET) "profiles/"
    def test_get_all_profiles(self):
        client = Client()
        response = client.get("/profiles/")
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertEqual(len(json_response), 2)
    
    # tests (POST) "profiles/"
    def test_create_profile(self):
        client = Client()
        data = {
            "name" : "Peter",
            "address" : "atlanta 800137",
            "mobile_number" : "9344671829",
            "email" : "peterdataguy@closeai.org", 
        }
        response = client.post("/profiles/", data)
        self.assertEqual(response.status_code, 200)  
        json_response = response.json()
        self.assertEqual(json_response["message"], "Profile created successfully")
    
    # tests (POST) "profiles/" with missing fields
    def test_create_profile_missing_field(self):
        client = Client()
        data = {
            "name" : "Ragahv",
            "address" : "Powai, Mumbai 400078",
            # "email" missing
        }
        response = client.post("/profiles/", data)
        self.assertEqual(response.status_code, 400)
        json_response = response.json()
        self.assertEqual(json_response["error_message"], "Name and Email are required fields")

    # tests (PUT) "profiles/" 
    def test_create_profile_method_not_allowed(self):
        client = Client()
        response = client.put("/profiles/")  
        self.assertEqual(response.status_code, 405)
        json_response = response.json()
        self.assertEqual(json_response["message"], "Method not allowed")

    # tests (GET) "/profiles/{id}"
    def test_get_profile_details(self):
        client = Client() 
        response = client.get(f"/profiles/{self.profile1.pk}/")
        self.assertEqual(response.status_code, 200)
    
    # tests (PUT) "/profiles/{id}"
    def test_update_profile_field(self):
        client = Client()
        data = {
            "name" : "Franz",
            "email" : "franstoogle@uix.io"
        } 
        response = client.put(f"/profiles/{self.profile1.pk}/", json.dumps(data))
        self.assertEqual(response.status_code, 200)
        updated_profile = Profile.objects.get(pk=self.profile1.pk)
        self.assertEqual(updated_profile.name, data["name"])
        self.assertEqual(updated_profile.email, data["email"])

    def test_delete_profile(self):
        response = self.client.delete(f"/profiles/{self.profile2.pk}/")
        self.assertEqual(response.status_code, 200)
        with self.assertRaises(Profile.DoesNotExist):
            Profile.objects.get(pk=self.profile2.pk)


