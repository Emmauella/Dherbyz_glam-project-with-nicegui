from nicegui import ui,app


def render():
    # Big container
    with ui.element("div").style("background-image: url('/assets/facecard.jpg')").classes("h-screen w-screen flex flex-col bg-cover bg-center items-center justify-center p-0"):
        # Navbar
        with ui.element("nav").classes("flex flex-row justify-between items-center fixed z-10 bg-pink-200/60 left-0 w-full top-0 px-20 py-5"):

            # LOGO
            # ui.label("LOGO").classes("font-bold text-2xl text-pink")
            ui.image("/assets/card.jpg").classes("h-[50px] w-[50px] border-2 rounded-full")
        
            

        
            # Navlink
            navlinks= [
                {"title": "Home", "path": "/"}, 
                {"title": "About", "path": "/"}, 
                {"title": "Menu", "path": "/"}, 
                {"title": "Reservation", "path": "/"},
                {"title": "Gallery", "path": "/"}, 
                {"title": "Blog", "path": "/"},
                {"title": "Contact", "path": "/"}
                ]
            
            with ui.row():
                for item in navlinks:
                    ui.link(item["title"], item ["path"]).classes("no-underline uppercase text-rose-500")
            
            # The Socials
            with ui.row().classes("text-pink text-lg font-bold"):
                ui.html('<i class="fa-brands fa-facebook"></i>')
                ui.html('<i class="fa-brands fa-instagram"></i>')
                ui.html('<i class="fa-brands fa-twitter"></i>')
                ui.html('<i class="fa-brands fa-whatsApp"></i>')
            

             

# Text
        
            
        with ui.element("div").classes('text-white font-bold text-center bg-black/50 h-full flex flex-col items-center justify-center w-full'):
         ui.label("Welcome to").classes("text-4xl mb 4 text-pink")
         ui.label("Dherbyz_glam").classes("text-8xl text-pink-600 mb-8")
         ui.label("MAKE THEM STARE").classes("text-pink-600 text-6m mb-4 ")
         
            
         ui.button("Book Us").props("color=pink-8")
    

     


    

