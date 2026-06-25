from helpers.config import get_settings, Settings
from fastapi import Depends
class BaseController:
    def __init__(self, app_settings: Settings = Depends(get_settings)):
        self.app_settings = app_settings
        
        
