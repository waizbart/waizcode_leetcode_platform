function clearTextArea() {
    const textArea = document.getElementsByTagName('textarea')[0];
    
    textArea.value = '';

    const event = new Event('input', { bubbles: true, cancelable: true });
    textArea.dispatchEvent(event);

    textArea.focus();
}

const clearButton = document.getElementById('reset');
clearButton.addEventListener('click', clearTextArea);