# CRC Simulator - Error Detection Demonstration

An interactive Python simulator that demonstrates how Cyclic Redundancy Check (CRC) works for error detection in data communication.

## 🎯 What This Simulator Does

This program provides a complete visual demonstration of the CRC error detection process:

1. **Sender Side**: Converts your message to binary and calculates CRC
2. **Transmission**: Simulates data transmission with possible noise/errors
3. **Receiver Side**: Verifies data integrity using CRC verification
4. **Error Handling**: Detects errors and requests retransmission if needed

## 🚀 How to Run

```bash
python crc_simulator.py
```

## 📋 Requirements

- Python 3.x
- No external dependencies required (uses only standard library)

## 🎮 Usage

1. Run the program
2. Enter any message you want to send
3. Enter a generator polynomial (try `1101` for starters)
4. Watch the animated CRC calculation and transmission process

## 🔧 How It Works

### CRC Calculation Process
1. **Binary Conversion**: Your message is converted to 8-bit binary ASCII
2. **Extension**: Data is extended with zeros (generator length - 1)
3. **Division**: Polynomial division using XOR operations
4. **Remainder**: The final remainder becomes the CRC checksum
5. **Transmission**: Original data + CRC is sent to receiver

### Error Detection
- Receiver performs the same division on received data
- If remainder is all zeros → No errors detected
- If remainder is non-zero → Error detected, request resend

## 🎨 Features

- **Animated Calculations**: Step-by-step visualization of CRC division
- **Visual XOR Operations**: See exactly how bits are processed
- **Transmission Simulation**: Random error injection (30% probability)
- **Interactive Interface**: User-friendly prompts and progress indicators
- **Complete Communication Flow**: From sender to receiver with error handling

## 📚 Example Generator Polynomials

- `1101` (x³ + x² + 1) - CRC-3
- `1011` (x³ + x + 1) - CRC-3
- `10011` (x⁴ + x + 1) - CRC-4
- `110011` (x⁵ + x⁴ + x + 1) - CRC-5

## 🧮 Technical Details

The simulator implements the standard CRC algorithm:
- Uses polynomial division with XOR operations
- Supports any generator polynomial
- Demonstrates real-world error detection scenarios
- Shows both calculation and verification processes

## 👨‍💻 Author

**Ashif** - [GitHub Profile](https://github.com/lordhanya)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note**: This educational simulator demonstrates the fundamental concepts of CRC error detection used in real-world communication protocols like Ethernet, USB, and many others.