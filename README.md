# S2S Hindcast Data Download Toolkit

## Overview

The Subseasonal-to-Seasonal (S2S) Prediction Project provides hindcast data from numerous global modeling centers via ECMWF, offering a convenient download interface and a relatively standardized data format. However, the diverse forecast run schedules (e.g., varying start dates based on day of week/month, fixed vs. on-the-fly model versions) can complicate multi-model research. 
It is particularly suitable for beginners who are not very familiar with meteorological data but need it to build data-driven models.

This toolkit is designed to automate the download of S2S hindcast data for a specified model from the ECMWF S2S database.

## Key Features

*   Retrieves all available hindcast data for a selected S2S model.
*   Manages forecast runs scheduled on specific days of the month or specific days of the week.
*   Handles both "fixed" model versions and "on-the-fly" hindcast strategy.
*   Retrieves data for the maximum available forecast lead time and all available ensemble members.
*   Supports downloading both hindcast and real‐time data out of the box.

## Usage Instructions

### 1. Prerequisites

*   Ensure you have an active ECMWF account.
*   You must agree to the S2S data usage terms and conditions.
*   The `ecmwf-api-client` Python package must be installed and correctly configured with your ECMWF API key.

### 2. Configuration

Before running the main script (`retrieve.py`), you will likely need to adjust parameters in the following files:

*   **`basic_info.py`**:
    *   `origin`: Set the identifier for the desired S2S model (e.g., `"ecmf"`).
    *   `fdir_root`: Specify the root directory where the downloaded data will be saved.
    *   `order["area"]`: Define the geographical extent for data retrieval (format: North/West/South/East).
    *   `model_version_year`: For models using the "on-the-fly" strategy, set this variable. It typically corresponds to the year for which the hindcast set is defined (e.g., using the previous year is a common practice).
    *   `var_name_list`: Customize the list of meteorological variables to be downloaded.

*   **`var_info.py`**:
    *   `grib_code`: If adding new variables not already defined, ensure their GRIB codes are included.
    *   other key values in a similar way

## What's New in This Update
*   Downloads both hindcast and real‐time datasets.
*   Compatible with operational strategy switches **mid‐year** (mixed‐strategy support).
*   Handles missing step0 data, leap‐day fallback and other edge cases for improved “plug‐and‐play” experience.

## Note

This toolkit was developed in 2022 and has been continuously updated.  
The operational strategies and data availability for S2S models have evolved since then.  
If you encounter issues, it's advisable to check the latest documentation for the specific S2S model you are interested in.
