document.getElementById('toggle_header').addEventListener('click', function() {
    const header = document.getElementById('toggle_header');
    if (header.classList.contains('red')) {
        header.classList.remove('red');
        header.classList.add('green');
    } else {
        header.classList.remove('green');
        header.classList.add('red');
    }
});