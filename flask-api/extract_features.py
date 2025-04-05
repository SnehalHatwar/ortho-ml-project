# extract_features.py

# Import your actual STL processing functions
# Replace these with your implemented methods
def compute_alignment(upper_path, lower_path):
    # TODO: Your logic for computing alignment from STL files
    return 0.02  # Replace with real logic

def compute_overjet(upper_path, lower_path):
    # TODO: Your logic for computing overjet from STL files
    return 0.03  # Replace with real logic

def compute_occlusion(upper_path, lower_path):
    # TODO: Your logic for computing occlusion score from STL files
    return 10.5  # Replace with real logic

def extract_features(upper_path, lower_path):
    alignment_score = compute_alignment(upper_path, lower_path)
    overjet = compute_overjet(upper_path, lower_path)
    occlusion_score = compute_occlusion(upper_path, lower_path)

    return [alignment_score, overjet, occlusion_score]
