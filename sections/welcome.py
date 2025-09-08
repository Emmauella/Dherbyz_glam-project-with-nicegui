from nicegui import ui

def render():
    with ui.element("div").classes("w-screen h-screen flex flex-row items-center"):

        with ui.element("div").classes("w-[50%] h-screen flex flex-col justify-center items-center text-center p-6"):
            ui.label("Foodie Hub").classes("text-green-500 italic text-3xl")
            ui.label("WELCOME").classes("text-5xl font-extrabold text-300 mt-2 font-poppins")

            ui.html(
                "A place to eat healthy.<br>"
                "At Foodie hub, we give you the best healthy food to make you live a good life<br>").classes("mt-6 text-m font-poppins")
            ui.link("About Us").classes("text-black mt-5 px-6 py-3 rounded-lg no-underline")

            # right side image container
        with ui.element("div").classes("" \
            "w-[50%] h-full flex items-center justify-center"):
            ui.image("/assets/makeupart.jpg").classes(
                "w-[70%] h-[65%] object-cover rounded-xl transitions-transform duration-500 ease-in-out transform hover:scale-110"                                                                                                        
                )
