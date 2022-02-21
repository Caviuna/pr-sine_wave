"""
Sine Wave
by Daniel Shiffman.
adapted by Andre Caviuna
 
Render a simple sine wave.
"""



xspacing = 16       # How far apart should each horizontal location be spaced

theta = 0.0         # Start angle at 0
amplitude = 75.0    # Height of wave
period = 400.0      # How many pixels before the wave repeats

# Value for incrementing X, a function of period and xspacing
dx = (TWO_PI / period) * xspacing 


def setup():
    size(640, 280)
    global w  # Width of entire wave
    w = width + 16
    # Using a list to store height values for the wave.
    global yvalues
    yvalues = [0.0] * (w / xspacing)

    global z  
    z = width + 16
    global zvalues
    zvalues = [0.0] * (z / xspacing)

    global z1  
    z1 = width + 16
    global z1values
    z1values = [0.0] * (z1 / xspacing)


def draw():
    background(random(255))
    strokeWeight(3)
    calcWave()
    renderWave()
    
    saveFrame("frames//###.png") 

def calcWave():
    global theta
    # Increment theta (try different values for 'angular velocity' here
    theta += 0.08 # 0.02 for see in processing , 0.08 for see in  Movie Maker 
    # For every x value, calculate a y value with sine function
    x = theta
    for i in range(len(yvalues)):
        yvalues[i] = sin(x) * amplitude
        x += dx
    for i in range(len(zvalues)):
        zvalues[i] = sin(x) * amplitude
        x += dx
    for i in range(len(z1values)):
        z1values[i] = sin(x) * amplitude
        x += dx

def renderWave():
    # A simple way to draw the wave with an ellipse and rectangle at each location
    for x in range(len(yvalues)):
        noStroke()
        fill(random(255), random(255), random(255))
        ellipse(x * xspacing, height / 2 + yvalues[x], 16, 16)
        color(31)

    for x in range(len(zvalues)):
        noStroke()
        fill(255)
        rect(x * xspacing, height / 2 + zvalues[x], 16, 16)

    for x in range(len(z1values)):
        noStroke()
        fill(255, 0, 0, 127)
        ellipse(x * xspacing, height / 2 + z1values[x], 16, 16)