import pyglet


# Load sounds
sound = pyglet.media.load("hola.m4a",streaming=False)
sound.play()
