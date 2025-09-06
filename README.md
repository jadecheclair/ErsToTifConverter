# ERS to GeoTIFF Converter

A simple Python tool to convert ERMapper (.ers) files to GeoTIFF format.

**Author:** Jade Checlair

## What it does

Converts ERMapper files to standard GeoTIFF format while preserving:
- Spatial coordinates and projections
- Data precision (32-bit float)
- Metadata and attributes
- Single or multi-band data

## Getting Started

### Step 1: Download this tool
- Click the green "Code" button above, then "Download ZIP"
- Extract the ZIP file to your computer
- You'll need the file called `ers_converter.py`

### Step 2: Install Python requirements
You need Python with these packages:

```bash
pip install rasterio numpy
```

### Step 3: Convert your ERS file
Open your terminal/command prompt and navigate to where you saved `ers_converter.py`, then run:

```bash
python ers_converter.py YOUR_ACTUAL_FILENAME.ers
```

**Important:** Replace `YOUR_ACTUAL_FILENAME.ers` with the real name of your ERS file!

## What you get

- **Same filename** with .tif extension instead of .ers
- **32-bit floating point** precision (no data loss)
- **LZW compression** (smaller file size)
- **Proper no-data handling** (NaN values)
- **All spatial information** preserved

## Requirements

- Python 3.7 or newer
- rasterio package
- numpy package

## Why use this?

ERMapper files (.ers) aren't supported by many modern GIS tools. This converter creates standard GeoTIFF files that work everywhere:

- QGIS
- ArcGIS
- Python/R analysis
- Web mapping tools
- Any GDAL-compatible software

## File types supported

- Single-band ERS files (like individual survey measurements)
- Multi-band ERS files (like RGB or multi-spectral data)
- Any ERMapper format that rasterio can read

## Troubleshooting

**"Usage: python ers_converter.py input.ers"**
- You forgot to specify your ERS file name
- Make sure to replace `input.ers` with your actual file name

**"File not found"**
- Check the file path and spelling
- Make sure the .ers file exists in the same folder as the Python script
- Or provide the full path to your ERS file

**"File not recognized as being in a supported file format"**
- ERS files often come with associated files (.ers.gi etc)
- Make sure ALL files that came with your .ers file are in the same folder
- Example: if you have `data.ers`, you might also need `data.ers.gi` or `data.ers.xml`
- Check that you have all the files that came with your ERS data

**"Required package not found"**
- Install dependencies: `pip install rasterio numpy`

**"Conversion failed"**
- Check if the ERS file is corrupted
- Ensure you have write permissions in the output directory

## For non-technical users

Don't worry if you're not familiar with programming! Here's the simple process:

1. Download this tool (the `ers_converter.py` file)
2. Install Python and the required packages
3. Put your ERS file AND all associated files in the same folder as the Python script
   - This includes any .ecw, .dat, .hdr files or other files with the same name
   - Example: if you have `survey.ers`, also copy `survey.ecw`, `survey.dat`, etc.
4. Open terminal/command prompt in that folder
5. Type: `python ers_converter.py` followed by your ERS file name
6. Press Enter and wait for "Conversion completed successfully"

## Technical details

The converter:
- Reads ERS files using rasterio/GDAL
- Converts data to 32-bit float (preserves precision)
- Uses LZW compression (lossless)
- Sets NaN for no-data values
- Copies all metadata and spatial reference information

## License

MIT License - feel free to use and modify.

## Contributing

Found a bug or want to improve something? Open an issue or send me a note at jade.checlair@gmail.com
