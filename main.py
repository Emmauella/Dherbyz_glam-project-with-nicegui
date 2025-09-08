from nicegui import ui,app

from sections import hero, welcome

# Expose the assets folder to the nicegui server
app.add_static_files("/assets", "assets")

# Link external icons to the head
ui.add_head_html('''<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css"><link rel="stylesheet" href="/assets/reset.css"/>''')


hero.render()
welcome.render()


ui.run()
