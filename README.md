<<<<<<< HEAD
# potato-disease-classification-cnn
Potato leaf disease classification using CNN, TensorFlow Serving, FastAPI, Docker and Gradio.
=======
# Potato Disease Classification Using CNN

## Project Overview
This project uses a Convolutional Neural Network (CNN) to classify potato leaf images into three categories:
- Early Blight
- Late Blight
- Healthy

## Technologies Used
- Python
- TensorFlow and Keras
- CNN
- Docker
- TensorFlow Serving
- FastAPI
- Gradio

## Dataset
The PlantVillage dataset contains 2,152 potato leaf images across three classes.

## Model Performance
- Test Accuracy: **97.66%**
- Test Loss: **0.0841**
- Image Size: 256 × 256
- Batch Size: 32

## Application Architecture
1. User uploads a potato leaf image through Gradio.
2. Gradio sends the image to the FastAPI backend.
3. FastAPI sends the image to TensorFlow Serving.
4. The CNN model predicts the disease class.
5. The application displays the predicted class and confidence score.

## Run the Project

Start TensorFlow Serving using Docker:

```powershell
docker start potatoes_model_container
```

Start FastAPI:

```powershell
python -m uvicorn main:app --host 127.0.0.1 --port 8000
```

Start Gradio in another terminal:

```powershell
python app.py
```

Open the application:

http://127.0.0.1:8502

## Screenshots
Add screenshots of:
- Gradio application
- Image upload and prediction results
- Confusion matrix

## Future Improvements
- Test with more unseen potato leaf images.
- Improve model generalization.
- Add more plant disease categories.

## Disclaimer
Predictions are model outputs and should not be treated as confirmed agricultural diagnoses.
>>>>>>> cfc204d (Add potato disease classification CNN project)
