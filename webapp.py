import streamlit as st
import psycopg2
import requests
import pandas as pd
from datetime import datetime


def main():
    st.title("HACKNU umag & zapis.kz case")
    st.subheader(':cake: by tortiki_remastered')


if __name__ == '__main__':
    main()

st.markdown("""---""")
st.markdown('Для начала работы, выберите таблицу. Таблица sales работает с информацией о продажах. Таблица supplies работает с информацией о закупках. Таблица Report дает доступ к получению информации о продажах и закупках.')
st.markdown("""---""")

option1 = st.selectbox('TABLE', ('Supply','Sales', 'Reports'))
if option1 == 'Supply':
    st.markdown("""---""")
    st.markdown(
        'Здесь вы можете создавать, редактировать, удалять и просмотривать записи таблицы закупок.')
    st.markdown("""---""")
    option2 = st.selectbox('METHOD', ('GET BY BARCODE','GET BY ID', 'POST', 'PUT', 'DELETE'))
    if option2 == 'GET BY BARCODE':
        barcode = st.text_input("BARCODE", "4870204391510", max_chars=13)

        default_startdate_str = "2022/01/01"
        default_startdate = datetime.strptime(
            default_startdate_str, '%Y/%m/%d')
        from_date = st.date_input(
            "Enter a date and time", value=default_startdate, key=1)
        
        default_enddate_str = "2022/12/31"
        default_enddate = datetime.strptime(default_enddate_str, '%Y/%m/%d')
        to_date = st.date_input("Enter a date and time",
                                value=default_enddate, key=2)
        
        submitted = st.button("Submit")
        if submitted:
            api_url = "http://127.0.0.1:8000/api/supplies/"
            todo = {"fromTime": from_date.isoformat(),
                    "toTime": to_date.isoformat(), 
                    "barcode": barcode}

            response = requests.get(api_url, json=todo)
            data = response.json()

            if data:
                st.table(data)
            else:
                st.write("No data found for the given parameters.")

    elif option2 == 'POST':
        barcode = st.text_input("BARCODE", "1010101010")
        price =st.text_input("PRICE", "0")
        quantity = st.text_input("QUANTITY", "0")
        supplytime = st.text_input("SUPPLY TIME", "yyyy-MM-dd HH:mm:ss")
        submitted = st.button("Submit")
        if submitted:
            api_url = "http://127.0.0.1:8000/api/supplies/"
            todo = {"barcode": barcode,
                    "price": price, "quantity": quantity, "supplyTime": supplytime}
            response = requests.post(api_url, json=todo)
            data = response.json().update(todo)
            if data:
                st.table(data)
            else:
                st.write("Error occured. Try again. Possibly incorrect input form.")
    elif option2 == 'PUT':
        id = st.text_input("ID", "1")
        barcode = st.text_input("BARCODE", "")
        price = st.text_input("PRICE", "")
        quantity = st.text_input("QUANTITY", "")
        supplyTime=st.text_input("SUPPLY TIME", "yyyy-MM-dd HH:mm:ss")
        submitted = st.button("Submit")
        if submitted:
            api_url = "http://127.0.0.1:8000/api/supplies/{}".format(id)
            todo = {
                    "barcode": barcode,
                    "price": price,
                    "quantity":quantity,
                    "supplyTime": supplyTime
                    }
            response = requests.post(api_url, json=todo)
            if response.status_codes == 200:
                st.markdown("DONE")
            else:
                st.markdown("ERROR. TRY AGAIN")
    elif option2 == 'DELETE':
        id = st.text_input("ID", "1")
        submitted = st.button("Submit")
        if submitted:
            api_url = "http://127.0.0.1:8000/api/supplies/{}".format(id)
            todo = {
                    }
            response = requests.post(api_url, json=todo)
            
            if response.status_codes == 200:
                st.markdown("DONE")
            else:
                st.markdown("ERROR. TRY AGAIN")
    elif option2 == 'GET BY ID':
        id = st.text_input("ID", "1")
        submitted = st.button("Submit")
        if submitted:
            api_url = "http://127.0.0.1:8000/api/supplies/{}".format(id)
            todo = {
                    }
            response = requests.get(api_url)
            data = response.json()
            if data:
                st.table(data)
            else:
                st.markdown("No mtching data found.")
elif option1 == 'Sales':
    st.markdown("""---""")
    st.markdown(
        'Здесь вы можете создавать, редактировать, удалять и просмотривать записи таблицы продаж.')
    st.markdown("""---""")
    option2 = st.selectbox('METHOD', ('GET BY BARCODE','GET BY ID', 'POST', 'PUT', 'DELETE'))
    if option2 == 'GET BY BARCODE':
        barcode = st.text_input("BARCODE", "4870204391510", max_chars=13)

        default_startdate_str = "2022/01/01"
        default_startdate = datetime.strptime(
            default_startdate_str, '%Y/%m/%d')
        from_date = st.date_input(
            "Enter a date and time", value=default_startdate, key=1)
        
        default_enddate_str = "2022/12/31"
        default_enddate = datetime.strptime(default_enddate_str, '%Y/%m/%d')
        to_date = st.date_input("Enter a date and time",
                                value=default_enddate, key=2)
        
        submitted = st.button("Submit")
        if submitted:
            api_url = "http://127.0.0.1:8000/api/sales/"
            todo = {"fromTime": from_date.isoformat(),
                    "toTime": to_date.isoformat(), 
                    "barcode": barcode}

            response = requests.get(api_url, json=todo)
            data = response.json()

            if data:
                st.table(data)
            else:
                st.write("No data found for the given parameters.")

    elif option2 == 'POST':
        barcode = st.text_input("BARCODE", "1010101010")
        price =st.text_input("PRICE", "0")
        quantity = st.text_input("QUANTITY", "0")
        supplytime = st.text_input("SUPPLY TIME", "yyyy-MM-dd HH:mm:ss")
        submitted = st.button("Submit")
        if submitted:
            api_url = "http://127.0.0.1:8000/api/sales/"
            todo = {"barcode": barcode,
                    "price": price, "quantity": quantity, "supplyTime": supplytime}
            response = requests.post(api_url, json=todo)
            data = response.json().update(todo)
            if data:
                st.table(data)
            else:
                st.write("Error occured. Try again. Possibly incorrect input form.")
    elif option2 == 'PUT':
        id = st.text_input("ID", "1")
        barcode = st.text_input("BARCODE", "")
        price = st.text_input("PRICE", "")
        quantity = st.text_input("QUANTITY", "")
        supplyTime=st.text_input("SUPPLY TIME", "yyyy-MM-dd HH:mm:ss")
        submitted = st.button("Submit")
        if submitted:
            api_url = "http://127.0.0.1:8000/api/sales/{}".format(id)
            todo = {
                    "barcode": barcode,
                    "price": price,
                    "quantity":quantity,
                    "supplyTime": supplyTime
                    }
            response = requests.post(api_url, json=todo)
            if response.status_codes == 200:
                st.markdown("DONE")
            else:
                st.markdown("ERROR. TRY AGAIN")
    elif option2 == 'DELETE':
        id = st.text_input("ID", "1")
        submitted = st.button("Submit")
        if submitted:
            api_url = "http://127.0.0.1:8000/api/sales/{}".format(id)
            todo = {
                    }
            response = requests.post(api_url, json=todo)
            
            if response.status_codes == 200:
                st.markdown("DONE")
            else:
                st.markdown("ERROR. TRY AGAIN")
    elif option2 == 'GET BY ID':
        id = st.text_input("ID", "1")
        submitted = st.button("Submit")
        if submitted:
            api_url = "http://127.0.0.1:8000/api/sales/{}".format(id)
            todo = {
                    }
            response = requests.get(api_url)
            data = response.json()
            if data:
                st.table(data)
            else:
                st.markdown("No mtching data found.")
elif option1 == 'Reports':
    st.markdown("""---""")
    st.markdown(
        'Здесь вы можете получить репорт о прибыли за период с учетом себестоимости.')
    st.markdown("""---""")
    barcode = st.text_input("BARCODE", "4870204391510", max_chars=13)

    default_startdate_str = "2022/01/01"
    default_startdate = datetime.strptime(
        default_startdate_str, '%Y/%m/%d')
    from_date = st.date_input(
        "Enter a date and time", value=default_startdate, key=1)
    
    default_enddate_str = "2022/12/31"
    default_enddate = datetime.strptime(default_enddate_str, '%Y/%m/%d')
    to_date = st.date_input("Enter a date and time",
                            value=default_enddate, key=2)
    
    submitted = st.button("Submit")
    if submitted:
        api_url = "http://127.0.0.1:8000/api/report/"
        todo = {"fromTime": from_date.isoformat(),
                "toTime": to_date.isoformat(), 
                "barcode": barcode}

        response = requests.get(api_url, json=todo)
        data = response.json()

        if data:
            st.table(data)
        else:
            st.write("No data found for the given parameters.")
