from nicegui import ui

def render():
    with ui.element("footer").classes('w-full bg-pink-800 text-white py-12 px-20'):
        with ui.grid(columns=4).classes('gap-8 w-full max-w-6xl mx-auto'):
            with ui.column():
                ui.label("Dherbyz_Glam").classes('text-2xl font-bold text-pink-300 mb-4')
                ui.label("Premium beauty salon in Kwashieman, Accra").classes('text-pink-100 mb-4')
                ui.label("Enhancing Beauty, Elevating Confidence").classes('text-pink-200 italic')

            with ui.column():
                ui.label("Quick Links").classes('text-xl font-semibold mb-4')
                links = ["About", "Services", "Gallery", "Testimonials", "Contact"]
                for link in links:
                    ui.label(link).classes('text-pink-100 hover:text-white cursor-pointer mb-2')

            with ui.column():
                ui.label("Services").classes('text-xl font-semibold mb-4')
                services = ["Makeup", "Hair Styling", "Nails", "Lashes", "Facials"]
                for service in services:
                    ui.label(service).classes('text-pink-100 mb-2')

            with ui.column():
                ui.label("Contact Info").classes('text-xl font-semibold mb-4')
                ui.label("📍 Kwashieman, Accra, Ghana").classes('text-pink-100 mb-2')
                ui.label("📞 +233 XX XXX XXXX").classes('text-pink-100 mb-2')
                ui.label("✉️ info@dherbyzglam.com").classes('text-pink-100 mb-2')

        with ui.element("div").classes('border-t border-pink-700 mt-8 pt-8 text-center'):
            ui.label("© 2024 Dherbyz_Glam. All rights reserved.").classes('text-pink-200')
            from sections.socials import render as render_socials
            render_socials()