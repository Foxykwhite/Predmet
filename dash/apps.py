import dash
from dash import dcc, html
import requests
import json

# Константы NoCodeDB
API_BASE_URL = "https://your-nocodedb-instance.com"  # Замени на свой URL
API_KEY = "your_api_key_here"  # Замени на свой API-ключ
TABLE_NAME = "questions"  # Название таблицы

def get_data():
    """Получает данные из NoCodeDB."""
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(f"{API_BASE_URL}/api/{TABLE_NAME}", headers=headers)
    if response.status_code == 200:
        return response.json()
    return []

# Инициализация Dash
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("Данные из NoCodeDB"),
    dcc.Interval(id='interval', interval=5000, n_intervals=0),  # Автообновление
    html.Ul(id='data-list')
])

@app.callback(
    dash.Output('data-list', 'children'),
    [dash.Input('interval', 'n_intervals')]
)
def update_data(_):
    """Обновляет список данных из NoCodeDB."""
    data = get_data()
    return [html.Li(item.get("question_text", "Нет данных")) for item in data]

if __name__ == "__main__":
    app.run_server(debug=True)