# CRC Simulator - Agent Guidelines

## Commands
- Run: `python crc_simulator.py`
- No test framework configured
- No linting tools configured
- No build process required

## Code Style Guidelines
- Use snake_case for function and variable names
- Use descriptive variable names (e.g., `binary_message`, `generator_list`)
- Add docstrings for functions explaining purpose
- Use 4-space indentation
- Import standard library modules at top
- Handle binary string operations with explicit type conversion
- Use list comprehensions where appropriate for clarity
- Print output for user interaction, not logging
- Keep functions focused on single responsibility
- Use XOR operator (`^`) for bitwise operations in CRC calculation