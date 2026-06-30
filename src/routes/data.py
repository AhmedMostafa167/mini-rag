from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers import DataController


data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1"]
                        )

@data_router.post('/updaod/{project_id}')
async def updaod_data(project_id: str,
                      file: UploadFile,
                      app_settings: Settings = Depends(get_settings)):

    controller = DataController()
    
    is_valid, result_message = controller.validate_file(file)
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, 
            content={"message": result_message}
            )   
    else: return True
    