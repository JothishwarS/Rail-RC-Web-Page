import streamlit as st
import pandas as pd
from openpyxl import load_workbook
import requests
from io import BytesIO

# ---------- Pages for BS8666:2005 ----------
def bs2005_actual_dia():
    st.markdown("<h3 style='text-align:center;'>Actual Dia - BS8666:2005</h3>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center;'>"
                "<img src='https://raw.githubusercontent.com/JothishwarS/Rail-RC-Web-Page/90ae0691b4786735d50bf779745f209cb70a7703/Actual%20Dia%202005.jpg' width='600'>"
                "</div>", unsafe_allow_html=True)

def bs2005_min_u_bar():
    st.markdown("<h3 style='text-align:center;'>Min U-bar Leg Values - BS8666:2005</h3>", unsafe_allow_html=True)
    raw_pdf = "https://raw.githubusercontent.com/JothishwarS/Rail-RC-Web-Page/90ae0691b4786735d50bf779745f209cb70a7703/BS8666-2005%20MIn%20legs%20of%20U-bars.pdf"
    viewer_url = f"https://docs.google.com/viewer?embedded=true&url={raw_pdf}"
    st.markdown(f"<div style='display:flex; justify-content:center;'>"
                f"<iframe src='{viewer_url}' width='750' height='750'></iframe></div>",
                unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center;'><a href='{raw_pdf}' download>📥 Download PDF</a></p>", unsafe_allow_html=True)

def bs2005_link_sc():
    st.markdown("<h3 style='text-align:center;'>Link SC Min Leg Values - BS8666:2005</h3>", unsafe_allow_html=True)
    excel_url = "https://raw.githubusercontent.com/JothishwarS/Rail-RC-Web-Page/64dcd0c287033258e878d3f44b8c54787610c6cd/Links%20SC%20Min%20values%20for%20BS8666.xlsx"

    shape_ranges_2005 = {
        "Shape Code 33": "A1:D10",
        "Shape Code 51": "A11:E20",
        "Shape Code 63": "A21:E30",
    }

    selected_shape = st.selectbox("Select Shape Code", list(shape_ranges_2005.keys()))

    try:
        response = requests.get(excel_url)
        response.raise_for_status()
        wb = load_workbook(BytesIO(response.content), data_only=True)
        ws = wb.active

        cell_range = shape_ranges_2005[selected_shape]
        data = ws[cell_range]
        table = [[cell.value for cell in row] for row in data]
        max_len = max(len(r) for r in table)
        normalized_table = [r + [None] * (max_len - len(r)) for r in table]

        df = pd.DataFrame(normalized_table[1:], columns=normalized_table[0])

        styled_df = df.style.set_table_styles([
            {'selector': 'th', 'props': [('background-color', '#FFF9C4'), ('text-align', 'center'), ('border', '1px solid black')]},
            {'selector': 'td', 'props': [('text-align', 'center'), ('border', '1px solid gray')]}
        ]).set_properties(**{'padding': '8px'}).hide(axis='index')

        st.markdown("<h4 style='text-align:center;'>Leg Values Table</h4>", unsafe_allow_html=True)

        html_table = styled_df.to_html()
        styled_html = (
        "<div style='display:flex; justify-content:center;'>"
        "<div style='border:1px solid #ccc; padding:10px;'>"
        + html_table +
        "</div></div>"
        )
        st.markdown(styled_html, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Could not load Excel or shape code range:\n{e}")

def bs2005_shape_codes():
    st.markdown("<h3 style='text-align:center;'>Shape Code List - BS8666:2005</h3>", unsafe_allow_html=True)
    raw_pdf = "https://raw.githubusercontent.com/JothishwarS/Rail-RC-Web-Page/90ae0691b4786735d50bf779745f209cb70a7703/BS8666-2005%20Shape%20Code%20List.pdf"
    viewer_url = f"https://docs.google.com/viewer?embedded=true&url={raw_pdf}"
    st.markdown(f"<div style='display:flex; justify-content:center;'>"
                f"<iframe src='{viewer_url}' width='750' height='750'></iframe></div>",
                unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center;'><a href='{raw_pdf}' download>📥 Download PDF</a></p>", unsafe_allow_html=True)

# ---------- Pages for BS8666:2020 ----------
def bs2020_actual_dia():
    st.markdown("<h3 style='text-align:center;'>Actual Dia - BS8666:2020</h3>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center;'>"
                "<img src='https://raw.githubusercontent.com/JothishwarS/Rail-RC-Web-Page/90ae0691b4786735d50bf779745f209cb70a7703/Actual%20Dia%202020.jpg' width='700'>"
                "</div>", unsafe_allow_html=True)

def bs2020_min_u_bar():
    st.markdown("<h3 style='text-align:center;'>Min U-bar Leg Values - BS8666:2020</h3>", unsafe_allow_html=True)
    raw_pdf = "https://raw.githubusercontent.com/JothishwarS/Rail-RC-Web-Page/90ae0691b4786735d50bf779745f209cb70a7703/BS8666-2020%20MIn%20legs%20of%20U-bars.pdf"
    viewer_url = f"https://docs.google.com/viewer?embedded=true&url={raw_pdf}"
    st.markdown(f"<div style='display:flex; justify-content:center;'>"
                f"<iframe src='{viewer_url}' width='750' height='750'></iframe></div>",
                unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center;'><a href='{raw_pdf}' download>📥 Download PDF</a></p>", unsafe_allow_html=True)

def bs2020_link_sc():
    st.markdown("<h3 style='text-align:center;'>Link SC Min Leg Values - BS8666:2020</h3>", unsafe_allow_html=True)
    excel_url = "https://raw.githubusercontent.com/JothishwarS/Rail-RC-Web-Page/64dcd0c287033258e878d3f44b8c54787610c6cd/Links%20SC%20Min%20values%20for%20BS8666.xlsx"

    shape_ranges_2020 = {
        "Shape Code 33": "G1:J10",
        "Shape Code 51": "G11:K20",
        "Shape Code 63": "G21:K30",
    }

    selected_shape = st.selectbox("Select Shape Code", list(shape_ranges_2020.keys()))

    try:
        response = requests.get(excel_url)
        response.raise_for_status()
        wb = load_workbook(BytesIO(response.content), data_only=True)
        ws = wb.active

        cell_range = shape_ranges_2020[selected_shape]
        data = ws[cell_range]

        # Normalize row length
        table = [[cell.value for cell in row] for row in data]
        max_len = max(len(r) for r in table)
        normalized_table = [r + [None] * (max_len - len(r)) for r in table]

        df = pd.DataFrame(normalized_table[1:], columns=normalized_table[0])

        # Style the DataFrame
        styled_df = df.style.set_table_styles([
            {'selector': 'th', 'props': [('background-color', '#E1F5FE'), ('text-align', 'center'), ('border', '1px solid black')]},
            {'selector': 'td', 'props': [('text-align', 'center'), ('border', '1px solid gray')]}
        ]).set_properties(**{'padding': '8px'}).hide(axis='index')

        st.markdown("<h4 style='text-align:center;'>Leg Values Table</h4>", unsafe_allow_html=True)
        html_table = styled_df.to_html()
        styled_html = (
        "<div style='display:flex; justify-content:center;'>"
        "<div style='border:1px solid #ccc; padding:10px;'>"
        + html_table +
        "</div></div>"
        )
        st.markdown(styled_html, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Could not load Excel or shape code range:\n{e}")

def bs2020_shape_codes():
    st.markdown("<h3 style='text-align:center;'>Shape Code List - BS8666:2020</h3>", unsafe_allow_html=True)
    raw_pdf = "https://raw.githubusercontent.com/JothishwarS/Rail-RC-Web-Page/90ae0691b4786735d50bf779745f209cb70a7703/BS8666-2020%20Shape%20Code%20List.pdf"
    viewer_url = f"https://docs.google.com/viewer?embedded=true&url={raw_pdf}"
    st.markdown(f"<div style='display:flex; justify-content:center;'>"
                f"<iframe src='{viewer_url}' width='750' height='750'></iframe></div>",
                unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center;'><a href='{raw_pdf}' download>📥 Download PDF</a></p>", unsafe_allow_html=True)

# ---------- Main App ----------
def main():
    st.sidebar.title("Standard Selector")
    standard = st.sidebar.selectbox("Choose a standard:", ["Select...", "BS8666:2005", "BS8666:2020", "Lap Values"])

    if standard == "BS8666:2005":
        st.markdown("<h1 style='text-align:center;'>BS8666:2005 Tools</h1>", unsafe_allow_html=True)
        option = st.sidebar.selectbox("Select tool:", [
            "Actual Dia",
            "Min U-bar Leg Values",
            "Link SC Min Leg Values",
            "Shape Code List"
        ])
        if option == "Actual Dia":
            bs2005_actual_dia()
        elif option == "Min U-bar Leg Values":
            bs2005_min_u_bar()
        elif option == "Link SC Min Leg Values":
            bs2005_link_sc()
        elif option == "Shape Code List":
            bs2005_shape_codes()

    elif standard == "BS8666:2020":
        st.markdown("<h1 style='text-align:center;'>BS8666:2020 Tools</h1>", unsafe_allow_html=True)
        option = st.sidebar.selectbox("Select tool:", [
            "Actual Dia",
            "Min U-bar Leg Values",
            "Link SC Min Leg Values",
            "Shape Code List"
        ])
        if option == "Actual Dia":
            bs2020_actual_dia()
        elif option == "Min U-bar Leg Values":
            bs2020_min_u_bar()
        elif option == "Link SC Min Leg Values":
            bs2020_link_sc()
        elif option == "Shape Code List":
            bs2020_shape_codes()

    elif standard == "Lap Values":
        st.set_page_config(layout="wide")
        st.subheader("EC2 Lap Values by Concrete Grade")

        excel_url = "https://raw.githubusercontent.com/JothishwarS/Rail-RC-Web-Page/main/EC2%20Lap%20Excel.xlsx"

        try:
            response = requests.get(excel_url)
            response.raise_for_status()
            wb = load_workbook(BytesIO(response.content), data_only=True)
            ws = wb.active

            grade_ranges = {
                "Concrete Grade C20/25": "A1:K9",
                "Concrete Grade C25/30": "A10:K18",
                "Concrete Grade C28/35": "A19:K27",
                "Concrete Grade C30/37": "A28:K36",
                "Concrete Grade C32/40": "A37:K45",
                "Concrete Grade C35/45": "A46:K54",
                "Concrete Grade C40/50": "A55:K63",
                "Concrete Grade C45/55": "A64:K72",
                "Concrete Grade C50/60": "A73:K81",
            }

            selected_grade = st.selectbox("Select Concrete Grade", list(grade_ranges.keys()))
            cell_range = grade_ranges[selected_grade]
            data = ws[cell_range]

            table = [[cell.value for cell in row] for row in data]
            df = pd.DataFrame(table[1:], columns=table[0])

            # Style DataFrame with black header borders
            styled_df = df.style.set_table_styles([
                {
                    'selector': 'th',
                    'props': [
                        ('background-color', '#C8E6C9'),
                        ('text-align', 'center'),
                        ('border', '1px solid black')
                    ]
                },
                {
                    'selector': 'td',
                    'props': [
                        ('text-align', 'center'),
                        ('border', '1px solid gray')
                    ]
                }
            ]).set_properties(**{'padding': '8px'}).hide(axis='index')

            # Render table
            st.markdown("<h4 style='text-align:center;'>Lap Values Table</h4>", unsafe_allow_html=True)

            html_table = styled_df.to_html()
            styled_html = (
                "<div style='display:flex; justify-content:center;'>"
                "<div style='border:1px solid #ccc; padding:10px;'>"
                + html_table +
                "</div></div>"
            )
            st.markdown(styled_html, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"❌ Could not load Excel or parse range:\n{e}")

    else:
        st.title("Welcome to The Rail Structures RC Code of Standards Web Page")
        st.write("Please choose a code of standard from the Standard Selector to begin.")

if __name__ == "__main__":
    main()
