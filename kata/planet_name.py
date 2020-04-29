def get_planet_name(id):
    # This doesn't work; Fix it!
    name= {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune"
    }.get(id)
    return name

if __name__ == '__main__':
    assert get_planet_name(2) == 'Venus'
    assert get_planet_name(5) == 'Jupiter'
    assert get_planet_name(3) == 'Earth'
    assert get_planet_name(1) == 'Mercury'