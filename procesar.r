datos_finales = read.csv('final_data.csv')

hist(datos_finales$tutorias_fallidas,
    main = "Tutorias sin atender",
    xlab = "Cantidad de tutorias",
    ylab = "Frecuencia"
    )

print(datos_finales)