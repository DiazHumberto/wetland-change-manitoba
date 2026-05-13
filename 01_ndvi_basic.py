import rasterio
import numpy as np
import matplotlib.pyplot as plt

# ---- FILE PATHS (CHANGE THESE) ----
red_path = "data/raw/B04.tif"   # Red band
nir_path = "data/raw/B08.tif"   # NIR band

# ---- LOAD BANDS ----
with rasterio.open(red_path) as red_src:
    red = red_src.read(1).astype(float)
    profile = red_src.profile

with rasterio.open(nir_path) as nir_src:
    nir = nir_src.read(1).astype(float)

# ---- AVOID DIVISION ERRORS ----
np.seterr(divide='ignore', invalid='ignore')

# ---- COMPUTE NDVI ----
ndvi = (nir - red) / (nir + red)

# ---- CLEAN VALUES ----
ndvi = np.clip(ndvi, -1, 1)

# ---- PLOT ----
plt.figure(figsize=(8, 6))
plt.imshow(ndvi, cmap='RdYlGn')
plt.colorbar(label='NDVI')
plt.title('NDVI - Manitoba Area')
plt.axis('off')
plt.show()