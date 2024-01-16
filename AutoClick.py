import win32api, win32con, time
import pyautogui as pygui

def click(x,y):
    # click even call
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

if __name__ == "__main__":
    while True:
        # get mouse's current positions
        positions = pygui.position()
        
        x = positions.x
        y = positions.y

        click(x,y)
        print('Moving to X = ',x,' and Y = ',y)
        # Click every 8 seconds
        time.sleep(8)
