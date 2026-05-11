from nicegui import ui

def render():
    with ui.element("div").classes('min-h-screen w-full bg-rose-200 flex flex-col items-center px-20 py-20').props('id=services'):
        ui.label("Our Services").classes("text-4xl font-bold text-pink-600 mb-10")

        services = [
            {"name": "Makeup", "image": "/assets/makeupside.jpg", "desc": "Professional makeup services for all occasions"},
            {"name": "Frontal Installation", "image": "/assets/braids.jpg", "desc": "Expert frontal wig installation"},
            {"name": "Wig Styling", "image": "/assets/hairgoals.jpg", "desc": "Beautiful wig styling and customization"},
            {"name": "Nails", "image": "/assets/modern.jpg", "desc": "Elegant nail art and care"},
            {"name": "Lashes", "image": "/assets/exp.jpg", "desc": "Eye-catching lash extensions"},
            {"name": "Hair Styling", "image": "/assets/hairtreatment.jpg", "desc": "Professional hair styling services"},
            {"name": "Bridal Glam", "image": "/assets/glamtime.jpg", "desc": "Complete bridal beauty packages"},
            {"name": "Pedicure & Manicure", "image": "/assets/salon.jpg", "desc": "Relaxing spa treatments"},
            {"name": "Facial Treatments", "image": "/assets/welcomepic.jpg", "desc": "Rejuvenating facial care"}
        ]

        with ui.grid(columns=3).classes('gap-8 w-full max-w-6xl'):
            for service in services:
                with ui.card().classes('p-6 shadow-lg rounded-2xl bg-white/90 backdrop-blur-sm border border-pink-100 hover:shadow-xl transition-all duration-300'):
                    ui.image(service["image"]).classes('w-full h-48 object-cover rounded-xl mb-4')
                    ui.label(service["name"]).classes('text-xl font-semibold text-pink-600 mb-2')
                    ui.label(service["desc"]).classes('text-gray-600 mb-4')
                    ui.button("Book Now", color='pink', on_click=lambda: ui.open('/bookings')).classes('w-full')


