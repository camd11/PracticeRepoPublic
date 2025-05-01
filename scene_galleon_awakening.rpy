label scene_galleon_awakening:

    # Scene Description: Waking up disoriented in a damp, creaking cabin aboard a massive galleon. The air smells of salt, damp wood, and something else... spectral?

    ```renpy
    label scene_galleon_awakening:
    
        scene bg ship_cabin_dim with dissolve
    
        # Add sound effects if available, e.g., ambient creaking wood and distant waves
        # play sound "sounds/ship_creak_loop.ogg" loop volume 0.7
        # play sound "sounds/distant_waves_loop.ogg" loop volume 0.5
    
        "..."
        "Ugh... my head..."
        "A dull throbbing pulsed behind my eyes, each beat echoing the slow, rhythmic sway beneath me."
        "Where... am I?"
        "My eyelids felt heavy, glued together. Forcing them open revealed only oppressive dimness."
        "Rough wood pressed against my back. Cold, damp wood."
        "The air was thick, heavy with the cloying scent of salt spray and old, wet timber."
        "But underneath that... there was something else."
        "A strange, almost metallic tang? No... more like the chilling emptiness of a long-abandoned cellar, or the static before a lightning strike."
        "It felt... spectral. Unsettling."
        "A low groan resonated through the structure around me – the sound of massive timbers straining against an unseen force."
        "Water sloshed rhythmically, somewhere nearby but muffled, distant."
        "I pushed myself up, muscles protesting weakly. The floor tilted under me, a constant, gentle rocking motion."
        "My eyes adjusted slowly to the gloom."
        "I was in a small cabin. Dark, damp wood formed the walls, floor, and low ceiling. Everything felt condensed, claustrophobic."
        "Faint light filtered in from somewhere, perhaps cracks in the walls or a grimy porthole, barely illuminating the cramped space."
        "Dust motes danced in the weak rays, disturbed by my movement."
        "A ship? It had to be. A large one, judging by the deep creaks and the slow, ponderous roll."
        "But how did I get here?"
        "My last memory was..."
        "It flickered, hazy and indistinct. Fragmented images, loud noises... then darkness."
        "Panic began to coil in my stomach."
        "This damp, creaking prison... that unsettling chill in the air... something was deeply wrong."
        "I needed to figure out where I was. And how to get off this ghost ship."
    
        # End the scene here, likely leading to exploration or another event.
        # jump scene_cabin_exploration # Example jump
        return
    ```

    # TODO: Add choices or jump to the next scene
    return
