import matplotlib.pyplot as plt
import random

def generar_grafico_diario():
    # Generar datos aleatorios para el gráfico
    dias = [i+1 for i in range(30)]
    actividades = [random.randint(1, 100) for _ in range(30)]

        
    # Crear el gráfico
    plt.figure(figsize=(14, 6))

    # Dibujar línea principal con marcadores
    plt.plot(dias, actividades, color='royalblue', linestyle='-', linewidth=2.5, marker='o', markersize=6, markerfacecolor='red', markeredgecolor='black', label="Actividades")

    # Sombreado bajo la curva
    plt.fill_between(dias, actividades, color='royalblue', alpha=0.2)

    # Etiquetas y título
    plt.title('Actividades registradas por día')
    plt.xlabel('Día del mes', fontsize=12)
    plt.ylabel('Cantidad de Actividades', fontsize=12)
    plt.xticks(dias, rotation=45)
    plt.yticks(fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.6)  # Líneas de referencia horizontales
    plt.legend()

    plt.tight_layout()
    
    plt.savefig("img/grafico_mensual.png", dpi=300, bbox_inches='tight')
    plt.show()

def generar_grafico_torta():
    # Generar datos aleatorios para el gráfico
    actividades = ['musica', 'deporte','ciencias','religión','política','tecnología','juegos','baile','comida'
                   ,'comida','otro']
    cantidad = [random.randint(1, 100) for _ in range(len(actividades))]
    total = sum(cantidad)

    # Crear el gráfico de torta
    plt.figure(figsize=(8, 8))
    plt.pie(cantidad, labels=actividades, autopct='%1.1f%%', startangle=140)
    plt.title('Distribución de actividades')
    
    plt.savefig("img/grafico_torta.png", dpi=300, bbox_inches='tight')
    plt.show()

def generar_grafico_3barras():
    #Generar grafico con 3 barras para cada mes con la cantidad de actividades en la mañana, medio dia y tarde
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    actividades = [random.randint(1, 100) for _ in range(len(meses))]
    actividades2 = [random.randint(1, 100) for _ in range(len(meses))]
    actividades3 = [random.randint(1, 100) for _ in range(len(meses))]
    x = range(len(meses))
    width = 0.25
        # Crear barras con desplazamiento
    plt.bar([pos - width for pos in x], actividades, width=width, label="Mañana")
    plt.bar(x, actividades2, width=width, label="Mediodía")
    plt.bar([pos + width for pos in x], actividades3, width=width, label="Tarde")
    plt.xticks(x, meses,rotation=45)
    plt.xlabel('Meses')
    plt.ylabel('Actividades')
    plt.title('Actividades registradas por mes')
    plt.legend()
    plt.tight_layout()

    plt.savefig("img/grafico_3barras.png", dpi=300, bbox_inches='tight')
    plt.show()






#generar_grafico_diario()    
#generar_grafico_torta()
generar_grafico_3barras()