# test_to_do_list_manager.py

import unittest
from unittest import TestCase
from to_do_list_manager import tasks, add_tasks, view_tasks

class TestToDoListManager(TestCase):
    def setUp(self):
        tasks.clear()

    def test_that_creates_a_single_task_into_the_tasks_list(self):
        add_tasks("Going to the Club")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["task"], "Going to the Club")
        
    def test_that_creates_a_multiple_tasks_into_the_tasks_list(self):
        add_tasks("Going to the Club")
        add_tasks("Schooling")
        add_tasks("Going to the Market")
        self.assertEqual(len(tasks), 3)
        self.assertEqual(tasks[2]["task"], "Going to the Market")
        
    def test_that_throws_an_error_if_empty_input_is_entered(self):
        add_tasks("")
        self.assertEqual(tasks[0]["task"], "")
        
    
    def test_that_shows_all_tasks(self):
        add_tasks("Writing an Exam")
        add_tasks("Eating Pizza")
        all_tasks = view_tasks()
        self.assertEqual(len(all_tasks), 2)
        
    def test_that_get_all_tasks_and_returns_empty_when_no_task_found(self):
        self.assertEqual(view_tasks(), [])
        
        	

