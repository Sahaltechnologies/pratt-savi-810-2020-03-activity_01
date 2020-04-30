import matplotlib.pyplot as plt
import contextily as ctx
import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['font.sans-serif'] = "Open Sans"


# create_map(point, buffer, gdf_int, tracts_file, index)

def create_map(
        point,
        buffer_pol,
        buffer_int,
        tracts,
        index,
        maps_dir='../maps',  # or try '/maps'
):
    tracts = tracts.to_crs(epsg=3857)
    point = point.to_crs(epsg=3857)

    fig, ax = plt.subplots(figsize=(12, 12))

    # plot tracts
    # tracts=tract.plot(  # do these variables or arguments need to be named?
    tracts.plot(
        ax=ax,
        facecolor='white',
        edgecolor='darkgrey',
        linewidth=.25,
        alpha=.5,
    )
    # buffer_pol.plot( # we don't really need to plot this, it's there with the buffer_int file
    # ax=ax,
    # facecolor="none",
    # edgecolor="red",
    # linewidth=2,
    # alpha=.6,
    # )
    # plot buffer_int
    buffer_int.plot(
        ax=ax,
        facecolor="orange",
        edgecolor='white',
        lw=.5,
        alpha=.8,
        # legend=True,
        # legend_kwds={'title': 'pop_est'}
    )
    # plot point - be sure that it's using epsg=3857
    point.plot(
        ax=ax,
        markersize=200,
        color='yellow',
        edgecolor='white',
        lw=.5,
    )

    # center the map
    ax.set_xlim(buffer_pol.bounds['minx'][index], buffer_pol.bounds['maxx'][index])
    ax.set_ylim(buffer_pol.bounds['miny'][index], buffer_pol.bounds['maxy'][index])

    population = buffer_int['pop_est'].sum().astype('int64')
    # add proportional sum of population for tracts in buffer int for buffer circle
    # population = population.astype('int64') to give a round number instead of a float
    plt.title(f'{point["address"][index]} - Population: {population}', fontsize=14)  # add title

    ctx.add_basemap(
        ax,
        source=ctx.providers.Stamen.TonerLite
    )

    ax.axis('off')  # turn off x, y axis lines
    ax.grid(False)

    plt.savefig(f'maps/map_{index}_int_tract_pop.pdf')
