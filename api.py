from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from PIL import Image
import io

from predict import predict_image

app = FastAPI()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Read the uploaded image
        image = await file.read()
        image = Image.open(io.BytesIO(image))
        
        predicted = predict_image(image)
        
        return {"predicted": predicted}
    except Exception as e:
        return {"error": str(e)}
       
       buffer = io.BytesIO()
       predicted.save(buffer, format="PNG")
       buffer.seek(0)
       return StreamingResponse(buffer, media_type="image/png")