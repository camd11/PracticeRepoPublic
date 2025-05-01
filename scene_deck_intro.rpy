label scene_deck_intro:

    # Scene Description: Emerging onto the deck of the Ghost Ship Galleon. The crew eyes you warily. The Quartermaster, Silas, approaches.

    ```renpy
    label scene_deck_intro:
    
        scene bg ghost_deck with fade
        play music "audio/music/suspense_ambient.ogg" # Placeholder music
    
        "A biting wind whips salt spray across your face as you stumble through the hatchway, emerging onto the deck of the galleon."
        "Grey, turbulent clouds churn overhead, mirroring the restless heave of the dark sea surrounding the ship."
        "The wood underfoot is worn smooth by countless storms and footsteps, groaning with the motion of the waves."
    
        "Work on deck ceases the moment you appear. Rough-looking sailors, faces etched by sun and sea, turn their heads."
        "Their eyes linger, sharp and suspicious. Whispers die down, replaced by an unnerving, watchful silence."
        "You feel like a rat cornered on its own sinking ship... except this ship seems unnervingly seaworthy, despite its spectral aura."
    
        "A figure detaches himself from the shadows near the mainmast and walks towards you."
        "He's older than most of the crew, lean but sturdy, with eyes like chips of flint. His coat is practical, his boots worn but well-kept. He stops a few paces away, arms crossed."
    
        show silas neutral at center with dissolve
    
        silas "Hold there. State your name and business aboard the *Sea Serpent*."
    
        "The *Sea Serpent*? That name... it doesn't feel right. A fragment, sharp and painful, surfaces in your mind – crashing waves, torn canvas, a different name whispered on the wind..."
        # Hinting at Jax's fragmented memories
    
        jax "(Steadying yourself) My name is Jax."
    
        "The man's expression doesn't soften. If anything, the scrutiny intensifies."
    
        silas "Jax. A name mentioned... in certain fragmented logs."
        silas "I am Silas, Quartermaster of this vessel. And you appear where you shouldn't be."
        silas "The crew is... particular about unexpected guests. Especially ones who surface from the depths like ill omens."
    
        "His gaze sweeps over you, assessing, missing nothing."
        "Another memory fragment flickers – a tattered chart, lines glowing faintly, a sense of desperate searching..."
    
        jax "I... I don't remember exactly how I got here. Things are... unclear."
    
        silas "Unclear."
        silas "Convenient. Clarity is a currency we value highly here. As is loyalty."
        silas "Some whispers associate your name with betrayal. With theft." # Hinting at Elena's belief
    
        "He takes another step closer, lowering his voice slightly, though the crew still watches intently."
    
        silas "We sail troubled waters, Jax. Every soul aboard must pull their weight and prove their worth. Doubly so for stowaways with fractured tales."
    
        menu:
            "Be cautious":
                jax "I understand the suspicion. I mean no harm. I'm just trying to piece things together."
                silas "Piece things together."
                silas "We are all trying to do that. But some pieces belong to others."
                silas "For now, you'll answer my questions. And stay where I can see you."
    
            "Be confused (Play into memory loss)":
                jax "Theft? Betrayal? I don't... I don't know what you're talking about. My head..."
                silas "A convenient affliction."
                silas "Perhaps your memory will improve under closer supervision. Perhaps not."
                silas "Either way, your presence requires explanation. Soon."
    
            "Be slightly defiant":
                jax "I may not know how I got here, but I'm no thief. And I answer for myself."
                silas "(A humourless chuckle) Bold words. Boldness can be useful. Or it can be fatal."
                silas "On this ship, Quartermaster Silas decides which. For now, you'll follow my lead."
    
        silas "Come with me. We have much to discuss, and the deck is no place for secrets or fractured minds."
        silas "The Captain will want to see you eventually. Pray you have satisfactory answers by then."
    
        "Silas turns, expecting you to follow. The crew's eyes track your every move as you step further onto the haunted deck of the galleon."
    
        # The scene could jump here, e.g., jump scene_silas_interrogation
        # Or just end, leading into the next part of the story flow.
        # End of scene script block.
    
        return
    ```

    # TODO: Add choices or jump to the next scene
    return
