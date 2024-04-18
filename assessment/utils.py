import subprocess

def run_python_script(script_path, *args):
    result = subprocess.run(['python', script_path] + list(args), capture_output=True, text=True)
    return result.stdout
