# **DNA: Digital Narrative Alchemist System**

## **Overview**

The **DNA: Digital Narrative Alchemist System** is a powerful content generation engine designed for tabletop role-playing game (TTRPG) Game Masters (GMs). It uses a unique “DNA” string—a coded representation of a game element’s core traits—to procedurally generate rich, narrative-driven content such as NPCs, factions, quests, magic items, and more.

This system is designed to:
- Combat creative block  
- Save preparation time  
- Introduce unique, thematically consistent elements into any game  

---

## **How It Works (Current GPT/Gem Implementation)**

In its current form, the system is designed to be used within a **Custom GPT or Gemini Gem** environment. The logic is distributed across four core files:

### **Core Components**

#### 🔹 `Master_System_Prompt.md` – *The Conductor*
- **Usage**: This file isn't uploaded, it's contents are the System Instructions. There are two, one for ChatGPT and one for Gemini.
- **Role**: The brain of the operation; manages the entire conversational flow.
- **Function**: Greets the user, presents creation menus, and orchestrates the generation flow (e.g., “Fully Random,” “Highly Detailed”).

#### 🔹 `Master_Generator_Knowledge.py` – *The DNA Forge*
- **Role**: The engine that forges unique DNA strings.
- **Function**: Contains Python functions (e.g., `generate_npc_dna()`, `generate_faction_dna()`) that generate base DNA for content.

#### 🔹 `Master_Menu_Options.md` – *The User Interface*
- **Role**: Defines the detailed, user-facing creation menus.
- **Function**: Presents forms for user inputs (e.g., NPC’s name, faction ideology) and guides how they influence DNA.

#### 🔹 `Master_Decoder_Knowledge.md` – *The Storyteller*
- **Role**: The core knowledge base for decoding DNA into narrative.
- **Function**: Translates DNA + user context into rich, structured content without showing the mechanical DNA.

---

## **The Workflow**

The generation process follows a context-driven hierarchy:

1. **Initiation**: Conversation begins, guided by `Master_System_Prompt.md`.
2. **Selection**: User chooses content type (e.g., NPC) and generation method (e.g., "Highly Detailed").
3. **DNA Generation**: `Master_Generator_Knowledge.py` generates base DNA.
4. **Context Gathering**: Prompts from `Master_Menu_Options.md` collect user input.
5. **DNA Modification**: User inputs alter the base DNA string to reflect specific intent.
6. **Decoding & Narrative Weaving**: Final DNA and context decoded via `Master_Decoder_Knowledge.md`.
7. **Final Output**: User receives a polished, system-agnostic narrative. The DNA is hidden from view.

---

## **Future Plans & Roadmap**

### **Phase 1: Core Engine Refactor**
- [ ] **Port DNA Generation**: Turn `Master_Generator_Knowledge.py` into a backend service (Flask/FastAPI) or JavaScript module.
- [ ] **Structure Decoding Prompts**: Convert prompts in `Master_Decoder_Knowledge.md` into structured JSON for API calls.

### **Phase 2: Web Interface (GUI) Development**
- [ ] **Framework Selection**: Choose React, Svelte, Vue.js, or similar.
- [ ] **UI/UX Design**: Build a clean, menu-driven interface.
- [ ] **Component Creation**: Turn menus from `Master_Menu_Options.md` into interactive forms.
- [ ] **Display Results**: Format and display final output attractively.

### **Phase 3: Backend & API Integration**
- [ ] **Backend Scaffolding**: Stand up a backend server or serverless architecture.
- [ ] **API Endpoints**: Create endpoints (e.g., `/generate/npc`) for front-end calls.
- [ ] **LLM Integration**: Use Gemini API (or similar) to decode DNA and return output.

### **Phase 4: Advanced Features**
- [ ] **User Accounts**: Login and save/edit content.
- [ ] **Campaign Management**: Link generated assets (e.g., tie an NPC to a quest).
- [ ] **Export Functionality**: Export to PDF, JSON, or Markdown.
- [ ] **Community Sharing**: Users can publish and browse shared content.

### **Want to give feedback? Click New issue → 🧪 DNA System – Structured Feedback and share your thoughts!**

---

## **License**

This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License](http://creativecommons.org/licenses/by-nc/4.0/).

You are free to:
- **Share** — copy and redistribute the material in any medium or format  
- **Adapt** — remix, transform, and build upon the material  

Under the following terms:
- **Attribution** — You must give appropriate credit  
- **NonCommercial** — You may not use the material for commercial purposes  

> **Note:** As the copyright holder, I reserve the right to use this project for commercial purposes.  
> See the `LICENSE` file for more details.
