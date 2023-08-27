import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Create a window
window = tk.Tk()
window.title("Image Resizer")
window.geometry("550x500")
window.iconbitmap("resizer.ico")  # Set the path to your icon file

# Load the PNG image
image = Image.open("..\Images\gradient 2.png")
photo = ImageTk.PhotoImage(image)

# Create a label widget to hold the image
background_label = tk.Label(window, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add an image label at the top center
# Replace with the actual path to your image file
image_path = r"..\Images\Image Resizer.png"
image = Image.open(image_path)
# Replace width and height with your desired dimensions
image = image.resize((130, 120))
image = ImageTk.PhotoImage(image)
image_label = tk.Label(window, image=image)
image_label.pack(pady=(15, 0))

def choose_image():
    """Open a file dialog to choose multiple image files."""
    file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    if file_paths:
        entry.delete(0, tk.END)
        entry.insert(0, ";".join(file_paths))  # Join the selected file paths with semicolon

# Function to choose the output destination
def choose_output_destination():
    """Open a folder dialog to choose the output destination folder."""
    folder_path = filedialog.askdirectory()
    if folder_path:
        output_entry.delete(0, tk.END)  # Clear the entry field
        output_entry.insert(0, folder_path)  # Set the chosen folder path in the entry field

from tqdm import tqdm  # Import the tqdm library

# Function to resize multiple images with a progress bar
def resize_multiple_images_with_progress():
    """Resize multiple selected images and save them to the output destination with a progress bar."""
    file_paths = entry.get().split(';')
    output_folder = output_entry.get()

    try:
        with tqdm(total=len(file_paths), desc="Resizing Images", unit="image") as progress_bar:
            for file_path in file_paths:
                image = Image.open(file_path)

                selected_dimension = dimension_var.get()
                if selected_dimension == "Custom":
                    custom_width = custom_width_entry.get()
                    custom_height = custom_height_entry.get()

                    if not custom_width.isdigit() or not custom_height.isdigit():
                        raise ValueError("Custom width and height must be numeric.")

                    width = int(custom_width)
                    height = int(custom_height)
                else:
                    width, height = dimensions[selected_dimension]

                resized_image = image.resize((width, height))

                file_name = file_path.split("/")[-1]
                output_path = f"{output_folder}/{file_name}_resized.{format_var.get()}"
                resized_image.save(output_path)

                progress_bar.update(1)

        messagebox.showinfo("Images Resized", "All images have been successfully resized and saved.")
    except Exception as e:
        messagebox.showerror("Error", "An error occurred: {}".format(str(e)))


# Predefined dimension choices with descriptions
dimensions = {
    "3000 x 3000 (Album Cover Art)": (3000, 3000),  # Album Cover Art
    "1920 x 1080 (Full HD)": (1920, 1080),  # HD Wallpaper
    "1280 x 720 (HD)": (1280, 720),  # HD Wallpaper
    "256 x 256 (Icon)": (256, 256),  # Icon
    "16 x 16 (Favicon)": (16, 16),  # Favicon
}

# Create a frame for the image selection
image_frame = tk.Frame(window)
image_frame.pack(fill="x", expand=True, pady=10)

# Create a button to choose an image file
choose_button = tk.Button(
    image_frame,
    text="Choose Image",
    bg="#E7E9EA",
    fg="#20211A",
    justify="center",
    font=("Tahoma", 11),
    command=choose_image,
)
choose_button.pack(side=tk.LEFT, fill="both", expand=True, padx=(10, 5))

# Create an entry field for the chosen image file path
entry = tk.Entry(image_frame, width=48)
entry.pack(side=tk.LEFT, fill="both", expand=True, padx=(0, 10))

# Create a frame for the output destination selection
output_frame = tk.Frame(window)
output_frame.pack(fill="x", expand=True, pady=10)

# Create a button to choose the output destination folder
choose_output_button = tk.Button(
    output_frame,
    text="Save Folder",
    bg="#E7E9EA",
    fg="#20211A",
    justify="center",
    font=("Tahoma", 11),
    command=choose_output_destination,
)
choose_output_button.pack(side=tk.LEFT, fill="both", expand=True, padx=(10, 5))

# Create an entry field for the chosen output destination folder
output_entry = tk.Entry(output_frame, width=45)
output_entry.pack(side=tk.LEFT, fill="both", expand=True, padx=(0, 10))

# Create a frame for the dimension selection
dimension_frame = tk.Frame(window)
dimension_frame.pack(fill="both", expand=True, pady=(10, 30))

# Create a label for the dimension selection
dimension_label = tk.Label(
    dimension_frame,
    text="Choose Dimensions:",
    bg="#E7E9EA",
    fg="#20211A",
    justify="center",
    font=("Tahoma", 11),
)
dimension_label.pack(side=tk.LEFT, fill="both", expand=True, padx=(10, 0))

# Create a dropdown menu for dimension selection
dimension_var = tk.StringVar(window)
dimension_var.set("3000 x 3000 (Album Cover Art)")  # Set initial dimension
dimension_menu = tk.OptionMenu(
    dimension_frame, dimension_var, *list(dimensions.keys()) + ["Custom"]
)
dimension_menu.pack(side=tk.LEFT, fill="both", expand=True, padx=(5, 10))

# Create a frame for custom dimension input
custom_dimension_frame = tk.Frame(window)

# Create labels and entry fields for custom width and height
custom_width_label = tk.Label(
    custom_dimension_frame,
    text="Custom Width:",
    bg="#E7E9EA",
    fg="#20211A",
    justify="center",
    font=("Tahoma", 11),
)
custom_width_label.pack(side=tk.LEFT, fill="both", expand=True, padx=(10, 5))

custom_width_entry = tk.Entry(custom_dimension_frame, width=10)
custom_width_entry.pack(side=tk.LEFT, fill="both", expand=True, padx=(0, 5))

custom_height_label = tk.Label(
    custom_dimension_frame,
    text="Custom Height:",
    bg="#E7E9EA",
    fg="#20211A",
    justify="center",
    font=("Tahoma", 11),
)
custom_height_label.pack(side=tk.LEFT, fill="both", expand=True, padx=(5, 5))

custom_height_entry = tk.Entry(custom_dimension_frame, width=10)
custom_height_entry.pack(side=tk.LEFT, fill="both", expand=True, padx=(0, 10))

# Create a frame for format selection
format_frame = tk.Frame(window)
format_frame.pack(fill="both", expand=True, pady=(10, 30))

# Create a label for the format selection
format_label = tk.Label(
    format_frame,
    text="Choose Format:",
    bg="#E7E9EA",
    fg="#20211A",
    justify="center",
    font=("Tahoma", 11),
)
format_label.pack(side=tk.LEFT, fill="both", expand=True, padx=(10, 0))

# Create a dropdown menu for format selection
format_var = tk.StringVar(window)
format_var.set("png")  # Set initial format
format_menu = tk.OptionMenu(format_frame, format_var, "gif", "ico", "jpeg", "jpg", "png")
format_menu.pack(side=tk.LEFT, fill="both", expand=True, padx=(5, 10))

# Add the custom dimension frame to the window
custom_dimension_frame.pack(fill="both", expand=True)

# Function to show or hide the custom dimension frame based on the selected dimension
def toggle_custom_dimension(*args):
    """Toggle the visibility of the custom dimension frame based on the selected dimension."""
    selected_dimension = dimension_var.get()
    if selected_dimension == "Custom":
        custom_dimension_frame.pack(fill="both", expand=True)
    else:
        custom_dimension_frame.pack_forget()

# Bind the toggle_custom_dimension function to the dimension variable
dimension_var.trace("w", toggle_custom_dimension)

# Create a button to resize the images with a progress bar
resize_button = tk.Button(
    window,
    text="Resize Images",
    bg="#E7E9EA",
    fg="#20211A",
    justify="center",
    font=("Tahoma", 12, "bold"),
    command=resize_multiple_images_with_progress,
)
resize_button.pack(fill="both", padx=10, pady=10)


# Adjust the width and height as desired
resize_button.config(width=12, height=1)
resize_button.pack(pady=(5, 17))

# Watermark label
watermark_label = tk.Label(
    window, text="pudszTTIOT", font=("Corbel", 9), bg="#2A292B", fg="#46F953"
)
watermark_label.pack(side=tk.BOTTOM, anchor="e")

# Start the GUI event loop
window.mainloop()
