import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

initial_velocity = 0.2
limit = 10
border = 1
min_distance = 2
number_of_particles = 100
repulsion_strength = 0.01
damping = 0.9

class Particle:
    def __init__(self, x, y):
        self.position = np.array([x, y])
        self.velocity = np.array([np.random.uniform(-initial_velocity, initial_velocity), np.random.uniform(-initial_velocity, initial_velocity)])
        self.color = 'blue'

    def update(self):
        if self.position[0] >= limit - border or self.position[0] <= -limit + border:
            self.velocity[0] = -self.velocity[0]
        if self.position[1] >= limit - border or self.position[1] <= -limit + border:
            self.velocity[1] = -self.velocity[1]
        self.position += self.velocity

class ParticleSystem:
    def __init__(self):
        self.particles = []

    def create_particles(self, num_particles):
        for _ in range(num_particles):
            new_particle = Particle(
                np.random.uniform(-limit + border, limit - border),
                np.random.uniform(-limit + border, limit - border)
            )
            self.particles.append(new_particle)

    def update(self):
        for p1 in self.particles:
            force = np.array([0.0, 0.0])
            for p2 in self.particles:
                if p1 != p2:
                    distance = np.linalg.norm(p1.position - p2.position)
                    if distance < min_distance:
                        direction = (p1.position - p2.position) / distance
                        force += direction * repulsion_strength / distance**2
            p1.velocity += force
            p1.velocity *= damping
            p1.update()

    def get_positions_colors(self):
        positions = np.array([p.position for p in self.particles])
        colors = np.array([p.color for p in self.particles])
        return positions, colors

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)

particle_system = ParticleSystem()
particle_system.create_particles(number_of_particles)

def update(frame):
    ax.clear()
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)

    particle_system.update()
    positions, colors = particle_system.get_positions_colors()

    if len(positions) > 0:
        ax.scatter(positions[:, 0], positions[:, 1], c=colors, alpha=0.6)

ani = animation.FuncAnimation(fig, update, frames=200, interval=50)

plt.show()