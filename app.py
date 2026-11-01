
import gradio as gr
import requests
from io import BytesIO

API_URL = "http://127.0.0.1:8000/predict"


def predict_disease(image):
    if image is None:
        return "Please upload a potato leaf image.", ""

    try:
        image_bytes = BytesIO()
        image.save(image_bytes, format="PNG")
        image_bytes.seek(0)

        response = requests.post(
            API_URL,
            files={
                "file": ("potato_leaf.png", image_bytes, "image/png")
            },
            timeout=60
        )

        response.raise_for_status()
        result = response.json()

        predicted_class = result["class"]
        confidence = result["confidence"]

        return predicted_class, f"{confidence:.2%}"

    except requests.exceptions.RequestException as error:
        return "Prediction failed. Check whether FastAPI is running.", str(error)


demo = gr.Interface(
    fn=predict_disease,
    inputs=gr.Image(type="pil", label="Upload Potato Leaf Image"),
    outputs=[
        gr.Textbox(label="Predicted Disease"),
        gr.Textbox(label="Confidence")
    ],
    title="Potato Disease Classification",
    description="Upload a potato leaf image to predict its disease."
)


if __name__ == "__main__":
    demo.launch(server_port=8502)
