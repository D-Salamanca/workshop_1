# Workshop_1

## Descripción
Este proyecto consiste en recibir un archivo CSV con datos de candidatos que participaron en procesos de selección. Los datos fueron generados aleatoriamente para simular un proceso real de selección de personal. El objetivo principal fue realizar análisis detallados y manipulaciones de los datos para obtener información relevante, y finalmente crear visualizaciones interactivas que permitan una comprensión profunda de las tendencias y patrones en los procesos de contratación.

## Herramientas Utilizadas
- **Python**: Utilizado para la manipulación y análisis de datos, empleando bibliotecas como Pandas y SQLAlchemy.
- **Jupyter Notebooks**: Para desarrollar el análisis, documentar el proceso y facilitar la reproducibilidad.
- **PostgreSQL**: Base de datos relacional utilizada para almacenar y gestionar los datos de los candidatos de manera eficiente.
- **Power BI**: Para la creación de visualizaciones interactivas y análisis avanzado de datos.
- **SQLAlchemy**: Librería ORM (Object Relational Mapping) que simplifica las interacciones con la base de datos PostgreSQL desde Python.
- **Plotly**: Utilizado para generar gráficos interactivos dentro de los notebooks de Jupyter.

## Acerca de los Datos
Este dataset contiene 50,000 filas con información sobre candidatos. Las columnas incluyen datos personales, resultados de evaluaciones técnicas, y detalles sobre el proceso de selección. Las columnas y sus tipos de datos antes de cualquier transformación son:

- **First Name**: Object
- **Last Name**: Object
- **Email**: Object
- **Country**: Object
- **Application Date**: Object
- **YOE (Years Of Experience)**: Integer
- **Seniority**: Object
- **Technology**: Object
- **Code Challenge Score**: Integer
- **Technical Interview Score**: Integer

## Organización del Repositorio
- **data**: Esta carpeta contiene el archivo CSV con los datos de los candidatos, llamado `candidates.csv`.
- **notebook**: Contiene los notebooks de Jupyter utilizados para la carga, preprocesamiento, y análisis de los datos.
  - `001_pre_load.ipynb`: Realiza la carga inicial y el preprocesamiento de los datos.
  - `002_eda_candidates.ipynb`: Realiza el análisis exploratorio de datos (EDA), identificando patrones y tendencias importantes.
- **src**: Contiene el archivo `db_connection.py`, que maneja la conexión a la base de datos PostgreSQL.
- **requirements.txt**: Lista las dependencias necesarias para ejecutar los notebooks.
- **README.md**: Este archivo, que proporciona una visión general del proyecto.

## Requisitos
### Instalación de Software
Para ejecutar este proyecto, necesitarás tener instalado:
- **Python**: [Descargar Python](https://www.python.org/downloads/)
- **PostgreSQL**: [Descargar PostgreSQL](https://www.postgresql.org/download/)
- **Power BI**: [Instalar Power BI Desktop](https://powerbi.microsoft.com/desktop/)

### Variables de Entorno
Configura un archivo `.env` en la raíz del proyecto con las siguientes variables para conectar con la base de datos PostgreSQL:

```bash
DB_USER=postgres
DB_PASSWORD=your_password_here
DB_HOST=localhost
DB_PORT=5432
DB_DB=workshop

## Instalación de Dependencias, Contribuciones y Contacto

### Instalación de Dependencias
Para ejecutar los notebooks de este proyecto, necesitarás instalar las dependencias listadas en `requirements.txt`. Puedes instalarlas ejecutando el siguiente comando:

```bash
pip install -r requirements.txt

##Contribuciones
Si deseas contribuir a este proyecto, sigue estos pasos:

Haz un fork de este repositorio.
Crea una nueva rama para tu feature o bugfix:
bash
Copiar código
git checkout -b nombre-de-la-rama
Realiza tus cambios y haz commit:
bash
Copiar código
git commit -m "Descripción clara de los cambios"
Haz push a tu rama:
bash
Copiar código
git push origin nombre-de-la-rama
Crea un Pull Request en GitHub.

##Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactarme a través de mi correo electrónico: d.salamanca0314@gmail.com.
