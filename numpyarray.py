import numpy as np

height_incm = np.array(
    [183, 191, 176, 198, 187, 201, 179, 194, 185, 203, 181, 189, 193, 189, 194, 169, 160, 202, 198, 188
     ])


heights_inM = height_incm / 100

print("Height of players in the Football team in cm=", height_incm)
print("Height of players in the Football team in Metres=", heights_inM)


avrg_mean = np.mean(heights_inM)
max_height = np.max(heights_inM)
min_height = np.min(heights_inM)

print("Average height of the team = ", avrg_mean)
print("Height of the tallest player=", max_height)
print('Height of the Shortest player=', min_height)
