from flask import Flask, request, render_template, jsonify
import numpy as np
from scipy.fft import fft2, ifft2, fftshift, ifftshift
import cv2
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)

def process_case1_defect_detection(image_array):
    """Case 1: Document Defect Detection using 2D FFT"""
    if len(image_array.shape) == 3:
        image_array = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    
    # Apply 2D FFT
    f_transform = fft2(image_array.astype(float))
    f_shift = fftshift(f_transform)
    
    # Create band-pass filter
    rows, cols = image_array.shape
    crow, ccol = rows//2, cols//2
    y, x = np.ogrid[-crow:rows-crow, -ccol:cols-ccol]
    d = np.sqrt(x*x + y*y)
    
    d_low = 20  # Lower cutoff
    d_high = 80  # Higher cutoff
    
    low_pass = 1 - np.exp(-d*d/(2*d_low*d_low))
    high_pass = np.exp(-d*d/(2*d_high*d_high))
    H = low_pass * high_pass
    
    filtered_f = f_shift * H
    filtered_image = np.real(ifft2(ifftshift(filtered_f)))
    
    # Enhance contrast
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced = clahe.apply(filtered_image.astype(np.uint8))
    
    # Sharpen
    kernel = np.array([[-1,-1,-1],
                      [-1, 9,-1],
                      [-1,-1,-1]])
    sharpened = cv2.filter2D(enhanced, -1, kernel)
    
    return cv2.normalize(sharpened, None, 0, 255, cv2.NORM_MINMAX)

def process_case2_texture_analysis(image_array):
    """Case 2: Texture Analysis using Gabor Filters"""
    if len(image_array.shape) == 3:
        gray = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    else:
        gray = image_array
        
    # Gabor filter parameters
    ksize = 31
    sigma = 5
    theta = np.pi/4
    lambda_ = 10
    gamma = 0.5
    psi = 0
    
    # Apply Gabor filter
    gabor_kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lambda_, gamma, psi)
    filtered = cv2.filter2D(gray, -1, gabor_kernel)
    
    # Enhance contrast
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    enhanced = clahe.apply(filtered)
    
    return enhanced

def process_case3_edge_detection(image_array):
    """Case 3: Advanced Edge Detection"""
    if len(image_array.shape) == 3:
        gray = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    else:
        gray = image_array
    
    # Denoise
    denoised = cv2.GaussianBlur(gray, (5,5), 0)
    
    # Canny edge detection
    edges = cv2.Canny(denoised, 50, 150)
    
    # Morphological operations
    kernel = np.ones((3,3), np.uint8)
    dilated = cv2.dilate(edges, kernel, iterations=1)
    
    return dilated

def process_case4_frequency_analysis(image_array):
    """Case 4: Frequency Domain Analysis"""
    if len(image_array.shape) == 3:
        gray = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    else:
        gray = image_array
    
    # Apply 2D FFT
    f_transform = fft2(gray.astype(float))
    f_shift = fftshift(f_transform)
    
    # Get magnitude spectrum
    magnitude_spectrum = 20 * np.log(np.abs(f_shift) + 1)
    
    # Normalize for display
    magnitude_spectrum = cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX)
    
    return magnitude_spectrum.astype(np.uint8)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    
    file = request.files['image']
    case = request.form.get('case', 'case1')  # Default to case1
    
    # Read image
    image = Image.open(file.stream)
    image_array = np.array(image)
    
    # Process based on case
    processing_functions = {
        'case1': process_case1_defect_detection,
        'case2': process_case2_texture_analysis,
        'case3': process_case3_edge_detection,
        'case4': process_case4_frequency_analysis
    }
    
    processed = processing_functions[case](image_array)
    
    # Convert to base64
    img = Image.fromarray(processed)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    return jsonify({
        'processed_image': f'data:image/png;base64,{img_str}'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)