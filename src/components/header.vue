<script setup>
import logo from '../assets/IMG/logoSF.png'
import relojDigital from './Reloj.vue'
import {ref,onMounted} from 'vue'
</script>
<template>
<div class="nav">
    <img class="inicio" :src="logo" alt="">
    <div class="titulo-contenedor">
        <h1 class="titulo">Dashboard Rendimientos Clasificación</h1>
    </div>
    <relojDigital/>
</div>

</template>
<style>
/* Estilos generales para el encabezado */
.nav {
    display: flex;
    align-items: center;
    background-color: #515A5A; /* Color de fondo */
    border-radius: 8px; /* Bordes redondeados */
    padding: 10px 20px; /* Espaciado interno */
    box-shadow: 0 6px 4px rgba(0, 0, 0, 0.1); /* Sombra */
}

/* Estilos para el logotipo */
.inicio {
    width: 50px; /* Ancho del logotipo */
    height: auto; /* Altura automática para mantener la proporción */
}

/* Estilos para el título */
.titulo-contenedor {
    margin: 0 auto; /* Centrar el contenido */
    text-align: center; /* Alinear el texto al centro */
    flex-grow: 1;
}

.titulo {
  margin: 0; /* Eliminar márgenes predeterminados */
  font-family: 'Georgia ', sans-serif; /* Cambiar la fuente a una fuente llamativa */
  color: #b99e78; /* Color del texto */
  font-size: 36px; /* Tamaño de fuente */
}

</style>