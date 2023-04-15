import streamlit as st
import psycopg2
import requests
import pandas as pd
from datetime import datetime
from datetime import time


def main():
    st.title("HACKNU umag & zapis.kz case")
    st.subheader(':cake: by tortiki_remastered')


if __name__ == '__main__':
    main()

st.markdown("""---""")
st.markdown('Для начала работы, выберите таблицу. Таблица sales работает с информацией о продажах. Таблица supplies работает с информацией о закупках. Таблица Report дает доступ к получению информации о продажах и закупках.')
st.markdown("""---""")

option1 = st.selectbox('TABLE', ('Supply', 'Sales', 'Reports'))
default_time = time(0, 0)
default_startdate_str = "2022/01/01"
default_startdate = datetime.strptime(default_startdate_str, '%Y/%m/%d')
default_enddate_str = "2022/12/31"
default_enddate = datetime.strptime(default_enddate_str, '%Y/%m/%d')

if option1 == 'Supply':
    st.markdown("""---""")
    st.markdown('Здесь вы можете создавать, редактировать, удалять и просмотривать записи таблицы закупок.')
    st.markdown("""---""")
    option2 = st.selectbox('METHOD', ('GET BY BARCODE','GET BY ID', 'POST', 'PUT', 'DELETE'))
    if option2 == 'GET BY BARCODE':
        barcode = st.text_input("BARCODE", "4870204391510", max_chars=13)

        col1, col2 = st.columns(2)
        from_date = col1.date_input(
            "Enter start date and time", value=default_startdate, key=1)
        from_time = col2.time_input(
            "Select a time:", default_time, step=300, key=2)
        start_datetime = datetime.combine(from_date, from_time)

        col3, col4 = st.columns(2)

        to_date = col3.date_input("Enter end date and time",
                                  value=default_enddate, key=3)
        to_time = col4.time_input(
            "Select a time:", default_time, step=300, key=4)
        to_datetime = datetime.combine(to_date, to_time)

        submitted = st.button("Submit")
        if submitted:
            api_url = "http://127.0.0.1:8000/api/supplies/"
            todo = {"fromTime": start_datetime.isoformat(),
                    "toTime": to_datetime.isoformat(),
                    "barcode": barcode}

            response = requests.get(api_url, json=todo)
            data = response.json()

            if data:
                st.table(data)
            else:
                st.write("No data found for the given parameters.")

    elif option2 == 'POST':
        barcode = st.text_input("BARCODE", "1010101010")
        price = st.text_input("PRICE", "0")
        quantity = st.text_input("QUANTITY", "0")

        col1, col2 = st.columns(2)
        to_date = col1.date_input("Enter end date and time",
                                  value=default_enddate, key=1)
        to_time = col2.time_input(
            "Select a time:", default_time, step=300, key=2)
        supplytime = datetime.combine(to_date, to_time)

        submitted = st.button("Submit")
        if submitted:
            api_url = "http://127.0.0.1:8000/api/supplies/"
            todo = {"barcode": barcode,
                    "price": price, 
                    "quantity": quantity, 
                    "supplyTime": supplytime.isoformat()}
            response = requests.post(api_url, json=todo)
            data = response.json()
            if data:
                st.table(data)
            else:
                st.write(
                    "Error occured. Try again. Possibly incorrect input form.")
                
    elif option2 == 'PUT':
        id = st.text_input("ID", "1")
        barcode = st.text_input("BARCODE", "123123")
        price = st.text_input("PRICE", "1")
        quantity = st.text_input("QUANTITY", "1")
        col1, col2 = st.columns(2)
        to_date = col1.date_input("Enter end date and time",
                                  value=default_enddate, key=1)
        to_time = col2.time_input(
            "Select a time:", default_time, step=300, key=2)
        supplyTime = datetime.combine(to_date, to_time)


        submitted = st.button("Submit")
        if submitted:
            api_url = "http://127.0.0.1:8000/api/supplies/{}/".format(id)
            todo = {
                    "id": id,
                    "barcode": barcode,
                    "price": price,
                    "quantity":quantity,
                    "supplyTime": supplyTime.isoformat()
                    }
            response = requests.put(api_url, json=todo)
            if response.status_code == 200:
                st.markdown("DONE")
            else:
                st.markdown("ERROR. TRY AGAIN")
    elif option2 == 'DELETE':
        id = st.text_input("ID", "1")
        submitted = st.button("Submit")
        if submitted:
            api_url = "http://127.0.0.1:8000/api/supplies/{}/".format(id)
            response = requests.delete(api_url)
            
            if response.status_code == 200:
                st.markdown("DONE")
            else:
                st.markdown("ERROR. TRY AGAIN")
    elif option2 == 'GET BY ID':
        id = st.text_input("ID", "1")
        submitted = st.button("Submit")
        if submitted:
            api_url = "http://127.0.0.1:8000/api/supplies/{}/".format(id)
            todo = {
                    }
            response = requests.get(api_url)
            try:
                data = response.json()
                st.table(data)
            except:
                st.markdown("No matching data found.")

elif option1 == 'Sales':
    st.markdown("""---""")
    st.markdown(
        'Здесь вы можете создавать, редактировать, удалять и просмотривать записи таблицы закупок.')
    st.markdown("""---""")
    option2 = st.selectbox('METHOD', ('GET BY BARCODE','GET BY ID', 'POST', 'PUT', 'DELETE'))
    if option2 == 'GET BY BARCODE':
        barcode = st.text_input("BARCODE", "4870204391510", max_chars=13)

        col1, col2 = st.columns(2)
        from_date = col1.date_input(
            "Enter start date and time", value=default_startdate, key=1)
        from_time = col2.time_input(
            "Select a time:", default_time, step=300, key=2)
        start_datetime = datetime.combine(from_date, from_time)

        col3, col4 = st.columns(2)

        to_date = col3.date_input("Enter end date and time",
                                  value=default_enddate, key=3)
        to_time = col4.time_input(
            "Select a time:", default_time, step=300, key=4)
        to_datetime = datetime.combine(to_date, to_time)

        submitted = st.button("Submit")
        if submitted:
            api_url = "http://127.0.0.1:8000/api/sales/"
            todo = {"fromTime": start_datetime.isoformat(),
                    "toTime": to_datetime.isoformat(),
                    "barcode": barcode}

            response = requests.get(api_url, json=todo)
            data = response.json()

            if data:
                st.table(data)
            else:
                st.write("No data found for the given parameters.")

    elif option2 == 'POST':
        barcode = st.text_input("BARCODE", "1010101010")
        price = st.text_input("PRICE", "0")
        quantity = st.text_input("QUANTITY", "0")

        col1, col2 = st.columns(2)
        to_date = col1.date_input("Enter end date and time",
                                  value=default_enddate, key=1)
        to_time = col2.time_input(
            "Select a time:", default_time, step=300, key=2)
        saletime = datetime.combine(to_date, to_time)

        submitted = st.button("Submit")
        if submitted:
            api_url = "http://127.0.0.1:8000/api/sales/"
            todo = {"barcode": barcode,
                    "price": price, 
                    "quantity": quantity, 
                    "saleTime": saletime.isoformat()}
            response = requests.post(api_url, json=todo)
            data = response.json()
            if data:
                st.table(data)
            else:
                st.write(
                    "Error occured. Try again. Possibly incorrect input form.")
                
    elif option2 == 'PUT':
        id = st.text_input("ID", "1")
        barcode = st.text_input("BARCODE", "123123")
        price = st.text_input("PRICE", "1")
        quantity = st.text_input("QUANTITY", "1")
        col1, col2 = st.columns(2)
        to_date = col1.date_input("Enter end date and time",
                                  value=default_enddate, key=1)
        to_time = col2.time_input(
            "Select a time:", default_time, step=300, key=2)
        supplyTime = datetime.combine(to_date, to_time)


        submitted = st.button("Submit")
        if submitted:
            api_url = "http://127.0.0.1:8000/api/sales/{}/".format(id)
            todo = {
                    "id": id,
                    "barcode": barcode,
                    "price": price,
                    "quantity":quantity,
                    "saleTime": supplyTime.isoformat()
                    }
            response = requests.put(api_url, json=todo)
            if response.status_code == 200:
                st.markdown("DONE")
            else:
                st.markdown("ERROR. TRY AGAIN")
    elif option2 == 'DELETE':
        id = st.text_input("ID", "1")
        submitted = st.button("Submit")
        if submitted:
            api_url = "http://127.0.0.1:8000/api/sales/{}/".format(id)
            response = requests.delete(api_url)
            
            if response.status_code == 200:
                st.markdown("DONE")
            else:
                st.markdown("ERROR. TRY AGAIN")
    elif option2 == 'GET BY ID':
        id = st.text_input("ID", "1")
        submitted = st.button("Submit")
        if submitted:
            api_url = "http://127.0.0.1:8000/api/sales/{}/".format(id)
            todo = {
                    }
            response = requests.get(api_url)
            try:
                data = response.json()
                st.table(data)
            except:
                st.markdown("No matching data found.")

elif option1 == 'Reports':
    st.markdown("""---""")
    st.markdown(
        'Здесь вы можете получить репорт о прибыли за период с учетом себестоимости.')
    st.markdown("""---""")
    barcode = st.text_input("BARCODE", "4870204391510", max_chars=13)

    col1, col2 = st.columns(2)
    start_date = col1.date_input(
        "Enter start date and time", value=default_startdate, key=5)
    start_time = col2.time_input(
        "Select a time:", default_time, step=300, key=6)
    startTime = datetime.combine(start_date, start_time)

    col3, col4 = st.columns(2)
    end_date = col3.date_input("Enter end date and time",
                              value=default_enddate, key=7)
    end_time = col4.time_input("Select a time:", default_time, step=300, key=8)
    endTime = datetime.combine(end_date, end_time)

    submitted = st.button("Submit")
    if submitted:
        api_url = "http://127.0.0.1:8000/api/report/"
        todo = {"fromTime": startTime.isoformat(),
                "toTime": endTime.isoformat(),
                "barcode": barcode}

        response = requests.get(api_url, json=todo)
        data = response.json()

        if data:
            st.table(data)
        else:
            st.write("No data found for the given parameters.")
