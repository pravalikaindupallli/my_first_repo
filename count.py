import os

label_dir = "GadgetMerged/MergedYOLOv8/labels/train"
class_counts = {}

for label_file in os.listdir(label_dir):
    with open(os.path.join(label_dir, label_file), "r") as f:
        for line in f:
            class_id = line.split()[0]
            class_counts[class_id] = class_counts.get(class_id, 0) + 1

print("Class distribution:")
for class_id, count in class_counts.items():
    print(f"Class {class_id}: {count} labels")
