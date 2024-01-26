<script>
import axios from 'axios';  
import Header  from './components/header.vue';

export default {
  components: {
      //traer el header
      Header
    },
  data() {
    return {
      datos: [],
    };
  },
  methods: {
    async obtenerData() {
      try {
        const fecha = new Date();
        const year = fecha.getFullYear();
        const month = (fecha.getMonth() + 1).toString().padStart(2, '0');
        const day = fecha.getDate().toString().padStart(2, '0');
        const fechaHoy = `${year}${month}${day}`;
        console.log(fechaHoy)

        const response = await axios.get(`http://172.19.10.8:8087/obtener_datos?parametro1=${fechaHoy}&parametro2=${fechaHoy}`);
        this.datos = response.data;

         // Filtrar los datos según el valor de CODPRO
        const filteredDatos_AL = this.datos.filter(item => item.CODPRO === 'AL').sort((a, b) =>  b.REND_HR - a.REND_HR);

        const filteredDatos_RO = this.datos.filter(item => item.CODPRO === 'RO').sort((a, b) =>  b.REND_HR - a.REND_HR);
        // Preparar los datos para Google Charts
        const data_grafico_AL = [['nombre', 'Rendimiento']];
        filteredDatos_AL.forEach(item => {
          data_grafico_AL.push([item.NOMBRE, item.REND_HR])

        });
        const data_grafico_RO = [['nombre', 'Rendimiento']];
        filteredDatos_RO.forEach(item => {
          data_grafico_RO.push([item.NOMBRE, item.REND_HR])
        });

        // Cargar Google Charts y dibujar el gráfico
        google.charts.load('current', { packages: ['corechart'] });
        google.charts.setOnLoadCallback(() => {
          console.log("Google Charts cargado correctamente");
          this.drawChart(data_grafico_AL, 'valoresAL','ALSTROEMELIA');
          this.drawChart(data_grafico_RO, 'valoresRO','ROSA');
      });
      } catch (error) {
        console.error(error);
      }
    },
    drawChart(data_grafico,containerID, title_secction) {
      console.log(data_grafico)
      if  (!data_grafico.length){
        console.log('aun no hay datos')
        return;
      }
      const data = google.visualization.arrayToDataTable([
        ['Nombre', 'Rendimiento', { role: 'style' }, { role: 'annotation' }],
        ...data_grafico.slice(1).map(item => [item[0], item[1], 'color: #5D6D7E', item[1] != null ? item[1].toFixed(0) : null]),
      ]);

      const options = {
        title: title_secction,
        titleTextStyle:{
          fontSize: 30,  // Tamaño de fuente del título
          bold: true,
          italic: false,
          textAlign: 'center'

        },
        width: 750,
        height: '100%',
        chartArea: {
          left: 300, // Ajusta según tus necesidades
          width: '100%', // También puedes ajustar el ancho total del área del gráfico
        },

        bar: { groupWidth: '80%' },
        legend: { position: 'none' },
        annotations: {
          textStyle: {
              fontName: 'Arial',
              fontSize: 12,
              bold: false,
              italic: false,
              color: '#EA3C3C', 
              format: '0'
            },
        },
        vAxis: {
          textStyle: {
            fontSize: 15, // Ajusta según tus necesidades
          },
        },
        animation: {
        startup: true, // Activa la animación en el inicio
        duration: 1000, // Duración de la animación en milisegundos
        easing: 'out', // Tipo de animación (puedes usar 'in' para una entrada más suave)
      },
      };

      const chart = new google.visualization.BarChart(document.getElementById(containerID));
      chart.draw(data, options);
          
        },
    },
  mounted() {
    this.obtenerData(); // Llamada inicial
    // Ejecutar la función cada 5 minutos
    this.intervalID = setInterval(this.obtenerData, 60000);
  },
};
</script>
<template>
  <Header/>
  <div v-if="datos.length">
    <div class="charts-container" >
      <div id="valoresAL" class="chart"></div>
      <div id="valoresRO" class="chart"></div>
    </div>
</div>
  <p v-else>No hay datos que mostrar</p>
</template>
<style scoped>
.charts-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  padding: 10px;
}

.chart {
  flex: 1;
  width: calc(100% - 50%);
  height: 650px;
  border: 1px solid #ddd;
  margin-top: 10px;
  box-sizing: border-box;
  position: relative;
}

.chart h1 {
  margin: 10px;
}

#valoresRO {
  margin-left: 10px;
}
p{
  text-align: center;
}

@media (max-width: 768px) {
  .chart {
    width: 100%;
    margin-left: 0;
  }
  #valoresRO {
    margin-left: 0;
  }
}


</style>
