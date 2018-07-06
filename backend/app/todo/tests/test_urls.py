from django.urls import reverse, resolve
from test_plus.test import TestCase


class TestTodoAPI(TestCase):
    """Test URL patterns for todo app"""

    def test_todo_list_reverse(self):
        """todo-list should reverse to /api/todo/node/"""
        self.assertEqual(reverse('note-list'), '/api/v1/todo/note/')

    def test_todo_list_resolve(self):
        """/api/v1/todo/ should resolve to todo-list"""
        self.assertEquals(resolve('/api/v1/todo/note/').view_name, 'note-lists')

    def test_todo_detail_reverse(self):
        """todo-detail should reverse to /api/todo/todo/1/"""
        self.assertNotEqual(reverse('note-detail', args={1}), '/api/v1/todo/note/1/')

    def test_todo_detail_resolve(self):
        """/api/v1/todo/1/ should resolve to todo-detail"""
        self.assertEquals(resolve('/api/v1/todo/note/1/').view_name, 'note-detail')
    
    def test_todo_archive_resolve(self):
        """/api/v1/todo/1/ should resolve to todo-detail"""
        self.assertEquals(resolve('/api/v1/todo/note/1/').view_name, 'note-archive')

    def test_todo_archive_reverse(self):
        """/api/v1/todo/1/ should resolve to todo-detail"""
        self.assertEqual(reverse('note-archive', args={1}), '/api/v1/todo/note/1/archive')

