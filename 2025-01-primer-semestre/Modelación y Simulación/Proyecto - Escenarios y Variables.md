<hr>

**Escenario de 7 - 9 am (baja demanda)**

Caja asistida
Media real tiempo de servicio (promedio): 2
Desviación estándar: 1

Autopago
Media real: 3.5
Desviación estándar: 1.5 

25 clientes

**Escenario de 9 - 10 am (baja demanda)**


_**Fórmulas**_

Source
Exponential: 
- Location: el valor mínimo que puede tomar la variable
- Scale: tiempo de llegada de clientes, cada cuánto llegan (valor medio de tiempo entre llegada)
- Stream: controlar la consecuencia aleatoria



Log_normal
normal_mean = ln(μ² / sqrt(σ² + μ²))
normal_stdev = sqrt(φ²)


| Horario    | Clientes | Duración (h) | λ (clientes/h) | Scale = 60 / λ |
| ---------- | -------- | ------------ | -------------- | -------------- |
| 7am – 9am  | 24       | 2h           | 12             | 5.00 min       |
| 9am – 10am | 12       | 1h           | 12             | 5.00 min       |
| 10am – 4pm | 558      | 6h           | 93             | 0.65 min       |
| 4pm – 9pm  | 1056     | 5h           | 211.2          | 0.28 min       |
