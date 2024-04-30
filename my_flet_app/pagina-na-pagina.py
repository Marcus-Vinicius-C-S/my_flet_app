import flet as ft

def main(page: ft.Page):
    def open_pagelet_end_drawer(e):
        pagelet.end_drawer.open = True
        pagelet.end_drawer.update()

    pagelet = ft.Pagelet(
        appbar=ft.AppBar(
            title=ft.Text("Página na Página"), bgcolor=ft.colors.AMBER_700, color=ft.colors.WHITE
        ),
        content=ft.Text("Corpo da Página", color=ft.colors.WHITE), 
        bgcolor=ft.colors.GREEN_700,
        bottom_app_bar=ft.BottomAppBar(
            bgcolor=ft.colors.BLUE,
            shape=ft.NotchShape.CIRCULAR,
            content=ft.Row(
                controls=[
                    ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE),
                    ft.Container(expand=True),
                    ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
                    ft.IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.RED_700),
                ]
            ),
        ),
        end_drawer=ft.NavigationDrawer(
            controls=[
                ft.NavigationDrawerDestination(
                    icon=ft.icons.ADD_TO_HOME_SCREEN_SHARP, label="Item 1"
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.ADD_COMMENT, label="Item 2"
                ),
            ],
        ),
        floating_action_button=ft.FloatingActionButton(
            "Abrir", on_click=open_pagelet_end_drawer,  bgcolor=ft.colors.RED_800, 
        ),
        floating_action_button_location=ft.FloatingActionButtonLocation.CENTER_DOCKED,
        width=400,
        height=400,
    )

    page.add(pagelet)


ft.app(target=main)