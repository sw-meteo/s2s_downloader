# S2S Hindcast Data Download Toolkit

## Overview

The Subseasonal-to-Seasonal (S2S) Prediction Project provides hindcast data from numerous global modeling centers via ECMWF, offering a convenient download interface and a relatively standardized data format. However, the diverse forecast run schedules (e.g., varying start dates based on day of week/month, fixed vs. on-the-fly model versions) can complicate multi-model research. 
It is particularly suitable for beginners who are not very familiar with meteorological data but need it to build data-driven models.

This toolkit is designed to automate the download of S2S hindcast data for a specified model from the ECMWF S2S database.

## Key Features

*   Retrieves all available hindcast data for a selected S2S model.
*   Manages forecast runs scheduled on specific days of the month or specific days of the week.
*   Handles both "fixed" model versions and "on-the-fly" hindcast strategy:
    *   For "on-the-fly" models: Downloads hindcasts for a defined range of past years relative to a specified `model_version_year`.
    *   For "fixed" models: Directly downloads the complete set of available hindcasts.
*   Retrieves data for the maximum available forecast lead time and all available ensemble members for hindcasts.

## Usage Instructions

### 1. Prerequisites

*   Ensure you have an active ECMWF account.
*   You must agree to the S2S data usage terms and conditions.
*   The `ecmwf-api-client` Python package must be installed and correctly configured with your ECMWF API key.

### 2. Configuration

Before running the main script (`retrieve.py`), you will likely need to adjust parameters in the following files:

*   **`retrieve.py`**:
    *   `origin`: Set the identifier for the desired S2S model (e.g., `"ecmf"`).
    *   `fdir_root`: Specify the root directory where the downloaded data will be saved.
    *   `order["area"]`: Define the geographical extent for data retrieval (format: North/West/South/East).

*   **`var_info.py`**:
    *   `var_name_list`: Customize the list of meteorological variables to be downloaded.
    *   `grib_code`: If adding new variables not already defined, ensure their GRIB codes are included.
    *   other key values in a similar way

*   **`origin_info.py`**:
    *   `model_version_year`: For models using the "on-the-fly" strategy, set this variable. It typically corresponds to the year for which the hindcast set is defined (e.g., using the previous year is a common practice).

### 3. Running the Script

Execute the `retrieve.py` script to begin the download process.

## Note

This toolkit was developed in 2022. The operational strategies and data availability for S2S models can change over time. If you encounter issues, it's advisable to check the latest documentation for the specific S2S model you are interested in. Contributions and suggestions for updates are welcome.

This README was language-polished by Gemini 2.5 Pro, and all generated content has been reviewed, corrected and confirmed by the author.
