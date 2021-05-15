import dash
import dash_html_components as html

import holoviews as hv
from holoviews.plotting.plotly.dash import to_dash



if __name__ == "__main__":
	from distributed import Client, local_client
	client = Client()

	import modin.pandas as pd

	df = pd.read_parquet('output_file.parquet')

	# Load dataset

	dataset = hv.Dataset(df)

	scatter = hv.Scatter(dataset, kdims=["passenger_count"], vdims=["total_amount"])
	# hist = hv.operation.histogram(
	#     dataset, dimension="petal_width", normed=False
	# )

	app = dash.Dash(__name__)
	components = to_dash(app, [scatter, ])

	app.layout = html.Div(components.children)
	app.run_server(debug=True)