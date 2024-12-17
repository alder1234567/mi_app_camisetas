import reflex as rx

@rx.page(route="/home")

def home() -> rx.Component:
    return rx.mobile_and_tablet(
        rx.vstack(
            rx.link(rx.icon("arrow-left",margin_top="3vh"),href="/splash"),
            rx.avatar(src="/oso.jpg", border_radius="50%", width="150px", height="150px",margin_left="14vh", margin_top="3vh"),
            rx.text("jose gonzales", text_align="center", margin_left="17vh"),
            rx.hstack(
                rx.vstack(rx.link(rx.text(rx.hstack("descargas",rx.icon("download"))),href="/download"),
                          rx.hstack(
                              rx.image(src="/oso.jpg"),
                              rx.image(src="/oso.jpg"),
                               width="70px", height="70px"),
                          rx.hstack(
                              rx.image(src="/oso.jpg"),
                              rx.image(src="/oso.jpg"),
                              width="70px", height="70px"),
                          rx.hstack(
                              rx.image(src="/oso.jpg"),
                              rx.image(src="/oso.jpg"),
                              width="70px", height="70px"),
                          rx.hstack(
                              rx.image(src="/oso.jpg"),
                              rx.image(src="/oso.jpg"),
                              width="70px", height="70px"),
                          rx.image(src="/oso.jpg", width="70px", height="70px"),
                          margin_left="3vh"
                          ),
                rx.vstack(rx.link(rx.text(rx.hstack("favoritos",rx.icon("bookmark"))),href="/favorite"),
                          rx.image(src="/oso.jpg",width="90px", height="90px"),
                          rx.image(src="/oso.jpg",width="90px", height="90px"),
                          rx.image(src="/oso.jpg",width="90px", height="90px"),
                          rx.image(src="/oso.jpg",width="90px", height="90px"),
                          margin_left="12vh"
                          ),
                          margin_top="3vh"
                )
            )
        )