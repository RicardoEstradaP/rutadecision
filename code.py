import streamlit as st

st.set_page_config(page_title="Ruta de Pruebas Estadísticas", layout="wide")

st.title("🔍 Ruta de Decisión para Seleccionar Pruebas Estadísticas")
st.markdown("Esta herramienta te guía paso a paso para saber qué prueba estadística usar. Pensada especialmente para psicología.")

st.markdown("---")
st.subheader("Paso 1: Objetivo del análisis")
step = st.radio(
    "¿Cuál es tu objetivo principal?",
    ["Selecciona una opción", "Comparar grupos", "Evaluar relación entre variables"],
    index=0,
    help="¿Quieres comparar grupos (como control vs experimental) o evaluar la relación entre variables (como ansiedad y autoestima)?"
)

if step == "Comparar grupos":
    st.subheader("Paso 2: Número de grupos")
    n_groups = st.radio("¿Cuántos grupos quieres comparar?", ["Selecciona", "2 grupos", "Más de 2 grupos"], index=0)

    if n_groups == "2 grupos":
        st.subheader("Paso 3: Tipo de muestras")
        tipo = st.radio("¿Las muestras son relacionadas o independientes?", ["Selecciona", "Relacionadas", "Independientes"], index=0)

        if tipo in ["Relacionadas", "Independientes"]:
            st.subheader("Paso 4: Supuestos de los datos")
            param = st.radio("¿Los datos cumplen normalidad y varianzas homogéneas?", ["Selecciona", "Sí", "No"], index=0)

            if param == "Sí":
                if tipo == "Relacionadas":
                    st.success("✅ Usa **t de Student para muestras relacionadas**")
                    st.markdown("**Ejemplo:** Comparar ansiedad antes y después de terapia en los mismos pacientes.")
                else:
                    st.success("✅ Usa **t de Student para muestras independientes**")
                    st.markdown("**Ejemplo:** Comparar ansiedad entre grupo control y experimental.")
            elif param == "No":
                if tipo == "Relacionadas":
                    st.success("✅ Usa **Wilcoxon**")
                    st.markdown("**Ejemplo:** Comparar autoestima antes y después de un taller con datos no normales.")
                else:
                    st.success("✅ Usa **U de Mann-Whitney**")
                    st.markdown("**Ejemplo:** Comparar empatía entre dos grupos distintos con datos no normales.")

    elif n_groups == "Más de 2 grupos":
        st.subheader("Paso 3: Tipo de muestras")
        tipo = st.radio("¿Las muestras son relacionadas o independientes?", ["Selecciona", "Relacionadas", "Independientes"], index=0)

        if tipo in ["Relacionadas", "Independientes"]:
            st.subheader("Paso 4: Supuestos de los datos")
            param = st.radio("¿Los datos cumplen normalidad y varianzas homogéneas?", ["Selecciona", "Sí", "No"], index=0)

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
                    st.markdown("**Ejemplo:** Comparar bienestar entre tres técnicas de intervención con datos no normales.")

elif step == "Evaluar relación entre variables":
    st.subheader("Paso 2: Tipo de variables")
    tipo_var = st.radio("¿Las variables son cuantitativas?", ["Selecciona", "Sí", "No o datos no normales"], index=0)

    if tipo_var == "Sí":
        st.subheader("Paso 3: Supuestos de normalidad y relación")
        relacion = st.radio("¿Tienen distribución normal y relación lineal?", ["Selecciona", "Sí", "No"], index=0)

        if relacion == "Sí":
            st.success("✅ Usa **Correlación de Pearson**")
            st.markdown("**Ejemplo:** Relación entre ansiedad y depresión en población clínica.")
        elif relacion == "No":
            st.success("✅ Usa **Correlación de Spearman**")
            st.markdown("**Ejemplo:** Relación entre horas de sueño y niveles de estrés.")

    elif tipo_var == "No o datos no normales":
        st.success("✅ Usa **Correlación de Spearman**")
        st.markdown("**Ejemplo:** Relación entre nivel socioeconómico (ordinal) y autoestima.")

# Footer
st.markdown(\"---\")
st.caption(\"Desarrollado para decisiones estadísticas en psicología.\")
