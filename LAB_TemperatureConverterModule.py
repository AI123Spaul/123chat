# Temperature Converter using Functions and Modules (Single File Version)

# --- Module Section ---
def celsius_to_fahrenheit(c):
"""Convert Celsius to Fahrenheit"""
return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
"""Convert Fahrenheit to Celsius"""
return (f - 32) * 5/9

# --- Main Program Section ---
def main():
print("Suvadip's Temperature Converter")
print("1# Celsius to Fahrenheit")
print("2# Fahrenheit to Celsius")

choice = input("Choose conversion (1 or 2): ")

try:
if choice == "1":
c = float(input("Suvadip requests to enter temperature in Celsius: "))
f = celsius_to_fahrenheit(c)
print(f"{c}°C is equal to {f:.2f}°F")
elif choice == "2":
f = float(input("Suvadip requests to enter temperature in Fahrenheit: "))
c = fahrenheit_to_celsius(f)
print(f"{f}°F is equal to {c:.2f}°C")
else:
print("Invalid choice. Please select 1 or 2.")
except ValueError:
print("Invalid input. Please enter numeric values.")

# Entry point
if __name__ == "__main__":
main()