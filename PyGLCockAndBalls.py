import glfw
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

def render_sphere():
    sphere = gluNewQuadric()
    glColor3f(1.0, 0.0, 0.0)  # Set the sphere's color to red
    gluSphere(sphere, 0.5, 32, 32)  # Create a red sphere with radius 0.5
    gluDeleteQuadric(sphere)

def render_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMaterialfv(GL_FRONT, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.8, 0.8, 0.8, 1.0))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
    glMaterialfv(GL_FRONT, GL_SHININESS, 100.0)
    light_position = (1.0, 1.0, 1.0, 0.0)
    light_ambient = (0.0, 0.0, 0.0, 1.0)
    light_diffuse = (1.0, 1.0, 1.0, 1.0)
    light_specular = (1.0, 1.0, 1.0, 1.0)

    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

    # Your rendering code here (e.g., background, 3D objects)

    render_sphere()  # Call the function to render the sphere

    glfw.swap_buffers(window)

# Make the window's context current
glfw.make_context_current(window)

# Main loop
while not glfw.window_should_close(window):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0, 0, -5)
    render_scene()

# Terminate GLFW
glfw.terminate()
