import pyautogui
import os
import time
import tkinter as tk

# Here I Create a folder to store the screenshots
screenshot_folder = r"C:\Users\UDAY KIRAN\Desktop\project 1\demo\Scripts\screenshot\ss_folder"

# If the folder does not exist, create it
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

# I created Function to create a flash effect
def flash_effect():
    flash = tk.Tk()
    flash.geometry(f"{flash.winfo_screenwidth()}x{flash.winfo_screenheight()}")
    flash.configure(bg='white')
    flash.attributes('-topmost', True)
    flash.update()
    flash.after(500, flash.destroy())

# I created a function to take a screenshot
def take_screenshot():
    flash_effect()
    timetamp = time.strftime('%y-%m-%d_%H-%M-%S')
    screenshot_path = os.path.join(screenshot_folder, f'screenshot_{timetamp}.png')
    pyautogui.screenshot(screenshot_path)


if __name__ == '__main__':
    take_screenshot()
