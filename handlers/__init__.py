from aiogram import Router


def setup_routers() -> Router:
    from . import saving_preferences, general_commands

    router = Router()
    router.include_router(general_commands.router)
    router.include_router(saving_preferences.router)

    return router
