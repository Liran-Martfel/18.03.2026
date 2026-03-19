import pygame
import random
import sys

# --- אתחול ---
pygame.init()
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cyber-Vegas Slot Machine - Custom Bet")
clock = pygame.time.Clock()

# צבעים
BG_COLOR = (10, 10, 20)
NEON_PURPLE = (179, 136, 255)
DARK_PURPLE = (48, 10, 80)
FOREST_GREEN = (57, 255, 20)
NEON_RED = (255, 31, 31)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)

# פונטים
font_ui = pygame.font.SysFont("consolas", 24, bold=True)
font_symbol = pygame.font.SysFont("segoe ui emoji", 65)

# נתוני המשחק
rate = [2, 3, 9, 7, 11]
symbols = ["🍒", "🍋", "⭐", "🔔", "💎"]
my_money = 50
bet_input_text = "5"  # הטקסט שהמשתמש מקליד
active_input = False  # האם תיבת הקלט במיקוד
reels = ["💎", "💎", "💎"]
is_spinning = False
spin_duration = 0
result_msg = ""


def check_win(current_reels):
    unique = len(set(current_reels))
    if unique == 1: return 3
    if unique == 2: return 2
    return None


def update_money(res, current_money, current_bet, current_reels):
    if res == 3:
        winning_symbol = current_reels[0]
        mult = rate[symbols.index(winning_symbol)]
        return current_money + ((current_bet * 777 * mult) - current_bet), "JACKPOT!"
    if res == 2:
        return current_money + ((current_bet * 11) - current_bet), "WINNER!"
    return current_money - current_bet, "TRY AGAIN"


def draw_lever(is_down):
    base_x, base_y = 780, 350
    lever_height = 100
    end_y = base_y + (lever_height if is_down else -lever_height)
    pygame.draw.line(screen, (100, 100, 100), (base_x, base_y), (base_x + 30, end_y), 15)
    pygame.draw.circle(screen, NEON_RED, (base_x + 30, end_y), 25)
    pygame.draw.circle(screen, (50, 50, 50), (base_x, base_y), 20)


# --- לולאה ראשית ---
running = True
input_rect = pygame.Rect(50, 150, 140, 40)  # מיקום תיבת הקלט

while running:
    screen.fill(BG_COLOR)

    # המרת הטקסט למספר (בדיקת בטיחות)
    try:
        current_bet = int(bet_input_text) if bet_input_text != "" else 0
    except ValueError:
        current_bet = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # בדיקה אם לחצו על תיבת הקלט
            if input_rect.collidepoint(event.pos):
                active_input = True
            else:
                active_input = False

            # בדיקת לחיצה על הידית
            if 750 < event.pos[0] < 850 and 200 < event.pos[1] < 500:
                if not is_spinning and 0 < current_bet <= my_money:
                    is_spinning = True
                    spin_duration = 40
                    result_msg = ""

        if event.type == pygame.KEYDOWN:
            if active_input:
                if event.key == pygame.K_BACKSPACE:
                    bet_input_text = bet_input_text[:-1]
                elif event.unicode.isdigit():  # מאפשר רק מספרים
                    if len(bet_input_text) < 5:  # הגבלת אורך
                        bet_input_text += event.unicode

            # הפעלה עם רווח (רק אם לא מקלידים כרגע)
            if event.key == pygame.K_SPACE and not active_input:
                if not is_spinning and 0 < current_bet <= my_money:
                    is_spinning = True
                    spin_duration = 40
                    result_msg = ""

    # עדכון לוגיקה
    if is_spinning:
        spin_duration -= 1
        reels = [random.choice(symbols) for _ in range(3)]
        if spin_duration <= 0:
            is_spinning = False
            res = check_win(reels)
            my_money, result_msg = update_money(res, my_money, current_bet, reels)

    # --- ציור ---
    # גוף המכונה
    pygame.draw.rect(screen, DARK_PURPLE, (150, 200, 600, 300), border_radius=20)
    pygame.draw.rect(screen, NEON_PURPLE, (150, 200, 600, 300), 5, border_radius=20)

    for i in range(3):
        x_p = 200 + (i * 180)
        pygame.draw.rect(screen, (20, 20, 40), (x_p, 250, 150, 200), border_radius=10)
        sym = font_symbol.render(reels[i], True, WHITE)
        screen.blit(sym, (x_p + (150 - sym.get_width()) // 2, 310))

    draw_lever(is_spinning)

    # UI וכסף
    balance_txt = font_ui.render(f"CASH: ${my_money}", True, FOREST_GREEN)
    screen.blit(balance_txt, (50, 50))

    # תיבת קלט להימור
    label_txt = font_ui.render("SET BET:", True, WHITE)
    screen.blit(label_txt, (50, 115))

    # צבע התיבה משתנה כשהיא פעילה
    box_color = FOREST_GREEN if active_input else NEON_PURPLE
    pygame.draw.rect(screen, (30, 30, 50), input_rect, border_radius=5)
    pygame.draw.rect(screen, box_color, input_rect, 2, border_radius=5)

    input_surface = font_ui.render(bet_input_text, True, WHITE)
    screen.blit(input_surface, (input_rect.x + 10, input_rect.y + 5))

    # הודעות
    msg_txt = font_ui.render(result_msg, True, GOLD if "WIN" in result_msg else NEON_RED)
    screen.blit(msg_txt, (WIDTH // 2 - msg_txt.get_width() // 2, 550))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()