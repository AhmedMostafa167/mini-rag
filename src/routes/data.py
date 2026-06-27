from fastapi import APIRouter, Depends, UploadFile
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
    
    is_valid = controller.validate_file(file)
    return is_valid