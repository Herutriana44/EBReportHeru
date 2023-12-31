# "https://docs.google.com/spreadsheets/d/1XFtZiRM1PoEIj6enN1XAZJBEWU8Be4dJa0pyFtJ5ZGU/gviz/tq?tqx=out:csv&sheet=List%20Paper"

import streamlit as st
import pandas as pd

button1_color = "#018205"
nav_color = "#018205"
jumbotron_color = "#73ff77"
body_color = "#b7f7b9"  # Updated body background color

st.set_page_config(
    page_title="Progress Penelitian Heru Triana"
)

file_path = "https://docs.google.com/spreadsheets/d/1XFtZiRM1PoEIj6enN1XAZJBEWU8Be4dJa0pyFtJ5ZGU/gviz/tq?tqx=out:csv&sheet=List%20Paper"
data_path = "https://docs.google.com/spreadsheets/d/1XFtZiRM1PoEIj6enN1XAZJBEWU8Be4dJa0pyFtJ5ZGU/gviz/tq?tqx=out:csv&sheet=Patient"
df = pd.read_csv(file_path)
# Mendapatkan nilai unik dari kolom "PIC"
pic_values = df["PIC"].unique()

# Menambahkan dropdown berdasarkan nilai kolom "PIC"
selected_pic = st.selectbox("Pilih PIC:", pic_values)

# Filter DataFrame berdasarkan nilai yang dipilih dari dropdown
filtered_df = df[df["PIC"] == selected_pic].reset_index(drop=True)

empty_data_count = filtered_df['Tujuan paper'].isnull().sum()
non_empty_data_count = filtered_df['Tujuan paper'].count()

jumlah_data = empty_data_count+non_empty_data_count

# Menampilkan jumlah data yang kosong
st.markdown(f"""
    
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
            <style>
                a {{
                    text-decoration: none;
                    color: white;
                }}
            .jumbotron {{
            background-color: {jumbotron_color};
            padding: 20px;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
        }}
        .footer {{
            text-align: center;
            padding: 10px;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: {nav_color};
            border-top: 1px solid #dee2e6;
            color: white;
        }}
            </style>
        
""",unsafe_allow_html=True)
st.markdown(
    f"""
    <div id="jumbotron" class="jumbotron">
        <h1>Progress Penelitian Meta Analisis Epidermolysis Bullosa - Heru Triana</h1>
        <h4>jumlah paper yang belum dibaca {empty_data_count} dari total {jumlah_data} paper</h4>
        <h4>Jumlah paper yang sudah dibaca: {non_empty_data_count} dari total {jumlah_data} paper</h4>
        <a href="{file_path}" class="btn btn-primary" style='text-decoration: none;'>
            Link Download list paper yang dibaca
         </a>
    </div>
    """
, unsafe_allow_html=True)

# """
# <a href="{data_path}" class="btn btn-primary" style='text-decoration: none;'>
#             Link Download Data Analisis Pasien
#          </a>
# """
