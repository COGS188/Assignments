import pygame
import numpy as np
import sys
import argparse
from bandits import egreedy, update


def main(epsilon: float = 0.1, mode: str = "manual"):

    # Initialize Pygame
    pygame.init()

    # Set up display
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Slot Machine Simulator")

    # Colors
    background_color = (30, 30, 30)
    button_color = (100, 200, 100)
    text_color = (255, 255, 255)
    highlight_color = (255, 0, 0)

    # Fonts
    font = pygame.font.Font(None, 36)

    # Slot machine settings
    n_machines = 3
    true_rewards_probabilities = np.random.rand(n_machines) * 0.9 + 0.1  # Random rewards between 0.1 and 1.0
    estimated_rewards = np.zeros(n_machines)
    play_counts = np.zeros(n_machines)

    # Cost and Rewards
    cost_per_play = 0.05
    total_reward = 0

    # Button dimensions
    button_width = 150
    button_height = 90
    button_margin = 100
    start_x = (screen_width - n_machines * button_width - (n_machines - 1) * button_margin) / 2
    # Game loop
    running = True
    reward = 0
    while running:
        screen.fill(background_color)
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mode == "manual":
                pos = pygame.mouse.get_pos()
                for i in range(n_machines):
                    x = start_x + i * (button_width + button_margin)
                    y = (screen_height - button_height) / 2
                    if x <= pos[0] <= x + button_width and y <= pos[1] <= y + button_height:
                        reward = np.random.rand() < true_rewards_probabilities[i]
                        play_counts[i] += 1
                        total_reward += reward - cost_per_play
                        estimated_rewards[i] += (reward - estimated_rewards[i]) / play_counts[i]

        # AI mode action
        if mode == "AI":
            # TODO: Implement the epsilon-greedy algorithm
            # TODO:  Select a machine to play, save that to chosen_machine

            # TODO: update the estimated rewards and play counts, update the estimated_reward for the chosen machine

            # TODO: calculate the reward and update the total reward

            # Add a small delay to see the AI in action
            # Draw the selected machine's picture in AI mode
            chosen_image = pygame.image.load("pull.jpg")
            chosen_image = pygame.transform.scale(chosen_image, (50, 50))
            chosen_x = start_x + chosen_machine * (button_width + button_margin) + button_width / 2 - 25
            chosen_y = (screen_height + button_height) / 2 + 20
            screen.blit(chosen_image, (chosen_x, chosen_y))
            pygame.time.wait(100)

        # Draw buttons and labels
        for i in range(n_machines):
            x = start_x + i * (button_width + button_margin)
            y = (screen_height - button_height) / 2
            pygame.draw.rect(screen, button_color, (x, y, button_width, button_height))

            machine_label = font.render(f"Machine {i+1}", True, text_color)
            machine_rect = machine_label.get_rect(center=(x + button_width / 2, y + button_height / 3))
            screen.blit(machine_label, machine_rect)
            # Add true reward display
            true_reward_label = font.render(
                f"True Win Prob: {true_rewards_probabilities[i]:.2f}", True, highlight_color
            )
            true_reward_rect = true_reward_label.get_rect(center=(x + button_width / 2, y - 20))
            screen.blit(true_reward_label, true_reward_rect)

            # Add Q-value (estimated reward) display
            q_label = font.render(f"Q: {estimated_rewards[i]:.2f}", True, highlight_color)
            q_rect = q_label.get_rect(center=(x + button_width / 2, y - 50))
            screen.blit(q_label, q_rect)

            plays_label = font.render(f"Plays: {int(play_counts[i])}", True, text_color)
            plays_rect = plays_label.get_rect(center=(x + button_width / 2, y + 2 * button_height / 3))
            screen.blit(plays_label, plays_rect)

        # Display total reward
        reward_text = font.render(f"Net Reward: {total_reward:.2f}", True, text_color)
        reward_rect = reward_text.get_rect(center=(screen_width / 2, 50))
        screen.blit(reward_text, reward_rect)

        # Display win/loss message and reward change
        message = f"{'Win' if reward else 'Loss'}, Reward: {(reward - cost_per_play):.2f}"
        message_text = font.render(message, True, text_color)
        message_rect = message_text.get_rect(center=(screen_width / 2, screen_height - 50))
        screen.blit(message_text, message_rect)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    # Run the main function
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Play the slot machine simulator in manual or AI mode.")
    parser.add_argument(
        "--mode",
        type=str,
        choices=["manual", "AI"],
        default="manual",
        help="Choose 'manual' to play the game yourself or 'AI' for the epsilon-greedy algorithm to play.",
    )
    parser.add_argument(
        "--epsilon",
        type=float,
        default="0.1",
        help="The epsilon value for the epsilon-greedy algorithm. Default is 0.1.",
    )
    args = parser.parse_args()
    main(args.epsilon, args.mode)
