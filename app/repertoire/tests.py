from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient
from rest_framework import status

class RepertoireTests(APITestCase, URLPatternsTestCase):

    urlpatterns = [
        path('', include('repertoire.urls')),
    ]
    client = APIClient()

    def test_get_files(self):
        """
        Get files list
        """
        url = reverse('file-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_file_with_id(self):
        """
        Get files with an id
        """
        url = reverse('file-detail', kwargs={"pk":1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND) # test DB is empty

    def test_file_works(self):
        """
        Get all the works in a file
        """
        url = reverse('file-works', kwargs={"pk":1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_file_works_for_an_id(self):
        """
        Get Works for a file with the work id passed
        """
        url = reverse('file-work', kwargs={"pk":1,"work_id":1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
