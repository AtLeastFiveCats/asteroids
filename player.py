from constants import *
from circleshape import *
from bullet import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.PLAYER_SHOOT_COOLDOWN = 0        

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255 ,255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.PLAYER_SHOOT_COOLDOWN -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            if pygame.K_a:
                return self.rotate(-dt)

        if keys[pygame.K_d]:
            if pygame.K_d:
                return self.rotate(dt)
        
        if keys[pygame.K_w]:
            if pygame.K_w:
                return self.move(dt)

        if keys[pygame.K_s]:
            if pygame.K_s:
                return self.move(-dt)

        if keys[pygame.K_SPACE]:
            if self.PLAYER_SHOOT_COOLDOWN <= 0:
                self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        self.PLAYER_SHOOT_COOLDOWN = 0.3
        #Creating a Shot instance
        bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        #calculating the velocity vector
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        bullet.velocity = direction * PLAYER_SHOOT_SPEED


