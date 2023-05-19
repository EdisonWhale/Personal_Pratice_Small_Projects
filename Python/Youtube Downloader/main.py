import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pytube import YouTube, exceptions
from moviepy.editor import VideoFileClip

class YoutubeDownloader(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Youtube Downloader')
        self.geometry("500x500")
        self.configure(bg="lightgrey")

        # URL Entry
        self.url_label = tk.Label(self, text="Enter video URL", bg="lightgrey",font=("Arial",18))
        self.url_entry = tk.Entry(self, width=50)
        self.url_label.pack(pady=10)
        self.url_entry.pack(pady=10)

        # Path selection
        self.path_label = tk.Label(self, text="Select path to download", bg="lightgrey")
        self.path_button = tk.Button(self, text="Select", command=self.get_path)
        self.path_label.pack(pady=10)
        self.path_button.pack(pady=10)

        # Download Buttons
        self.download_video_button = tk.Button(self, text='Download Video', command=self.download_video)
        self.download_audio_button = tk.Button(self, text='Download Audio', command=self.download_audio)
        self.download_video_button.pack(pady=10)
        self.download_audio_button.pack(pady=10)

        # Progress Bar
        self.progress = ttk.Progressbar(self, orient='horizontal', length=300, mode='determinate')
        self.progress.pack(pady=20)

        # Message Box
        self.message_box = tk.Text(self, height=5, width=60)
        self.message_box.pack(pady=10)

        # Created by label
        self.created_by_label = tk.Label(self, text="Created by Edison ❤", bg="lightgrey",font=("Arial",12))
        
        self.created_by_label.pack(side='bottom', pady=10)


    def get_path(self):
        """Select a path for downloads."""
        self.path = filedialog.askdirectory()
        if self.path:
            self.path_label.config(text=self.path)
        else:
            messagebox.showwarning("Warning", "No directory selected")

    def on_progress_do_this(self, stream, chunk, bytes_remaining):
        """Update the progress bar during the download."""
        total = stream.filesize
        bytes_downloaded = total - bytes_remaining
        percentage_of_completion = bytes_downloaded / total * 100
        self.progress['value'] = percentage_of_completion
        self.update_idletasks()

    def download_video(self):
        """Download a video from a URL."""
        if not hasattr(self, 'path'):
            messagebox.showwarning("Warning", "Please select a download path")
            return

        video_path = self.url_entry.get()
        if not video_path:
            messagebox.showwarning("Warning", "Please provide a valid URL")
            return

        try:
            self.message_box.insert(tk.END, "Downloading video...please wait!\n")
            self.update()
            yt = YouTube(video_path, on_progress_callback=self.on_progress_do_this)
            stream = yt.streams.get_highest_resolution()
            stream.download(self.path)
            self.message_box.insert(tk.END, "Video download complete\n")
            self.update()
            messagebox.showinfo("Success", "Video downloaded successfully")
        except exceptions.RegexMatchError as e:
            self.message_box.insert(tk.END, f"An error occurred: {str(e)}\n")
            self.update()
            messagebox.showwarning("Error", f"An error occurred while downloading the video: {str(e)}")

    def download_audio(self):
        """Download audio from a URL."""
        if not hasattr(self, 'path'):
            messagebox.showwarning("Warning", "Please select a download path")
            return

        video_path = self.url_entry.get()
        if not video_path:
            messagebox.showwarning("Warning", "Please provide a valid URL")
            return

        try:
            self.message_box.insert(tk.END, "Downloading audio...please wait!\n")
            self.update()
            yt = YouTube(video_path, on_progress_callback=self.on_progress_do_this)
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_path = audio_stream.download(self.path)
            new_path = os.path.join(self.path, 'audio.mp3')

            if os.path.exists(new_path):
                os.remove(new_path)

            video_clip = VideoFileClip(audio_path)
            audio_file = video_clip.audio
            audio_file.write_audiofile(new_path)
            audio_file.close()

            video_clip.close()
            os.remove(audio_path)  # remove the original audio file

            self.message_box.insert(tk.END, "Audio download complete\n")
            self.update()
            messagebox.showinfo("Success", "Audio downloaded successfully")
        except exceptions.RegexMatchError as e:
            self.message_box.insert(tk.END, f"An error occurred: {str(e)}\n")
            self.update()
            messagebox.showwarning("Error", f"An error occurred while downloading the audio: {str(e)}")

if __name__ == '__main__':
    app = YoutubeDownloader()
    app.mainloop()
