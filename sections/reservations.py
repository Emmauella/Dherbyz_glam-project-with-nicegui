# from nicegui import ui

# def render():
    
#         with ui.element("div").style("background-image: url('/assets/makeup.jpg')").classes("w-screen h-screen flex flex-col bg-cover bg-center items-center justify-center bg-black/20 p-0 bg-black/300"):
#             with ui.row().classes('gap-10 flex-wrap justify-center flex'):
                    

#                     with ui.card().classes('w-80 p-20 shadow-xl rounded-2xl bg-[url("/assets/exp2.jpg")] bg-cover bg-center h-[100%]'):
#                         with ui.element("div").classes("bg-black/50 w-full h-full "):
                
#                             ui.label('Makeup Expo').classes('text-xl font-poppins mb-50 text-pink')
                    

#                     with ui.card().classes('w-80 p-20 shadow-2xl rounded-2xl bg-[url("assets/iso.jpg")] bg-cover bg-center'):
#                         ui.label('Free Makeup Tutorial').classes('text-ml font-poppins mb-50 text-pink')
                        

#                     with ui.card().classes('w-80 p-20 shadow-xl rounded-2xl bg-[url("/assets/glamtime.jpg")] bg-cover bg-center h-[50%]'):
#                         ui.label('Glamz Time').classes('text-xl font-semibold mb-50 text-pink')
                        

                    # with ui.card().classes('w-80 p-20 shadow-xl rounded-2xl bg-url[("/assets/hairtreatment.jpg")] bg-cover bg-center h-[50%]'):
                    #     ui.label('Giving back beauty day').classes('text-xl font-semibold mb-50 text-pink')

      
           
            

        #     # right side image container
        # with ui.element.classes("" \
        #     "w-[70%] h-full flex items-left justify-left"):
        #     ui.image("/assets/salon.jpg").classes(
        #         "w-[70%] h-[70%] object-cover rounded-xl transitions-transform duration-500 ease-in-out transform hover:scale-110"                                                                                                        
        #         )
 


from nicegui import ui

def render():
    with ui.element("div").classes('min-h-screen w-full bg-pink-100 flex flex-col items-center px-20 py-20').props('id=booking'):
        ui.label("Book Your Appointment").classes("text-4xl font-bold text-pink-600 mb-10")

        with ui.card().classes('p-8 shadow-lg rounded-2xl bg-white/90 backdrop-blur-sm border border-pink-100 max-w-2xl w-full'):
            ui.label("Select Service").classes('text-2xl font-semibold text-pink-600 mb-4')
            service_select = ui.select(['Makeup', 'Hair Styling', 'Nails', 'Lashes', 'Facial'], value='Makeup').classes('w-full mb-4')

            ui.label("Choose Date & Time").classes('text-2xl font-semibold text-pink-600 mb-4')
            date_picker = ui.date().classes('w-full mb-4')
            time_select = ui.select(['9:00 AM', '10:00 AM', '11:00 AM', '2:00 PM', '3:00 PM', '4:00 PM'], value='9:00 AM').classes('w-full mb-4')

            ui.label("Your Details").classes('text-2xl font-semibold text-pink-600 mb-4')
            name_input = ui.input('Full Name').classes('w-full mb-4')
            phone_input = ui.input('Phone Number').classes('w-full mb-4')
            email_input = ui.input('Email').classes('w-full mb-4')

            ui.button("Book Appointment", color='pink').classes('w-full text-lg py-3').on_click(lambda: ui.notify('Booking confirmed!', type='positive'))

            # Second card
            with ui.column().classes('items-center'):
                ui.card().classes('w-80 h-60 shadow-2xl rounded-2xl bg-[url("/assets/iso.jpg")] bg-cover bg-center')
                ui.label('Free Makeup Tutorial').classes('text-ml font-poppins text-pink mt-4')

            # Third card
            with ui.column().classes('items-center'):
                ui.card().classes('w-80 h-60 shadow-xl rounded-2xl bg-[url("/assets/glamtime.jpg")] bg-cover bg-center')
                ui.label('Glamz Time').classes('text-xl font-semibold text-pink mt-4')
