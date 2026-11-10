import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
from ultralytics import YOLO
import cv2
import threading

# Load YOLO model
model = YOLO("yolov8n.pt")

def detect_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
    )
    
    if not file_path:
        return
    
    status_label.config(text="⏳ Sedang memproses...")
    result_text.delete(1.0, tk.END)

    def run_detection():
        results = model(file_path)
        result = results[0]

        # Gambar dengan bounding box
        result_img = result.plot()
        result_img = cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB)
        
        img = Image.fromarray(result_img)
        img = img.resize((600, 400))
        imgtk = ImageTk.PhotoImage(image=img)

        panel.config(image=imgtk)
        panel.image = imgtk

        # Tampilkan detail object
        boxes = result.boxes
        total_obj = len(boxes)

        result_text.insert(tk.END, f"Total Object Terdeteksi: {total_obj}\n\n")

        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            label = model.names[cls_id]
            result_text.insert(tk.END, f"{label} ({conf:.2f})\n")

        status_label.config(text="✅ Deteksi selesai")

    threading.Thread(target=run_detection).start()


# ================= GUI =================
root = tk.Tk()
root.title("YOLOv8 Object Detection")
root.geometry("750x700")

title = tk.Label(root, text="YOLO Image Detection", font=("Arial", 16, "bold"))
title.pack(pady=10)

btn = tk.Button(root, text="Upload Gambar & Deteksi", command=detect_image)
btn.pack(pady=5)

status_label = tk.Label(root, text="Menunggu gambar...", fg="blue")
status_label.pack(pady=5)

panel = tk.Label(root)
panel.pack(pady=10)

# Scrollable text result
frame = tk.Frame(root)
frame.pack(pady=10, fill="both", expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

result_text = tk.Text(frame, height=10, yscrollcommand=scrollbar.set)
result_text.pack(fill="both", expand=True)

scrollbar.config(command=result_text.yview)

root.mainloop()