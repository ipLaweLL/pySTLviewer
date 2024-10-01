# pySTLviewer
A python based STL viewer. This project involves rendering and simulating 3D objects using Python.

## Requirements

To run this project, ensure you have the following packages installed:

- *pygame*: A set of Python modules designed for writing video games, but also useful for rendering.
- *PyOpenGL*: A cross-platform Python binding to OpenGL for rendering 3D objects.
- *numpy*: A fundamental package for scientific computing with Python.
- *numpy-stl*: A library to easily read and write STL (Stereolithography) files, which are widely used for 3D object representation.

## Installation Instructions

1. *Clone the repository* (or create your own project structure):

   ```bash
   git clone https://github.com/ipLaweLL/pySTLviewer.git
   cd pySTLviewer
2. **Set up a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. *Install the required Python packages*:

   ```bash
   pip install pygame pyopengl numpy numpy-stl

## STL File Placement

For better results and ease of use, ensure that the STL file you want to render is saved in the same directory as your main Python script. This makes file access easier and avoids potential path issues.

    /project-directory
    │
    ├── STLviewer.py
    ├── object.stl
    ├── README.md
    └── (other files...)

## Usage

Once all the dependencies are installed and the STL file is in place, you can run the project by executing the main script:
   python STLviewer.py

## Project Overview

This project demonstrates how to load an STL file and render it using OpenGL through PyOpenGL, while managing input events and display updates using pygame. It is designed to be extensible for more complex simulations and 3D graphics projects.

## Additional Notes

- Ensure that you have OpenGL properly installed on your system. Some platforms may require additional setup.
- The code has been tested with Python 3.8+.
- For large STL files, loading times may vary depending on your system configuration.
