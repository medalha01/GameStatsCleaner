# E-Sports Match Data Cleaner

## Overview

This repository contains tools for processing and cleaning datasets of E-Sports matches, specifically League of Legends (LoL) esports match data provided by Oracle's Elixir. These tools are designed to prepare data for machine learning applications, focusing primarily on match results. The functionality can be extended to handle other aspects such as player damage and dragon kills.

## Features

- **Data Treatment**: Selects and processes relevant columns from the raw dataset, such as game identifiers, team names, and match outcomes.
- **Null Cleaning**: Removes rows with missing values in crucial columns and replaces other missing values with a placeholder to maintain data integrity.
- **Sharding**: Splits the cleaned dataset into smaller chunks for easier handling and processing, useful for large datasets.
- **Data Aggregation**: Aggregates data by game ID to provide concise summaries of each match.

## Getting Started

1. **Clone the repository**: Begin by cloning this repo to your local machine.
2. **Data Source**: Download the required datasets from [Oracle's Elixir](https://oracleselixir.com/tools/downloads).
3. **Setup and Run**: Use the provided scripts to process your downloaded datasets.

## Usage

The main functionality is provided through a Python script that automates the cleaning and processing of datasets. It reads the CSV files for different years, applies cleaning operations, and shards the data into manageable files.

## Requirements

- Python 3.8+
- Pandas library

## Contributing

Contributions are welcome. Please open an issue to discuss proposed changes or open a pull request with your updates.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

