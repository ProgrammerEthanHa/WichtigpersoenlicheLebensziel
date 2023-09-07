import streamlit as st
import pandas as pd
import altair as alt

st.header("Wie wichtig ist für Sie das jeweilige persönliche Lebensziel?")
st.subheader("")

source = pd.DataFrame({
        'Anteil (%)': [88, 80, 78, 75, 75, 73, 70, 65, 62, 60, 38, 30],
        'Ziel': ['Gute Ausbildung', 'Partnerschaft', 'Finanzielle Absicherung', 'Selbstbestimmung und Invidualität', 'Eigene Kinder haben', 'Das Leben heute genießen', 'Gesünder leben', 'Berufliche Entwickelung', 'Genügend Raum für Freizeit und Hobbies', 'Besitz der eigenen vier Wände', 'Die Welt entdecken', 'Sich gesellschaftlich engagieren']
})
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil (%):Q',
        x='Ziel:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis: 1003 Befragte; 20005
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Statista research Department")