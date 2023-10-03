import tkinter as tk
from PIL import Image, ImageTk
import pygame

class GIFPlayer:
    def __init__(self, root, gif_path, audio_path):
        self.root = root
        self.gif_path = gif_path
        self.audio_path = audio_path

        # Initialize the GUI
        self.initialize_gui()
        
        # Load the GIF file
        self.load_gif()
        
        # Enable audio playback
        self.play_audio()

    def initialize_gui(self):
        # Configure the main window
        self.root.title("GIF AND MP3 PLAYER")
        self.root.configure(bg="black")

        # Create a canvas for displaying the GIF image
        self.canvas = tk.Canvas(self.root, width=400, height=300, bd=0)
        self.canvas.grid(row=0, column=0, columnspan=2)

        # Create a play button
        play_image = ImageTk.PhotoImage(Image.open("play.png"))
        self.play_button = tk.Button(self.root, image=play_image, command=self.play, bg="black", bd=0)
        self.play_button.image = play_image
        self.play_button.grid(row=1, column=0, padx=10, pady=10)

        # Create a stop button
        stop_image = ImageTk.PhotoImage(Image.open("stop.png"))
        self.stop_button = tk.Button(self.root, image=stop_image, command=self.stop, bg="black", bd=0)
        self.stop_button.image = stop_image
        self.stop_button.grid(row=1, column=1, padx=10, pady=10)

    def load_gif(self):
        # Load the GIF file and create a list of frames
        self.gif = Image.open(self.gif_path)
        self.gif_frames = []
        try:
            while True:
                self.gif_frames.append(self.gif.copy())
                self.gif.seek(len(self.gif_frames))
        except EOFError:
            pass
        self.current_frame = 0
        self.show_frame()

    def show_frame(self):
        # Display the current frame on the canvas
        frame = self.gif_frames[self.current_frame]
        self.photo = ImageTk.PhotoImage(frame)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def play_audio(self):
        # Initialize Pygame and load the audio file
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.audio_path)
        pygame.mixer.music.set_volume(0.5)

    def play(self):
        # Start playing the audio and animate the frames
        pygame.mixer.music.play()
        self.animate()

    def stop(self):
        # Stop playing the audio
        pygame.mixer.music.stop()

    def animate(self):
        # Move to the next frame and call the animate function again after a short delay
        self.current_frame += 1
        if self.current_frame == len(self.gif_frames):
            self.current_frame = 0
        self.show_frame()
        self.root.after(100, self.animate)

# Initialize the main window and run the application
if __name__ == "__main__":
    root = tk.Tk()
    gif_path = "RAT.gif" # Write the file path for the gif file here
    audio_path = "RAT.mp3" # Write the file path for the mp3 file here
    app = GIFPlayer(root, gif_path, audio_path)
    root.mainloop()
