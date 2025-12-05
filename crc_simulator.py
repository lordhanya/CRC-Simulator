def calculate_crc(data, generator):
    """Calculate CRC remainder"""
    # Convert strings to lists for easier manipulation
    data_bits = list(data)
    gen_bits = list(generator)

    # Append zeros to data (degree of generator - 1)
    zeros_to_add = len(gen_bits) - 1
    extended_data = data_bits + ["0"] * zeros_to_add

    # Perform binary division
    dividend = extended_data.copy()

    for i in range(len(data_bits)):
        if dividend[i] == "1":
            # XOR operation
            for j in range(len(gen_bits)):
                dividend[i + j] = str(int(dividend[i + j]) ^ int(gen_bits[j]))

    # Extract remainder (last zeros_to_add bits)
    remainder = dividend[-zeros_to_add:]
    return "".join(remainder)


def add_crc_to_data(data, generator):
    """Add CRC to data for transmission"""
    crc = calculate_crc(data, generator)
    transmitted_data = data + crc
    return transmitted_data


def check_received_data(received_data, generator):
    """Check if received data has errors"""
    # Calculate CRC on received data
    remainder = calculate_crc(received_data, generator)

    # If remainder is all zeros, no error
    if all(bit == "0" for bit in remainder):
        return True  # No error
    else:
        return False  # Error detected


def simulate_error(data, error_position):
    """Simulate transmission error"""
    if error_position >= len(data):
        return data  # Position out of range

    # Convert to list, flip bit, convert back
    data_list = list(data)
    original_bit = data_list[error_position]
    data_list[error_position] = "1" if original_bit == "0" else "0"

    return "".join(data_list)


def main():
    """Main program interface"""
    print("=== CRC Error Detection Simulator ===")
    print()

    # Get user input
    data = input("Enter data bits: ")
    generator = input("Enter generator polynomial: ")

    print(f"\nData: {data}")
    print(f"Generator: {generator}")
    print()

    # Step 1: Calculate CRC
    crc = calculate_crc(data, generator)
    print(f"CRC calculated: {crc}")

    # Step 2: Create transmitted data
    transmitted_data = add_crc_to_data(data, generator)
    print(f"Transmitted data: {transmitted_data}")
    print()

    # Step 3: Simulate error
    print("Simulating transmission error...")
    error_position = 2  # Flip 3rd bit (index 2)
    received_with_error = simulate_error(transmitted_data, error_position)
    print(f"Received data (with error): {received_with_error}")

    # Step 4: Check for errors
    has_error = not check_received_data(received_with_error, generator)
    print(f"Error detected: {'Yes' if has_error else 'No'}")
    print()

    # Step 5: Check without error
    print("Checking without error...")
    no_error = not check_received_data(transmitted_data, generator)
    print(f"Error detected: {'Yes' if no_error else 'No'}")


if __name__ == "__main__":
    main()
