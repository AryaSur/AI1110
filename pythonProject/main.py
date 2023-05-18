import random
import pygame
import os
import sys

# Shuffle the playlist
def create_random_playlist(audio_files):
    random.shuffle(audio_files)
    return audio_files


# List of 20 songs
audio_files = [str(i) + '.mp3' for i in range(1, 21)]

# Create a random playlist
random_playlist = create_random_playlist(audio_files)

# Initialize pygame mixer
pygame.init()

# Initialize the GUI
pygame.display.init()
width, height = 400, 200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Music Player")

font = pygame.font.Font(None, 36)
start_button = pygame.Rect(50, 80, 100, 40)
pause_button = pygame.Rect(160, 80, 100, 40)
next_button = pygame.Rect(270, 80, 100, 40)

# Play each song in the random playlist
for song in random_playlist:
    # Load song
    pygame.mixer.music.load(song)

    # Play song
    pygame.mixer.music.play()
    print("Shuffled playlist: ")
    print(song)
    index = 0
    playing = 1
    # Wait until the song finishes playing
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    # Check if the mouse click is within any button rectangle
                    if start_button.collidepoint(event.pos):
                        if not playing:
                            print("Playing:", random_playlist[index])
                            pygame.mixer.music.unpause()
                            playing = True
                    elif pause_button.collidepoint(event.pos):
                        if playing:
                            print("Paused:", random_playlist[index])
                            pygame.mixer.music.pause()
                            playing = False
                    elif next_button.collidepoint(event.pos):
                        if index < len(random_playlist) - 1:
                            index += 1
                            print("Playing:", random_playlist[index])
                            pygame.mixer.music.load(random_playlist[index])
                            pygame.mixer.music.play()
                            playing = True
                        else:
                            print("End of playlist.")
                            sys.exit()

        screen.fill((255, 255, 255))  # Clear the screen
        pygame.draw.rect(screen, (0, 255, 0), start_button)
        pygame.draw.rect(screen, (255, 255, 0), pause_button)
        pygame.draw.rect(screen, (0, 0, 255), next_button)

        start_text = font.render("Start", True, (0, 0, 0))
        screen.blit(start_text, (start_button.x + 20, start_button.y + 10))

        pause_text = font.render("Pause", True, (0, 0, 0))
        screen.blit(pause_text, (pause_button.x + 20, pause_button.y + 10))

        next_text = font.render("Next", True, (0, 0, 0))
        screen.blit(next_text, (next_button.x + 25, next_button.y + 10))

        pygame.display.update()  # Update the display

    # Clear the previous song
    pygame.mixer.music.stop()




# Clean up
pygame.mixer.quit()
pygame.quit()