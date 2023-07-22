import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Create a window
window = tk.Tk()
window.title("Image Resizer")
window.geometry("550x500")
window.iconbitmap("resizer.ico")  # Set the path to your icon file

# Load the PNG image
image = Image.open("G:\Software\py\Python Creations\Completed\Projects\ImageResizer\Images\gradient 2.png")
photo = ImageTk.PhotoImage(image)

# Create a label widget to hold the image
background_label = tk.Label(window, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add an image label at the top center
# Replace with the actual path to your image file
image_path = "G:\Software\py\Python Creations\Completed\Projects\ImageResizer\Images\Image Resizer.png"
image = Image.open(image_path)
# Replace width and height with your desired dimensions
image = image.resize((130, 120))
image = ImageTk.PhotoImage(image)
image_label = tk.Label(window, image=image)
image_label.pack(pady=(15, 0))


# Function to choose an image file
def choose_image():
    if file_path := filedialog.askopenfilename(
        filetypes=[("Image files", "*.png *.jpg *.jpeg")]
    ):
        entry.delete(0, tk.END)  # Clear the entry field
        entry.insert(0, file_path)  # Set the chosen file path in the entry field


# Function to choose the output destination
def choose_output_destination():
    if folder_path := filedialog.askdirectory():
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
        if selected_dimension == "Custom":
            width = int(custom_width_entry.get())
            height = int(custom_height_entry.get())
        else:
            width, height = dimensions[selected_dimension]

        # Resize the image
        resized_image = image.resize((width, height))

        # Save the resized image to the output destination
        # Extract the file name from the file path
        file_name = file_path.split("/")[-1]
        # Construct the output path with the selected format
        output_path = f"{output_folder}/{file_name}_resized.{format_var.get()}"
        resized_image.save(output_path)

        # Show a success message box
        messagebox.showinfo(
            "Image Resized", "The image has been successfully resized and saved."
        )

        # Display the resized image
        resized_image.show()
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except PermissionError:
        messagebox.showerror("Error", "Permission denied to access the file.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to resize the image: {str(e)}")

# Predefined dimension choices with descriptions
dimensions = {
    "1920 x 1080 (Full HD)": (1920, 1080),  # HD Wallpaper
    "1280 x 720 (HD)": (1280, 720),  # HD Wallpaper
    "400 x 300 (Icon)": (400, 300),  # Icon
    "250 x 250 (Thumbnail)": (250, 250),  # Thumbnail
    "200 x 200 (Favicon)": (200, 200),  # Favicon
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
dimension_var.set("1920 x 1080 (Full HD)")  # Set initial dimension
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


# Add the custom dimension frame to the window
custom_dimension_frame.pack(fill="both", expand=True)

# Function to show or hide the custom dimension frame based on the selected dimension
def toggle_custom_dimension(*args):
    selected_dimension = dimension_var.get()
    if selected_dimension == "Custom":
        custom_dimension_frame.pack(fill="both", expand=True)
    else:
        custom_dimension_frame.pack_forget()

# Bind the toggle_custom_dimension function to the dimension variable
dimension_var.trace("w", toggle_custom_dimension)

# Create a button to resize the image
resize_button = tk.Button(
    window,
    text="Resize Image",
    bg="#E7E9EA",
    fg="#20211A",
    justify="center",
    font=("Tahoma", 12, "bold"),
    command=resize_image,
)
resize_button.pack(fill="both", padx=10, pady=10)

# Adjust the width and height as desired
resize_button.config(width=12, height=1)
resize_button.pack(pady=(5, 17))

# Watermark label
watermark_label = tk.Label(
    window, text="pudszTTIOT", font=("Corbel", 9), bg="#2A292B", fg="#46F953"
)
watermark_label.place(relx=1.0, rely=1.0, anchor="se", x=0, y=0)

# Start the GUI event loop
window.mainloop()
