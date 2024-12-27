from aiogram import Router
from .handlers.start import router as start_router
from .handlers.complaint import router as complaint_router

def setup_routers():
   router = Router()
   router.include_router(start_router)
   router.include_router(complaint_router)
   return router
