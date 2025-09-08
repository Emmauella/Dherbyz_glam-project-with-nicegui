from nicegui import ui,app


def render():
    # Big container
    with ui.element("div").style("background-image: url('/assets/salon.jpg')").classes("h-screen w-screen flex flex-col bg-cover bg-center items-center justify-center p-0"):
        # Navbar
        with ui.element("nav").classes("flex flex-row justify-between items-center fixed left-0 w-full top-0 px-20 py-10"):

            # LOGO
            ui.label("LOGO").classes("font-bold text-2xl text-green")
        
            

        
            # Navlinks
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
                    ui.link(item["title"], item ["path"]).classes("no-underline uppercase text-white")
            
            # The Socials
            with ui.row().classes("text-white text-lg font-bold"):
                ui.html('<i class-"fa-brands fa-facebook"></i>')
                ui.html('<i class-"fa-brands fa-instagram"></i>')
                ui.html('<i class-"fa-brands fa-twitter"></i>')
                ui.html('<i class-"fa-brands fa-whatsApp"></i>')

             

# Text
        with ui.element("div").classes('text-white font-bold text-center bg-black/50 h-full flex flex-col items-center justify-center w-full'):
         ui.label("Welcome to").classes("text-4xl mb 4")
         ui.label("Dherbyz_glam").classes("text-8xl text-white-600 mb-8")
         ui.button("Book").props("color=white-7")
     


    

