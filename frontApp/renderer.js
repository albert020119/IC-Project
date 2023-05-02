const { ipcRenderer } = require('electron');

const checkboxAttach = document.querySelector('#checkboxAttach');
const checkboxAim = document.querySelector('#checkboxAim');
const checkboxWall = document.querySelector('#checkboxWall');
const checkboxRadar = document.querySelector('#checkboxRadar');
const checkboxAntiflash= document.querySelector('#checkboxAntiflash');
const checkboxTrigger= document.querySelector('#checkboxTrigger');


checkboxAttach.addEventListener('change', (event) => {
  if (event.target.checked) {
    ipcRenderer.send('run-python-script');
  }
  checkbox.blur(); // remove focus from the checkbox
  setTimeout(function() {
    checkbox.focus(); // add focus back to the checkbox
  }, 0);
});
checkboxAim.addEventListener('change', (event) => {
  if (event.target.checked) {
    ipcRenderer.send('run-python-script');
  }
});
checkboxWall.addEventListener('change', (event) => {
  if (event.target.checked) {
    ipcRenderer.send('run-python-script-Wall');
  }
  else {
    ipcRenderer.send('kill-python-script-Wall');
  }
});
checkboxBunny.addEventListener('change', (event) => {
  if (event.target.checked) {
    ipcRenderer.send('run-python-script-Bunny');
  }
});
checkboxAntiflash.addEventListener('change', (event) => {
  if (event.target.checked) {
    ipcRenderer.send('run-python-script-Antiflash');
  }
});
checkboxTrigger.addEventListener('change', (event) => {
  if (event.target.checked) {
    ipcRenderer.send('run-python-script');
  }
});
