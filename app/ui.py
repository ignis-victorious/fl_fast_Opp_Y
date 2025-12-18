#
#  Import LIBRARIES
import flet as ft
import requests

#  Import FILES
#  ______________________


def build_ui(page: ft.Page) -> None:
    main_message = ft.Text(value="Input two numbers", size=40)
    # main_message = ft.Text(value="Flet plus FastAPI Demo", size=40)

    # create input fields for two numbers
    input_a = ft.TextField(label="First Number", value="2", width=200)
    input_b = ft.TextField(label="Second Number", value="4", width=200)

    def call_api(e):
        num_a = int(input_a. value)
        num_b = int(input_b.value)
    
        main_message. value = "Calculating... "
        page.update() 

        def make_request():
            response = requests.post("http://localhost:8550/api/add",json={"a":num_a,"b":num_b}, timeout=10) 
            data = response.json()
            main_message. value = f"Result: {data['result']}"
            page.update() 
        page.run_thread(make_request)

    def get_health() -> None:
        response: requests.Response = requests.get(url="http://0.0.0.0:8550/api/health")
        data = response.json()
        main_message.value = f"Health status: {data['status']}"
        page.update()  # type: ignore
        # pass

    health_button = ft.Button(content="get health", on_click=lambda e: page.run_thread(handler=get_health))
    calculate_button = ft.Button(content="Calculate", on_click=call_api)
    page.add(ft.Row(controls=[input_a, input_b, calculate_button]), main_message, health_button)
