import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Ruta de Pruebas Estadísticas", layout="wide")

st.title("🔍 Ruta de Decisión para Seleccionar Pruebas Estadísticas")
st.markdown("Esta herramienta te ayuda a decidir qué prueba estadística usar según tus datos. Pensada especialmente para psicología.")

# Paso inicial
step = st.radio("¿Cuál es tu objetivo principal?", [
    "Comparar grupos",
    "Evaluar relación entre variables"
])

if step == "Comparar grupos":
    n_groups = st.radio("¿Cuántos grupos quieres comparar?", ["2 grupos", "Más de 2 grupos"])

    if n_groups == "2 grupos":
        related = st.radio("¿Las muestras son relacionadas o independientes?", ["Relacionadas", "Independientes"])

        parametric = st.radio("¿Tus datos cumplen con los supuestos de normalidad y varianza homogénea?", ["Sí", "No"])

        if related == "Relacionadas":
            if parametric == "Sí":
                st.success("✅ Usa la prueba **t de Student para muestras relacionadas**")
                st.markdown("**Ejemplo:** Comparar el nivel de ansiedad antes y después de una intervención psicológica en los mismos pacientes.")
            else:
                st.success("✅ Usa la prueba **Wilcoxon**")
                st.markdown("**Ejemplo:** Comparar puntajes de autoestima antes y después de un taller cuando los datos no son normales.")
        else:
            if parametric == "Sí":
                st.success("✅ Usa la prueba **t de Student para muestras independientes**")
                st.markdown("**Ejemplo:** Comparar el estrés entre grupo control y grupo experimental.")
            else:
                st.success("✅ Usa la prueba **U de Mann-Whitney**")
                st.markdown("**Ejemplo:** Comparar niveles de empatía entre dos grupos con distribución no normal.")

    else:
        related = st.radio("¿Las muestras son relacionadas o independientes?", ["Relacionadas", "Independientes"])
        parametric = st.radio("¿Tus datos cumplen con los supuestos de normalidad y varianza homogénea?", ["Sí", "No"])

        if related == "Relacionadas":
            if parametric == "Sí":
                st.success("✅ Usa **ANOVA de medidas repetidas**")
                st.markdown("**Ejemplo:** Evaluar el efecto de 3 tipos de terapia sobre la ansiedad en los mismos participantes.")
            else:
                st.success("✅ Usa **Prueba de Friedman**")
                st.markdown("**Ejemplo:** Evaluar cambios en depresión en 3 momentos distintos sin normalidad.")
        else:
            if parametric == "Sí":
                st.success("✅ Usa **ANOVA de un factor**")
                st.markdown("**Ejemplo:** Comparar el rendimiento académico entre tres técnicas de estudio.")
            else:
                st.success("✅ Usa **Kruskal-Wallis**")
                st.markdown("**Ejemplo:** Comparar el nivel de bienestar subjetivo en 3 grupos con datos no normales.")

elif step == "Evaluar relación entre variables":
    tipo_var = st.radio("¿Tus variables son cuantitativas?", ["Sí", "No o tienen distribución no normal"])

    if tipo_var == "Sí":
        normal_lineal = st.radio("¿Tienen distribución normal y relación lineal?", ["Sí", "No"])

        if normal_lineal == "Sí":
            st.success("✅ Usa **Correlación de Pearson**")
            st.markdown("**Ejemplo:** Relación entre puntuación en ansiedad y depresión en población clínica.")
        else:
            st.success("✅ Usa **Correlación de Spearman**")
            st.markdown("**Ejemplo:** Relación entre horas de sueño y niveles de estrés cuando no hay normalidad.")
    else:
        st.success("✅ Usa **Correlación de Spearman**")
        st.markdown("**Ejemplo:** Relación entre nivel socioeconómico (ordinal) y autoestima.")

# Footer
st.markdown("---")
st.caption("Desarrollado para decisiones estadísticas en psicología.")
