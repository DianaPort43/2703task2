from geometry import calculate_area

def test_calculate_area():
    assert calculate_area("rectangle", width=4, height=5) == 20
    assert calculate_area("square", side=4) == 16
    assert round(calculate_area("circle", radius=3), 2) == 28.27