<script>
    export default{
        name:"relojDigital", 
        data(){
            return{
                horas: 0,
                minutos:0,
                segundos:0
            }
        },
        mounted(){
            setInterval(() => this.setTiempo(),1000)
        },
        methods:{
            setTiempo() {
                const date = new Date();
                let horas = date.getHours();
                let minutos = date.getMinutes();
                let segundos = date.getSeconds();
                horas  = horas <= 9 ? `${horas}`.padStart(2,0): horas;
                minutos  = minutos <= 9 ? `${minutos}`.padStart(2,0): minutos;
                segundos  = segundos <= 9 ? `${segundos}`.padStart(2,0): segundos;
                this.horas = horas;
                this.minutos = minutos;
                this.segundos = segundos;
            }
        }
    }
</script>
<template>
    <div class="container">
        <div class="reloj">
            <div class="horas">{{ horas }}</div>
            <div class="divisor">:</div>
            <div class="minutos">{{ minutos }}</div>
            <div class="divisor">:</div>
            <div class="segundos">{{ segundos }}</div>
        </div>
    </div>
</template>
<style>
.reloj{
    display: inline-flex;
    font-family: '', sans-serif;
    font-size: 45px;
    font-weight: bold;
    color: #FDFEFE;
}
</style>