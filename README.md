# Workshop_1

## Descripción

Este proyecto consiste en recibir un archivo CSV con datos de candidatos que participaron en procesos de selección (estos datos fueron generados aleatoriamente). El objetivo principal fue realizar análisis y manipulaciones en estos datos para obtener información relevante y, finalmente, crear visualizaciones de datos.

## Herramientas Utilizadas

- **Python**: Para la manipulación y análisis de datos.
- **Jupyter Notebooks**: Para desarrollar el análisis y documentar el proceso.
- **PostgreSQL**: Utilizado como base de datos para almacenar y gestionar los datos.
- **Power BI**: Para visualizar los resultados y análisis de datos.
- **SQLAlchemy**: Utilizado para manejar operaciones con la base de datos a través de ORM (Object Relational Mapping).

## Acerca de los Datos

Este dataset tiene 50,000 filas de datos sobre candidatos. Los nombres de las columnas y sus respectivos tipos de datos antes de la transformación son:

- **First Name**: Object
- **Last Name**: Object
- **Email**: Object
- **Country**: Object
- **Application Date**: Object
- **Yoe (Years Of Experience)**: Integer
- **Seniority**: Object
- **Technology**: Object
- **Code Challenge Score**: Integer
- **Technical Interview**: Integer

## Organización del Repositorio

- **data**: Esta carpeta contiene el archivo CSV con los datos de los candidatos, llamado 'candidates.csv'.
- **notebook**: Contiene los notebooks de Jupyter. El notebook `001_pre_load.ipynb` realiza la carga y preprocesamiento inicial de los datos, mientras que `002_eda_candidates.ipynb` realiza el análisis exploratorio de datos.
- **src**: Contiene el archivo `db_connection.py`, que maneja la conexión a la base de datos PostgreSQL.

## Requisitos

1. **Instalar Python**: [Descargas de Python](https://www.python.org/downloads/)
2. **Instalar PostgreSQL**: [Descargas de PostgreSQL](https://www.postgresql.org/download/)
3. **Instalar Power BI**: [Instalar Power BI Desktop](https://powerbi.microsoft.com/es-es/desktop/)

## Variables de Entorno

Para ejecutar este proyecto, necesitas configurar un archivo `.env` en la raíz del proyecto con las siguientes variables:

```plaintext
DB_USER=postgres
DB_PASSWORD=  # Agrega tu contraseña aquí
DB_HOST=localhost
DB_PORT=5
DB_DB=workshop
```
## Requisitos

Para ejecutar los notebooks de este proyecto, necesitarás instalar las dependencias listadas en `requirements.txt`. Puedes instalarlas ejecutando:

```bash
pip install -r requirements.txt
```

## Uso

1. **Clona este repositorio** en tu máquina local:
   ```bash
   git clone https://github.com/D-Salamanca/workshop_1.git
   ```

2. **Navega al directorio del proyecto**:
   ```bash
   cd workshop_1
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Abre y ejecuta los notebooks** utilizando Jupyter Notebook o JupyterLab:
   ```bash
   jupyter notebook notebook/001_pre_load.ipynb
   ```

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork de este repositorio.
2. Crea una nueva rama para tu feature o bugfix:
   ```bash
   git checkout -b nombre-de-la-rama
   ```
3. Realiza tus cambios y haz commit:
   ```bash
   git commit -m "Descripción clara de los cambios"
   ```
4. Haz push a tu rama:
   ```bash
   git push origin nombre-de-la-rama
   ```
5. Crea un Pull Request en GitHub.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo `LICENSE` para más detalles.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarme a través de mi correo electrónico: [d.salamanca0314@gmail.com](mailto:d.salamanca0314@gmail.com).

