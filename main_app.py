# main_app.py - Changed Version

# No more os import needed

def greet(name):
    """Greets a user."""
    print(f"Hola, {name}!") # Changed greeting
    
def calculate_sum(a, b):
    """Calculates the sum of two numbers."""
    try:
        return a + b
    except Exception as e: # Broad exception
        print(f"Error calculating sum: {e}")
        return 0

if __name__ == "__main__":
    greet("Mundo")
    total = calculate_sum(10, 20)
    print(f"Total: {total}")
