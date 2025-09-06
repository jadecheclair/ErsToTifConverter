# ERS to GeoTIFF Converter

A simple Python tool to convert ERMapper (.ers) files to GeoTIFF format.

**Author:** Jade Checlair

## What it does

Converts ERMapper files to standard GeoTIFF format while preserving:
- Spatial coordinates and projections
- Data precision (32-bit float)
- Metadata and attributes
- Single or multi-band data

## Installation

You need Python with these packages:

```bash
pip install rasterio numpy
```

## Usage

Simple one-line conversion:

```bash
python ers_converter.py input_file.ers
```

This creates `input_file.tif` in the same directory.

### Examples

```bash
python ers_converter.py uranium_survey.ers
# Creates: uranium_survey.tif

python ers_converter.py magnetic_data.ers  
# Creates: magnetic_data.tif
```

## What you get

- **Same filename** with .tif extension
- **32-bit floating point** precision (no data loss)
- **LZW compression** (smaller file size)
- **Proper no-data handling** (NaN values)
- **All spatial information** preserved

## Requirements

- Python 3.7+
- rasterio
- numpy

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

**"File not found"**
- Check the file path and spelling
- Make sure the .ers file exists

**"Required package not found"**
- Install dependencies: `pip install rasterio numpy`

**"Conversion failed"**
- Check if the ERS file is corrupted
- Ensure you have write permissions in the output directory

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
