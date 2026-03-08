# Production Test

This project is an automated testing framework designed to run on a Raspberry Pi for validating electronic products during manufacturing. It interfaces with devices under test (DUT) using ST-Link and Serial connections.

## Features

- **Automated Testing**: Runs a sequence of tests defined in `tests.py`.
- **ST-Link Integration**: Uses `pystlink` to communicate with STM32 microcontrollers, enabling programming and verification.
- **Serial Communication**: Interacts with the DUT via serial ports for functional testing (`ser.py`).
- **Configuration**: Test parameters and limits are configurable via `config.ini`.
- **Logging**: Results are saved to `results.ini` or displayed in the console.

## Project Structure

- `main.py`: The entry point for the testing application.
- `tests.py`: Contains the specific test cases to be executed.
- `checks.py`: Helper functions for validating test results.
- `config.ini`: Configuration file for test thresholds, port settings, etc.
- `pystlink/`: Library for ST-Link communication.
- `ranges.py`: Defines acceptable value ranges for test measurements.

## Usage

1. **Setup**:
   - Connect the Raspberry Pi to the DUT via ST-Link and/or Serial.
   - Ensure Python 3 is installed along with dependencies (e.g., `pyserial`, `usb`).
2. **Configuration**:
   - Edit `config.ini` to match the specifications of the product being tested.
3. **Execution**:
   - Run the main script:
     ```bash
     python3 main.py
     ```
   - Follow the on-screen prompts to start the test cycle.

## Requirements

- Raspberry Pi (or Linux machine)
- Python 3.x
- `libusb` (for ST-Link access)
- ST-Link V2 programmer
