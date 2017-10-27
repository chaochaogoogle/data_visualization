import pygal.maps.world
wm = pygal.maps.world.World()
wm.title = 'North, Central, and South American'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central American', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South American', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americans.svg')