# SPHEREx Mission: Sky Change Explorer

An interactive visual analytics and temporal tracking dashboard built for the **NASA Space Apps Challenge** using Python, Streamlit, NumPy, and Matplotlib.

## Overview
The **SPHEREx Mission: Sky Change Explorer** simulates near-infrared (NIR) time-series data to provide continuous spatiotemporal monitoring of the celestial sphere. Designed for astronomers and researchers, the application tracks variable stellar activity, high-latitude transient sources, and moving cosmic bodies across a 24-month mission lifecycle.

---

## Core Features
* **Observation Controls (Sidebar):** Toggle between discrete Near-Infrared bands (**Band 1**, **Band 2**, and **Band 3**) and step chronologically through a **1–24 month mission timeline slider**.
* **2D Sky View Grid:** High-resolution simulated spatial heatmap plotting surface brightness in **MegaJanskys per steradian (MJy/sr)** using a perceptually uniform `inferno` colormap.
* **Target Metadata Tracking:** Cosmic glassmorphism tracking card displaying real-time metadata (Target ID, tracking status, classification, and equatorial sky coordinates).
* **Light Curve Variation Analysis:** Quantitative temporal plotting tool charting flux intensity fluctuations over time to spot periodic variables and anomalous transient spikes.

---

## Tech Stack & Architecture
* **Python:** Core logic and data pipeline execution.
* **Streamlit:** Responsive web-based analytical dashboard interface.
* **NumPy:** High-performance multi-dimensional array operations and mock dataset synthesis.
* **Matplotlib:** Publication-ready scientific visualizations and spatial heatmaps.

