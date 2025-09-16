import random
import time

# --- Utility Functions ---
def slow_print(text, delay=0.03):
    """Prints text slowly for atmosphere."""
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()

def alien_glyphs(length=10):
    symbols = "⟁⌖⟟⌬⋔⟊⏃⊑⟒⍜⎅⋉⌇⌿⍀☌☍☊⚳"
    return "".join(random.choice(symbols) for _ in range(length))

def alien_speech(message, knowledge):
    """Alien language becomes clearer with more knowledge."""
    clarity = knowledge // 2
    if clarity >= len(message):
        return message
    scrambled = list(message)
    for i in range(len(message) - clarity):
        scrambled[i] = random.choice("⟟⋔⟊⍜⎅⌇")
    return "".join(scrambled)


# --- Game Data ---
player = {
    "health": 10,
    "sanity": 10,
    "knowledge": 0,
    "inventory": []
}

locations = {
    "ruins": "Broken monoliths and glowing glyphs whisper forgotten truths.",
    "jungle": "The alien jungle hums with unseen life. The air vibrates.",
    "caves": "Crystal walls shimmer, and echoes twist into voices.",
    "temple": "The obsidian temple looms... sealed until you hold 3 artifacts."
}

required_artifacts = {"crystal orb", "glyph tablet", "alien shard"}


# --- Game Functions ---
def intro():
    slow_print("🌌 You awaken under two moons, in the ruins of a forgotten alien world...")
    slow_print("Glyphs burn into your mind:")
    slow_print(alien_glyphs(30))
    slow_print("\nA whisper: 'SEEK... THE TEMPLE... THREE KEYS... TRUTH...'\n")


def show_stats():
    print(f"\n❤️ Health: {player['health']} | 🧠 Sanity: {player['sanity']} | 📖 Knowledge: {player['knowledge']}")
    print(f"🎒 Inventory: {player['inventory']}\n")


def explore(location):
    if location == "temple" and not required_artifacts.issubset(player["inventory"]):
        slow_print("⚠️ The temple doors remain sealed. You sense 3 artifacts are needed...")
        return

    slow_print(f"\nYou enter the {location.upper()}: {locations[location]}")
    
    if location == "temple":
        final_battle()
        return
    
    event = random.choice(["alien", "artifact", "glyph", "madness", "trap", "nothing"])
    
    if event == "alien":
        alien_encounter()
    elif event == "artifact":
        find_artifact()
    elif event == "glyph":
        glyph_puzzle()
    elif event == "madness":
        madness_vision()
    elif event == "trap":
        trap_event()
    else:
        slow_print("The silence here feels heavy... but nothing happens.")


def alien_encounter():
    slow_print("\n👁 A shadowy alien entity appears, its form shifting like smoke...")
    msg = alien_speech("JOIN US OR PERISH", player["knowledge"])
    slow_print(f"It utters: {msg}")
    
    choice = input("Do you [1] fight, [2] communicate, [3] flee? ")
    
    if choice == "1":
        outcome = random.choice(["win", "lose"])
        if outcome == "win":
            slow_print("⚔️ You strike bravely! The alien dissolves into mist.")
            player["sanity"] -= 1
        else:
            slow_print("☠️ The alien engulfs you in shadows. You barely escape.")
            player["health"] -= 3
    elif choice == "2":
        if player["knowledge"] > 2:
            slow_print("✨ The alien seems to understand... it gifts you an artifact.")
            player["inventory"].append("alien shard")
        else:
            slow_print("The alien tilts its head... then vanishes, leaving you drained.")
            player["sanity"] -= 2
    else:
        slow_print("You retreat quickly, your heart pounding.")


def find_artifact():
    artifact = random.choice(list(required_artifacts))
    if artifact not in player["inventory"]:
        slow_print(f"🔮 You discover a {artifact}!")
        player["inventory"].append(artifact)
    else:
        slow_print("You find broken remnants of something once powerful...")


def glyph_puzzle():
    slow_print("\nYou find glowing alien glyphs carved into the stone...")
    real_word = random.choice(["LIFE", "VOID", "STAR", "FIRE", "TIME"])
    scrambled = "".join(random.sample(real_word, len(real_word)))
    slow_print(f"The glyphs rearrange: {alien_glyphs(10)} [{scrambled}] {alien_glyphs(10)}")
    
    guess = input("Translate the glyph word: ").strip().upper()
    if guess == real_word:
        slow_print("🌟 The glyphs shine brighter... knowledge flows into you.")
        player["knowledge"] += 1
    else:
        slow_print("⚡ The glyphs reject you. A psychic backlash shakes your mind.")
        player["sanity"] -= 2


def madness_vision():
    slow_print("\n🌑 A wave of psychic energy crashes over you...")
    vision = alien_glyphs(40)
    slow_print(f"Visions flood your mind: {vision}")
    player["sanity"] -= 1


def trap_event():
    slow_print("\n⚠️ A hidden alien mechanism activates! A dart strikes you...")
    player["health"] -= 2


def final_battle():
    slow_print("\n🏛 You step into the obsidian temple. Glyphs ignite across the walls...")
    slow_print("A towering alien guardian emerges, its form shifting between flesh and crystal.")
    msg = alien_speech("ONLY ONE MAY ASCEND", player["knowledge"])
    slow_print(f"It proclaims: {msg}")
    
    choice = input("Do you [1] fight, [2] attempt to communicate, [3] surrender? ")
    
    if choice == "1":
        if "crystal orb" in player["inventory"]:
            slow_print("⚔️ With the crystal orb, your strikes resonate with alien energy!")
            slow_print("The guardian shatters. You ascend into starlight... 🌌")
            ending("ascension")
        else:
            slow_print("☠️ The guardian overwhelms you. Your journey ends here...")
            ending("death")
    elif choice == "2":
        if player["knowledge"] >= 5:
            slow_print("✨ You speak the alien tongue fluently now.")
            slow_print("The guardian kneels and grants you passage beyond the stars.")
            ending("understanding")
        else:
            slow_print("Your words falter... the guardian strikes you down.")
            ending("death")
    else:
        slow_print("You kneel before the guardian... it engulfs you in eternal darkness.")
        ending("death")


def ending(type_):
    if type_ == "ascension":
        slow_print("\n🌌 Ending: You ascend beyond mortal form, joining the alien stars.")
    elif type_ == "understanding":
        slow_print("\n📖 Ending: You become the first human fluent in the alien tongue, bridging worlds.")
    else:
        slow_print("\n💀 Ending: The ruins claim another soul. Silence returns.")
    exit()


# --- Main Loop ---
def game():
    intro()
    
    while player["health"] > 0 and player["sanity"] > 0:
        show_stats()
        print("Where will you go? [ruins / jungle / caves / temple / quit]")
        choice = input("> ").lower()
        
        if choice in locations:
            explore(choice)
        elif choice == "quit":
            slow_print("\nYour journey ends here... but the glyphs remain.")
            break
        else:
            slow_print("That path does not exist.")
    
    slow_print("\n💀 Your mind or body could not endure the alien world...")
    slow_print("The ruins fall silent once more.")


if __name__ == "__main__":
    game()
