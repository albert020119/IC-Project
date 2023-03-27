const { ipcRenderer } = require('electron');

const myCheckbox = document.querySelector('#my-checkbox');

myCheckbox.addEventListener('change', (event) => {
  if (event.target.checked) {
    ipcRenderer.send('run-python-script');
  }
});