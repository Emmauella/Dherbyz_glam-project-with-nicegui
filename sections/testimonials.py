from nicegui import ui

def render():
    with ui.element("div").classes('min-h-screen w-full bg-gradient-to-br from-pink-50 to-rose-100 flex flex-col items-center px-20 py-20').props('id=testimonials'):
        ui.label("What Our Clients Say").classes("text-4xl font-bold text-pink-600 mb-10")

        testimonials = [
            {
                "name": "Adwoa Mensah",
                "text": "Amazing service! Debby transformed my look for my wedding day. Highly recommend!",
                "rating": 5,
                "image": "/assets/exp2.jpg"
            },
            {
                "name": "Kofi Asante",
                "text": "Professional and skilled team. My hair has never looked better!",
                "rating": 5,
                "image": "/assets/iso.jpg"
            },
            {
                "name": "Nana Ama",
                "text": "The best beauty salon in Accra. Always satisfied with their work.",
                "rating": 5,
                "image": "/assets/debby.jpg"
            }
        ]

        with ui.grid(columns=3).classes('gap-8 w-full max-w-6xl'):
            for testimonial in testimonials:
                with ui.card().classes('p-6 shadow-lg rounded-2xl bg-white/90 backdrop-blur-sm border border-pink-100'):
                    with ui.row().classes('items-center mb-4'):
                        ui.image(testimonial["image"]).classes('w-12 h-12 rounded-full mr-4')
                        ui.label(testimonial["name"]).classes('font-semibold text-pink-600')

                    # Star rating
                    with ui.row().classes('mb-4'):
                        for _ in range(testimonial["rating"]):
                            ui.html('<i class="fas fa-star text-yellow-400"></i>')

                    ui.label(f'"{testimonial["text"]}"').classes('text-gray-700 italic')

        # Call to action
        with ui.element("div").classes('mt-12 text-center'):
            ui.label("Ready to experience the Dherbyz_Glam difference?").classes('text-2xl font-semibold text-pink-600 mb-4')
            ui.button("Book Your Appointment Now", color='pink', on_click=lambda: ui.open('/bookings')).classes('text-lg px-8 py-3')