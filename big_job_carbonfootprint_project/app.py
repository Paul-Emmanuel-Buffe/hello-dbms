from flask import Flask, render_template, request
from db_connection import fetch_all
import plotly.graph_objs as go
import plotly.offline as pyo
import json



def created_app():
# appli Flask
    app = Flask(__name__)

    #Routes
    @app.route("/")
    def index():
        query="""
                SELECT * FROM (
                            SELECT *
                            FROM original_raw
                            LIMIT 5
                        )
                UNION ALL
                SELECT * FROM (
                    SELECT *
                    FROM original_raw
                    LIMIT 7 OFFSET (SELECT COUNT(*) -10 FROM original_raw)
                )
            """

        data = fetch_all(query)
        return render_template("index.html", data=data)

    @app.route("/observations")
    def observations(): 
        # requette sql pour obtenir les données mondiales
        query= """ SELECT
                    ROUND(gas)       AS "Gaz",
                    ROUND(oil)       AS "Pétrole",
                    ROUND(coal)      AS "Charbon",
                    ROUND(nuclear)   AS "Nucléaire",
                    ROUND(hydro)     AS "Hydro",
                    ROUND(renewable) AS "Renouvelables"
                FROM world
                WHERE region = 'world';"""

        data = fetch_all(query)

        # selection des colonnes premier graph
        columns = ["Gaz", "Pétrole", "Charbon", "Nucléaire", "Hydro", "Renouvelables"]

        # valeurs correspondantes
        values = [data[0][col] for col in columns]

        # couleurs choisies
        colors = [
                    '#1F4E79',
                    '#C44536',
                    '#4D4D4D',
                    '#6A5ACD',
                    '#2E8B57',
                    '#F2B705'
                ]

        # création du graph
        fig = go.Figure(data=[go.Pie(
            labels=columns,
            values=values,
            marker=dict(colors=colors),
            hoverinfo='label+percent',
            textinfo='label',
            textfont=dict(size=14),
            hoverlabel=dict(font=dict(size=16))
        )])

        # mise en page
        fig.update_layout(
            title_text="Mix énergétique mondial",
            title_font_size=18,
            title_x=0.5,
            showlegend=False,
            margin=dict(t=50, b=20, l=20, r=20)
        )

        ## Second graph
        query_2 = """
                    SELECT
                        region,
                        CEIL(gas + oil + coal) AS "Energies fossiles",
                        ROUND(hydro + renewable + nuclear) AS "Energies ditent propres"
                    FROM world WHERE region = 'world'
            """

        data_2  = fetch_all(query_2)

        # selection des colonnes second graph
        columns_2 = ["Energies fossiles", "Energies ditent propres"]

        # valeurs correspondantes
        values_2 = [data_2[0][col] for col in columns_2]

        # couleurs choisies
        colors_2 = [
                        '#8B0000',  # Énergies fossiles – rouge sombre 
                        '#228B22'   # Énergies dites propres – vert profond 
                    ]

        # création du graph
        fig_2 = go.Figure(data=[go.Pie(
            labels=columns_2,
            values=values_2,
            marker=dict(colors=colors_2),
            hoverinfo='label+percent',
            textinfo='label',
            textfont=dict(size=14),
            hoverlabel=dict(font=dict(size=16))
        )])

        # mise en page
        fig_2.update_layout(
            title_text="Production électrique mondiale : fossile vs bas-carbone",
            title_font_size=18,
            title_x=0.5,
            showlegend=False,
            margin=dict(t=50, b=20, l=20, r=20)
        )

        ### Card 2 - graph en barres
        query_3 = """
                    SELECT 
                        CASE region
                            WHEN 'east asia & pacific' THEN 'Asie-Pacifique'
                            WHEN 'europe & central' THEN 'Europe & Asie Centrale'
                            WHEN 'latin america & caribbean' THEN 'Amérique Latine & Caraïbes'
                            WHEN 'middle east & north afrika' THEN 'Moyen-Orient & Afrique du Nord'
                            WHEN 'north america' THEN 'Amérique du Nord'
                            WHEN 'south asia' THEN 'Asie du Sud'
                            WHEN 'sub­saharan africa'THEN 'Afrique Subsaharienne'
                            ELSE region  
                        END AS region,
                        (gas + oil + coal) AS "Energies fossiles",
                        ROUND(hydro + renewable + nuclear) AS "Autres"
                    FROM world
                    WHERE region != 'world'
                    ORDER BY region;
                """

        data_3 = fetch_all(query_3)

        # Tri par ordre alphabétique des régions traduites
        data_3_sorted = sorted(data_3, key=lambda x: x['region'])

        regions = [row['region'] for row in data_3_sorted]
        fossiles = [row['Energies fossiles'] for row in data_3_sorted]
        autres = [row['Autres'] for row in data_3_sorted]

        # couleurs 
        colors_bar = ['#C85A54', '#5CB85C']

        # Création du bar chart
        fig_3 = go.Figure(data=[
            go.Bar(
                name='Énergies fossiles',
                x=regions,
                y=fossiles,
                marker_color=colors_bar[0],
                text=[f"{v}%" for v in fossiles],
                textposition='auto'
            ),
            go.Bar(
                name='Énergies bas-carbone',
                x=regions,
                y=autres,
                marker_color=colors_bar[1],
                text=[f"{v}%" for v in autres],
                textposition='auto'
            )
        ])

        # Mise en page
        fig_3.update_layout(
            barmode='group',
            title_font_size=18,
            title_x=0.5,
            xaxis_title="Régions",
            yaxis_title="Pourcentage (%)",
            width=1000,
            height=500,
            margin=dict(t=50, b=100, l=50, r=50)
        )

       ## Card 3 - Graph à barres horizontales empilées
        query_4 = """
                                SELECT 
                                    CASE country
                                        WHEN 'china' THEN 'Chine'
                                        WHEN 'united states' THEN 'États-Unis'
                                        WHEN 'india' THEN 'Inde'
                                        WHEN 'japan' THEN 'Japon'
                                        WHEN 'russia' THEN 'Russie'
                                    END AS "Pays",
                                    coal      AS "Charbon",
                                    gas       AS "Gaz",
                                    oil       AS "Pétrole",
                                    nuclear   AS "Nucléaire",
                                    hydro     AS "Hydraulique",
                                    renewable AS "Renouvelables"
                                FROM country
                                WHERE country IN ('china', 'united states', 'india', 'japan', 'russia')
                                ORDER BY 3 DESC;
                            """

        data_4 = fetch_all(query_4)

        # Préparation des listes
        # Préparation des listes
        pays = [row['Pays'] for row in data_4]
        gaz = [row['Gaz'] for row in data_4]
        petrole = [row['Pétrole'] for row in data_4]
        charbon = [row['Charbon'] for row in data_4]
        nucleaire = [row['Nucléaire'] for row in data_4]
        hydraulique = [row['Hydraulique'] for row in data_4]
        renouvelables = [row['Renouvelables'] for row in data_4]

        # couleurs 
        colors_bar = [
                        '#FF6B6B',  # Gaz –
                        '#FFA94D',  # Pétrole 
                        '#4D79FF',  # Charbon 
                        '#6F42C1',  # Nucléaire 
                        '#4DBD33',  # Hydraulique 
                        '#20C997'   # Renouvelables 
                    ]


        # Création du bar chart


        # Préparation des listes depuis data_4
        pays = [row['Pays'] for row in data_4]
        gaz = [row['Gaz'] for row in data_4]
        petrole = [row['Pétrole'] for row in data_4]
        charbon = [row['Charbon'] for row in data_4]
        nucleaire = [row['Nucléaire'] for row in data_4]
        hydraulique = [row['Hydraulique'] for row in data_4]
        renouvelables = [row['Renouvelables'] for row in data_4]

            # Création du graphique en barres horizontales empilées
        graph_4 = go.Figure()
        graph_4.add_trace(go.Bar(name='Charbon', y=pays, x=charbon, orientation='h', marker_color=colors_bar[2]))  # charbon en premier
        graph_4.add_trace(go.Bar(name='Gaz', y=pays, x=gaz, orientation='h', marker_color=colors_bar[0]))
        graph_4.add_trace(go.Bar(name='Pétrole', y=pays, x=petrole, orientation='h', marker_color=colors_bar[1]))
        graph_4.add_trace(go.Bar(name='Nucléaire', y=pays, x=nucleaire, orientation='h', marker_color=colors_bar[3]))
        graph_4.add_trace(go.Bar(name='Hydraulique', y=pays, x=hydraulique, orientation='h', marker_color=colors_bar[4]))
        graph_4.add_trace(go.Bar(name='Renouvelables', y=pays, x=renouvelables, orientation='h', marker_color=colors_bar[5]))

        graph_4.update_layout(
            barmode='stack',
            xaxis_title="Contribution des différentes sources dans le mix énergétique",
            yaxis_title="Pays",
            bargap=0.2,
            legend_title="Sources d'énergie",
            template="plotly_white",
            xaxis=dict(
                    ticksuffix=" %"
                ),
            yaxis=dict(
                automargin=True,
                tickfont=dict(size=15)
                ),
                margin=dict(l=150, r=150)
            )


       ## Card 4
       ## Card 4 - Mix énergétique (Danemark)
        query_5 = """
            SELECT
                gas       AS "Gaz",
                oil       AS "Pétrole",
                coal      AS "Charbon",
                renewable AS "Renouvelables",
                2.3 AS "Autres"
            FROM country
            WHERE country = 'denmark';
        """


        data_5 = fetch_all(query_5)

        columns_5 = [
                    "Gaz",
                    "Pétrole",
                    "Charbon",
                    "Renouvelables",
                    "Autres"
                ]

        # valeurs correspondantes
        values_5 = [data_5[0][col] for col in columns_5]

        # couleurs éclaircies (même teintes, plus lisibles)
        colors = [
            '#4F81BD',  # Bleu – Gaz 
            '#E57368',  # Rouge – Pétrole 
            '#8C8C8C',  # Gris – Charbon 
            '#FFD166',  # Jaune – Renouvelables 
            '#7C5CFF' # Autres
        ]


                
        # création du graph
        fig_5 = go.Figure(data=[go.Pie(
            labels=columns_5,
            values=values_5,
            marker=dict(colors=colors),
            hoverinfo='label+percent',
            textinfo='label',
            textfont=dict(size=14),
            hoverlabel=dict(font=dict(size=16))
        )])

        # mise en page  
        fig_5.update_layout(
            title_text="Danemark",
            title_font_size=18,
            title_x=0.5,
            showlegend=False,
            margin=dict(t=50, b=20, l=20, r=20)
        )


       ##  Mix énergétique (Nicaragua)
        query_6 = """
            SELECT
                oil       AS "Pétrole",
                hydro     AS "Hydro",
                renewable  AS "Renouvelables"
            FROM country
            WHERE country = 'nicaragua';
        """


        data_6 = fetch_all(query_6)

        columns_6 = [
                        "Pétrole",
                        "Hydro",
                        "Renouvelables"
                    ]

        # valeurs correspondantes
        values_6 = [data_6[0][col] for col in columns_6]

        # couleurs éclaircies (même teintes, plus lisibles)
        colors = [
            '#E57368',  # Rouge – Pétrole 
            '#6FCF97',  # Vert – Hydraulique 
            '#FFD166'   # Jaune – Renouvelables 
        ]


                
        # création du graph
        fig_6 = go.Figure(data=[go.Pie(
            labels=columns_6,
            values=values_6,
            marker=dict(colors=colors),
            hoverinfo='label+percent',
            textinfo='label',
            textfont=dict(size=14),
            hoverlabel=dict(font=dict(size=16))
        )])

        # mise en page  
        fig_6.update_layout(
            title_text="Nicargua",
            title_font_size=18,
            title_x=0.5,
            showlegend=False,
            margin=dict(t=50, b=20, l=20, r=20)
        )

       ##  Mix énergétique (kenya)
        query_7 = """
            SELECT
                oil       AS "Pétrole",
                hydro     AS "Hydro",
                renewable  AS "Renouvelables"
            FROM country
            WHERE country = 'kenya';
        """


        data_7 = fetch_all(query_7)

        columns_7 = [
                        "Pétrole",
                        "Hydro",
                        "Renouvelables"
                    ]

        # valeurs correspondantes
        values_7 = [data_7[0][col] for col in columns_7]

        # couleurs éclaircies (même teintes, plus lisibles)
        colors = [
            '#E57368',  # Rouge – Pétrole  
            '#6FCF97',  # Vert – Hydraulique 
            '#FFD166'   # Jaune – Renouvelables 
        ]


                
        # création du graph
        fig_7 = go.Figure(data=[go.Pie(
            labels=columns_7,
            values=values_7,
            marker=dict(colors=colors),
            hoverinfo='label+percent',
            textinfo='label',
            textfont=dict(size=14),
            hoverlabel=dict(font=dict(size=16))
        )])

        # mise en page  
        fig_7.update_layout(
            title_text="Kenya",
            title_font_size=18,
            title_x=0.5,
            showlegend=False,
            margin=dict(t=50, b=20, l=20, r=20)
        )
            
       # Conversion en JSON pour tous les graphs
        graph = fig.to_json()
        graph_2 = fig_2.to_json()
        graph_3 = fig_3.to_json()
        graph_4_json = graph_4.to_json()  
        graph_5_json = fig_5.to_json()
        graph_6_json = fig_6.to_json()
        graph_7_json = fig_7.to_json()


        return render_template(
            "observations.html", 
            graph=graph,
            graph_2=graph_2,
            graph_bar=graph_3,
            graph_4=graph_4_json,
            graph_5=graph_5_json,
            graph_6=graph_6_json,
            graph_7=graph_7_json
        )


    @app.route("/analyse")
    def analyse():
        selected_country = request.args.get('country', None)

        countries_data = fetch_all("SELECT DISTINCT country FROM country ORDER BY country")
        countries = [row['country'].capitalize() for row in countries_data]

        where_clause = ""
        if selected_country:
            country_sql = selected_country.lower()
            where_clause = f"WHERE LOWER(country) = '{country_sql}'"

        # Requête modifiée pour agréger TOUS les pays si aucun n'est sélectionné
        query = f"""
            WITH emissions AS (
                SELECT
                    country,
                    coal*820 AS coal_emission,
                    gas*490 AS gas_emission,
                    oil*740 AS oil_emission,
                    nuclear*12 AS nuclear_emission,
                    hydro*24 AS hydro_emission,
                    renewable*41 AS renewable_emission
                FROM country
                {where_clause}
            ),
            totals AS (
                SELECT
                    SUM(coal_emission) AS coal_emission,
                    SUM(gas_emission) AS gas_emission,
                    SUM(oil_emission) AS oil_emission,
                    SUM(nuclear_emission) AS nuclear_emission,
                    SUM(hydro_emission) AS hydro_emission,
                    SUM(renewable_emission) AS renewable_emission,
                    SUM(coal_emission + gas_emission + oil_emission + nuclear_emission + hydro_emission + renewable_emission) AS total
                FROM emissions
            )
            SELECT
                ROUND(coal_emission/NULLIF(total,0)*100,2) AS coal_pct,
                ROUND(gas_emission/NULLIF(total,0)*100,2) AS gas_pct,
                ROUND(oil_emission/NULLIF(total,0)*100,2) AS oil_pct,
                ROUND(nuclear_emission/NULLIF(total,0)*100,2) AS nuclear_pct,
                ROUND(hydro_emission/NULLIF(total,0)*100,2) AS hydro_pct,
                ROUND(renewable_emission/NULLIF(total,0)*100,2) AS renewable_pct
            FROM totals;
        """

        data = fetch_all(query)
        print("DATA:", data)  # <--- pour debug

        columns = ["coal_pct","gas_pct","oil_pct","nuclear_pct","hydro_pct","renewable_pct"]
        labels = ["Charbon","Gaz","Pétrole","Nucléaire","Hydro","Renouvelables"]

        if data:
            values = [data[0][col] if data[0][col] is not None else 0 for col in columns]
            country_label = selected_country.capitalize() if selected_country else "Tous les pays"
        else:
            values = [0]*6
            country_label = "Tous les pays"

        fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        fig.update_layout(title_text=f"Mix énergétique : {country_label}")

        graph = fig.to_json()

        return render_template("analyse.html",
                            graph=graph,
                            countries=countries,
                            selected_country=selected_country)

    
    @app.route("/methodologie")
    def methodologie():
        return render_template("methodologie.html")
    
    return app