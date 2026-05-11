from nicegui import ui,app


def render():
    # Big container
    with ui.element("div").style("background-image: url('/assets/facecard.jpg')").classes("h-screen w-screen flex flex-col bg-cover bg-center items-center justify-center p-0").props('id=home'):
        # Navbar is now rendered separately on each page

        # Text


        with ui.element("div").classes('text-white font-bold text-center bg-black/50 h-full flex flex-col items-center justify-center w-full'):
         ui.label("Welcome to").classes("text-4xl mb 4 text-pink")
         ui.label("Dherbyz_glam").classes("text-8xl text-pink-600 mb-8")
         ui.label("MAKE THEM STARE").classes("text-pink-600 text-6m mb-4 ")


         ui.button("Book Us", on_click=lambda: ui.open('/bookings')).props("color=pink-8")
    

     


    

