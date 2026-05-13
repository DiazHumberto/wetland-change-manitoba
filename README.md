# Monitoring Wetland Vegetation Change in Manitoba Using Satellite Imagery and Python

## Overview

This project analyzes vegetation changes in Manitoba wetlands using satellite imagery and geospatial data processing techniques in Python. The workflow combines GIS, remote sensing, and environmental data science to monitor vegetation health over time using the Normalized Difference Vegetation Index (NDVI).

The project is designed as a portfolio piece demonstrating skills in:

- Geospatial analysis
- Remote sensing
- Python for environmental data science
- Raster and vector data processing
- GIS workflows
- Data visualization
- Dashboard development with Streamlit

---

## Objectives

- Process Sentinel-2 satellite imagery
- Compute NDVI for vegetation analysis
- Detect vegetation changes across time
- Visualize geospatial patterns and environmental trends
- Build an interactive dashboard for exploration

---

## Technologies Used

### Programming
- Python 3

### Geospatial Libraries
- geopandas
- rasterio
- rioxarray

### Data Analysis
- numpy
- pandas

### Visualization
- matplotlib
- folium

### Dashboard
- Streamlit

---

## Project Structure

```text
wetland-change-manitoba/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│   ├── 01_ndvi.ipynb
│   ├── 02_clip_and_ndvi.ipynb
│
├── src/
│   ├── data_processing.py
│   ├── ndvi.py
│   ├── visualization.py
│
├── app/
│   └── streamlit_app.py
│
├── outputs/
│   ├── maps/
│   ├── figures/
│
├── requirements.txt
├── README.md
└── .gitignore