import random
import art, game_data

score = 0
compare_a = random.choice(game_data.data)
compare_b = random.choice(game_data.data)

print(art.logo, '\n\n')

while True:
    if compare_a['follower_count'] > compare_b['follower_count']:
        correct_answer = 'a'
    elif compare_a['follower_count'] < compare_b['follower_count']:
        correct_answer = 'b'
    else:
        correct_answer = ''

    print(f"[A] { compare_a['name']}: a {compare_a['description']} from {compare_a['country']}. {compare_a['follower_count']} million followers")
    print(art.vs, '\n')
    print(f"[B] {compare_b['name']}: a {compare_b['description']} from {compare_b['country']}")

    answer = input("\nWhich one has more followers on Instagram? A or B: ").lower()

    if correct_answer and not answer == correct_answer:
        break

    print(f"\nCorrect! {compare_b['name']} has {compare_b['follower_count']} million followers\n")
    score += 1
    compare_a = compare_b
    compare_b = random.choice(game_data.data)

print(f"\n\nGame Over! Your Final Score was {score}.")