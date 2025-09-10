from nicegui import ui

def render():
    # Social links
    links = {
        "Facebook": "https://facebook.com/yourpage",
        "Instagram": "https://instagram.com/yourprofile",
        "Telegram": "https://t.me/yourchannel",
        "WhatsApp": "https://wa.me/233XXXXXXXXX",  # Replace with your phone number
    }

    # Icons and Tailwind color classes
    social_styles = {
        "Facebook": {"icon": "facebook", "classes": "bg-[#1877F2]"},   # Facebook blue
        "Instagram": {"icon": "instagram", "classes": "bg-[#E4405F]"}, # Instagram pink/red
        "Telegram": {"icon": "send", "classes": "bg-[#0088cc]"},       # Telegram blue
        "WhatsApp": {"icon": "whatsapp", "classes": "bg-[#25D366]"},   # WhatsApp green
    }

    with ui.row().classes("gap-6 p-4 justify-center"):
        for name, url in links.items():
            ui.button(on_click=lambda url=url: ui.open(url)) \
                .props(f"icon={social_styles[name]['icon']}") \
                .classes(
                    f"{social_styles[name]['classes']} text-white "
                    "rounded-full w-12 h-12 flex items-center justify-center "
                    "text-xl shadow-md hover:opacity-80 transition"
                ) \
                .tooltip(name)   # shows tooltip on hover

    render()
    
