import reflex as rx

@rx.page(route="/umboarding1")

def umboarding1() -> rx.Component:
    return rx.mobile_and_tablet(
        rx.vstack(
            rx.image(src="/oso.jpg"),
            rx.text("diseños de camisetas, personalizables, elije tu camiseta favorita y pruebalo sin nececidad de comprarlo",
                     text_align="center",
                     margin_top="5vh"),
            rx.hstack(
                rx.box(
                    bg="blue",
                    width="30px",
                    height="10px",
                    border_radius="5px",
                    margin="5px"),
                rx.box(
                    bg="#000000",
                    width="30px",
                    height="10px",
                    border_radius="5px",
                    margin="5px"),
                rx.box(
                    bg="#000000",
                    width="30px",
                    height="10px",
                    border_radius="5px",
                    margin="5px"),
                    margin_top="17vh",
                    margin_left="14vh"),
            rx.link(rx.button("SIGUIENTE"),margin_left="17vh",href="/umboarding2")
        )
    )