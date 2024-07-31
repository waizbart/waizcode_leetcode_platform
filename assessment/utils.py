import subprocess

def run_python_script_with_input(script_path, input_str):
    """
    Run a python script with input string and return the output string.
    """
    process = subprocess.Popen(['python', script_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    input_str += '\n'
    
    stdout, stderr = process.communicate(input=input_str.encode())

    output = stdout.decode()
    error = stderr.decode()

    output_lines = output.strip().splitlines()

    clean_output = '\n'.join(output_lines)

    if error:
        clean_output += '\n' + error

    return clean_output

def save_code_file(content, file_path):
    """
    Save the code content to a file.
    """
    with open(file_path, "w") as f:
        f.write(content)
