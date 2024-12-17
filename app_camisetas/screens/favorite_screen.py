import reflex as rx

@rx.page(route="/favorite")

def favorite() -> rx.Component:
    return rx.mobile_and_tablet(
        rx.vstack(
            rx.link(rx.icon("arrow-left",margin_top="2vh"),href="/home"),
            rx.text("FAVORITOS",margin_top="3vh"),
            rx.hstack(
                rx.image(src="/oso.jpg",width="115px", height="135px",margin_left="4vh"),
                rx.icon(tag="heart", color="red",zise="2em",margin_left="15vh",margin_top="6vh"),
                margin_top="2vh"
                ),
            rx.hstack(
                rx.image(src="/oso.jpg",width="115px", height="135px",margin_left="4vh"),
                rx.icon(tag="heart", color="red",zise="2em",margin_left="15vh",margin_top="6vh")
                ),
            rx.hstack(
                rx.image(src="/oso.jpg",width="115px", height="135px",margin_left="4vh"),
                rx.icon(tag="heart", color="red",zise="2em",margin_left="15vh",margin_top="6vh")
                ),
            rx.hstack(
                rx.image(src="/oso.jpg",width="115px", height="135px",margin_left="4vh"),
                rx.icon(tag="heart", color="red",zise="2em",margin_left="15vh",margin_top="6vh")
                ),
            )
        )