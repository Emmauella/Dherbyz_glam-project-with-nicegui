from nicegui import ui

# SERVICES / MENU SECTION
def render():
    with ui.element('section').classes(
        'min-h-screen w-full bg-pink-100 flex flex-col items-center px-20 py-20'
    ):
        ui.label('Our Services').classes('text-4xl font-bold mb-10 text-center text-pink')

        with ui.row().classes('gap-10 flex-wrap justify-center flex'):

            with ui.card().classes('w-80 p-20 shadow-xl rounded-2xl bg-[url("/assets/makeupside.jpg")] bg-cover bg-center h-[50%]'):
                with ui.element("div").classes("bg-black/50 w-full h-full "):
                    ui.label('Makeup').classes('text-xl font-poppins mb-50 text-pink')
             

            with ui.card().classes('w-80 p-20 shadow-xl rounded-2xl bg-[url("assets/braids.jpg")] bg-cover bg-center'):
                ui.label('Hair & Braids').classes('text-ml font-poppins mb-50 text-pink')
                

            with ui.card().classes('w-80 p-20 shadow-xl rounded-2xl bg-[url("/assets/soft-angled-brows.jpg")] bg-cover bg-center h-[50%]'):
                ui.label('Add-ons').classes('text-xl font-semibold mb-50 text-pink')
                

            with ui.card().classes('w-80 p-20 shadow-xl rounded-2xl bg-url[("/assets/hairtreatment.jpg")] bg-cover bg-center h-[50%]'):
                ui.label('Treatments').classes('text-xl font-semibold mb-50 text-pink')
           





