import pygame
import win32api
import win32con
import win32gui
from pygame._sdl2.video import Window

pygame.init()

class Tab:
    def __init__(self, icon, name):
        #self.icon = icon
        self.name = name
        self.messages = {
            "microphone": False,
            "camera": False,
            "screen_record": False,
        }

class VortexTabDisplay:
    def __init__(self, parent_window):
        self.screen = pygame.display.set_mode((800, 600), pygame.NOFRAME) # For borderless, use pygame.NOFRAME
        self.transparent = (255, 0, 128)  # Transparency color
        self.parent_window = parent_window
        self.font = pygame.font.SysFont("Arial", 20)

        # Create layered window
        self.hwnd = pygame.display.get_wm_info()["window"]
        win32gui.SetWindowLong(self.hwnd, win32con.GWL_EXSTYLE,
                            win32gui.GetWindowLong(self.hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
        # Set window transparency color
        win32gui.SetLayeredWindowAttributes(self.hwnd, win32api.RGB(*self.transparent), 0, win32con.LWA_COLORKEY)

        # Set window position
        win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

        # set window borderless
        win32gui.SetWindowLong(self.hwnd, win32con.GWL_STYLE, win32con.WS_POPUP)

        # tabs
        self.tabs = []
        self.tabs.append(Tab(None, "Camera"))
 
    def draw(self):
        self.screen.fill(self.transparent)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.parent_window.close()
                quit()

        for tab in self.tabs:
            # self.screen.blit(tab.icon, (0, 0))
            # draw text
            self.font.render(tab.name, True, (255, 255, 255))

        pygame.display.flip()
        win32gui.UpdateWindow(self.hwnd)

    def update(self):
        try:
            window = Window.from_display_module()
            window.size = (self.parent_window.get_size()[0], self.parent_window.tab_bar_height)
            self.parent_window.set_location(*window.position)

            # make window on top of the parent window
            win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        except:
            pass
