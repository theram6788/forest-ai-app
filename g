import streamlit as st

st.set_page_config(page_title="The Last Breathe: A Tale of Two Souls", page_icon="🌿", layout="wide")

SCENES = {
    "intro": {
        "chapter": "Prologue",
        "title": "🌿 The Last Breathe: A Tale of Two Souls",
        "text": """
Tabaah ho chuki dharti... aur uski raakh mein ek hara patta.

Tum Elbert ho — ek mamuli soldier, jo iss khamosh maut ki duniya mein ek impossible signal dekh raha hai: **Hope is still alive.**

Aaj tumhari har choice se decide hoga:
- kya duniya dobara jeegi,
- kya pyaar andhere se jeet paayega,
- aur kya legacy bach paayegi.
""",
        "choices": [
            {"label": "Mission start karo", "next": "leaf_incident", "effects": {"hope": 2}}
        ],
    },
    "leaf_incident": {
        "chapter": "Chapter 1 · The Green Life",
        "title": "The Incident",
        "text": """
Elbert dharti ki satah par utarta hai. Har taraf raakh.
Phir achanak... ek **nanha sa hara patta**.
Jaise hi tum use chhoote ho, aasman phat padta hai — meteorites ka tandav.
""",
        "choices": [
            {"label": "Bunker ki taraf daudo", "next": "co_briefing", "effects": {"trust": 1}},
            {"label": "Patte ka sample collect karo", "next": "co_briefing", "effects": {"hope": 2, "darkness": 1}},
        ],
    },
    "co_briefing": {
        "chapter": "Chapter 1 · The Green Life",
        "title": "Hope is still alive",
        "text": """
CO tumhari report par hasta hai. Tum seedha uski aankhon mein dekh ke bolte ho:

**"Hope is still alive, Sir."**

Bunker mein panic hai. Bahar apocalypse.
""",
        "choices": [
            {"label": "CO ke orders follow karo", "next": "transformation", "effects": {"trust": 2}},
            {"label": "Apne instinct par wapas surface jao", "next": "transformation", "effects": {"hope": 2}},
        ],
    },
    "transformation": {
        "chapter": "Chapter 1 · The Green Life",
        "title": "The Transformation",
        "text": """
Surface par tumhe illusions gher lete hain. FOMO, purani yaadein, ajeeb awaazein.
Ek vishal meteorite tumhare exo-suit ko tod deta hai.

Par tum marte nahi.
Tum **mask ke bina saans le rahe ho**.
Tum ab sirf insaan nahi rahe — **Ultra-Human**.
""",
        "choices": [
            {"label": "Nayi powers test karo", "next": "zoye_rescue", "effects": {"blue_light": 2, "darkness": 1}},
            {"label": "Seedha mission objective pe focus karo", "next": "zoye_rescue", "effects": {"trust": 1, "hope": 1}},
        ],
    },
    "zoye_rescue": {
        "chapter": "Chapter 1 · The Green Life",
        "title": "The Horror in the Basement",
        "text": """
Andheri galiyon mein tumhe apna purana ghar milta hai.
Wahan Zoye fasi hoti hai.
Tum use bachakar bunker bhejte ho aur khud basement utarte ho.

Neeche tumhara intezar kar rahi hai: **The Dark Spider**.
""",
        "choices": [
            {"label": "Aggressive attack", "next": "virus_bite", "effects": {"darkness": 2}},
            {"label": "Calculated strike", "next": "virus_bite", "effects": {"trust": 1, "blue_light": 1}},
        ],
    },
    "virus_bite": {
        "chapter": "Chapter 1 · The Green Life",
        "title": "Virus in Blood",
        "text": """
Dark Spider mar jaati hai... par uska virus tumhare khoon mein ghul chuka hai.
CO tumhe marne ke liye chhod deta hai.
Zoye bagawat karti hai, cure churaati hai, tumhe zinda karti hai.

Tum dono milkar CO ko khatam kar dete ho.
Duniya dobara hari ho jaati hai.

CO marte waqt phusphusata hai:
**"Tum apni legacy par pachtaoge!"**
""",
        "choices": [
            {"label": "5 saal aage badho", "next": "dark_world"}
        ],
    },
    "dark_world": {
        "chapter": "Chapter 2 · The Dark Soul",
        "title": "The Fall of a Hero",
        "text": """
5 saal baad duniya hari hai, par ped ab insaanon ko nigalne lage hain.
Aasman gehra neela hai. Elbert ke andar ki darkness jag chuki hai.

Red Moon ki raat mein Dave Zoye ko warn karta hai — par pyaar andha hota hai.
""",
        "choices": [
            {"label": "Zoye ko dhoondo", "next": "dead_world", "effects": {"hope": 1}},
            {"label": "Dark Elbert ka shikaar karo", "next": "dead_world", "effects": {"darkness": 1}},
        ],
    },
    "dead_world": {
        "chapter": "Chapter 2 · The Dark Soul",
        "title": "The Dead World",
        "text": """
Ab waqt badal chuka hai:
- Dave (26): thaka hua lead
- Cathie (19): Elbert ki beti, jiske andar Blue Light hai
- Zoye (34): missing

Asli dar tumhare peeche hai — 49 saal ka Dark Elbert,
jo Cathie ki Blue Light ko nigalne aa raha hai.
""",
        "choices": [
            {"label": "Cathie ki training pe focus", "next": "final_stand", "effects": {"blue_light": 2}},
            {"label": "Dave ki tactical team build karo", "next": "final_stand", "effects": {"trust": 2}},
        ],
    },
    "final_stand": {
        "chapter": "Finale · Ultimate Sacrifice",
        "title": "The Final Stand",
        "text": """
Red Moon ke neeche final confrontation shuru hoti hai.
Cathie apni Blue Light se Dark Soul ko ek pal ke liye shaant karti hai.
Elbert ki aankhon mein pehli baar beti ke liye pyaar dikhta hai.

Ab faisla tumhare haath mein hai.
""",
        "choices": [
            {"label": "Dave ko signal do — गोली चलाओ", "next": "ending_sacrifice", "effects": {"hope": 2}},
            {"label": "Elbert ko bachane ki koshish karo", "next": "ending_corruption", "effects": {"darkness": 2}},
        ],
    },
    "ending_sacrifice": {
        "chapter": "Ending A",
        "title": "The Ultimate Sacrifice",
        "text": """
Dave bhari dil se woh goli chalata hai jo 10 saal pehle chalni chahiye thi.
Elbert girte hue Cathie ka naam leta hai.

Dark Soul toot jaata hai.
Blue Light aasman mein failkar jungle ko balance kar deti hai.

**Ending unlocked: Legacy Through Sacrifice**
""",
        "choices": [],
    },
    "ending_corruption": {
        "chapter": "Ending B",
        "title": "Love Against the Abyss",
        "text": """
Tum goli rok dete ho. Ek pal ko lagta hai Elbert wapas aa gaya.
Phir Dark Soul control le leta hai.

Cathie ki Blue Light ka aadha hissa nigal liya jata hai.
Duniya bachti hai, par permanent andhere ke daag ke saath.

**Ending unlocked: Half-Light World**
""",
        "choices": [],
    },
}

DEFAULT_STATS = {"hope": 0, "darkness": 0, "trust": 0, "blue_light": 0}


def restart_game() -> None:
    st.session_state.current_scene = "intro"
    st.session_state.stats = DEFAULT_STATS.copy()
    st.session_state.path = []


if "current_scene" not in st.session_state:
    restart_game()

scene = SCENES[st.session_state.current_scene]

st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 55%, #052e2b 100%);
    border: 1px solid #334155;
    border-radius: 18px;
    padding: 1.2rem 1.4rem;
    color: #e2e8f0;
    box-shadow: 0 12px 40px rgba(0,0,0,0.35);
}
.chapter {
    color: #34d399;
    font-weight: 700;
    letter-spacing: 0.3px;
}
</style>
""", unsafe_allow_html=True)

st.title("🌿 The Last Breathe: A Tale of Two Souls")
st.caption("Interactive story survival game (Hinglish Sci-Fi + Psychological Horror)")

left, right = st.columns([2.2, 1], gap="large")

with left:
    st.markdown('<div class="hero">', unsafe_allow_html=True)
    st.markdown(f'<div class="chapter">{scene["chapter"]}</div>', unsafe_allow_html=True)
    st.subheader(scene["title"])
    st.write(scene["text"])
    st.markdown("</div>", unsafe_allow_html=True)

    if scene["choices"]:
        st.markdown("### Choose your action")
        for idx, choice in enumerate(scene["choices"]):
            if st.button(choice["label"], key=f"choice_{idx}", use_container_width=True):
                effects = choice.get("effects", {})
                for k, v in effects.items():
                    st.session_state.stats[k] += v

                st.session_state.path.append({
                    "from": st.session_state.current_scene,
                    "choice": choice["label"],
                    "effects": effects,
                })
                st.session_state.current_scene = choice["next"]
                st.rerun()
    else:
        st.success("Story arc complete. Try different choices for alternate outcomes.")
        if st.button("🔁 Play Again", use_container_width=True):
            restart_game()
            st.rerun()

with right:
    st.markdown("### Character Energies")
    for stat, value in st.session_state.stats.items():
        label = stat.replace("_", " ").title()
        st.metric(label, value)

    st.markdown("### Journey Log")
    if not st.session_state.path:
        st.write("No decisions yet.")
    else:
        for i, step in enumerate(st.session_state.path[-6:], start=1):
            st.write(f"{i}. {step['choice']}")

    st.button("Reset Story", on_click=restart_game, use_container_width=True)
