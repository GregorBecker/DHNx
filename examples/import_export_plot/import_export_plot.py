import district_heating_simulation as dhs
import matplotlib.pyplot as plt

# initialize a thermal network
thermal_network = dhs.network.ThermalNetwork()

# load data from csv
thermal_network.load_from_csv('data_csv_input')

# save thermal network to csv
thermal_network.save_to_csv('data_csv_output')

# get graph of thermal network
graph = thermal_network.get_nx_graph()

# plot static map
static_map = dhs.plotting.StaticMap(thermal_network)

static_map.draw(background_map=False)
plt.savefig('static_map_wo_background.png')

static_map.draw(background_map=True)
plt.savefig('static_map_w_background.png')

# plot interactive map
interactive_map = dhs.plotting.InteractiveMap(thermal_network)
map = interactive_map.draw()
map.save('interactive_map.html')