from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseEnums   
class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.SIZE_SCALE: int = 1048576 # convert MB to bytes
        
    def validate_file(self, file: UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseEnums.FILE_TYPE_NOT_SUPPORTED.value

        if file.size > self.app_settings.FILE_ALLOWED_SIZE*self.SIZE_SCALE:
            return False, ResponseEnums.FILE_SIZE_EXCEEDED.value
        
        return True, ResponseEnums.FILE_VALIDATION_SUCESS.value