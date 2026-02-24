from model_grid_fs_storage import *
from fastapi import APIRouter, Request


# class GridFSOrchestrator():
#     def __init__(self):
#         self.router = APIRouter()




# new_router = GridFSOrchestrator().router

# @new_router.post("/set_image")
# async def set_image_data(request: Request):
#     bin_file = await request.body()
    
#     return f"\nBLLLLLA\n{bin_file}\nBLLLLA\n




class GridFSOrchestrator:

    def __init__(self, db):
        self.router = APIRouter()
        self.fs = GridFSStorage().get_grid_fs()
        self.router.post("/set_image")(self.set_image_data)

    async def set_image_data(self, request: Request):
        bin_file = await request.body()
        file_id = self.fs.put(bin_file)
        return {"file_id": str(file_id)}