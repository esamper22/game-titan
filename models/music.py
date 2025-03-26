from pyray import (
    close_audio_device,
    load_music_stream,
    play_music_stream,
    set_music_volume,
    stop_music_stream,
    unload_music_stream,
    update_music_stream,
)


class Music:
    def __init__(self, music=None):
        self.music = load_music_stream(music)
    
    def update(self):
        update_music_stream(self.music)

    def play(self):
        play_music_stream(self.music)
    
    def stop(self):
        stop_music_stream(self.music)
        
    def set_volume(self, value=1.0):
        set_music_volume(self.music, value)

    def reset(self):
        self.stop()
        self.play()

    def unload(self):
        stop_music_stream(self.music)
        unload_music_stream(self.music)
        close_audio_device()

    