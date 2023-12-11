# pages/home/page5.py
from dash import html, dcc
from pages.home.sidebar import layout as sidebar_layout

conclusion_text = """
**Fire Incidents Analysis: Insights**

1. Fire incidents are predominantly triggered by Medical Emergencies, Structural Fires, and Alarm activations.
2. A notable upward trend is observed in the annual frequency of fire emergency calls.
3. Particularly high numbers of fire incidents were recorded in September 2021, closely followed by December 2007.
4. The neighborhoods with the highest frequency of fire incidents are Tenderloin, South of Market, and Mission St.
5. In comparison to other locations, Lincoln Park, Treasure Island, and Bernal Heights exhibit longer response times to fire incidents.
"""

suggestions_text = """
**Suggestions for Improvement**

1. Implement community awareness programs to educate residents about fire safety measures and prevention strategies in high-risk areas such as Tenderloin, South of Market, and Mission St.
2. Enhance public access to fire safety resources, including conducting workshops and distributing informational pamphlets, to empower communities in understanding and mitigating fire risks.
3. Collaborate with local authorities and organizations to establish neighborhood-specific emergency response plans tailored to the unique challenges of areas with frequent fire incidents.
4. Introduce technology-driven solutions, such as mobile apps or smart alert systems, to expedite emergency response times in locations with historically high response delays, including Lincoln Park, Treasure Island, and Bernal Heights.
5. Explore the possibility of implementing predictive analytics and artificial intelligence to forecast potential fire-prone areas, enabling proactive measures and resource allocation.
6. Establish a community task force comprising residents, local businesses, and emergency services to foster a collaborative approach in addressing fire safety concerns and implementing preventive measures.
7. Conduct periodic evaluations and updates to the fire incident response plan, taking into account evolving community dynamics and changes in risk factors.
"""

heading_style = {"color": "rgb(255, 107, 107)", "text-align": "center", "margin-top": "50px"}

layout = html.Div(
    [
        html.Div(
            sidebar_layout,
            style={"width": "5%", "float": "left", "height": "calc(100vh - 100px)"},
        ),
        html.Div(
            [
                html.H2("Conclusion and Suggestions", style=heading_style),
                html.H3("Insights", style={"color": "rgb(255, 107, 107)", "margin-top": "10px"}),
                dcc.Markdown(conclusion_text),
                html.H3("Suggestions", style={"color": "rgb(255, 107, 107)", "margin-top": "20px"}),
                dcc.Markdown(suggestions_text),
            ],
            style={
                "width": "80%",
                "float": "left",
                "height": "calc(100vh - 100px)",
                "padding": "20px",
            },
        ),
    ],
    style={"margin-top": "100px", "width": "100%", "height": "calc(100vh - 100px)"},
)
