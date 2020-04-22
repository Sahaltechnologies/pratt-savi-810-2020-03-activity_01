import matplotlib.pyplot as plt
import contextily as ctx


def create_map(point, buffer_pol, buffer_int, tracts, index):
    fig, ax = plt.subplots(figsize=(12, 12))


    # plot buffer_pol

    # plot tracts

    # plot buffer_int
       
    # plot point - be sure that it's using epsg=3857


    # center the map 
    ax.set_xlim(buffer_pol.bounds['minx'][index], buffer_pol.bounds['maxx'][index])
    ax.set_ylim(buffer_pol.bounds['miny'][index], buffer_pol.bounds['maxy'][index])

    population = buffer_int['pop_est'].sum()  # calc sum pop for buffer_int
    plt.title(f'{buffer["address"][index]} - Population: {population:,.0f}')  # add title

    ctx.add_basemap(
        ax,
        url='https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png'
    )  # add basemap

    ax.axis('off')  # turn off x, y axis lines

    plt.savefig(f'maps/map_{index}_int_tract_pop.png')
