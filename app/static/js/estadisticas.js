async function cargarGraficoActividades() {
  try {
    const response = await fetch("http://127.0.0.1:5000/actividades_por_dia");
    if (!response.ok) throw new Error("No se pudo obtener actividades");
    const data = await response.json();

    const parsedData = data.map((item) => {
      const [year, month, day] = item.date.split("-").map(Number);
      return [Date.UTC(year, month - 1, day), item.cantidad];
    });

    renderizarGraficoActividades(parsedData);
  } catch (error) {
    console.error("Error al cargar el gráfico de actividades:", error);
    renderizarGraficoActividades([]);
  }
}


async function cargarGraficoTorta() {
  try {
    const response = await fetch("http://127.0.0.1:5000/actividades_por_tipo");
    if (!response.ok) throw new Error("No se pudo obtener datos para la torta");
    const data = await response.json();

    // Transformar el objeto a array para Highcharts
    const parsedData = Object.entries(data).map(([key, value]) => ({
      name: key,
      y: value,
    }));

    renderizarGraficoTorta(parsedData);
  } catch (error) {
    console.error("Error al cargar el gráfico de torta:", error);
    renderizarGraficoTorta([]);
    
  }
}

async function cargarGraficoHorasPorMes() {
  try {
    const response = await fetch("http://127.0.0.1:5000/actividades_por_mes");
    if (!response.ok) throw new Error("No se pudo obtener datos por hora y mes");

    const data = await response.json();
    const { categorias, series } = procesarDatosMes(data);

    renderizarGraficoMes(categorias, series);
  } catch (error) {
    console.error("Error al cargar gráfico de horas por mes:", error);
    renderizarGraficoMes([], []);
  }
}

function procesarDatosMes(data) {
  const meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
  ];

  const categorias = meses;
  const manana = [];
  const mediodia = [];
  const tarde = [];

  for (let i = 1; i <= 12; i++) {
    const valores = data[i] || { mañana: 0, mediodia: 0, tarde: 0 };
    manana.push(valores["mañana"] || 0);
    mediodia.push(valores["mediodia"] || 0);
    tarde.push(valores["tarde"] || 0);
  }

  return {
    categorias,
    series: [
      { name: "Mañana", data: manana, color: "#FFB347" },
      { name: "Mediodía", data: mediodia, color: "#FC2865" },
      { name: "Tarde", data: tarde, color: "#66C2A5" }
    ]
  };
}

function renderizarGraficoMes(categorias, series) {
  Highcharts.chart("container-mes", {
    chart: {
      type: "column"
    },
    title: {
      text: "Actividades por Mes y Franja Horaria"
    },
    xAxis: {
      categories: categorias,
      crosshair: true
    },
    yAxis: {
      min: 0,
      title: {
        text: "Cantidad de Actividades"
      }
    },
    tooltip: {
      shared: true,
      formatter: function () {
        let s = `<b>${this.points[0].key}</b><br/>`;
        this.points.forEach(point => {
          s += `${point.series.name}: <b>${point.y}</b><br/>`;
        });
        return s;
      }
    },
    plotOptions: {
      column: {
        pointPadding: 0.2,
        borderWidth: 0
      }
    },
    series: series
  });
}



function renderizarGraficoActividades(data) {
  Highcharts.chart("container-dia", {
    chart: {
      type: "scatter",
    },
    title: {
      text: "Número de Actividades Registradas por Día",
    },
    xAxis: {
      type: "datetime",
      dateTimeLabelFormats: {
        month: "%b %e, %Y",
      },
      title: {
        text: "Fecha",
      },
    },
    yAxis: {
      title: {
        text: "Número de Actividades",
      },
    },
    legend: {
      align: "left",
      verticalAlign: "top",
      borderWidth: 0,
    },
    tooltip: {
      formatter: function () {
        const fecha = Highcharts.dateFormat("%Y-%m-%d", this.x);
        return `Fecha: <b>${fecha}</b><br>Cantidad: <b>${this.y}</b>`;
      },
    },
    series: [
      {
        name: "Actividad",
        data: data,
        marker: {
          enabled: true,
          radius: 4,
        },
        color: "#FC2865",
      },
    ],
    lang: {
      noData: "No hay datos disponibles"
    },
    noData: {
      style: {
        fontWeight: "bold",
        fontSize: "15px",
        color: "#303030"
      }
    }
  });
}

function renderizarGraficoTorta(data) {
  Highcharts.chart("container-torta", {
    chart: {
      type: "pie",
    },
    title: {
      text: "Distribución de Categorías",
    },
    tooltip: {
      pointFormat: '{series.name}: <b>{point.y}</b> ({point.percentage:.1f}%)',
    },
    accessibility: {
      point: {
        valueSuffix: '%',
      },
    },
    plotOptions: {
      pie: {
        allowPointSelect: true,
        cursor: "pointer",
        dataLabels: {
          enabled: true,
          format: "<b>{point.name}</b>: {point.y}",
          style: {
            fontWeight: "bold",
            fontSize: "13px",
          },
        },
      },
    },
    legend: {
      align: "left",
      verticalAlign: "top",
      borderWidth: 0,
    },
    series: [
      {
        name: "Cantidad",
        colorByPoint: true,
        data: data,
      },
    ],
    lang: {
      noData: "No hay datos disponibles",
    },
    noData: {
      style: {
        fontWeight: "bold",
        fontSize: "15px",
        color: "#303030",
      },
    },
  });
}
// Call the function to load the chart data
cargarGraficoActividades();
cargarGraficoTorta();
cargarGraficoHorasPorMes();

