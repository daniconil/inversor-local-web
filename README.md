# inversor-local-web
Medidor de datos ofrecidos por un inversor Huawei de placas fotovoltaicas a través de la red local. Versión web en HTML.

# Lectura de inversor Huawei en red local sobre distribución tipo Debian/Ubuntu

Este script sirve para leer, localmente, los datos ofrecidos por inversores Huawei de placas fotovoltaicas. Probablemente, si tienes una estructura montada de esta marca, uses la app Fusion Solar tanto en móvil como en navegador para acceder a tus datos de consumo, autoconsumo y exportación. Con este script, puedes obtener los datos en tiempo real.


**Nota importante :** Para el funcionamiento de este script es imprescindible tener un inversor de energía fotovoltaica presente en la red local. Si no, arrojará error de IP al no localizar ningún dispositivo en esa dirección. 

# Requisitos

## 1. Instalación de Python y dependencias

Con el siguiente comando, comprobamos la versión que tenemos instalada.

```
python3 --version
```

1.a Si no tenemos python instalado, haremos lo siguiente para hacerlo junto a las dependencias necesarias en el siguiente punto:

```
sudo apt install python3 pip
```

## 2. Instalación de wrapper huawei-solar

A través del siguiente comando, instalamos el *wrapper* huawei-solar, que servirá de conector entre el inversor Huawei y nuestro equipo. Esto hará que instale **pytz** y **pymodbus** que se encargarán de establecer la zona horaria y la comunicación asíncrona con el inversor:

```
pip install huawei-solar
```
Más información de huawei-solar en https://pypi.org/project/huawei-solar/
Más información de pytz en https://pypi.org/project/pytz/
Más información de pymodbus en https://pypi.org/project/pymodbus/

## 3. Modificación de IP

Debemos modificar **[INSERT_INVERTER_LOCAL_IP]** de la línea 12 por la IP local del inversor Huawei. Accede al script:
```
nano inversorlocal.py
```
Y modifica la variable indicada:

```
h = huawei_solar.HuaweiSolar(host="[INSERT_INVERTER_LOCAL_IP]")
```

## 4. Ejecución del script

Una vez modificado el script, ejecutamos el siguiente comando y nos ofrece datos básicos.

```
python3 main.py
```
Y obtendremos en la terminal el siguiente aviso

```
Server started http://localhost:8081
```

Accedemos mediante a ese navegador a esa dirección y obtendremos un listado de datos básicos.

## Ejemplo con valores en W:

Input energy (registered by panels)
> Se trata de la energía de entrada que las placas fotovoltaicas están captando en ese instante.
Active energy (ready to be taken)
> Energía que llega al inversor, se percibe una pérdida aproximada del 2% con respecto a la energía de entrada.
Exported energy
> Energía que no está siendo usada y que se vierte a la red eléctrica común para ser compensada económicamente.
Energy consumption currently
> Energía que se está consumiendo en ese momento
Date
> Fecha
Time
> Hora concreta de la lectura de datos 

```
Input energy (registered by panels): 1624 W
Active energy (ready to be taken): 1589 W
Exported energy (discharged to be compensated): 1415 W
Energy consumption currently: 174 W
Date: 16/05/2022
Time: 12:24:37
Timezone: Europe/Madrid
```
# Notas

- Este sencillo script puede ofrecerte multitud de posibilidades para crearte tu propia app ejecutado en local.

- Dentro del script puedes observar otros datos de interés que pueden publicarse en el resultado, tales como la eficiencia, el modelo del inversor o el número de serie.

- La web se actualizará cada 10 segundos con datos vueltos a importar debido a la función `importlib.reload(huawei_solar)`

