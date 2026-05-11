from nicegui import ui

def render():
    with ui.element("div").classes('min-h-screen w-full bg-gradient-to-br from-pink-50 to-rose-100 flex flex-col items-center px-20 py-20').props('id=about'):
        ui.label("About Dherbyz_Glam").classes("text-4xl font-bold text-pink-600 mb-10")

        with ui.grid(columns=2).classes('gap-12 w-full max-w-6xl items-center'):
            with ui.column():
                ui.label("Our Story").classes('text-3xl font-semibold text-pink-600 mb-4')
                ui.label("Dherbyz_Glam is a premium beauty salon located in Kwashieman, dedicated to enhancing beauty and elevating confidence. Our team of skilled professionals brings years of experience in makeup, hair styling, and beauty treatments.").classes('text-gray-700 mb-6 leading-relaxed')
                ui.label("Mission & Vision").classes('text-2xl font-semibold text-pink-600 mb-4')
                ui.label("To provide exceptional beauty services that empower our clients to feel their most beautiful selves.").classes('text-gray-700 mb-6')

            with ui.column():
                ui.image("/assets/sal.jpg").classes('w-full h-96 object-cover rounded-2xl shadow-lg')

        # Team section
        ui.label("Meet Our Team").classes("text-3xl font-bold text-pink-600 mt-16 mb-8")

        team = [
            {"name": "Debby", "role": "Founder & Lead Stylist", "image": "/assets/debby.jpg"},
            {"name": "Sarah", "role": "Makeup Artist", "image": "/assets/exp2.jpg"},
            {"name": "Emma", "role": "Hair Specialist", "image": "/assets/iso.jpg"}
        ]

        with ui.grid(columns=3).classes('gap-8 w-full max-w-6xl'):
            for member in team:
                with ui.card().classes('p-6 text-center shadow-lg rounded-2xl bg-white/90 backdrop-blur-sm border border-pink-100'):
                    ui.image(member["image"]).classes('w-32 h-32 object-cover rounded-full mx-auto mb-4')
                    ui.label(member["name"]).classes('text-xl font-semibold text-pink-600 mb-2')
                    ui.label(member["role"]).classes('text-gray-600')