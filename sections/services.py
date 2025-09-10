# from nicegui import ui

# # SERVICES / MENU SECTION
    # def render():
    #     with ui.element('section').classes(
    #         'min-h-screen w-full bg-pink-100 flex flex-col items-center px-20 py-20'
#         ):
#         def render():
#         with ui.element("div").style("background-image: url('/assets/makeup.jpg')").classes(
#             "w-screen h-screen flex flex-col bg-cover bg-center items-center justify-center bg-black/20 p-0 bg-black/300"
#         ):
#             with ui.row().classes('gap-10 flex-wrap justify-center flex'):
                
#                 # First card
#                 with ui.column().classes('items-center'):
#                     ui.card().classes('w-80 h-60 shadow-xl rounded-2xl bg-[url("/assets/exp2.jpg")] bg-cover bg-center')
#                     ui.label('Makeup Expo').classes('text-xl font-poppins text-pink mt-4')

#                 # Second card
#                 with ui.column().classes('items-center'):
#                     ui.card().classes('w-80 h-60 shadow-2xl rounded-2xl bg-[url("/assets/iso.jpg")] bg-cover bg-center')
#                     ui.label('Free Makeup Tutorial').classes('text-ml font-poppins text-pink mt-4')

#                 # Third card
#                 with ui.column().classes('items-center'):
#                     ui.card().classes('w-80 h-60 shadow-xl rounded-2xl bg-[url("/assets/glamtime.jpg")] bg-cover bg-center')
#                     ui.label('Glamz Time').classes('text-xl font-semibold text-pink mt-4')






from nicegui import ui

def render():
    with ui.element("div").classes('min-h-screen w-full bg-rose-200 flex flex-col items-center px-20 py-20'
        "w-screen h-screen flex flex-col bg-cover bg-center items-center justify-center bg-black/20 p-0 bg-black/300"
    ):
        with ui.label("Our Services").classes('texl-3xl justify-center font-poppins text-pink mt-4'):
           with ui.row().classes('gap-10 flex-wrap justify-center flex'):
            
            # First card
            with ui.column().classes('items-center'):
                ui.card().classes('w-80 h-60 shadow-xl rounded-2xl bg-[url("/assets/makeupside.jpg")] bg-cover bg-center')
                ui.label('Makeup').classes('text-xl font-poppins text-pink mt-4')

            # Second card
            with ui.column().classes('items-center'):
                ui.card().classes('w-80 h-60 shadow-xl rounded-2xl bg-[url("/assets/braids.jpg")] bg-cover bg-center')
                ui.label('Hair/Braids').classes('text-xl font-poppins text-pink mt-4')

            # Third card
            with ui.column().classes('items-center'):
                ui.card().classes('w-80 h-60 shadow-xl rounded-2xl bg-[url("/assets/add.jpg")] bg-cover bg-center')
                ui.label('Add Ons').classes('text-xl font-semibold text-pink mt-4')


