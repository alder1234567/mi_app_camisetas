import reflex as rx

@rx.page(route="/login")

def login() -> rx.Component:
    return rx.mobile_and_tablet(
        rx.vstack(
            rx.link(rx.icon("arrow-left",margin_top="19px", margin_left="-5vh"),href="/autentication"),
            rx.text("CORREO ELECTRONICO", margin_top="10vh"),
            rx.input(placeholder="ingrese correo electronico...", width="70%", border_whidth="2px", height="5vh"),
            rx.text("CONTASEÑA",margin_top="7vh"),
            rx.input(placeholder="ingrese contraseña...", width="70%", border_whidth="2px", height="5vh"),
            rx.link(rx.button("SIGUIENTE",margin_top="15vh", margin_left="7.5vh", width="20vh"),href="/home"),
            margin_left="5vh"
        )
    )