import reflex as rx

@rx.page(route="/download")

def download() -> rx.Component:
    return rx.mobile_and_tablet(
        rx.vstack(
            rx.link(rx.icon("arrow-left",margin_top="3vh", margin_bottom="7vh"),href="/home"),
            rx.hstack(
                rx.image(src="/oso.jpg"),
                rx.image(src="/oso.jpg"),
                rx.image(src="/oso.jpg"),
                width="110px", height="110px"),
            rx.hstack(
                rx.image(src="/oso.jpg"),
                rx.image(src="/oso.jpg"),
                rx.image(src="/oso.jpg"),
                width="110px", height="110px", margin_top="3vh"),
            rx.hstack(
                rx.image(src="/oso.jpg"),
                rx.image(src="/oso.jpg"),
                rx.image(src="/oso.jpg"),
                width="110px", height="110px",margin_top="3vh"),
            rx.hstack(
                rx.image(src="/oso.jpg"),
                rx.image(src="/oso.jpg"),
                rx.image(src="/oso.jpg"),
                width="110px", height="110px",margin_top="3vh"),
                margin_left="1.5vh"
            )
    )