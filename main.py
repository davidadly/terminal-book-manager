from ebookapp import EBookApp
from startup_animation import startup_animation

if __name__ == "__main__":
    startup_animation()
    app = EBookApp()
    app.run()
