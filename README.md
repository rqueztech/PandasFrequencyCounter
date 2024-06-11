# Pandas Frequency Counter

This project is a simple yet powerful tool for counting the frequency of values in each column of a CSV file using the Pandas library. Users can interactively view the frequency counts of any column by either its name or index.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Features

- Load and analyze CSV files with tab-delimited columns.
- Interactive command-line interface to view frequency counts of any column.
- Toggle column names visibility for easier navigation.
- Clear the screen for a clean and clutter-free display.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- pandas library
- A CSV file named `sampledata.csv` with tab-delimited columns

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/rqueztech/PandasFrequencyCounter.git
    cd PandasFrequencyCounter
    ```

2. Install the required Python packages:

    ```bash
    pip install pandas
    ```

3. Ensure your CSV file is named `sampledata.csv` and is placed in the same directory as the script.

## Usage

Run the script using Python:

```bash
python frequency_counter.py
```

## Example

Here's a brief example of how to use the tool:

1. When you run the script, you'll be prompted to enter the column name or index you want to see the frequency count of.

    ```
    Enter the column name or index you want to see the frequency count of (or 'toggle' to toggle column names):
    ```

2. If you enter a column index or name, the frequency count of that column will be displayed.

    ```
    1 Column1                
    2 Column2                
    3 Column3                
    4 Column4                
    5 Column5                
    
    Enter the column name or index you want to see the frequency count of (or 'toggle' to toggle column names):
    ```

3. To toggle the display of column names, type `toggle`.

4. To clear the screen, type `clear`.

5. Press Enter after viewing the frequency count to continue.

## Contributing

Contributions are welcome! If you have suggestions for improvements or find any bugs, please open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License
This project is licensed under the [MIT License](LICENSE).

