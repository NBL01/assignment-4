# from django.test import TestCase
# from django.urls import reverse, resolve
# from tasks.views import index, updateTask, deleteTask


# class URLRoutingTests(TestCase):

#     def test_list_url_resolves(self):
#         url = reverse('list')
#         self.assertEqual(resolve(url).func, index)

#     def test_update_task_url_resolves(self):
#         url = reverse('update_task', args=['1'])
#         self.assertEqual(resolve(url).func, updateTask)

#     def test_delete_url_resolves(self):
#         url = reverse('delete', args=['1'])
#         self.assertEqual(resolve(url).func, deleteTask)


from django.test import TestCase
from .models import Task

class SmokeTest(TestCase):
    def test_create_task(self):
        # Test if you can create a Task instance
        task = Task.objects.create(title="Test Task")
        self.assertEqual(task.title, "Test Task")

    def test_read_task(self):
        # Test if you can retrieve a Task instance from the database
        task = Task.objects.create(title="Test Task")
        retrieved_task = Task.objects.get(id=task.id)
        self.assertEqual(retrieved_task.title, "Test Task")

    def test_update_task(self):
        # Test if you can update a Task instance
        task = Task.objects.create(title="Test Task")
        task.title = "Updated Task"
        task.save()
        updated_task = Task.objects.get(id=task.id)
        self.assertEqual(updated_task.title, "Updated Task")

    def test_delete_task(self):
        # Test if you can delete a Task instance
        task = Task.objects.create(title="Test Task")
        task_id = task.id
        task.delete()
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=task_id)
