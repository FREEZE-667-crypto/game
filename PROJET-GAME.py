import pygame
import sys

# Initialisation
pygame.init()
LARGEUR, HAUTEUR = 500, 700
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Jeu de course 2D")

# Couleurs

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (200, 0, 0)

# Joueur
voiture_larg, voiture_haut = 50, 80
voiture_x = LARGEUR // 2 - voiture_larg // 2
voiture_y = HAUTEUR - voiture_haut - 20
vitesse = 5

# Ennemi
ennemi_x = LARGEUR // 2 - voiture_larg // 2
ennemi_y = -100
ennemi_vitesse = 5

clock = pygame.time.Clock()

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Contrôles
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT] and voiture_x > 0:
        voiture_x -= vitesse
    if touches[pygame.K_RIGHT] and voiture_x < LARGEUR - voiture_larg:
        voiture_x += vitesse

    # Mouvement ennemi
    ennemi_y += ennemi_vitesse
    if ennemi_y > HAUTEUR:
        ennemi_y = -100
        ennemi_x = pygame.mouse.get_pos()[0] - voiture_larg // 2

    # Détection collision
    joueur_rect = pygame.Rect(voiture_x, voiture_y, voiture_larg, voiture_haut)
    ennemi_rect = pygame.Rect(ennemi_x, ennemi_y, voiture_larg, voiture_haut)
    if joueur_rect.colliderect(ennemi_rect):
        print("💥 Collision !")
        pygame.quit()
        sys.exit()

    # Affichage
    fenetre.fill(BLANC)
    pygame.draw.rect(fenetre, ROUGE, joueur_rect)  # voiture joueur
    pygame.draw.rect(fenetre, NOIR, ennemi_rect)   # voiture ennemie
    pygame.display.flip()
    clock.tick(60)
import pygame


