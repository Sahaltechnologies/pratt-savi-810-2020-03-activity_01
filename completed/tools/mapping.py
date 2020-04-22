import matplotlib.pyplot as plt
import contextily as ctx


def create_map(point, buffer, buffer_int, tracts, index):
    fig, ax = plt.subplots(figsize=(12, 12))

    buffer.plot(
        ax=ax,
        facecolor="none",
        edgecolor="orange",
    )

    tracts.plot(
        ax=ax,
        facecolor="none",
        edgecolor="grey",
    )

    buffer_int.plot(
        ax=ax,
        facecolor="orange",
        alpha=0.5,
        edgecolor="orange",
    )

    point.to_crs(epsg=3857).plot(
        ax=ax,
        facecolor='orange',
        markersize=500,
        marker="D",
    )

    ax.set_xlim(buffer.bounds['minx'][index], buffer.bounds['maxx'][index])
    ax.set_ylim(buffer.bounds['miny'][index], buffer.bounds['maxy'][index])

    population = buffer_int['pop_est'].sum()
    plt.title(f'{buffer["address"][index]} - Population: {population:,.0f}')

    ctx.add_basemap(
        ax,
        url='https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png'
    )

    ax.axis('off')

    plt.savefig(f'maps/map_{index}_int_tract_pop.png')
