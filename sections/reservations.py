from nicegui import ui

def render():
    with ui.element("div").classes('min-h-screen w-full bg-pink-100 flex justify-center px-6 pt-32 pb-12').props('id=booking'):
        with ui.column().classes('w-full max-w-7xl gap-8 items-center'):
            ui.label("Book Your Transformation").classes("text-4xl md:text-5xl font-bold text-pink-700 text-center mb-4")
            ui.label("Elevate your glam with a personalized appointment crafted just for you. Choose your service, stylist, and perfect date for a flawless experience.").classes("text-md md:text-lg text-pink-600 text-center max-w-3xl mx-auto")

            with ui.row().classes('gap-8 flex-col lg:flex-row items-start'):
                with ui.card().classes('glass-card p-8 flex-1'):
                    ui.label("Select Your Services").classes('text-2xl font-semibold text-pink-700 mb-4')

                    service_select = ui.select(
                        ['Signature Facial', 'Hair Styling', 'Nail Art', 'Lashes Lift', 'Bridal Glam'],
                        value='Signature Facial',
                        label='Service'
                    ).classes('w-full mb-6')

                    ui.label("Choose Date & Time").classes('text-2xl font-semibold text-pink-700 mb-4')
                    with ui.row().classes('gap-4 flex-wrap mb-6'):
                        date_picker = ui.date().classes('flex-1 min-w-[180px]')
                        time_select = ui.select(['9:00 AM', '10:30 AM', '12:00 PM', '2:00 PM', '4:00 PM'], value='10:30 AM', label='Time').classes('flex-1 min-w-[180px]')

                    ui.label("Choose Your Professional").classes('text-2xl font-semibold text-pink-700 mb-4')
                    professional_select = ui.select(
                        ['Aimee Baker', 'Lacey Makeover', 'Ruby Stone', 'Emma Lashes'],
                        value='Aimee Baker',
                        label='Professional'
                    ).classes('w-full mb-6')

                    ui.label("Customer Information").classes('text-2xl font-semibold text-pink-700 mb-4')
                    name_input = ui.input('Full Name').classes('w-full mb-4')
                    phone_input = ui.input('Phone Number').classes('w-full mb-4')
                    email_input = ui.input('Email').classes('w-full mb-4')
                    notes_input = ui.textarea('Tell us your preferences').classes('w-full mb-6')

                    ui.button("Confirm Booking", color='pink').classes('w-full text-lg py-4').on_click(lambda: ui.notify('Booking confirmed! We will contact you soon.', type='positive'))

                with ui.column().classes('w-full lg:w-[420px] gap-6'):
                    with ui.card().classes('booking-card p-6'):
                        ui.label("Appointment Summary").classes('text-2xl font-semibold text-pink-700 mb-4')
                        service_summary = ui.label("Service: Signature Facial").classes('text-sm text-pink-700')
                        date_summary = ui.label("Date: Select a date").classes('text-sm text-rose-600')
                        time_summary = ui.label("Time: 10:30 AM").classes('text-sm text-rose-600')
                        pro_summary = ui.label("Professional: Aimee Baker").classes('text-sm text-rose-600')
                        customer_summary = ui.label("Customer: Your details will appear here once entered.").classes('text-sm text-pink-600')

                        ui.separator().classes('my-4')
                        ui.label("Estimated Total").classes('text-sm font-medium text-pink-500')
                        total_label = ui.label("₦120,000").classes('text-3xl font-bold text-pink-700')

                    with ui.card().classes('booking-card p-6'):
                        ui.label("Choose Your Professional").classes('text-2xl font-semibold text-pink-700 mb-4')
                        with ui.row().classes('gap-3 flex-wrap'):
                            for name, role in [
                                ('Aimee Baker', 'Beauty Specialist'),
                                ('Lacey Makeover', 'Hair & Glam Expert'),
                                ('Ruby Stone', 'Makeup Artist')
                            ]:
                                with ui.card().classes('professional-card p-4 flex-1 min-w-[150px]'):
                                    ui.label(name).classes('font-semibold text-pink-700')
                                    ui.label(role).classes('text-sm text-pink-600')

                    with ui.card().classes('booking-card p-6'):
                        ui.label("Need Help?").classes('text-2xl font-semibold text-pink-700 mb-4')
                        ui.label("Call us or send a message to book a bespoke transformation at your convenience.").classes('text-sm text-rose-600 leading-6')
                        ui.label("WhatsApp: +234 800 123 4567").classes('text-sm font-semibold text-pink-700 mt-4')

    def update_summary():
        service_summary.set_text(f"Service: {service_select.value}")
        date_summary.set_text(f"Date: {date_picker.value or 'Select a date'}")
        time_summary.set_text(f"Time: {time_select.value}")
        pro_summary.set_text(f"Professional: {professional_select.value}")
        name = name_input.value.strip() if name_input.value else ''
        phone = phone_input.value.strip() if phone_input.value else ''
        email = email_input.value.strip() if email_input.value else ''
        if name or phone or email:
            customer_summary.set_text(f"Customer: {name or '—'}, {phone or '—'}, {email or '—'}")
        else:
            customer_summary.set_text("Customer: Your details will appear here once entered.")

    service_select.on('update:model-value', lambda _: update_summary())
    date_picker.on('update:model-value', lambda _: update_summary())
    time_select.on('update:model-value', lambda _: update_summary())
    professional_select.on('update:model-value', lambda _: update_summary())
    name_input.on('update:model-value', lambda _: update_summary())
    phone_input.on('update:model-value', lambda _: update_summary())
    email_input.on('update:model-value', lambda _: update_summary())
