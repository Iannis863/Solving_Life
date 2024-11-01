import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Particle:
    def __init__(self, x, y):
        self.position = np.array([x, y])
        self.velocity = np.array([np.random.uniform(-2, 2), np.random.uniform(0, 1)])
        self.lifetime = np.random.uniform(50, 100)

    def update(self):
        self.position += self.velocity
        self.lifetime -= 1  # Decrease lifetime

    def get_color(self):
        ratio = self.lifetime / 150
        r = 1.0
        g = 1.0 * ratio
        b = 0.0
        return r, g, b


class ParticleSystem:
    def __init__(self, base_position):
        self.particles = []
        self.base_position = base_position

    def update(self):
        for p in self.particles:
            p.update()

        self.particles = [p for p in self.particles if p.lifetime > 0]

        num_new_particles = 1000
        for _ in range(num_new_particles):
            new_particle = Particle(
                self.base_position[0] + np.random.uniform(-2, 2),
                self.base_position[1]
            )
            self.particles.append(new_particle)

        if len(self.particles) > 10000:
            self.particles = self.particles[-10000:]

    def get_positions_and_colors(self):
        positions = np.array([p.position for p in self.particles])
        colors = np.array([p.get_color() for p in self.particles])
        return positions, colors


fig, ax = plt.subplots()
ax.set_xlim(-20, 20)
ax.set_ylim(1, 8)
ax.axis('off')

base_position = np.array([0, 0])
particle_system = ParticleSystem(base_position=base_position)


def update(frame):
    ax.clear()
    ax.set_xlim(-20, 20)
    ax.set_ylim(1, 8)
    ax.axis('off')

    particle_system.update()
    positions, colors = particle_system.get_positions_and_colors()

    if len(positions) > 0:
        ax.scatter(positions[:, 0], positions[:, 1], c = colors, alpha=0.3)


ani = animation.FuncAnimation(fig, update, frames=200, interval=50)

plt.show()
