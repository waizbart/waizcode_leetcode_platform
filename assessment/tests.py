from django.test import TestCase

# Create your tests here.
from assessment.utils import run_python_script

class RunPythonScriptTestCase(TestCase):
    def test_run_python_script(self):
        output = run_python_script('tmp/code/test.py')
        self.assertEqual(output, 'OK\n')