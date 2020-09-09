import pyglet
audio = pyglet.media.load("prueba.wav")
audio.play()

# Load sounds
#sound = pyglet.media.load("prueba.wav",streaming=False)
left_sound = pyglet.media.load("left.wav", streaming=False)
right_sound = pyglet.media.load("right.wav", streaming=False)


left_sound.play()
#sound.play()
pyglet.app.run()
right_sound.play()

