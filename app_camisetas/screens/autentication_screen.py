import reflex as rx

@rx.page(route="/autentication")

def autentication() -> rx.Component:
    return rx.mobile_and_tablet(
        rx.vstack(
            rx.link(rx.icon("arrow-left",margin_top="19px"),href="/umboarding1", margin_left="-40vh"),
            rx.avatar(src="/oso.jpg", border_radius="50%", width="150px", height="150px", margin_top="9vh"),
            rx.text("""Inicie Sesion o registrese""", text_align="center", margin_top="5vh"),
            rx.text("para poder ingresar"),
            rx.link(rx.button("INICIAR SESION",width="20vh"),href="/login",margin_top="5vh"),
            rx.link(rx.button("REGISTRARTE",width="18vh"),href="/register",margin_top="4vh"),
            rx.hstack(),
             align_items="center"
        )
    )