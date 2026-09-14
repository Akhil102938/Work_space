def asteroid_collision(asteroids):
    alive = []

    for current in asteroids:

        # Handle possible collisions
        while alive and alive[-1] > 0 and current < 0:

            if abs(alive[-1]) < abs(current):
                alive.pop()

            elif abs(alive[-1]) == abs(current):
                alive.pop()
                current = 0
                break

            else:
                current = 0
                break

        # Add surviving asteroid
        if current != 0:
            alive.append(current)

    return alive


asteroids = [
    5, 10, -5, 8, -8, 12, -3, -4,
    7, -10, 6, 4, -5, -12, 15
]

result = asteroid_collision(asteroids)

print(result)
