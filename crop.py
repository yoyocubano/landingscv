import sys
print(sys.executable)
import os
from PIL import Image

def process_images():
    brain_dir = "/Users/yoyocubano/.gemini/antigravity/brain/75c70558-144f-461d-b001-4cf9bb47a418"
    out_dir = "assets/certs"
    
    img1_path = os.path.join(brain_dir, "media__1773471604147.jpg")
    img2_path = os.path.join(brain_dir, "media__1773471648544.jpg")
    img3_path = os.path.join(brain_dir, "media__1773471659378.jpg")
    
    # Process Image 3 (ACCA Universal) - Rotate 90 CW and save
    if os.path.exists(img3_path):
        img3 = Image.open(img3_path)
        img3_rot = img3.rotate(-90, expand=True)
        img3_rot.save(os.path.join(out_dir, "acca_universal.jpg"), quality=90)
        print("Image 3 rotated and saved.")

    # Process Image 2 (Excellent Trade Training) - Save as is
    if os.path.exists(img2_path):
        img2 = Image.open(img2_path)
        img2.save(os.path.join(out_dir, "excellent_trade.jpg"), quality=90)
        print("Image 2 saved.")

    # Process Image 1 (4 cards) - crop
    if os.path.exists(img1_path):
        img1 = Image.open(img1_path)
        w, h = img1.size
        
        # Margins guessing, typically cards take up most width, let's leave 10% on sides
        x_start = int(w * 0.15)
        x_end = int(w * 0.85)
        
        # Vertical split: let's inspect the image, they are roughly distributed evenly in the middle
        # We can crop generously or try 4 equal segments between y=10% and y=90%
        # Or even better, just divide h into 4
        # Assuming they start somewhere around y=10% and end around y=90%
        y_span = h * 0.8 / 4
        margins = [
            (int(h * 0.1), int(h * 0.1 + y_span * 0.9)),
            (int(h * 0.1 + y_span * 1), int(h * 0.1 + y_span * 1.9)),
            (int(h * 0.1 + y_span * 2), int(h * 0.1 + y_span * 2.9)),
            (int(h * 0.1 + y_span * 3), int(h * 0.1 + y_span * 3.9))
        ]
        
        names = ["rigger_b_and_i.jpg", "forklift_b_and_i.jpg", "cpr_redcross.jpg", "osha_30.jpg"]
        for i, (y0, y1) in enumerate(margins):
            crop = img1.crop((x_start, y0, x_end, y1))
            crop.save(os.path.join(out_dir, names[i]), quality=90)
            print(f"Image 1, card {i+1} saved.")

if __name__ == "__main__":
    process_images()
