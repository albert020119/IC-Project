const { app, BrowserWindow, ipcMain } = require('electron');
const { spawn } = require('child_process');

let win;

let pythonProcess;

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

  ipcMain.on('run-python-script-Wall', () => {
   pythonProcess = spawn('python', ['C:/Users/Tudor/Desktop/pythonPrograms/csgoCheat/functions/wall.py']);
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

ipcMain.on('run-python-script-Bunny', () => {
   pythonProcess = spawn('python', ['C:/Users/Tudor/Desktop/pythonPrograms/csgoCheat/functions/bunny.py']);
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

ipcMain.on('run-python-script-Antiflash', () => {
   pythonProcess = spawn('python', ['C:/Users/Tudor/Desktop/pythonPrograms/csgoCheat/functions/antiflash.py']);
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


  ipcMain.on('kill-python-script-Wall', ()=>{
    if (pythonProcess!==null) {
      pythonProcess.kill('SIGTERM');
      pythonProcess=null;
    }
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

