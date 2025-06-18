import streamlit as st

# Configuración general
st.set_page_config(page_title="Ruta de Pruebas Estadísticas", layout="wide")

# Estilos CSS
st.markdown("""
<style>
    .main {
        background-color: #f7f9fc;
        color: #333333;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    h1, h2, h3, h4 {
        color: #2c3e50;
        font-weight: 600;
    }
    .stRadio > div > label {
        padding: 8px 15px;
        border-radius: 8px;
        background-color: #e1ecf4;
        margin-bottom: 8px;
        display: block;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stRadio > div > label:hover {
        background-color: #c8d7ea;
    }
    .stRadio > div > label[data-baseweb="radio"] input:checked + span {
        background-color: #3498db !important;
        color: white !important;
    }
    .stSuccess {
        background-color: #d1f0d1;
        border-left: 5px solid #27ae60;
        padding: 10px 15px;
        border-radius: 6px;
        margin-top: 15px;
    }
    hr {
        border: none;
        height: 1px;
        background-color: #dce3e8;
        margin: 25px 0;
    }
</style>
""", unsafe_allow_html=True)

# Título y subtítulo
st.title("🌟 Ruta de Decisión Estadística")
st.markdown("**¿No sabes qué prueba estadística usar?**\n\nSigue esta ruta sencilla paso a paso para elegir la prueba ideal según tus datos.")
st.markdown("---")

# Paso 1
st.subheader("Paso 1: Objetivo del análisis")
step = st.radio(
    "¿Cuál es tu objetivo principal?",
    ["Selecciona una opción", "Comparar grupos", "Evaluar relación entre variables", "Predecir una variable"],
    index=0,
    help="Elige si deseas comparar grupos, explorar relaciones o hacer predicciones."
)

# Opción: Comparar grupos
if step == "Comparar grupos":
    st.subheader("Paso 2: Número de grupos")
    n_groups = st.radio(
        "¿Cuántos grupos quieres comparar?",
        ["Selecciona", "2 grupos", "Más de 2 grupos"],
        index=0
    )

    if n_groups == "2 grupos":
        st.subheader("Paso 3: Tipo de muestras")
        tipo = st.radio(
            "¿Las muestras son relacionadas o independientes?",
            ["Selecciona", "Relacionadas", "Independientes"],
            index=0
        )

        if tipo in ["Relacionadas", "Independientes"]:
            st.subheader("Paso 4: Supuestos de los datos")
            param = st.radio(
                "¿Los datos cumplen normalidad y varianzas homogéneas?",
                ["Selecciona", "Sí", "No"],
                index=0
            )

            if param == "Sí":
                if tipo == "Relacionadas":
                    st.success("✅ Usa **t de Student para muestras relacionadas**")
                    st.markdown("**Ejemplo:** Comparar ansiedad antes y después de una intervención en los mismos pacientes.")
                else:
                    st.success("✅ Usa **t de Student para muestras independientes**")
                    st.markdown("**Ejemplo:** Comparar ansiedad entre grupo control y grupo experimental.")
            elif param == "No":
                if tipo == "Relacionadas":
                    st.success("✅ Usa **Wilcoxon**")
                    st.markdown("**Ejemplo:** Comparar autoestima antes y después de un taller con datos no normales.")
                else:
                    st.success("✅ Usa **U de Mann-Whitney**")
                    st.markdown("**Ejemplo:** Comparar empatía entre dos grupos distintos con datos no normales.")

    elif n_groups == "Más de 2 grupos":
        st.subheader("Paso 3: Tipo de muestras")
        tipo = st.radio(
            "¿Las muestras son relacionadas o independientes?",
            ["Selecciona", "Relacionadas", "Independientes"],
            index=0
        )

        if tipo in ["Relacionadas", "Independientes"]:
            st.subheader("Paso 4: Supuestos de los datos")
            param = st.radio(
                "¿Los datos cumplen normalidad y varianzas homogéneas?",
                ["Selecciona", "Sí", "No"],
                index=0
            )

            if param == "Sí":
                if tipo == "Relacionadas":
                    st.success("✅ Usa **ANOVA de medidas repetidas**")
                    st.markdown("**Ejemplo:** Evaluar efecto de 3 terapias en los mismos pacientes.")
                else:
                    st.success("✅ Usa **ANOVA de un factor**")
                    st.markdown("**Ejemplo:** Comparar estrés entre tres grupos distintos.")
            elif param == "No":
                if tipo == "Relacionadas":
                    st.success("✅ Usa **Friedman**")
                    st.markdown("**Ejemplo:** Comparar ansiedad en 3 momentos distintos sin normalidad.")
                else:
                    st.success("✅ Usa **Kruskal-Wallis**")
                    st.markdown("**Ejemplo:** Comparar bienestar entre tres técnicas con datos no normales.")

# Opción: Evaluar relación entre variables
elif step == "Evaluar relación entre variables":
    st.subheader("Paso 2: Tipo de variables")
    tipo_var = st.radio(
        "¿Las variables son cuantitativas?",
        ["Selecciona", "Sí", "No o datos no normales"],
        index=0
    )

    if tipo_var == "Sí":
        st.subheader("Paso 3: Supuestos de relación")
        relacion = st.radio(
            "¿Tienen distribución normal y relación lineal?",
            ["Selecciona", "Sí", "No"],
            index=0
        )

        if relacion == "Sí":
            st.success("✅ Usa **Correlación de Pearson**")
            st.markdown("**Ejemplo:** Relación entre ansiedad y depresión en población clínica.")
        elif relacion == "No":
            st.success("✅ Usa **Correlación de Spearman**")
            st.markdown("**Ejemplo:** Relación entre horas de sueño y niveles de estrés.")

    elif tipo_var == "No o datos no normales":
        st.success("✅ Usa **Correlación de Spearman**")
        st.markdown("**Ejemplo:** Relación entre nivel socioeconómico (ordinal) y autoestima.")

# Opción: Predecir una variable
elif step == "Predecir una variable":
    st.subheader("Paso 2: Tipo de variables involucradas")
    pred_var = st.radio(
        "¿La variable que quieres predecir es cuantitativa?",
        ["Selecciona", "Sí", "No"],
        index=0
    )

    if pred_var == "Sí":
        st.subheader("Paso 3: Número de predictores")
        n_preds = st.radio(
            "¿Cuántas variables usarás para predecir?",
            ["Selecciona", "Una", "Dos o más"],
            index=0
        )

        if n_preds == "Una":
            st.subheader("Paso 4: Supuestos del modelo")
            sup = st.radio(
                "¿Relación lineal, normalidad y homocedasticidad?",
                ["Selecciona", "Sí", "No"],
                index=0
            )

            if sup == "Sí":
                st.success("✅ Usa **Regresión lineal simple**")
                st.markdown("**Ejemplo:** Predecir estatura a partir del peso.")
            elif sup == "No":
                st.success("✅ Usa **Modelos no paramétricos o transformación de datos**")
                st.markdown("**Ejemplo:** Si la relación no es lineal, intenta transformación logarítmica o una regresión no paramétrica.")

        elif n_preds == "Dos o más":
            st.subheader("Paso 4: Supuestos del modelo")
            sup = st.radio(
                "¿Se cumplen linealidad, normalidad, homocedasticidad y no multicolinealidad?",
                ["Selecciona", "Sí", "No"],
                index=0
            )

            if sup == "Sí":
                st.success("✅ Usa **Regresión lineal múltiple**")
                st.markdown("**Ejemplo:** Predecir nivel de estrés usando horas de sueño y apoyo social.")
            elif sup == "No":
                st.success("✅ Considera **regresión robusta o regularización**")
                st.markdown("**Ejemplo:** Usa regresión de Ridge, Lasso o técnicas no paramétricas.")

    elif pred_var == "No":
        st.success("✅ Usa **Regresión logística binaria o multinomial**")
        st.markdown("**Ejemplo:** Predecir si una persona tiene ansiedad (sí/no) a partir de variables cuantitativas.")

st.markdown("---")
st.caption("✨ Ricardo Estrada")
