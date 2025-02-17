import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Word Bee Game Visuals")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 204, 0)
GREY = (200, 200, 200)

# Font
font = pygame.font.Font(None, 50)
fontTwo =  pygame.font.Font(None, 25)
WORDS =  {
    "lamp": 5,
    "clap": 5,
    "grim" : 5,
    "trap" : 5,
    "brim" : 5,
    'stamp' : 5,
    "cramp": 5,
    "ramp" : 5,
    "clamp" : 5,
    "grip" : 5,
}
letters = [ 'L', 'A', 'M', 'G', 'I', 'R' , 'P' ]


# Position for rectangles
positions = [(100, 150), (160, 90), (222, 90), (280, 150), (222, 215), (160, 215), (190, 153)]

# Font
font = pygame.font.Font(None, 30)

# Input text
guess = ""
input_box = pygame.Rect(50, 35, 190, 40)  # Input box rectangle
submitted_texts = []
response_text = ""


#Draw a hexagonal shaped  square letter boxes
def draw_letters():
    for i, letter in enumerate(letters):
        rect = pygame.Rect(positions[i][0], positions[i][1], 60, 60)
        pygame.draw.rect(screen, YELLOW, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)
        text = font.render(letter, True, BLACK)
        screen.blit(text, (positions[i][0] + 15, positions[i][1] + 10))

#Guess the words
def guesses(guess):
    global response_text
    print("Guess", guess)       
    if guess in WORDS:
        print(f"Good Job! You got {WORDS[guess]} points!")
        WORDS.pop(guess)
        print(f"You  left with {len(WORDS)} words to guess!")
        submitted_texts.append(guess)
        response_text= f"Good Job! {len(WORDS)} words left"
        if len(WORDS) == 0: 
            response_text = "You won!"
            submitted_texts.clear()
            pygame.quit()
    else:
        print("Word not found! Try Again!")
        response_text = "Word not found! Try Again!"




# Game loop
while True:
    screen.fill(WHITE)
    welcomeText= '''Welcome to Spelling Bee Game'''


     # Render input text inside the box
    text_surface = font.render(welcomeText, True, BLACK)
    screen.blit(text_surface, (50, 5))
   
 
    # Draw input box with grey border line
    pygame.draw.rect(screen, GREY, input_box, 2)
    

   

    draw_letters()

     # Render input text inside the box
    text_surface = font.render(guess, True, BLACK)
    screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))

    x_offset = 20
    for text in submitted_texts:
        submitted_surface = fontTwo.render(text, True, BLACK)
        screen.blit(submitted_surface, (x_offset, 300))
        x_offset += 60
    
    text_surface = font.render(response_text, True, BLACK)
    screen.blit(text_surface,(20, 350))

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         # Keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                guesses(guess)
                guess = ""
                
            elif event.key == pygame.K_BACKSPACE:
                guess = guess[:-1]
            else:
                guess += event.unicode


    pygame.display.flip()




    
# main()