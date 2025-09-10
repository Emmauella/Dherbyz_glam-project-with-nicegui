from nicegui import ui

def render():
    with ui.element("div").classes("w-screen h-screen flex flex-row items-center bg-rose-100 "):

        with ui.element("div").classes("w-[50%] h-screen flex flex-col justify-center items-center text-center p-6"):
            ui.label("DHERBYZ_GLAM").classes("text-pink-500 italic text-3xl")
            ui.label("WELCOME").classes("text-5xl font-extrabold text-300 mt-2 font-poppins text-pink")

            ui.html(
                "Makeup Services.<br>"
                "Hair & Braids<br>").classes("mt-10 text-m font-poppins text-pink")
            ui.link("About Us").classes("text-pink-700 mt-5 px-6 py-3 rounded-lg no-underline")

            # right side image container
        with ui.element("div").classes("" \
            "w-[50%] h-full flex items-center justify-center"):
            ui.image("/assets/sal.jpg").classes(
                "w-[70%] h-[65%] object-cover rounded-xl transitions-transform duration-500 ease-in-out transform hover:scale-110"                                                                                                        
                )
