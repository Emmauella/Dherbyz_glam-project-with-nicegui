from nicegui import ui

def render():
    with ui.element("div").classes('min-h-screen w-full bg-pink-50 flex flex-col items-center px-20 py-20').props('id=gallery'):
        ui.label("Our Gallery").classes("text-4xl font-bold text-pink-600 mb-10")

        gallery_images = [
            "/assets/makeup.jpg", "/assets/braids.jpg", "/assets/hairgoals.jpg",
            "/assets/glamtime.jpg", "/assets/modern.jpg", "/assets/exp.jpg",
            "/assets/hairtreatment.jpg", "/assets/salon.jpg", "/assets/welcomepic.jpg"
        ]

        with ui.grid(columns=3).classes('gap-6 w-full max-w-6xl'):
            for image in gallery_images:
                ui.image(image).classes('w-full h-64 object-cover rounded-2xl shadow-lg hover:shadow-xl transition-shadow duration-300 cursor-pointer')