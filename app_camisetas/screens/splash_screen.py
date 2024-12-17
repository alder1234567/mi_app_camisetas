import reflex as rx

@rx.page(route="/splash")

def splash() -> rx.Component:
    return rx.mobile_and_tablet(
        rx.container(
            rx.color_mode.button(position="top-right"),
            rx.vstack(
                rx.link(rx.avatar(src="/oso.jpg", width="200px", height="200px", padding="10px", margin_bottom="35px", border_radius="50%"),href="/umboarding1"),
                rx.text("app_camisetas", size="6"),
                display="flex",
                align_items="center",
                margin_top="24vh",
                height="100vh"
            ),
        ),
    )