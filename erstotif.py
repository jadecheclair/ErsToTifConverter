#!/usr/bin/env python3
"""
Simple ERS to GeoTIFF Converter

Convert ERMapper (.ers) files to GeoTIFF format.

Author: Jade Checlair
"""

import os
import sys
import rasterio
import numpy as np

def convert_ers_to_geotiff(ers_path, output_path=None):
    """
    Convert ERS file to GeoTIFF format
    
    Args:
        ers_path (str): Path to input ERS file
        output_path (str, optional): Path for output GeoTIFF
        
    Returns:
        str: Path to output file if successful, None if failed
    """
    print(f"Converting: {ers_path}")
    
    if not os.path.exists(ers_path):
        print(f"Error: File not found")
        return None
    
    if output_path is None:
        base_name = os.path.splitext(ers_path)[0]
        output_path = f"{base_name}.tif"
    
    try:
        with rasterio.open(ers_path) as src:
            print(f"Input: {src.width} x {src.height}, {src.count} band(s), {src.dtypes[0]}")
            
            # Read the data
            if src.count == 1:
                data = src.read(1, masked=True)
            else:
                data = src.read(masked=True)
            
            # Convert to 32-bit float with proper no-data handling
            profile = src.profile.copy()
            profile.update({
                'driver': 'GTiff',
                'dtype': 'float32',
                'compress': 'lzw',
                'nodata': np.nan
            })
            
            with rasterio.open(output_path, 'w', **profile) as dst:
                if src.count == 1:
                    dst.write(data.filled(np.nan).astype(np.float32), 1)
                else:
                    for i in range(src.count):
                        dst.write(data[i].filled(np.nan).astype(np.float32), i + 1)
                
                # Copy metadata
                dst.update_tags(**src.tags())
            
            # Basic stats
            if src.count == 1:
                valid_data = data.compressed()
                if len(valid_data) > 0:
                    print(f"Data range: {valid_data.min():.3f} to {valid_data.max():.3f}")
                    print(f"Valid pixels: {len(valid_data):,}")
            else:
                print(f"Multi-band file with {src.count} bands converted")
            
            print(f"Output: {output_path}")
            return output_path
            
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    """Simple command line usage"""
    if len(sys.argv) != 2:
        print("Usage: python ers_converter.py input.ers")
        print("Example: python ers_converter.py my_data.ers")
        print("Output will be saved as input.tif")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Auto-generate output filename (same name, .tif extension)
    output_file = os.path.splitext(input_file)[0] + ".tif"
    
    result = convert_ers_to_geotiff(input_file, output_file)
    
    if result:
        print("Conversion completed successfully")
    else:
        print("Conversion failed")
        sys.exit(1)

if __name__ == "__main__":
    main()
