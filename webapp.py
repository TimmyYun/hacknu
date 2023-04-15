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
    option2 = st.selectbox('METHOD', ('GET', 'POST', 'PUT', 'DELETE'))
    if option2 == 'GET':
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
        barcode = st.text_input("ID", "1010101010")
        date_time = st.text_input("FROM TIME", "yyyy-MM-dd HH:mm:ss")
        to_date = st.text_input("TO_DATE", "yyyy-MM-dd HH:mm:ss")
        submitted = st.button("Submit")
        if submitted:
            api_url = "http://127.0.0.1:8000/api/supplies/"
            todo = {"fromTime": from_date,
                    "toTime": to_date, "barcode": barcode}
            response = requests.post(api_url, json=todo)
            response.json()
elif option1 == 'Sales':
    st.markdown("""---""")
    st.markdown(
        'Здесь вы можете создавать, редактировать, удалять и просмотривать записи таблицы продаж.')
    st.markdown("""---""")
    option2 = st.selectbox('METHOD', ('GET', 'POST', 'PUT', 'DELETE'))
    if option2 == 'GET':
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
elif option1 == 'Reports':
    st.markdown("""---""")
    st.markdown(
        'Здесь вы можете получить репорт о прибыли за период с учетом себестоимости.')
    st.markdown("""---""")

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
# @st.experimental_memo(ttl=600)
# def run_query(query): #for read
#     with conn.cursor() as cur:
#         cur.execute(query)
#         return cur.fetchall()
# def run_query_c(query): #for CUD
#     with conn.cursor() as cur:
#         try:
#             cur.execute(query)
#         except:
#             cur.execute("rollback")
#             cur.execute(query)

# def show_disease_types():
#         try:
#             column1 = run_query("SELECT id FROM sales;")
#             column2 = run_query("SELECT description FROM diseasetype;")
#             st.write(pd.DataFrame({
#                 'ID': column1,
#                 'Description': column2,
#             }))
#         except:
#             st.write(pd.DataFrame([{
#                 'ID': 0,
#                 'Description': "",
#             }]))
# def show_diseases():
#     try:
#         column1 = run_query("SELECT disease_code FROM Disease;")
#         column2 = run_query("SELECT pathogen FROM Disease;")
#         column3 = run_query("SELECT description FROM Disease;")
#         column4 = run_query("SELECT id FROM Disease;")
#         # Print results.
#         st.write(pd.DataFrame({
#             'Disease code': column1,
#             'Pathogen': column2,
#             'Description' : column3,
#             'ID' : column4,
#         }))
#     except:
#         st.write(pd.DataFrame([{
#             'Disease code': "",
#             'Pathogen': "",
#             'Description' : "",
#             'ID' : 0
#         }]))
# def show_countries():
#     try:
#         column1 = run_query("SELECT cname FROM Country;")
#         column2 = run_query("SELECT population FROM Country;")
#         # Print results.
#         st.write(pd.DataFrame({
#             'Country': column1,
#             'Population': column2,
#         }))
#     except:
#         st.write(pd.DataFrame([{
#             'Country': "",
#             'Population': 0
#         }]))
# def show_discoveries():
#     try:
#         column1 = run_query("SELECT cname FROM Discover;")
#         column2 = run_query("SELECT disease_code FROM Discover;")
#         column3 = run_query("SELECT first_enc_date FROM Discover;")
#         # Print results.
#         st.write(pd.DataFrame({
#             'Country': column1,
#             'Disease code': column2,
#             'First encounter': column3
#         }))
#     except:
#         st.write(pd.DataFrame([{
#             'Country': "",
#             'Disease code': "",
#             'First encounter': ""
#         }]))
# def show_users():
#     try:
#         column1 = run_query("SELECT email FROM Users;")
#         column2 = run_query("SELECT name FROM Users;")
#         column3 = run_query("SELECT surname FROM Users;")
#         column4 = run_query("SELECT salary FROM Users;")
#         column5 = run_query("SELECT phone FROM Users;")
#         column6 = run_query("SELECT cname FROM Users;")
#         # Print results.
#         st.write(pd.DataFrame({
#             'Email': column1,
#             'Name': column2,
#             'Surname' : column3,
#             'Salary' : column4,
#             'Phone': column5,
#             'Country': column6,
#         }))
#     except:
#         st.write(pd.DataFrame([{
#             'Email': "",
#             'Name': "",
#             'Surname' : "",
#             'Salary' : 0,
#             'Phone': "",
#             'Country': "",
#         }]))
# def show_public_servants():
#     try:
#         column1 = run_query("SELECT email FROM Publicservant;")
#         column2 = run_query("SELECT department FROM Publicservant;")
#         # Print results.
#         st.write(pd.DataFrame({
#             'Email': column1,
#             'Department': column2,
#         }))
#     except:
#         st.write(pd.DataFrame([{
#             'Email': "",
#             'Department': "",
#         }]))
# def show_doctors():
#     try:
#         column1 = run_query("SELECT email FROM Doctor;")
#         column2 = run_query("SELECT degree FROM Doctor;")
#         # Print results.
#         st.write(pd.DataFrame({
#             'Email': column1,
#             'Degree': column2,
#         }))
#     except:
#         st.write(pd.DataFrame([{
#             'Email': "",
#             'Degree': "",
#         }]))
# def show_specialize():
#     try:
#         column1 = run_query("SELECT id FROM Specialize;")
#         column2 = run_query("SELECT email FROM Specialize;")
#         # Print results.
#         st.write(pd.DataFrame({
#             'ID': column1,
#             'Specialize': column2,
#         }))
#     except:
#         st.write(pd.DataFrame([{
#             'ID': 0,
#             'Specialize': "",
#         }]))
# def show_specialize():
#     try:
#         column1 = run_query("SELECT id FROM Specialize;")
#         column2 = run_query("SELECT email FROM Specialize;")
#         # Print results.
#         st.write(pd.DataFrame({
#             'ID': column1,
#             'Specialize': column2,
#         }))
#     except:
#         st.write(pd.DataFrame([{
#             'ID': 0,
#             'Specialize': "",
#         }]))
# def show_records():

#     try:
#         column1 = run_query("SELECT email FROM Record;")
#         column2 = run_query("SELECT cname FROM Record;")
#         column3 = run_query("SELECT disease_code FROM Record;")
#         column4 = run_query("SELECT total_deaths FROM Record;")
#         column5 = run_query("SELECT total_patients FROM Record;")
#         # Print results.
#         st.write(pd.DataFrame({
#             'Email': column1,
#             'Country': column2,
#             'Disease code': column3,
#             'Total deaths': column4,
#             'Total patients': column5,
#         }))
#     except:
#         st.write(pd.DataFrame([{
#             'Email': "",
#             'Country': "",
#             'Disease code': "",
#             'Total deaths': 0,
#             'Total patients': 0,
#         }]))

# def create_diseases():
#     new_val1 = st.text_input('Disease code')
#     new_val2 = st.text_input('Pathogen')
#     new_val3 = st.text_input('Description of the disease')
#     new_val4 = st.number_input('ID of the disease', step=1)
#     if new_val1 != "" and new_val2 != "" and new_val3 != "" and new_val4 != 0:
#         try:
#             run_query_c(f"INSERT INTO Disease VALUES ('{new_val1}', '{new_val2}', '{new_val3}', {new_val4});")
#         except:
#             run_query_c("CREATE TABLE Disease(disease_code varchar(50) PRIMARY KEY,pathogen varchar(20) NOT NULL,description varchar(140) NOT NULL,id integer NOT NULL,FOREIGN KEY (id) References DiseaseType (id) ON DELETE CASCADE ON UPDATE CASCADE);")
#             run_query_c(f"INSERT INTO Disease VALUES ('{new_val1}', '{new_val2}', '{new_val3}', {new_val4});")
# def create_disease_types():
#     new_val1 = st.number_input('ID of the disease', step=1)
#     new_val2 = st.text_input('Description of the disease')
#     if new_val1 != 0 and new_val2 != "":
#         try:
#             run_query_c(f"INSERT INTO Diseasetype VALUES ('{new_val1}', '{new_val2}');")

#         except:
#             run_query_c("CREATE TABLE Diseasetype(id integer PRIMARY KEY,description varchar(140) NOT NULL); ")
#             run_query_c(f"INSERT INTO Diseasetype VALUES ('{new_val1}', '{new_val2}');")

# def create_country():
#     new_val1 = st.text_input('Country')
#     new_val2 = st.number_input('Population', step=1)
#     if new_val1 != "" and new_val2 != 0:
#         try:
#             run_query_c(f"INSERT INTO Country VALUES ('{new_val1}', '{new_val2}');")

#         except:
#             run_query_c("CREATE TABLE Country(cname varchar(50) PRIMARY KEY,population bigint NOT NULL);")
#             run_query_c(f"INSERT INTO Country VALUES ('{new_val1}', '{new_val2}');")

# def create_discover():
#     new_val1 = st.text_input('Country')
#     new_val2 = st.text_input('Disease code')
#     new_val3 = st.text_input('First encounter date')
#     if new_val1 != "" and new_val2 != "" and new_val3 != "":
#         try:
#             run_query_c(f"INSERT INTO Discover VALUES ('{new_val1}', '{new_val2}', '{new_val3}');")

#         except:
#             run_query_c("CREATE TABLE Discover(cname varchar(50) NOT NULL,disease_code varchar(50) NOT NULL,first_enc_date date NOT NULL, FOREIGN KEY (disease_code) References Disease (disease_code) ON DELETE CASCADE ON UPDATE CASCADE, FOREIGN KEY (cname) References Country (cname) ON DELETE CASCADE ON UPDATE CASCADE); ")
#             run_query_c(f"INSERT INTO Discover VALUES ('{new_val1}', '{new_val2}', '{new_val3}');")

# def create_user():
#     new_val1 = st.text_input('Email')
#     new_val2 = st.text_input('Name')
#     new_val3 = st.text_input('Surname')
#     new_val4 = st.number_input('Salary', step=1)
#     new_val5 = st.text_input('Phone number')
#     new_val6 = st.text_input('Country')
#     if new_val1 != "" and new_val2 != "" and new_val3 != "" and new_val4 != 0 and new_val5 != "" and new_val6 != "":
#         try:
#             run_query_c(f"INSERT INTO Users VALUES ('{new_val1}', '{new_val2}', '{new_val3}', {new_val4}, '{new_val5}', '{new_val6}');")

#         except:
#             run_query_c("CREATE TABLE Users(email varchar(60) PRIMARY KEY,name varchar(30) NOT NULL,surname varchar(40) NOT NULL,salary integer,phone varchar(20) NOT NULL,cname varchar(50) NOT NULL,FOREIGN KEY (cname) References Country (cname) ON DELETE CASCADE ON UPDATE CASCADE);")
#             run_query_c(f"INSERT INTO Users VALUES ('{new_val1}', '{new_val2}', '{new_val3}', {new_val4}, '{new_val5}', '{new_val6}');")

# def create_public_servant():
#     new_val1 = st.text_input('Email')
#     new_val2 = st.text_input('Department')
#     if new_val1 != "" and new_val2 != "":
#         try:
#             run_query_c(f"INSERT INTO PublicServant VALUES ({new_val1}, '{new_val2}');")

#         except:
#             run_query_c("CREATE TABLE PublicServant(email varchar(60) UNIQUE, department varchar(50) NOT NULL,FOREIGN KEY (email) References Users (email) ON DELETE CASCADE ON UPDATE CASCADE);)")
#             run_query_c(f"INSERT INTO PublicServant VALUES ({new_val1}, '{new_val2}');")

# def create_doctor():
#     new_val1 = st.text_input('Email')
#     new_val2 = st.text_input('Degree')
#     if new_val1 != "" and new_val2 != "":
#         try:
#             run_query_c(f"INSERT INTO Doctor VALUES ('{new_val1}', '{new_val2}');")

#         except:
#             run_query_c("CREATE TABLE Doctor(email varchar(60) UNIQUE,degree varchar(20) NOT NULL,FOREIGN KEY (email) References Users (email) ON DELETE CASCADE ON UPDATE CASCADE); )")
#             run_query_c(f"INSERT INTO Doctor VALUES ('{new_val1}', '{new_val2}');")

# def create_specialize():
#     new_val1 = st.number_input('ID', step=1)
#     new_val2 = st.text_input('Email')
#     if new_val1 != 0 and new_val2 != "":
#         try:
#             run_query_c(f"INSERT INTO Specialize VALUES ({new_val1}, '{new_val2}');")

#         except:
#             run_query_c("CREATE TABLE Specialize(id integer NOT NULL,email varchar(60) NOT NULL,FOREIGN KEY (id) References DiseaseType (id) ON DELETE CASCADE ON UPDATE CASCADE,FOREIGN KEY (email) References Doctor (email) ON DELETE CASCADE ON UPDATE CASCADE);)")
#             run_query_c(f"INSERT INTO Specialize VALUES ({new_val1}, '{new_val2}');")

# def create_record():
#     new_val1 = st.text_input('Email')
#     new_val2 = st.text_input('Country')
#     new_val3 = st.text_input('Disease code')
#     new_val4 = st.number_input('Total deaths')
#     new_val5 = st.number_input('Total patients', step=1)
#     if new_val1 != "" and new_val2 != "" and new_val3 != "" and new_val4 != 0 and new_val5 != 0:
#         try:
#             run_query_c(f"INSERT INTO Record VALUES('{new_val1}', '{new_val2}', '{new_val3}', {new_val4}, {new_val5})")

#         except:
#             run_query_c("CREATE TABLE Record(email varchar(60) NOT NULL,cname varchar(50) NOT NULL, disease_code varchar(50) NOT NULL,total_deaths integer NOT NULL,total_patients integer NOT NULL,FOREIGN KEY (disease_code) References Disease (disease_code) ON DELETE CASCADE ON UPDATE CASCADE,FOREIGN KEY (cname) References Country (cname) ON DELETE CASCADE ON UPDATE CASCADE,FOREIGN KEY (email) References PublicServant (email) ON DELETE CASCADE ON UPDATE CASCADE);)")
#             run_query_c(f"INSERT INTO Record VALUES('{new_val1}', '{new_val2}', '{new_val3}', {new_val4}, {new_val5}")


# def update_disease_type():
#     1
# def update_disease():
#     row = st.number_input("Choose the row by id", step=1)
#     new_val1 = st.text_input('Disease code')
#     new_val2 = st.text_input('Pathogen')
#     new_val3 = st.text_input('Description of the disease')
#     new_val4 = st.number_input('ID of the disease', step=1)
#     if new_val1 != "" and new_val2 != "" and new_val3 != "" and new_val4 != 0:
#         try:
#             run_query_c(f"UPDATE Disease SET disease_code = '{new_val1}', pathogen = '{new_val2}', description = '{new_val3}', id = {new_val4} WHERE id = {row};")
#         except:
#             st.write("Can't update this value")
# def update_country():
#     row = st.text_input("Choose the row by country")
#     new_val1 = st.text_input('Country')
#     new_val2 = st.number_input('Population', step=1)
#     if new_val1 != "" and new_val2 != 0:
#         try:
#             run_query_c(f"UPDATE Country SET cname='{new_val1}', population = '{new_val2}' WHERE cname = '{row}';")
#         except:
#             st.write("Can't update this value")
# def update_discovery():
#     row = st.text_input("Choose the row by country")
#     new_val1 = st.text_input('Country')
#     new_val2 = st.text_input('Disease code')
#     new_val3 = st.text_input('First encounter date')
#     if new_val1 != "" and new_val2 != "" and new_val3 != "":
#         try:
#             run_query_c(f"UPDATE Discover SET cname = '{new_val1}', disease_code =  '{new_val2}', first_enc_date = '{new_val3}' WHERE cname = '{row}';")
#         except:
#             st.write("Can't update this value")
# def update_user():

#     row = st.text_input("Choose the row by email")
#     new_val1 = st.text_input('Email')
#     new_val2 = st.text_input('Name')
#     new_val3 = st.text_input('Surname')
#     new_val4 = st.number_input('Salary', step=1)
#     new_val5 = st.text_input('Phone number')
#     new_val6 = st.text_input('Country')
#     if new_val1 != "" and new_val2 != "" and new_val3 != "" and new_val4 != 0 and new_val5 != "" and new_val6 != "" :
#         try:
#             run_query_c(f"UPDATE Users SET email = '{new_val1}', name= '{new_val2}', surname= '{new_val3}', salary= {new_val4}, phone= '{new_val5}', cname= '{new_val6}' WHERE email={row};")
#         except:
#             st.write("Can't update this value")
# def update_public_servant():
#     row = st.text_input("Choose the row by email")
#     new_val1 = st.text_input('Email')
#     new_val2 = st.text_input('Department')
#     if new_val1 != "" and new_val2 != "":
#         try:
#             run_query_c(f"UPDATE PublicServant SET email='{new_val1}', department='{new_val2}' WHERE email={row};")
#         except:
#             st.write("Can't update this value")
# def update_doctor():
#     row = st.text_input("Choose the row by email")
#     new_val1 = st.text_input('Email')
#     new_val2 = st.text_input('Degree')
#     if new_val1 != "" and new_val2 != "":
#         try:
#             run_query_c(f"UPDATE Doctor SET email ='{new_val1}', degree= '{new_val2}' WHERE email={row};")
#         except:
#             st.write("Can't update this value")
# def update_specialize():
#     row = st.text_input("Choose the row by email")
#     new_val1 = st.number_input('ID', step=1)
#     new_val2 = st.text_input('Email')
#     if new_val1 != 0 and new_val2 != "":
#         try:
#             run_query_c(f"UPDATE Specialize SET id={new_val1}, email= '{new_val2}' WHERE email={row};")
#         except:
#             st.write("Can't update this value")
# def update_record():
#     row = st.text_input("Choose the row by email")
#     new_val1 = st.text_input('Email')
#     new_val2 = st.text_input('Country')
#     new_val3 = st.text_input("Disease code")
#     new_val4 = st.number_input('Total deaths')
#     new_val5 = st.number_input('Total patients', step=1)
#     if new_val1 != "" and new_val2 != "" and new_val3 != "" and new_val4 != 0 and new_val5 != 0:
#         try:
#             run_query_c(f"UPDATE Record SET email='{new_val1}', cname= '{new_val2}', disease_code= '{new_val3},'total_deaths= {new_val4}, total_patients={new_val5} WHERE email={row}")
#         except:
#             st.write("Can't update this value")

# def delete_disease_type():

#     run_query_c("DROP TABLE Diseasetype CASCADE;")
# def delete_disease():
#     run_query_c("DROP TABLE Disease CASCADE;")
# def delete_country():
#     run_query_c("DROP TABLE Country CASCADE;")
# def delete_discover():
#     run_query_c("DROP TABLE Discover CASCADE;")
# def delete_users():
#     run_query_c("DROP TABLE Users CASCADE;")
# def delete_public_servant():
#     run_query_c("DROP TABLE Publicservant CASCADE;")
# def delete_doctor():
#     run_query_c("DROP TABLE Doctor CASCADE;")
# def delete_specialize():
#     run_query_c("DROP TABLE Specialize CASCADE;")
# def delete_record():
#     run_query_c("DROP TABLE Record CASCADE;")
# option = st.selectbox('Choose an option', ('CREATE', 'READ', 'UPDATE', 'DELETE'))

# if option == 'CREATE':
#     option2 = st.selectbox('Choose the table', ('Disease Types', 'Diseases', 'Countries', 'Discovery', 'Users', 'Public Servants', 'Doctor', 'Specialize', 'Record'))
#     if option2 == "Disease Types":
#         create_disease_types()
#         show_disease_types()
#     elif option2 == "Diseases":
#         create_diseases()
#         show_diseases()
#     elif option2 == "Countries":
#         create_country()
#         show_countries()
#     elif option2 == "Users":
#         create_user()
#         show_users()
#     elif option2 == "Public Servants":
#         create_public_servant()
#         show_public_servants()
#     elif option2 == 'Doctor':
#         create_doctor()
#         show_doctors()
#     elif option2 == "Specialize":
#         create_specialize()
#         show_specialize()
#     elif option2 == "Record":
#         create_record()
#         show_records()
# elif(option == 'READ'):
#     if st.checkbox("Show disease types" ):
#         show_disease_types()
#     if st.checkbox("Show diseases"):
#         show_diseases()
#     if st.checkbox("Show countries"):
#         show_countries()
#     if st.checkbox("Show discoveries of diseases"):
#         show_discoveries()
#     if st.checkbox("Show users"):
#         show_users()
#     if st.checkbox("Show public servants"):
#         show_public_servants()
#         if st.checkbox("Show records"):
#             show_records()
#     if st.checkbox("Show doctors"):
#         show_doctors()
#         if st.checkbox("Show specialize"):
#             show_specialize()

# elif(option == 'UPDATE'):
#     option2 = st.selectbox('Choose which table to update', ('Disease Types', 'Diseases', 'Countries', 'Discoveries', 'Users', 'Public Servants', 'Doctor', 'Specialize', 'Record'))
#     if option2 == "Disease Types":
#         show_disease_types()
#         row = st.number_input("Choose the row by id", step=1)
#         new_val1 = st.number_input('ID of the disease', step=1)
#         new_val2 = st.text_input('Description of the disease')
#         if new_val1 != 0 and new_val2 != "" and st.button("UPDATE"):
#             try:
#                 run_query_c(f"UPDATE Diseasetype SET id = {new_val1}, description = '{new_val2}' WHERE id = {row};")
#             except:
#                 st.write("Can't update this value")
#         show_disease_types()
#         st.experimental_rerun()
#     elif option2 == "Diseases":
#         update_disease()
#         show_diseases()
#         st.experimental_rerun()
#     elif option2 == "Countries":
#         update_country()
#         show_countries()
#         st.experimental_rerun()
#     elif option2 == 'Discoveries':
#         update_discovery()
#         show_discoveries()
#         st.experimental_rerun()
#     elif option2 == "Users":
#         update_user()
#         show_users()
#         st.experimental_rerun()
#     elif option2 == "Public Servants":
#         update_public_servant()
#         show_public_servants()
#         st.experimental_rerun()
#     elif option2 == "Doctor":
#         update_doctor()
#         show_doctors()
#         st.experimental_rerun()
#     elif option2 == "Specialize":
#         update_specialize()
#         show_specialize()
#         st.experimental_rerun()
#     elif option2 == "Record":
#         update_record()
#         show_records()
#         st.experimental_rerun()

# elif(option=="DELETE"): #delete
#     option2 = st.selectbox('Choose a table', ('Disease Types', 'Diseases', 'Countries', 'Discoveries', 'Users', 'Public Servants', 'Doctor', 'Specialize', 'Record'))
#     if option2 == "Disease Types":
#         row = st.number_input("Choose the row by id", step=1)
#         try:
#             run_query_c(f"DELETE FROM Diseasetype where id = {row}")
#         except:
#             st.write("Can't delete this row")
#         show_disease_types()
#         if st.button("Delete this table"):
#             delete_disease_type()
#             st.experimental_rerun()
#     elif option2 == "Diseases":
#         if st.button("Delete this table"):
#             delete_disease()
#         show_diseases()
#     elif option2 == "Countries":
#         if st.button("Delete this table"):
#             delete_country()
#             st.experimental_rerun()
#         show_countries()
#     elif option2 == 'Discoveries':
#         if st.button("Delete this table"):
#             delete_discover()
#             st.experimental_rerun()
#         show_discoveries()
#     elif option2 == "Users":
#         if st.button("Delete this table"):
#             delete_users()
#             st.experimental_rerun()
#         show_users()
#     elif option2 == "Public Servants":
#         if st.button("Delete this table"):
#             delete_public_servant()
#             st.experimental_rerun()
#         show_public_servants()
#     elif option2 == "Doctor":
#         if st.button("Delete this table"):
#             delete_doctor()
#             st.experimental_rerun()
#         show_doctors()
#     elif option2 == "Specialize":
#         if st.button("Delete this table"):
#             delete_specialize()
#             st.experimental_rerun()
#         show_specialize()
#     elif option2 == "Record":
#         if st.button("Delete this table"):
#             delete_record()
#             st.experimental_rerun()
#         show_records()
