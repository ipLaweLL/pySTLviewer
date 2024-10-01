import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from stl import mesh
import numpy as np

def load_stl(stl_path):
    try:
        stl_model = mesh.Mesh.from_file(stl_path)
        print(f"STL file loaded successfully. Number of vectors: {len(stl_model.vectors)}")
        return stl_model
    except Exception as e:
        print(f"Error loading STL file: {e}")
        return None

def get_model_dimensions(triangles):
    min_coords = np.min(triangles, axis=(0, 1))
    max_coords = np.max(triangles, axis=(0, 1))
    dimensions = max_coords - min_coords
    return dimensions

def shift_to_center(triangles):
    min_coords = np.min(triangles, axis=(0, 1))
    max_coords = np.max(triangles, axis=(0, 1))
    center = (min_coords + max_coords) / 2
    return triangles - center

def create_vbo(data):
    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, data.nbytes, data, GL_STATIC_DRAW)
    print(f"VBO created with {len(data)} vertices")
    return vbo

def draw_stl_vbo(num_vertices):
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, None)
    glDrawArrays(GL_LINES, 0, num_vertices)
    glDisableClientState(GL_VERTEX_ARRAY)
    glColor3f(0,0,0)

def main():
    pygame.init()
    
    stl_path = input("Enter name/path of the STL file: ")
    stl_model = load_stl(stl_path)
    if stl_model is None:
        pygame.quit()
        return

    display = (1200, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("STL Viewer")

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)

    triangles = shift_to_center(stl_model.vectors)
    dimensions = get_model_dimensions(triangles)
    max_dimension = np.max(dimensions)
    scale_factor = 5.0 / max_dimension

    vertices = []
    for triangle in triangles:
        vertices.extend([triangle[0], triangle[1],
                         triangle[1], triangle[2],
                         triangle[2], triangle[0]])

    vertices = np.array(vertices, dtype=np.float32).flatten()
    vbo = create_vbo(vertices)

    clock = pygame.time.Clock()
    rotation_x, rotation_y = 0, 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    dx, dy = event.rel
                    rotation_y += dx * 0.5
                    rotation_x -= dy * 0.5

            if event.type == pygame.MOUSEWHEEL:
                scale_factor *= 1.1 ** event.y

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        glClearColor(1,1,1,1)
        glTranslatef(0, 0, -10)
        

        glRotatef(rotation_x, 1, 0, 0)
        glRotatef(rotation_y, 0, 1, 0)
        glScalef(scale_factor, scale_factor, scale_factor)

    
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        draw_stl_vbo(len(vertices) // 3)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()