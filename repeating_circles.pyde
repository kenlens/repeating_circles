def setup():
        # colors needed: deep lavender, yellow, black, white, pink, pastel purple
    moon = 100
    size (650, 500)
    x = 100
    y = 100
    while x < 650:
        y = 100
        while y < 500:
            print("x is " + str(x) + " and y is " + str(y))
            if x % 15 == 0:
                fill(240, 128, 128)
            ellipse(x, y, 100, 100)
            
            y = y + 110
        x = x + 110

    
