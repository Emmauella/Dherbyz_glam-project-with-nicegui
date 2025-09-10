from nicegui import ui

def render():
    
        with ui.element("div").style("background-image: url('/assets/makeup.jpg')").classes("w-screen h-screen flex flex-col bg-cover bg-center items-center justify-center bg-black/20 p-0 bg-black/300"):
            with ui.row().classes('gap-10 flex-wrap justify-center flex'):
                    

                    with ui.card().classes('w-80 p-20 shadow-xl rounded-2xl bg-[url("/assets/exp2.jpg")] bg-cover bg-center h-[100%]'):
                        with ui.element("div").classes("bg-black/50 w-full h-full "):
                
                            ui.label('Makeup Expo').classes('text-xl font-poppins mb-50 text-pink')
                    

                    with ui.card().classes('w-80 p-20 shadow-2xl rounded-2xl bg-[url("assets/iso.jpg")] bg-cover bg-center'):
                        ui.label('Free Makeup Tutorial').classes('text-ml font-poppins mb-50 text-pink')
                        

                    with ui.card().classes('w-80 p-20 shadow-xl rounded-2xl bg-[url("/assets/glamtime.jpg")] bg-cover bg-center h-[50%]'):
                        ui.label('Glamz Time').classes('text-xl font-semibold mb-50 text-pink')
                        

                    # with ui.card().classes('w-80 p-20 shadow-xl rounded-2xl bg-url[("/assets/hairtreatment.jpg")] bg-cover bg-center h-[50%]'):
                    #     ui.label('Giving back beauty day').classes('text-xl font-semibold mb-50 text-pink')

      
           
            

        #     # right side image container
        # with ui.element.classes("" \
        #     "w-[70%] h-full flex items-left justify-left"):
        #     ui.image("/assets/salon.jpg").classes(
        #         "w-[70%] h-[70%] object-cover rounded-xl transitions-transform duration-500 ease-in-out transform hover:scale-110"                                                                                                        
        #         )
 