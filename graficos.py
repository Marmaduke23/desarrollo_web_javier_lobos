import matplotlib.pyplot as plt
import random

def generar_grafico_mensual():
    # Generar datos aleatorios para el gráfico
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    ventas = [random.randint(10, 500) for _ in range(12)]

    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.plot(meses, ventas, color='skyblue')
    plt.title('Actividades registradas por mes')
    plt.xlabel('Meses')
    plt.ylabel('Actividades registradas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plt.savefig("img/grafico_mensual.png", dpi=300, bbox_inches='tight')
    plt.show()

generar_grafico_mensual()    
