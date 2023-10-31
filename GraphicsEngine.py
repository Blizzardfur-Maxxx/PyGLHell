import glfw
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Initialize the GLFW library
if not glfw.init():
    print("Failed to initialize GLFW")
    exit()

# Create a windowed mode window and its OpenGL context
window = glfw.create_window(800, 600, "My GLFW Window", None, None)

if not window:
    glfw.terminate()
    exit()

# Make the window's context current
glfw.make_context_current(window)

def backround_render():
    background_texture = pygame.image.load("background_texture.png")
    background_data = pygame.image.tostring(background_texture, "RGBX", 1)
    width, height = background_texture.get_width(), background_texture.get_height()
    background_texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, background_texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, background_data)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, background_texture_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-1, -1, 0)
    glTexCoord2f(1, 0)
    glVertex3f(1, -1, 0)
    glTexCoord2f(1, 1)
    glVertex3f(1, 1, 0)
    glTexCoord2f(0, 1)
    glVertex3f(-1, 1, 0)
    glEnd()
    glDisable(GL_TEXTURE_2D)

def render_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMaterialfv(GL_FRONT, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.8, 0.8, 0.8, 1.0))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
    glMaterialfv(GL_FRONT, GL_SHININESS, 10.0)
    light_position = (5.0, 5.0, 1.0, 1.0)
    light_ambient = (1.0, 1.0, 1.0, 1.0)
    light_diffuse = (1.0, 1.0, 1.0, 1.0)
    light_specular = (1.0, 1.0, 1.0, 1.0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

def render_sphere():
    sphere = gluNewQuadric()
    glColor3f(1.0, 0.0, 0.0)  # Set the sphere's color to red
    gluSphere(sphere, 0.5, 32, 32)  # Create a red sphere with radius 0.5
    gluDeleteQuadric(sphere)

def render_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set clear color to black (R, G, B, Alpha)
    glLoadIdentity()
    backround_render()
    render_lighting()
    render_sphere()
    glfw.swap_buffers(window)

# Main loop
while not glfw.window_should_close(window):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0, 0, -5)
    render_scene()

# Terminate GLFW
glfw.terminate()
