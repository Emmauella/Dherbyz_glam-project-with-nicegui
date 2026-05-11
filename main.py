from nicegui import ui, app

from sections import hero, services, reservations, about, gallery, contact, testimonials, socials, footer

# Expose the assets folder to the nicegui server
app.add_static_files("/assets", "assets")

# Link external icons to the head
ui.add_head_html('''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
<link rel="stylesheet" href="/assets/reset.css"/>
<link rel="stylesheet" href="/assets/style.css"/>
''', shared=True)

# Home page
@ui.page('/')
def home_page():
    render_navbar()
    hero.render()
    about.render()
    gallery.render()
    testimonials.render()
    footer.render()

# Services page
@ui.page('/services')
def services_page():
    # Render navbar on services page
    render_navbar()
    services.render()
    footer.render()

# Bookings page
@ui.page('/bookings')
def bookings_page():
    # Render navbar on bookings page
    render_navbar()
    reservations.render()
    footer.render()

# Contact page
@ui.page('/contact')
def contact_page():
    # Render navbar on contact page
    render_navbar()
    contact.render()
    footer.render()

def render_navbar():
    """Render the navbar for individual pages"""
    with ui.element("nav").classes("flex flex-row justify-between items-center fixed z-10 bg-pink-200/60 left-0 w-full top-0 px-20 py-5"):
        # LOGO
        ui.image("/assets/card.jpg").classes("h-[50px] w-[50px] border-2 rounded-full")

        # Navlink
        navlinks = [
            {"title": "Home", "path": "/#home"},
            {"title": "About", "path": "/#about"},
            {"title": "Services", "path": "/services"},
            {"title": "Gallery", "path": "/#gallery"},
            {"title": "Testimonials", "path": "/#testimonials"},
            {"title": "Booking", "path": "/bookings"},
            {"title": "Contact", "path": "/contact"}
        ]

        with ui.row():
            for item in navlinks:
                ui.link(item["title"], item["path"]).classes("no-underline uppercase text-rose-500 hover:text-pink-700 transition-colors")

        # The Socials
        with ui.row().classes("text-pink text-lg font-bold"):
            ui.html('<i class="fa-brands fa-facebook"></i>')
            ui.html('<i class="fa-brands fa-instagram"></i>')
            ui.html('<i class="fa-brands fa-twitter"></i>')
            ui.html('<i class="fa-brands fa-whatsapp"></i>')

ui.run()
