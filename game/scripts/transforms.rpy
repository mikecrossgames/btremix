define fastdissolve = Dissolve(0.1)
define middissolve = Dissolve(0.25)
define slowdissolve = Dissolve(1.0)

style default:
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]

transform fadetoeasein(old_alpha, new_alpha, duration=1.0):
    alpha old_alpha
    easein duration alpha new_alpha

