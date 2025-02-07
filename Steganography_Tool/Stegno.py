import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk  # Make sure you have Pillow installed: pip install Pillow

from Modules import encoder, decoder

class SteganographyTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Steganography Tool")
        self.root.geometry("600x400")

        self.image_path = ""
        self.encoded_image_path = ""

        # UI Elements
        self.load_image_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_image_button.pack(pady=10)

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.encode_button = tk.Button(root, text="Encode Message", command=self.encode_message)
        self.encode_button.pack(pady=5)

        self.decode_button = tk.Button(root, text="Decode Message", command=self.decode_message)
        self.decode_button.pack(pady=5)

        self.message_text = tk.Text(root, height=5, width=50)
        self.message_text.pack(pady=5)

    def load_image(self):
        self.image_path = filedialog.askopenfilename(
            initialdir="./images",
            title="Select Image",
            filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg"), ("All files", "*.*"))
        )
        if self.image_path:
            img = Image.open(self.image_path)
            img = img.resize((300, 200), Image.LANCZOS)  # Resize for display
            self.image = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.image)
            self.image_label.image = self.image

    def encode_message(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please load an image first.")
            return

        message = self.message_text.get("1.0", tk.END).strip()  # Get text from the Text widget
        if not message:
            messagebox.showerror("Error", "Please enter a message to encode.")
            return

        try:
            self.encoded_image_path = filedialog.asksaveasfilename(
                initialdir="./",
                title="Save Encoded Image",
                defaultextension=".png",
                filetypes=(("PNG files", "*.png"),)
            )
            if self.encoded_image_path:
                encoder.encode(self.image_path, message, self.encoded_image_path)
                messagebox.showinfo("Success", f"Message encoded and saved to {self.encoded_image_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Encoding failed: {e}")

    def decode_message(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please load an image first.")
            return

        try:
            hidden_message = decoder.decode(self.image_path)
            self.message_text.delete("1.0", tk.END) # Clear existing text
            self.message_text.insert("1.0", hidden_message) # Insert decoded text
            messagebox.showinfo("Decoded Message", f"Decoded message: {hidden_message}")

        except Exception as e:
            messagebox.showerror("Error", f"Decoding failed: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    tool = SteganographyTool(root)
    root.mainloop()
