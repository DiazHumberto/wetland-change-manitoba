# Monitoring Wetland Vegetation Change in Manitoba Using Satellite Imagery and Python

## Overview

This project analyzes vegetation changes in Manitoba wetlands using satellite imagery and geospatial data processing techniques in Python. The workflow combines GIS, remote sensing, and environmental data science to monitor vegetation health over time using the Normalized Difference Vegetation Index (NDVI).

The project is being developed as a portfolio piece demonstrating practical skills in geospatial analytics, remote sensing, environmental monitoring, and Python-based data science.

---

## Objectives

* Process Sentinel-2 satellite imagery
* Compute NDVI for vegetation analysis
* Detect vegetation changes across time
* Visualize geospatial patterns and environmental trends
* Develop reproducible geospatial workflows
* Build an interactive dashboard for environmental monitoring

---

## Why This Project Matters

Wetlands play a critical role in biodiversity conservation, water regulation, carbon storage, and climate resilience. Monitoring vegetation changes through satellite imagery provides valuable insights into ecosystem health and supports evidence-based environmental decision-making.

This project demonstrates how open geospatial data and Python-based analytics can be used to monitor environmental change at regional scales.

---

## Study Area

The initial study area focuses on wetland and vegetation dynamics in Manitoba, Canada, with an emphasis on regions surrounding Winnipeg and the Lake Winnipeg watershed.

Future versions of the project may expand to additional ecologically significant regions in Manitoba to support broader environmental monitoring and change detection analyses.

---

## Technologies Used

### Programming

* Python 3

### Geospatial Libraries

* GeoPandas
* Rasterio
* Rioxarray

### Data Analysis

* NumPy
* Pandas

### Visualization

* Matplotlib
* Folium

### Dashboard Development

* Streamlit

### Version Control

* Git
* GitHub

---

## Skills Demonstrated

This project demonstrates practical experience in:

* Remote Sensing
* GIS Analysis
* Raster Data Processing
* Vector Data Processing
* Coordinate Reference Systems (CRS)
* Environmental Data Science
* Python Development
* Data Visualization
* Spatial Analysis
* Streamlit Dashboard Development
* Git and GitHub Version Control

---

## Data Sources

### Satellite Imagery

Sentinel-2 imagery obtained from:

* Copernicus Open Access Hub
* USGS EarthExplorer

### Geospatial Boundaries

Administrative and environmental datasets obtained from:

* Manitoba Open Data Portal
* Government of Canada Open Data

---

## NDVI Methodology

The project uses the Normalized Difference Vegetation Index (NDVI):

```text
NDVI = (NIR - Red) / (NIR + Red)
```

Where:

* NIR = Near Infrared Band (Sentinel-2 B08)
* Red = Red Band (Sentinel-2 B04)

Typical interpretation:

| NDVI Value | Interpretation              |
| ---------- | --------------------------- |
| < 0        | Water, clouds, snow         |
| 0 - 0.2    | Bare soil or urban surfaces |
| 0.2 - 0.5  | Sparse vegetation           |
| > 0.5      | Dense healthy vegetation    |

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
```

---

## Current Workflow

### Phase 1 — Environment Setup

* Configure Python virtual environment
* Install geospatial libraries
* Organize project structure

### Phase 2 — NDVI Computation

* Load Sentinel-2 imagery
* Extract Red and NIR bands
* Compute NDVI
* Generate vegetation maps

### Phase 3 — GIS Processing

* Load vector boundaries
* Reproject coordinate systems
* Clip rasters to study area
* Create focused analysis regions

### Phase 4 — Change Detection (In Progress)

* Compare vegetation conditions across multiple years
* Identify areas of degradation or improvement
* Generate change maps and statistics

### Phase 5 — Dashboard Development (Planned)

* Interactive map visualization
* NDVI exploration tools
* Environmental monitoring dashboard using Streamlit

---

## Future Improvements

* Multi-year time series analysis
* Machine learning-based land cover classification
* Automated satellite imagery download pipeline
* Climate and weather data integration
* Wetland health indicators
* Cloud deployment of dashboard
* Automated reporting workflow

---

## Setup Instructions

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install rasterio geopandas rioxarray matplotlib numpy pandas streamlit
```

### Save Environment

```bash
pip freeze > requirements.txt
```

---

## Expected Outputs

* NDVI vegetation maps
* Change detection maps
* Environmental monitoring visualizations
* Interactive Streamlit dashboard
* Reproducible geospatial workflow

---

## Author

### Humberto Eleazar Díaz Maridueña

Environmental Engineer and Data Professional with experience in:

* Environmental Science
* Ecological Restoration
* Geographic Information Systems (GIS)
* Artificial Intelligence and Machine Learning
* Data Science and Statistical Analysis
* Python Programming

Professional interests include environmental monitoring, geospatial analytics, remote sensing, and the application of AI to sustainability and conservation challenges.

Location: Winnipeg, Manitoba, Canada

---

## License

This project is intended for educational, research, and portfolio purposes.
