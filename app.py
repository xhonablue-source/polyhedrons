import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

# Page setup
st.set_page_config(page_title="MathCraft: Polyhedrons", page_icon="📦", layout="wide")
st.title("📦 MathCraft: Polyhedrons – Geometry in 3D!")
st.markdown("*Developed by Xavier Honablue M.Ed for cognitivecloud.ai*")

# --- Image Loader ---
def load_image(filename):
    try:
        return Image.open(filename)
    except:
        return None

# --- Sidebar Navigation ---
st.sidebar.title("🔍 Explore Sections")
section = st.sidebar.radio("Jump to a section:", [
    "📚 Lesson: What Are Polyhedrons?",
    "🔢 Vocabulary & Rules",
    "🧠 Euler's Formula",
    "📸 Visual Gallery",
    "🧪 Polyhedron Playground",
    "📐 Build Tetrahedral Sheet",
    "📎 Real-World Applications"
])

# --- Section 1: Lesson ---
if section == "📚 Lesson: What Are Polyhedrons?":
    st.header("📚 Understanding Polyhedrons")
    st.markdown("""
    **Polyhedrons** are solid 3D shapes with flat polygonal faces, straight edges, and vertices (corners). 

    These include:
    - **Platonic Solids** (all faces and angles equal)
    - **Archimedean Solids** (faces are regular but not all the same)

    They form the building blocks of geometry and appear in nanoscience, architecture, crystals, and more!
    """)

# --- Section 2: Vocabulary ---
elif section == "🔢 Vocabulary & Rules":
    st.header("📘 Polyhedron Vocabulary & Geometry Rules")
    st.markdown("""
    - **Face:** A flat surface (e.g., square or triangle)
    - **Edge:** Where two faces meet
    - **Vertex:** A corner where edges meet
    - **Euler’s Formula:** \( V - E + F = 2 \) for convex polyhedrons
    - **Regular Polyhedrons:** All faces are the same shape and size
    """)

# --- Section 3: Euler's Formula ---
elif section == "🧠 Euler's Formula":
    st.header("🧠 Explore Euler’s Polyhedron Formula")
    st.latex(r"V - E + F = 2")

    st.markdown("Try entering your own values to see if it works!")
    V = st.number_input("Vertices (V)", min_value=0, value=8)
    E = st.number_input("Edges (E)", min_value=0, value=12)
    F = st.number_input("Faces (F)", min_value=0, value=6)

    if V - E + F == 2:
        st.success(f"✅ Euler’s Formula holds: {V} - {E} + {F} = 2")
    else:
        st.error(f"❌ Doesn't hold: {V} - {E} + {F} = {V - E + F}")

# --- Section 4: Visual Gallery ---
elif section == "📸 Visual Gallery":
    st.header("📸 Polyhedron Gallery")
    st.markdown("A visual library of major polyhedrons:")

    cols = st.columns(3)
    image_files = {
        "Tetrahedron": "assets/tetrahedron.png",
        "Cube (Hexahedron)": "assets/cube.png",
        "Octahedron": "assets/octahedron.png",
        "Dodecahedron": "assets/dodecahedron.png",
        "Icosahedron": "assets/icosahedron.png"
    }

    for (name, path), col in zip(image_files.items(), cols * 2):
        img = load_image(path)
        if img:
            col.image(img, caption=name, use_column_width=True)
        else:
            col.warning(f"Image not found for {name}")

# --- Section 5: Playground ---
elif section == "🧪 Polyhedron Playground":
    st.header("🧪 Interactive Polyhedron Explorer")
    st.markdown("""
    Adjust sliders below to build your own abstract 3D shapes and explore how face/edge/vertex ratios affect geometry!
    """)

    sides = st.slider("Number of sides per face", 3, 12, 6)
    faces = st.slider("Number of faces", 4, 32, 8)
    st.markdown(f"You chose a shape with {faces} faces that are {sides}-gons.")
    st.info("This tool is conceptual, great for understanding abstract 3D geometry.")

# --- Section 6: Build Tetrahedral Sheet ---
elif section == "📐 Build Tetrahedral Sheet":
    st.header("📐 Construct a Sheet of Tetrahedrons")
    st.markdown("""
    This activity simulates building a 2D sheet using repeated tetrahedrons — just like some nanostructures and molecular crystals.
    
    You can imagine each tetrahedron as a triangle pyramid.
    """)
    grid_size = st.slider("Number of tetrahedrons in a row", 1, 10, 5)

    fig, ax = plt.subplots(figsize=(8, 4))
    for i in range(grid_size):
        x = i * 2
        triangle = plt.Polygon([[x, 0], [x + 1, 1.5], [x + 2, 0]], closed=True, color='skyblue', edgecolor='black')
        ax.add_patch(triangle)
    ax.set_xlim(0, grid_size * 2)
    ax.set_ylim(0, 2)
    ax.axis('off')
    st.pyplot(fig)

# --- Section 7: Real-World Connections ---
elif section == "📎 Real-World Applications":
    st.header("📎 Where Polyhedrons Show Up in Real Life")
    st.markdown("""
    ✅ **Beehives:** Hexagonal packing structures maximize space.

    ✅ **Viruses:** Many viral shells are icosahedrons — combining symmetry and strength.

    ✅ **Kevlar/Teflar Body Armor:** Nano-polyhedrons reinforce fibers.

    ✅ **Architecture:** Geodesic domes (like Buckminster Fuller's) use polyhedrons for light-weight strength.

    ✅ **Crystals & Nanoscience:** Atomic and molecular structures form repeating polyhedrons.
    """)

# --- End ---
st.markdown("---")
st.success("✅ Lesson complete. Ready to build your own solid ideas!")
