const { app, BrowserWindow, ipcMain } = require('electron');
const { spawn } = require('child_process');

let win;
function createWindow () {
  win = new BrowserWindow({
    width: 400,
    height: 600,
    resizable: false,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    }
  });

  win.loadFile('index.html');
  //win.webContents.openDevTools();
}

app.whenReady().then(() => {
  createWindow();

  ipcMain.on('run-python-script', () => {
   const pythonProcess = spawn('python', ['C:/Users/Tudor/Desktop/frontApp/script.py']);
;
    
    pythonProcess.stdout.on('data', (data) => {
      console.log(`stdout: ${data}`);
    });

    pythonProcess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
    });

    pythonProcess.on('close', (code) => {
      console.log(`Python script exited with code ${code}`);
    });
  });
});
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});

