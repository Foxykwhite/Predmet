import dash
from dash import dcc, html, dash_table, Input, Output
import requests
import pandas as pd

# Настройки API NoCodeDB
API_URL = "https://wa7do48r.nocodb.com/api/v1/db/data/noco/pasoibnqa50ffip/"
TABLES = {
    "Users": "mz3bz9ea8gpqk5h/views/vw2r89pcwax9odme",
    "Products": "mwe6sjazzfgpp0k/views/vwxcq3uh93l2hscy",
    "Orders": "mvi86romvhumuc6/views/vwc2td9n6wx3nwxz",
    "Item Orders": "mrj6y58hns0lzk6/views/vw9utx2urbgrnvsh"
}
HEADERS = {
    "xc-token": "a5b8vd1z3T2QSEQ-P5Dfio6mfjRgBLywKFkRuvo9"  # Замени на свой токен
}

# Функция для получения данных
def fetch_data(table_name, endpoint):
    url = f"{API_URL}{endpoint}?offset=0&limit=100&includeSortAndFilterColumns=true"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data.get('list', []))

        # Применяем преобразования только к Orders и Item Orders
        if table_name in ["Orders", "Item Orders"]:
            for col in df.columns:
                df[col] = df[col].apply(lambda x: str(x) if isinstance(x, (dict, list)) else x)

            # Переименовываем столбцы, если есть русские буквы
            df.columns = [col.encode('ascii', 'ignore').decode('ascii') for col in df.columns]

            # Заполняем NaN пустыми строками
            df.fillna("", inplace=True)

        return df
    else:
        print("Ошибка запроса:", response.status_code, response.text)
        return pd.DataFrame()

# Инициализация Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Данные из NoCodeDB"),
    dcc.Dropdown(
        id="table-dropdown",
        options=[{"label": name, "value": name} for name in TABLES.keys()],
        value="Users",  # Значение по умолчанию
        clearable=False
    ),
    dash_table.DataTable(
        id="data-table",
        page_size=10
    )
])

# Callback для обновления таблицы
@app.callback(
    Output("data-table", "columns"),
    Output("data-table", "data"),
    Input("table-dropdown", "value")
)
def update_table(selected_table):
    df = fetch_data(selected_table, TABLES[selected_table])
    return [{"name": col, "id": col} for col in df.columns], df.to_dict("records")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)
