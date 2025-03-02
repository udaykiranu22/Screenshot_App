We need to install pyautogui for to taking screenshot. 
Make sure where you want to store the screenshot images, for that create one folder for that provide that path in code.
Download app logo from icon8 or someother, any png. we should convert into ico format.
Again we should download one more module called pyinstaller.
After that we should run one line in cmd :
        pyinstaller --onefile --windowed --icon=iconimage.ico screenshot.py
It will create 2 folders called Build and dist.
      Our app is ready in dist folder, you can pin to taskbar.
use it by clicking on it.
