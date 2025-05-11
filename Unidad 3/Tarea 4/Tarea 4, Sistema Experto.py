# Función para poder verificar las respuestas
def pedirOpcion(pregunta, opciones_validas):
    while True:
        respuesta = input(pregunta).lower()
        if respuesta in opciones_validas:
            return respuesta
        print(f"Opción no válida. Debes elegir entre: {', '.join(opciones_validas)}.")

# Función principal para obtener la recomendación
def sistemaExperto():
    recomendacion = ""

    # Entradas del usuario
    objetivo = pedirOpcion("¿Cuál es tu objetivo? (bajar de peso / mantener peso / ganar masa muscular): ",
                        ["bajar de peso", "mantener peso", "ganar masa muscular", "bajar", "mantener", "ganar"])
    actividad = pedirOpcion("¿Cuál es tu nivel de actividad? (sedentario / moderada / activo): ", 
                        ["sedentario", "moderada", "activo"])
    preferencia = pedirOpcion("¿Eres vegano, vegetariano u omnívoro?: ", 
                        ["vegano", "vegetariano", "omnívoro", "omnivoro"])
    lactosa = pedirOpcion("¿Tienes alergia a la lactosa? (sí / no): ", 
                        ["sí", "si", "no"])
    gluten = pedirOpcion("¿Tienes intolerancia al gluten? (sí / no): ",
                        ["sí", "si", "no"])
    frutos_secos = pedirOpcion("¿Tienes alergia a los frutos secos? (sí / no): ", 
                        ["sí", "si", "no"])
    tiempo = pedirOpcion("¿Tienes poco tiempo o mucho tiempo para cocinar?: ", 
                        ["poco tiempo", "mucho tiempo", "mucho", "poco"])

    # En este caso tomamos en cuenta tres condiciones, ya que hay que tomar en cyenta tanto el objetivo como el nivel de actividad y
    # la preferencia para poder hacer una recomendación más precisa

    # Reglas basadas en objetivos y nivel de actividad
    if objetivo in ["bajar", "bajar de peso"]:
        if actividad == "activo":
            if preferencia == "vegano":
                recomendacion += "- Dieta hipocalórica vegetal: tofu, legumbres, vegetales frescos y cereales integrales.\n"
            elif preferencia == "vegetariano":
                recomendacion += "- Dieta con vegetales frescos, huevo, lácteos bajos en grasa y avena.\n"
            elif preferencia in ["omnívoro", "omnivoro"]:
                recomendacion += "- Dieta hipocalórica rica en vegetales frescos, proteínas magras como pollo o tofu,\n"
                recomendacion += "  y carbohidratos complejos como avena y arroz integral.\n"
        elif actividad == "sedentario":
            if preferencia == "vegano":
                recomendacion += "- Dieta muy baja en calorías, evitando procesados y azúcares, basada en vegetales, tofu y legumbres.\n"
            elif preferencia == "vegetariano":
                recomendacion += "- Dieta baja en calorías con verduras, frutas con baja carga glucémica y lácteos ligeros.\n"
            elif preferencia in ["omnívoro", "omnivoro"]:
                recomendacion += "- Dieta muy baja en calorías, evitando azúcares, procesados y grasas saturadas.\n"
                recomendacion += "  El control de porciones o el ayuno intermitente pueden ayudarte.\n"
        elif actividad == "moderada":
            if preferencia == "vegano":
                recomendacion += "- Dieta con legumbres, vegetales ricos en fibra y tofu. Ideal para perder peso sin perder energía.\n"
            elif preferencia == "vegetariano":
                recomendacion += "- Vegetales, frutas, legumbres y proteínas como huevo o lácteos bajos en grasa.\n"
            elif preferencia in ["omnívoro", "omnivoro"]:
                recomendacion += "- Dieta rica en legumbres, vegetales con fibra y proteínas magras,\n"
                recomendacion += "  ideal para perder peso sin afectar tu energía diaria.\n"

    elif objetivo in ["mantener", "mantener peso"]:
        if actividad == "sedentario":
            if preferencia == "vegano":
                recomendacion += "- Dieta equilibrada vegetal con porciones justas: cereales integrales, legumbres y verduras.\n"
            elif preferencia == "vegetariano":
                recomendacion += "- Dieta con frutas, verduras, cereales integrales y derivados lácteos moderados.\n"
            elif preferencia in ["omnívoro", "omnivoro"]:
                recomendacion += "- Dieta equilibrada con porciones justas, enfocada en alimentos naturales y no procesados.\n"
        elif actividad == "moderada":
            if preferencia == "vegano":
                recomendacion += "- Dieta balanceada vegana: frutas, verduras, quinoa, arroz integral y fuentes de B12.\n"
            elif preferencia == "vegetariano":
                recomendacion += "- Dieta con vegetales, frutas, cereales integrales, huevo y yogures ligeros.\n"
            elif preferencia in ["omnívoro", "omnivoro"]:
                recomendacion += "- Dieta balanceada que incluya frutas, verduras y cereales integrales.\n"
        elif actividad == "activo":
            if preferencia == "vegano":
                recomendacion += "- Dieta vegetal con alto contenido calórico saludable: frutos secos, legumbres, aceite de oliva.\n"
            elif preferencia == "vegetariano":
                recomendacion += "- Dieta con lácteos, huevo, aguacate y cereales completos para mantener energía.\n"
            elif preferencia in ["omnívoro", "omnivoro"]:
                recomendacion += "- Dieta con carnes magras, grasas saludables como aguacate y carbohidratos complejos.\n"

    elif objetivo in ["ganar masa muscular", "ganar"]:
        if actividad == "activo":
            if preferencia == "vegano":
                recomendacion += "- Dieta hipercalórica con legumbres, cereales, tofu, frutos secos y batidos vegetales.\n"
            elif preferencia == "vegetariano":
                recomendacion += "- Dieta con huevos, lácteos, cereales integrales y legumbres. Come cada 3 horas.\n"
            elif preferencia in ["omnívoro", "omnivoro"]:
                recomendacion += "- Dieta hipercalórica con muchas proteínas (animales o vegetales), carbohidratos complejos\n"
                recomendacion += "  como papa o quinoa y grasas buenas como nueces o aceite de oliva. Come cada 3 horas.\n"
        elif actividad == "moderada":
            if preferencia == "vegano":
                recomendacion += "- Dieta rica en calorías vegetales: arroz, lentejas, tofu, semillas y mantequillas naturales.\n"
            elif preferencia == "vegetariano":
                recomendacion += "- Proteínas como huevo y lácteos, cereales integrales, mantequillas de nuez.\n"
            elif preferencia in ["omnívoro", "omnivoro"]:
                recomendacion += "- Proteínas de calidad (huevo, legumbres), arroz integral, mantequillas naturales.\n"
                recomendacion += "  Aumenta progresivamente tus porciones.\n"
        elif actividad == "sedentario":
            if preferencia == "vegano":
                recomendacion += "- Superávit calórico leve con alimentos vegetales densos en nutrientes: frutos secos, cereales, tofu.\n"
            elif preferencia == "vegetariano":
                recomendacion += "- Aumenta calorías con huevo, lácteos, cereales integrales y frutas calóricas.\n"
            elif preferencia in ["omnívoro", "omnivoro"]:
                recomendacion += "- Con poco movimiento, puedes comenzar con superávit calórico leve\n"
                recomendacion += "  y proteínas de buena calidad. Añade ejercicio progresivamente.\n"

    # En estas reglas solo tomamos en cuenta una condición, lo tomamos como un agregado al final de la recomendación
    # para saber qué cosas evitar en general, alternativas con las alergias, y qué tipo de comida preparar con el tiempo disponible

    # Reglas por alergias
    if lactosa in ["sí", "si"]:
        recomendacion += "- Evita leche, quesos y yogures comunes. Usa leches vegetales como avena o almendra.\n"
    if gluten in ["sí", "si"]:
        recomendacion += "- Elimina trigo, cebada y centeno. Usa arroz, maíz, papa, quinoa o productos sin gluten.\n"
    if frutos_secos in ["sí", "si"]:
        recomendacion += "- Evita nueces, almendras y maní. Usa aguacate, semillas o aceite de oliva como alternativas.\n"

    # Reglas por tiempo disponible
    if tiempo in ["poco tiempo", "poco"]:
        recomendacion += "- Prepara platos simples: ensaladas con proteína, batidos, wraps o snacks saludables.\n"
        recomendacion += "  Considera cocinar en lotes (meal prep) para toda la semana.\n"
    elif tiempo in ["mucho", "mucho tiempo"]:
        recomendacion += "- Puedes cocinar desde cero: sopas, guisos, panes integrales y postres bajos en azúcar.\n"

    # Resultado final
    print("\n--- Recomendación de Dieta Personalizada ---")
    print(recomendacion)

# Ejecutar
sistemaExperto()
