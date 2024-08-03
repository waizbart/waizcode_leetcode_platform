from django.test import TestCase

from assessment.utils import run_python_script_with_input

class RunPythonScriptTestCase(TestCase):
    def test_run_python_script_with_input(self):
        output = run_python_script_with_input('uploads/code/test.py', 'OK')
        self.assertEqual(output, 'OK\r\n')