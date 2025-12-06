import time
import random
import sys


def animate_text(text, delay=0.03):
    """Animate text printing character by character"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def animate_progress(message, duration=2):
    """Show animated progress with dots"""
    animate_text(message, delay=0.05)
    for _ in range(duration):
        time.sleep(0.5)
        sys.stdout.write(".")
        sys.stdout.flush()
    print()


def visualize_xor_operation(dividend, generator, position):
    """Visualize XOR operation at current position"""
    print(f"\nPosition {position}:")
    print(f"Dividend: {dividend}")
    print(f"Generator: {' ' * position}{generator}")
    
    result = list(dividend)
    gen_list = list(generator)
    
    for i in range(len(gen_list)):
        if position + i < len(result):
            xor_result = int(result[position + i]) ^ int(gen_list[i])
            result[position + i] = str(xor_result)
    
    print(f"Result:   {''.join(result)}")
    time.sleep(1)
    return ''.join(result)


def main():
    print("=" * 75)
    print("   __________  ______   _____ ______  _____  ____    ___  __________  ____ ")
    print(r"  / ____/ __ \/ ____/  / ___//  _/  |/  / / / / /   /   |/_  __/ __ \/ __ \ ")
    print(r" / /   / /_/ / /       \__ \ / // /|_/ / / / / /   / /| | / / / / / / /_/ /")
    print(r"/ /___/ _, _/ /___    ___/ // // /  / / /_/ / /___/ ___ |/ / / /_/ / _, _/ ")
    print(r"\____/_/ |_|\____/   /____/___/_/  /_/\____/_____/_/  |_/_/  \____/_/ |_|  ")
    print()
    print("=" * 75, 'by Ashif')
    
    animate_text("\n📤 SENDER SIDE", 0.05)
    message = input("\nEnter the message you want to send: ")
    generator = input("Enter the generator polynomial (e.g., 1101): ")
    
    print("\n" + "-" * 40)
    animate_text("🔄 CONVERTING MESSAGE TO BINARY...", 0.03)
    binary_message = string_to_binary(message)
    print(f"Original message: '{message}'")
    print(f"Binary representation: {binary_message}")
    
    print("\n" + "-" * 40)
    animate_text("🧮 CALCULATING CRC...", 0.03)
    time.sleep(1)
    
    transmitted_data, crc_remainder = crc_calculator_with_animation(binary_message, generator)
    
    print("\n" + "-" * 40)
    animate_text("📡 TRANSMITTING DATA...", 0.03)
    animate_progress("Sending message to receiver", 3)
    
    # Simulate transmission with possible error
    error_probability = 0.3  # 30% chance of error for demonstration
    has_error = random.random() < error_probability
    
    if has_error:
        animate_text("⚠️  NOISE DETECTED DURING TRANSMISSION!", 0.05)
        received_data = introduce_error(transmitted_data)
    else:
        animate_text("✅ Transmission completed successfully!", 0.05)
        received_data = transmitted_data
    
    print("\n" + "=" * 60)
    animate_text("📥 RECEIVER SIDE", 0.05)
    print("=" * 60)
    
    print(f"Received data: {received_data}")
    
    print("\n" + "-" * 40)
    animate_text("🔍 VERIFYING DATA INTEGRITY...", 0.03)
    time.sleep(1)
    
    error_detected = verify_crc_with_animation(received_data, generator)
    
    print("\n" + "=" * 60)
    animate_text("📊 TRANSMISSION RESULT", 0.05)
    print("=" * 60)
    
    if error_detected:
        animate_text("❌ ERROR FOUND!", 0.05)
        animate_text("🔄 REQUESTING RESEND...", 0.05)
        animate_progress("Resending message", 2)
        animate_text("✅ Message received successfully after resend!", 0.05)
    else:
        animate_text("✅ NO ERRORS DETECTED!", 0.05)
        animate_text("🎉 MESSAGE RECEIVED SUCCESSFULLY!", 0.05)
    
    print(f"\nOriginal message: '{message}'")
    print(f"CRC remainder: {crc_remainder}")
    print(f"Generator polynomial: {generator}")


def string_to_binary(message):
    """Convert string message to binary representation"""
    binary_value = []
    for char in message:
        ascii_value = ord(char)
        binary_char = bin(ascii_value)[2:].zfill(8)
        binary_value.append(binary_char)
    return "".join(binary_value)


def crc_calculator_with_animation(binary_message, generator):
    """Calculate CRC with step-by-step animation"""
    num_zeros = len(generator) - 1
    extended_data = binary_message + "0" * num_zeros
    
    print(f"Extended data (with {num_zeros} zeros): {extended_data}")
    print(f"Generator polynomial: {generator}")
    print(f"Generator length: {len(generator)} bits")
    
    dividend = list(extended_data)
    generator_list = list(generator)
    n = len(generator_list)
    
    animate_text("\n🔄 Performing CRC division steps:", 0.03)
    time.sleep(1)
    
    for i in range(len(dividend) - n + 1):
        if dividend[i] == "1":
            current_pos = i
            current_dividend = ''.join(dividend)
            
            # Show current step
            print(f"\nStep {i + 1}:")
            print(f"Current dividend: {current_dividend}")
            print(f"XOR with generator at position {current_pos}")
            
            # Perform XOR operation
            for j in range(n):
                xor_result = int(dividend[current_pos + j]) ^ int(generator_list[j])
                dividend[current_pos + j] = str(xor_result)
            
            result_after_xor = ''.join(dividend)
            print(f"Result after XOR: {result_after_xor}")
            time.sleep(0.8)
    
    remainder = ''.join(dividend[-(n - 1):])
    transmitted_data = binary_message + remainder
    
    print(f"\n🧮 CRC Remainder: {remainder}")
    print(f"📤 Transmitted data: {transmitted_data}")
    
    return transmitted_data, remainder


def introduce_error(data):
    """Introduce random bit error for demonstration"""
    data_list = list(data)
    error_pos = random.randint(0, len(data_list) - 1)
    original_bit = data_list[error_pos]
    data_list[error_pos] = '1' if original_bit == '0' else '0'
    
    print(f"🔧 Error introduced at position {error_pos}: {original_bit} → {data_list[error_pos]}")
    return ''.join(data_list)


def verify_crc_with_animation(received_data, generator):
    """Verify CRC at receiver side with animation"""
    n = len(generator)
    data_without_crc = received_data[:-(n - 1)]
    received_crc = received_data[-(n - 1):]
    
    print(f"Data part: {data_without_crc}")
    print(f"Received CRC: {received_crc}")
    
    # Calculate CRC of received data
    dividend = list(received_data)
    generator_list = list(generator)
    
    animate_text("\n🔄 Performing CRC verification:", 0.03)
    time.sleep(1)
    
    for i in range(len(dividend) - n + 1):
        if dividend[i] == "1":
            for j in range(n):
                xor_result = int(dividend[i + j]) ^ int(generator_list[j])
                dividend[i + j] = str(xor_result)
    
    remainder = ''.join(dividend[-(n - 1):])
    print(f"Calculated remainder: {remainder}")
    
    # Check if all zeros (no error)
    is_all_zeros = all(bit == '0' for bit in remainder)
    
    if is_all_zeros:
        animate_text("✅ Remainder is all zeros - No errors detected!", 0.05)
        return False
    else:
        animate_text("❌ Remainder is not all zeros - Error detected!", 0.05)
        return True


if __name__ == "__main__":
    main()
