import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Create a window
window = tk.Tk()
window.title("Image Resizer")
window.geometry("400x250")

# Function to choose an image file
def choose_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    entry.delete(0, tk.END)  # Clear the entry field
    entry.insert(0, file_path)  # Set the chosen file path in the entry field

# Function to choose the output destination
def choose_output_destination():
    folder_path = filedialog.askdirectory()
    output_entry.delete(0, tk.END)  # Clear the entry field
    output_entry.insert(0, folder_path)  # Set the chosen folder path in the entry field

# Function to resize the image
def resize_image():
    # Get the selected file path and output destination from the entry fields
    file_path = entry.get()
    output_folder = output_entry.get()

    try:
        # Open the image using PIL
        image = Image.open(file_path)

        # Get the selected dimension
        selected_dimension = dimension_var.get()
        width, height = dimensions[selected_dimension]

        # Resize the image
        resized_image = image.resize((width, height))

        # Convert the image to RGB color mode
        resized_image = resized_image.convert("RGB")

        # Save the resized image to the output destination
        file_name = file_path.split("/")[-1]  # Extract the file name from the file path
        output_path = f"{output_folder}/{file_name}_resized.jpg"  # Construct the output path
        resized_image.save(output_path)

        # Show a success message box
        messagebox.showinfo("Image Resized", "The image has been successfully resized and saved.")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except PermissionError:
        messagebox.showerror("Error", "Permission denied to access the file.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to resize the image: {str(e)}")

# Predefined dimension choices
dimensions = {
    "1920 x 1080 pixels": (1920, 1080),
    "1280 x 720 pixels": (1280, 720),
    "250 x 250 pixels": (250, 250),
    "1200 x 630 pixels": (1200, 630)
}

# Create a frame for the image selection
image_frame = tk.Frame(window)
image_frame.pack(pady=10)

# Create a button to choose an image file
choose_button = tk.Button(image_frame, text="Choose Image", command=choose_image, width=15)
choose_button.pack(side=tk.LEFT, padx=(0, 5))

# Create an entry field for the chosen image file path
entry = tk.Entry(image_frame, width=30)
entry.pack(side=tk.LEFT)

# Create a frame for the output destination selection
output_frame = tk.Frame(window)
output_frame.pack(pady=10)

# Create a button to choose the output destination folder
choose_output_button = tk.Button(output_frame, text="Output Destination", command=choose_output_destination, width=15)
choose_output_button.pack(side=tk.LEFT, padx=(0, 5))

# Create an entry field for the chosen output destination folder
output_entry = tk.Entry(output_frame, width=30)
output_entry.pack(side=tk.LEFT)

# Create a frame for the dimension selection
dimension_frame = tk.Frame(window)
dimension_frame.pack(pady=10)

# Create a label for the dimension selection
dimension_label = tk.Label(dimension_frame, text="Choose Dimensions:")
dimension_label.pack(side=tk.LEFT)

# Create a dropdown menu for dimension selection
dimension_var = tk.StringVar(window)
dimension_var.set("1920 x 1080 pixels")  # Set initial dimension
dimension_menu = tk.OptionMenu(dimension_frame, dimension_var, *dimensions.keys())
dimension_menu.pack(side=tk.LEFT, padx=(5, 0))

# Create a button to trigger image resizing
resize_button = tk.Button(window, text="Resize Image", command=resize_image, padx=20, pady=10)
resize_button.pack(pady=20)

# Start the GUI event loop
window.mainloop()
