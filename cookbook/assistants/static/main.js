document.getElementById('run-script').addEventListener('click', () => {
    fetch('/run-script')
        .then(response => response.json())
        .then(data => {
            document.getElementById('output').textContent = data.output || data.error;
        });
});
