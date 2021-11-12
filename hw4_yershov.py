# Создать VIEW функцию которая возвращает список уникальных имён (FirstName) из таблицы Customers.
#
# def get_unique_name() -> '/unique_name'
# Для получения уникальных значений можно использовать средства Python, а можно это решить при помощи SQL, если
# воспользоваться предложением `GROUP BY`.

from flask import Flask
from db import execute_query
from formater import list_rec2html_br

app = Flask(__name__)


@app.route('/unique_name')
def get_unique_name():
    sql = 'select "FirstName" from customers'

    records = execute_query(sql)
    result = []
    for _ in records:
        result.append(_[0])

    return list_rec2html_br(sorted(set(result)))


@app.route('/unique_name_sql')
def get_unique_name_sql():
    sql = 'select "FirstName" from customers group by "FirstName"'

    records = execute_query(sql)
    result = []
    for _ in records:
        result.append(_[0])

    return list_rec2html_br(result)


app.run(debug=True)
