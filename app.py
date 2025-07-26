import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from math import sqrt

# --- Page Setup ---
st.set_page_config(page_title="🔺 MathCraft: Polyhedron Playground", page_icon="📦", layout="wide")
st.title("📦 MathCraft: Polyhedron Playground")
st.markdown("*Developed by Xavier Honablue M.Ed for cognitivecloud.ai*")

# --- Sidebar Navigation ---
st.sidebar.title("🔍 Explore Polyhedrons")
section = st.sidebar.radio("Choose a Section", [
    "📦 Introduction to Polyhedrons",
    "🔺 Build a Sheet of Tetrahedrons",
    "🌐 Platonic Solids Viewer",
    "🧬 Real World Polyhedra",
    "🧠 Quiz: Name That Shape!"
])

# --- Section 1: Introduction ---
if section == "📦 Introduction to Polyhedrons":
    st.header("📦 What Are Polyhedrons?")
    st.markdown("""
    A **polyhedron** is a 3-dimensional shape with flat polygonal faces, straight edges, and sharp corners or vertices.
    The most famous polyhedra are the **Platonic solids**: tetrahedron, cube, octahedron, dodecahedron, and icosahedron.

    These shapes are not only fun to study — they appear **throughout nature and technology**, from **beehives** to **nanostructures**, **virus shells**, and even **Kevlar armor**.
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/8/87/Platonic_Solids_Animation.gif", caption="Platonic Solids")

# --- Section 2: Tetrahedron Sheet Builder ---
elif section == "🔺 Build a Sheet of Tetrahedrons":
    st.header("🔺 Create a Tetrahedron Mesh")
    st.markdown("""
    Here's an interactive way to **tile tetrahedrons** into a 2D sheet that resembles the underlying **molecular structure of strong materials** like Teflon and Kevlar.
    """)
    cols = st.columns([2, 1])
    with cols[1]:
        rows = st.slider("Number of rows", 1, 10, 4)
        cols = st.slider("Number of columns", 1, 10, 4)

    fig = go.Figure()
    unit = 1
    h = sqrt(3)/2 * unit

    for i in range(rows):
        for j in range(cols):
            x0 = j * unit
            y0 = i * h
            x1 = x0 + unit / 2
            y1 = y0 + h
            x2 = x0 + unit
            y2 = y0
            fig.add_trace(go.Scatter(
                x=[x0, x1, x2, x0], y=[y0, y1, y2, y0],
                mode="lines",
                fill="toself",
                line=dict(color="royalblue")
            ))

    fig.update_layout(
        title="Tiled Tetrahedron Mesh",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        height=500
    )
    st.plotly_chart(fig)

# --- Section 3: Platonic Solids Viewer ---
elif section == "🌐 Platonic Solids Viewer":
    st.header("🌐 Platonic Solids Explorer")
    st.markdown("Choose a Platonic solid to view and rotate:")
    solid = st.selectbox("Pick a solid:", ["Tetrahedron", "Cube", "Octahedron", "Dodecahedron", "Icosahedron"])

    # Dictionary of vertex positions for rendering (simplified sample for demonstration)
    st.info(f"Interactive 3D viewers will be added soon. You selected: **{solid}**")

# --- Section 4: Real World Examples ---
elif section == "🧬 Real World Polyhedra":
    st.header("🧬 Polyhedra in the Real World")
    st.markdown("""
    - 🐝 **Beehives** use hexagonal tiling — an efficient polyhedral shape — to store honey.
    - 🦠 **Viruses** like HIV have icosahedral symmetry.
    - 🔬 **Carbon Nanostructures** form cages called buckyballs (fullerenes).
    - 🛡️ **Kevlar Body Armor** uses tetrahedral mesh geometry for strength.
    - 🏛️ **Architecture**: Domes and space frames often use polyhedral modules for stability.
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Buckyball_structure.png/600px-Buckyball_structure.png", caption="Carbon Fullerene (Buckyball)")

# --- Section 5: Quiz ---
elif section == "🧠 Quiz: Name That Shape!":
    st.header("🧠 Quiz: Name That Polyhedron")
    q1 = st.radio("Which shape has 8 faces and all are equilateral triangles?", ["Cube", "Octahedron", "Dodecahedron"])
    q2 = st.radio("Which shape has 12 pentagonal faces?", ["Icosahedron", "Cube", "Dodecahedron"])

    if st.button("Check Answers"):
        score = 0
        if q1 == "Octahedron":
            score += 1
        if q2 == "Dodecahedron":
            score += 1

        st.success(f"Your score: {score}/2")
        if score < 2:
            st.markdown("👉 Review the [Platonic Solids](https://en.wikipedia.org/wiki/Platonic_solid) section!")

# --- End ---
st.markdown("---")
st.markdown("""
<p style="text-align: center; color: #999; font-size: 0.9rem;">
All MathCraft lessons are part of the CognitiveCloud.ai initiative to empower STEM learners through engaging, standards-aligned technology.
</p>
""", unsafe_allow_html=True)
