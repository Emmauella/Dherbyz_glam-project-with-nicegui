from nicegui import ui

def render():
    with ui.element("div").classes('min-h-screen w-full bg-rose-50 flex flex-col items-center px-20 py-20').props('id=contact'):
        ui.label("Contact Us").classes("text-4xl font-bold text-pink-600 mb-10")

        with ui.grid(columns=2).classes('gap-12 w-full max-w-6xl'):
            with ui.column():
                ui.label("Get In Touch").classes('text-3xl font-semibold text-pink-600 mb-6')

                contact_info = [
                    {"icon": "fas fa-map-marker-alt", "text": "Kwashieman, Accra, Ghana"},
                    {"icon": "fas fa-phone", "text": "+233 XX XXX XXXX"},
                    {"icon": "fas fa-envelope", "text": "info@dherbyzglam.com"},
                    {"icon": "fas fa-clock", "text": "Mon-Sat: 9AM-7PM, Sun: 10AM-4PM"}
                ]

                for info in contact_info:
                    with ui.row().classes('items-center mb-4'):
                        ui.html(f'<i class="{info["icon"]} text-pink-600 mr-3"></i>')
                        ui.label(info["text"]).classes('text-gray-700')

                ui.label("Send us a message").classes('text-2xl font-semibold text-pink-600 mt-8 mb-4')
                name_input = ui.input('Your Name').classes('w-full mb-4')
                email_input = ui.input('Your Email').classes('w-full mb-4')
                message_input = ui.textarea('Your Message').classes('w-full mb-4')
                ui.button("Send Message", color='pink').classes('w-full')

            with ui.column():
                ui.label("Location").classes('text-2xl font-semibold text-pink-600 mb-4')
                # Placeholder for map - in a real app, you'd embed Google Maps
                with ui.card().classes('p-8 bg-gray-100 rounded-2xl text-center'):
                    ui.html('<i class="fas fa-map text-4xl text-pink-600 mb-4"></i>')
                    ui.label("Interactive Map").classes('text-xl text-gray-600')
                    ui.label("Kwashieman, Accra").classes('text-gray-500')

            