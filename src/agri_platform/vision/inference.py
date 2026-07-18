from .models import ImagePrediction
class VisionInference:
    def predict(self,image_path:str):
        return ImagePrediction(image_id=image_path,label="healthy",confidence=0.91)
