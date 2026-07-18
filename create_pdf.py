import sys
from fpdf import FPDF
from fpdf.enums import XPos, YPos

class EcoTrackPDF(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_margins(15, 20, 15)
        self.set_auto_page_break(auto=True, margin=20)
        
    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(148, 163, 184) # Slate-400
            self.cell(0, 10, "EcoTrack - Carbon Footprint Tracker Project Documentation", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="R")
            self.set_draw_color(226, 232, 240) # Slate-200
            self.line(15, 28, 195, 28)
            self.ln(4)
            
    def footer(self):
        if self.page_no() > 1:
            self.set_y(-15)
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(148, 163, 184) # Slate-400
            self.cell(0, 10, f"Page {self.page_no()}", border=0, new_x=XPos.RIGHT, new_y=YPos.TOP, align="C")

    # Helper methods for content layout
    def heading_1(self, text):
        self.ln(2)
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(16, 185, 129) # Emerald-500
        self.cell(0, 10, text, border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_fill_color(16, 185, 129)
        self.rect(15, self.get_y() - 1, 40, 1, "F")
        self.ln(2)
        
    def heading_2(self, text):
        self.ln(2)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(30, 41, 59) # Slate-800
        self.cell(0, 8, text, border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1)

    def heading_3(self, text):
        self.ln(1)
        self.set_font("Helvetica", "B", 9.5)
        self.set_text_color(71, 85, 105) # Slate-600
        self.cell(0, 6, text, border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1)
        
    def paragraph(self, text):
        self.set_font("Helvetica", "", 9.5)
        self.set_text_color(51, 65, 85) # Slate-700
        self.multi_cell(0, 5, text, border=0)
        self.ln(2)
        
    def bullet_point(self, title, text):
        self.set_font("Helvetica", "B", 9.5)
        self.set_text_color(51, 65, 85)
        self.write(5, f"  * {title}: ")
        self.set_font("Helvetica", "", 9.5)
        self.set_text_color(71, 85, 105)
        self.write(5, f"{text}\n")
        self.set_x(15) # reset left margin indentation
        
    def code_block(self, code):
        self.ln(2)
        self.set_fill_color(241, 245, 249) # Slate-100
        self.set_draw_color(226, 232, 240) # Slate-200
        self.set_font("Courier", "", 8.5)
        self.set_text_color(15, 23, 42) # Slate-900
        lines = code.split("\n")
        height = len(lines) * 4.5 + 4
        # Check page break
        if self.get_y() + height > 270:
            self.add_page()
        start_x = self.get_x()
        start_y = self.get_y()
        self.rect(start_x, start_y, 180, height, "DF")
        self.set_y(start_y + 2)
        for line in lines:
            self.set_x(start_x + 5)
            self.cell(0, 4.5, line, border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_y(start_y + height)
        self.ln(2)

    def draw_table(self, headers, data, col_widths):
        self.ln(2)
        self.set_fill_color(226, 232, 240) # Slate-200 for header
        self.set_draw_color(203, 213, 225) # Slate-300
        self.set_text_color(15, 23, 42) # Slate-900
        self.set_font("Helvetica", "B", 8.5)
        
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 8, h, border=1, align="C", fill=True)
        self.ln()
        
        self.set_font("Helvetica", "", 8.5)
        self.set_text_color(51, 65, 85)
        
        for row in data:
            for i, val in enumerate(row):
                self.cell(col_widths[i], 7, str(val), border=1, align="C")
            self.ln()
        self.ln(2)

    def cover_page(self):
        self.add_page()
        self.set_fill_color(6, 78, 59) # Emerald-900
        self.rect(0, 0, 210, 297, "F")
        
        self.set_y(80)
        self.set_font("Helvetica", "B", 40)
        self.set_text_color(255, 255, 255)
        self.cell(0, 15, "EcoTrack", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        
        self.ln(5)
        self.set_font("Helvetica", "", 16)
        self.set_text_color(167, 243, 208) # Emerald-200
        self.multi_cell(0, 8, "Carbon Footprint Tracker & AI Lifestyle Swaps\nComprehensive Enterprise System Documentation", border=0, align="C")
        
        self.ln(10)
        self.set_fill_color(52, 211, 153) # Emerald-400
        self.rect(75, self.get_y(), 60, 1.5, "F")
        
        self.set_y(210)
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(255, 255, 255)
        self.cell(0, 6, "Technology Stack:", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.set_font("Helvetica", "", 10.5)
        self.set_text_color(209, 250, 229) # Emerald-100
        self.cell(0, 6, "React.js (Vite + Tailwind CSS + Chart.js) | Flask Python Web Server", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.cell(0, 6, "Firebase Firestore & Auth | Groq LLM API (llama-3.3-70b-versatile)", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        
        self.ln(15)
        self.set_font("Helvetica", "I", 9.5)
        self.set_text_color(167, 243, 208) # Emerald-200
        self.cell(0, 6, "Reference Document: Enterprise Blueprint and AI Custom Integration Guide", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.cell(0, 6, "Prepared for Eco-Track Platform Assessment", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        
    def table_of_contents_pg2(self):
        self.add_page()
        self.set_y(30)
        self.set_font("Helvetica", "B", 20)
        self.set_text_color(15, 23, 42) # Slate-900
        self.cell(0, 10, "Table of Contents", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_fill_color(16, 185, 129)
        self.rect(15, self.get_y(), 30, 1.2, "F")
        self.ln(8)
        
        toc_items = [
            ("Chapter 1: Executive Summary & Detailed Scope", 3),
            ("Chapter 2: Core Platform Functional Requirements", 4),
            ("Chapter 3: System Use Cases & Core Logging Scenarios", 5),
            ("Chapter 4: Architectural Design & Modular Mapping", 7),
            ("Chapter 5: Architectural Flow & Process Diagrams", 8),
            ("Chapter 6: Data Modeling & Firestore Schema Specs", 9),
            ("Chapter 7: Backend API Specifications & Router Modules", 11),
            ("Chapter 8: Emission Coefficients & Calculation Models", 13),
            ("Chapter 9: Frontend Architecture & Client Routing", 14),
            ("Chapter 10: State Management & Auth Context Mechanics", 15),
            ("Chapter 11: Daily Habits Logger Interface State Machine", 16),
            ("Chapter 12: Gamification Engine & Logging Streaks Math", 17),
            ("Chapter 13: Achievements Evaluation Matrix & Badges", 18),
            ("Chapter 14: AI Recommendation Engine & Prompt Optimization", 19),
            ("Chapter 15: External APIs & Proxy Calculations", 20),
            ("Chapter 16: Setup Guide & Local Dev Verification", 21),
            ("Chapter 17: Platform Testing & Validation Protocols", 22),
            ("Chapter 18: Non-Functional Specifications & Future Roadmap", 23)
        ]
        
        self.set_font("Helvetica", "", 10.5)
        self.set_text_color(51, 65, 85) # Slate-700
        
        for item, page in toc_items:
            self.cell(145, 7.5, item, border=0)
            self.cell(20, 7.5, "." * (180 - len(item) * 2), border=0, align="R")
            self.cell(15, 7.5, str(page), border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="R")
            self.ln(1)

    def draw_architecture_diagram_pg8(self):
        self.ln(5)
        x_start = 15
        y_start = self.get_y()
        self.set_fill_color(248, 250, 252) # Slate-50
        self.set_draw_color(226, 232, 240) # Slate-200
        self.rect(x_start, y_start, 180, 160, "DF")
        
        self.set_fill_color(239, 246, 255) # Light blue
        self.set_draw_color(59, 130, 246) # Blue-500
        self.rect(25, y_start + 8, 160, 30, "DF")
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(30, 41, 59)
        self.text(32, y_start + 14, "React.js Frontend (Served on Port 5173)")
        self.set_font("Helvetica", "", 8.5)
        self.set_text_color(71, 85, 105)
        self.text(32, y_start + 20, "- Dashboard & Gauge (React-Gauge-Chart / Tailwind)")
        self.text(32, y_start + 25, "- Daily Habit Logger (Travel, Food, Energy forms)")
        self.text(32, y_start + 30, "- History & Analytics Charts (Chart.js)")
        self.text(120, y_start + 20, "- Streaks & Achievements Shelf")
        self.text(120, y_start + 25, "- AI Suggestions Client Interface")
        self.text(120, y_start + 30, "- Profile Settings & Calculators")

        self.set_draw_color(100, 116, 139)
        self.set_fill_color(100, 116, 139)
        self.line(105, y_start + 38, 105, y_start + 53)
        self.polygon(((102, y_start + 50), (108, y_start + 50), (105, y_start + 53)), style="F")
        self.set_font("Helvetica", "B", 7)
        self.set_text_color(100, 116, 139)
        self.text(108, y_start + 46, "REST API (HTTPS/JSON)")

        self.set_fill_color(236, 253, 245) # Light green
        self.set_draw_color(16, 185, 129) # Emerald-500
        self.rect(25, y_start + 54, 160, 30, "DF")
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(30, 41, 59)
        self.text(32, y_start + 60, "Flask Python Backend (Served on Port 5000)")
        self.set_font("Helvetica", "", 8.5)
        self.set_text_color(71, 85, 105)
        self.text(32, y_start + 66, "- API Router / Endpoint Controller Layer")
        self.text(32, y_start + 71, "- Carbon Core Calculator (emission factors math)")
        self.text(32, y_start + 76, "- Streak Tracker Logic (comparing logs calendar)")
        self.text(120, y_start + 66, "- Middleware Authentication Token Verifier")
        self.text(120, y_start + 77, "- Groq LLM API Integration Layer")
        self.text(120, y_start + 82, "- Carbon Interface Request Handler")

        y_arrow_start = y_start + 84
        y_service_box = y_start + 110
        
        services = [
            ("Firebase Auth", 25, 35, (239, 246, 255), (59, 130, 246)),
            ("Groq API", 65, 35, (253, 242, 248), (219, 39, 119)),
            ("Carbon Interface", 105, 35, (254, 243, 199), (217, 119, 6)),
            ("Firebase Firestore", 145, 35, (255, 237, 213), (234, 88, 12))
        ]

        for name, bx, bw, bg, border in services:
            self.set_draw_color(100, 116, 139)
            self.set_fill_color(100, 116, 139)
            cx = bx + (bw / 2)
            self.line(cx, y_arrow_start, cx, y_service_box - 2)
            self.polygon(((cx - 2, y_service_box - 5), (cx + 2, y_service_box - 5), (cx, y_service_box - 2)), style="F")
            
            self.set_fill_color(*bg)
            self.set_draw_color(*border)
            self.rect(bx, y_service_box, bw, 25, "DF")
            
            self.set_font("Helvetica", "B", 8)
            self.set_text_color(30, 41, 59)
            
            self.set_y(y_service_box + 3)
            self.set_x(bx)
            self.multi_cell(bw, 3, name, border=0, align="C")
            self.set_font("Helvetica", "", 7)
            self.set_text_color(71, 85, 105)
            self.set_y(y_service_box + 9)
            self.set_x(bx)
            if "Auth" in name:
                self.multi_cell(bw, 3, "JWT Sessions & Token Verification", border=0, align="C")
            elif "Groq" in name:
                self.multi_cell(bw, 3, "llama-3.3-70b suggestions API", border=0, align="C")
            elif "Carbon" in name:
                self.multi_cell(bw, 3, "Live electricity & flight factors API", border=0, align="C")
            elif "Firestore" in name:
                self.multi_cell(bw, 3, "Daily logs collection & user database", border=0, align="C")

        self.set_y(y_start + 160)
        self.ln(10)

def generate_pdf():
    pdf = EcoTrackPDF()
    
    # ---------------- PAGE 1 ----------------
    pdf.cover_page()
    
    # ---------------- PAGE 2 ----------------
    pdf.table_of_contents_pg2()
    
    # ---------------- PAGE 3 ----------------
    pdf.add_page()
    pdf.heading_1("Chapter 1: Executive Summary & Detailed Scope")
    pdf.heading_2("1.1 Environmental Motivation")
    pdf.paragraph(
        "Individual carbon footprint tracking is a crucial starting point for mitigating greenhouse gas "
        "accumulation. Daily activities, such as transportation, dietary patterns, and home utility consumption, "
        "collectively represent more than 60% of global emissions. However, typical users encounter "
        "several barriers in modifying these habits: carbon footprint mathematics is complex, data tracking is "
        "tedious, and recommendations are often general rather than context-specific."
    )
    pdf.paragraph(
        "EcoTrack represents an integrated solution that eliminates these obstacles. By developing an "
        "intuitive, single-page habits logger, connecting it to databases, and leveraging AI models, "
        "EcoTrack translates daily decisions into clear scientific values, rewards consistent behavior, and "
        "provides personalized suggestions for emissions reduction."
    )
    pdf.heading_2("1.2 Strategic Platform Scope")
    pdf.paragraph(
        "EcoTrack is designed as a localized utility platform optimized for rapid evaluation and scaling: "
    )
    pdf.bullet_point("Real-Time Inputs Tracking", "Allows users to log and preview carbon emissions metrics on-the-fly, prior to DB persistence.")
    pdf.bullet_point("Flexible Persistence Architectures", "Integrates with Firebase Firestore and provides an offline in-memory Demo Mode to support evaluation without cloud services.")
    pdf.bullet_point("AI Recommendation Loops", "Generates custom suggestions based on user profiles using the Groq API (LLaMA 3.3).")
    pdf.bullet_point("Standard Verification Gateways", "Supports proxy interfaces with third-party emissions datasets like the Carbon Interface API.")
    
    # ---------------- PAGE 4 ----------------
    pdf.add_page()
    pdf.heading_1("Chapter 2: Core Platform Functional Requirements")
    pdf.heading_2("2.1 Core Functions Matrix")
    pdf.paragraph(
        "The platform supports several primary features configured across the client-server stack:"
    )
    pdf.bullet_point("Daily Habits Logger Form", "A multi-step, validated entry wizard that records distances (km), diet choices, food waste flags, electricity usage (kWh), and HVAC details.")
    pdf.bullet_point("Dashboard Carbon Gauge Widget", "An visual indicator displaying total emissions logged today relative to the user's budget, with dynamic color grading.")
    pdf.bullet_point("AI Swap Generator client", "Connects to the suggestions engine to fetch and render customized lifestyle changes with estimated CO2 offsets.")
    pdf.bullet_point("30-Day Historical Data Engine", "Analyzes, computes, and renders long-term statistics (average, best, worst, total) and chart metrics via Chart.js plugins.")
    pdf.bullet_point("Profile Settings Controller", "Allows users to toggle budget limits, display names, country locales, and visual themes.")
    pdf.bullet_point("Achievements Manager", "Tracks streaks and compares logs history to unlock 10 specific achievement badges.")
    
    pdf.heading_2("2.2 System Security & Scope Constraints")
    pdf.paragraph(
        "To ensure robust operations in various environments, the platform maintains strict design rules: "
    )
    pdf.bullet_point("Local REST Isolation", "CORS policy restricts access to valid frontend hosts, and client API configurations remain isolated within configuration files.")
    pdf.bullet_point("API Key Protection", "Sensitive API keys (Groq, Carbon Interface, Firebase) are loaded only on the server using dotenv variables.")
    pdf.bullet_point("Input Character Sanitization", "Validates values (e.g. range checks, float parses) on the backend to prevent injection attempts or memory overflows.")
    
    # ---------------- PAGE 5 ----------------
    pdf.add_page()
    pdf.heading_1("Chapter 3: System Use Cases & Core Logging Scenarios")
    pdf.heading_2("3.1 Daily Logging Flows & Verification")
    pdf.paragraph(
        "EcoTrack is designed around realistic workflows. The section below describes the primary logging scenarios:"
    )
    pdf.heading_3("Scenario A: Logging Daily Transportation Activities")
    pdf.paragraph(
        "1. The user navigates to the Logger form. The system defaults to the Travel step.\n"
        "2. The user inputs their transport mode (e.g. car_petrol) and distance traveled (e.g. 35 km).\n"
        "3. The user specifies passenger count (e.g. 3 for carpooling).\n"
        "4. The system calculates the carbon footprint for this leg, dividing the baseline emissions by the passenger count.\n"
        "5. The backend saves the daily log. The dashboard gauge displays the travel footprint fraction and progress against their daily limit."
    )
    pdf.heading_3("Scenario B: Logging Daily Diet Choices & Food Waste")
    pdf.paragraph(
        "1. The user proceeds to the Food step in the Logger.\n"
        "2. The user selects their diet style (meat-heavy, omnivore, vegetarian, vegan).\n"
        "3. The user enters meal count (representing the proportion of standard meals tracked, e.g. 2 out of 3).\n"
        "4. The user toggles the food waste flag. If checked, a 10% penalty is added to food emissions.\n"
        "5. The system saves the document, updating the total daily emissions and reflecting the results on the dashboard."
    )
    
    # ---------------- PAGE 6 ----------------
    pdf.add_page()
    pdf.heading_1("Chapter 3: System Use Cases (Continued)")
    pdf.heading_2("3.2 Advanced Utility Logging & Custom Recommendations Use Cases")
    pdf.heading_3("Scenario C: Logging Home Utility Details")
    pdf.paragraph(
        "1. The user navigates to the Energy step in the Logger.\n"
        "2. The user enters electricity consumption in kWh (constrained between 0 and 30 kWh per day).\n"
        "3. The user toggles checkboxes for active heating or cooling (AC).\n"
        "4. The system computes emissions using the grid factor, adding flat rates of 2.0 kg for heating and 1.5 kg for AC.\n"
        "5. The system aggregates all categories and updates the daily total."
    )
    pdf.heading_3("Scenario D: Fetching AI Lifestyle Swaps")
    pdf.paragraph(
        "1. The user navigates to the Suggestions tab on the client.\n"
        "2. The frontend sends today's logged data (totals and category parameters) to the suggestions endpoint.\n"
        "3. The backend constructs a structured prompt and sends it to the Groq API (LLaMA 3.3).\n"
        "4. The AI returns three personalized suggestions with estimated CO2 savings.\n"
        "5. The suggestions are rendered as category-themed cards with visual copy shortcuts."
    )
    pdf.heading_3("Scenario E: Analytics Dashboard Operations")
    pdf.paragraph(
        "1. The user opens the History tab.\n"
        "2. The system fetches the last 30 daily logs chronologically.\n"
        "3. The client calculates the 7-day average, lowest day, highest day, and monthly total.\n"
        "4. Chart.js plugins render a 30-day line trend vs budget, a 14-day stacked bar breakdown, and a 30-day activity heatmap."
    )

    # ---------------- PAGE 7 ----------------
    pdf.add_page()
    pdf.heading_1("Chapter 4: Architectural Design & Modular Mapping")
    pdf.heading_2("4.1 Component Architecture Model")
    pdf.paragraph(
        "EcoTrack is built using a decoupled client-server architecture. This separation ensures that the frontend "
        "user interface remains responsive and distinct from backend database and API logic. Communication "
        "occurs over HTTP using RESTful JSON payloads."
    )
    pdf.paragraph(
        "The project folder structure is organized as follows:"
    )
    pdf.bullet_point("backend/", "Contains Flask API routes, configurations, virtual environment, and database schemas.")
    pdf.bullet_point("backend/routes/", "Blueprint modules isolating calculator math, database logging, AI suggestions, and third-party APIs.")
    pdf.bullet_point("frontend/", "React application built with Vite and styled with Tailwind CSS and custom stylesheets.")
    pdf.bullet_point("frontend/src/components/", "Reusable UI widgets (GaugeCard, Navbar, BadgeCard, SuggestionCard, Login/Register forms).")
    pdf.bullet_point("frontend/src/pages/", "Application pages (Dashboard, LogToday, History, Achievements, Profile).")
    pdf.bullet_point("frontend/src/context/", "Context modules coordinating authentication states, JWT token storage, and themes.")
    pdf.bullet_point("metadata / assets", "Public folder resources and visual dependencies.")
    
    # ---------------- PAGE 8 ----------------
    pdf.add_page()
    pdf.heading_1("Chapter 5: Architectural Flow & Process Diagrams")
    pdf.heading_2("5.1 Complete Platform Component Map Diagram")
    pdf.paragraph(
        "The diagram below details the data flow between frontend views, Flask controller blueprints, and database "
        "services:"
    )
    pdf.draw_architecture_diagram_pg8()
    
    # ---------------- PAGE 9 ----------------
    pdf.add_page()
    pdf.heading_1("Chapter 6: Data Modeling & Firestore Schema Specs")
    pdf.heading_2("6.1 Firebase Firestore Collections")
    pdf.paragraph(
        "For authenticated cloud operations, EcoTrack utilizes Firebase Firestore. The database relies on "
        "two core collections: 'users' and 'habits'. Below are the JSON schema specifications for each model:"
    )
    pdf.heading_3("The Users Collection (/users/{uid})")
    pdf.paragraph(
        "This collection stores user profile configurations, streaks, and unlocked achievements. Each document is "
        "keyed by the user's Firebase Auth UID."
    )
    pdf.code_block(
        "{\n"
        "  \"uid\": \"auth_user_uid_hash\",\n"
        "  \"displayName\": \"John Eco Hero\",\n"
        "  \"patient_name\": \"John Eco Hero\", // Legacy key alignment\n"
        "  \"budget\": 8.0,\n"
        "  \"weekly_goal\": 10.0,\n"
        "  \"theme\": \"dark\",\n"
        "  \"country\": \"in\",\n"
        "  \"last_logged_date\": \"2026-07-05\",\n"
        "  \"streak\": 3,\n"
        "  \"badges\": [\n"
        "    {\n"
        "      \"id\": \"first_step\",\n"
        "      \"unlocked_at\": \"2026-07-03\"\n"
        "    },\n"
        "    {\n"
        "      \"id\": \"green_day\",\n"
        "      \"unlocked_at\": \"2026-07-04\"\n"
        "    }\n"
        "  ]\n"
        "}"
    )
    
    # ---------------- PAGE 10 ----------------
    pdf.add_page()
    pdf.heading_1("Chapter 6: Data Modeling & Persistence (Continued)")
    pdf.heading_2("6.2 Habits Logging Schema (/habits/{uid}_{date})")
    pdf.paragraph(
        "Daily logs are saved in the 'habits' collection. Each document represents a single user's logged habits "
        "for a specific date. To optimize query performance and ensure direct lookups, the document ID is "
        "structured as '{uid}_{date}' (e.g. 'user123_2026-07-05')."
    )
    pdf.code_block(
        "{\n"
        "  \"uid\": \"auth_user_uid_hash\",\n"
        "  \"date\": \"2026-07-05\",\n"
        "  \"travel\": {\n"
        "    \"mode\": \"car_petrol\",\n"
        "    \"distance\": 25.0,\n"
        "    \"passengers\": 2\n"
        "  },\n"
        "  \"food\": {\n"
        "    \"diet_type\": \"vegetarian\",\n"
        "    \"meal_count\": 3,\n"
        "    \"food_waste\": false\n"
        "  },\n"
        "  \"energy\": {\n"
        "    \"electricity_kwh\": 8.5,\n"
        "    \"heating\": false,\n"
        "    \"ac\": true\n"
        "  },\n"
        "  \"travel_emissions\": 2.4,\n"
        "  \"food_emissions\": 3.81,\n"
        "  \"energy_emissions\": 3.48,\n"
        "  \"total\": 9.69,\n"
        "  \"timestamp\": \"2026-07-05T14:58:29.123Z\"\n"
        "}"
    )
    pdf.heading_2("6.3 In-Memory Demo Database Specification")
    pdf.paragraph(
        "When running in Demo Mode (uid: 'demo_user'), cloud storage is replaced by an in-memory dictionary "
        "defined in firebase_config.py. The state replicates Firestore operations using basic key lookups, "
        "resetting on backend restart."
    )
    
    # ---------------- PAGE 11 ----------------
    pdf.add_page()
    pdf.heading_1("Chapter 7: Backend API Specifications & Router Modules")
    pdf.heading_2("7.1 API Endpoint Registry")
    pdf.paragraph(
        "The Flask server exposes endpoints registered using Blueprints. Below is the API specification "
        "for carbon calculations:"
    )
    pdf.heading_3("Emissions Calculation Endpoint")
    pdf.paragraph(
        "Compute carbon footprint values dynamically. This endpoint is stateless and does not write to the database."
    )
    pdf.bullet_point("URL & Method", "POST /api/calculate/footprint")
    pdf.bullet_point("Headers", "Content-Type: application/json")
    pdf.heading_3("Request Body Example")
    pdf.code_block(
        "{\n"
        "  \"travel\": {\"mode\": \"car_petrol\", \"distance\": 25, \"passengers\": 2},\n"
        "  \"food\": {\"diet_type\": \"vegetarian\", \"meal_count\": 3, \"food_waste\": false},\n"
        "  \"energy\": {\"electricity_kwh\": 8.5, \"heating\": false, \"ac\": true}\n"
        "}"
    )
    pdf.heading_3("Response Body (200 OK)")
    pdf.code_block(
        "{\n"
        "  \"success\": true,\n"
        "  \"travel_emissions\": 2.4,\n"
        "  \"food_emissions\": 3.81,\n"
        "  \"energy_emissions\": 3.48,\n"
        "  \"total\": 9.69,\n"
        "  \"breakdown\": { ... }\n"
        "}"
    )
    
    # ---------------- PAGE 12 ----------------
    pdf.add_page()
    pdf.heading_1("Chapter 7: Backend API Specifications (Continued)")
    pdf.heading_2("7.2 Habits Persistence & Achievements Endpoints")
    pdf.heading_3("Log Habits Endpoint")
    pdf.paragraph(
        "Compute and save today's carbon footprint log. Updates the user's logging streak."
    )
    pdf.bullet_point("URL & Method", "POST /api/habits/log")
    pdf.bullet_point("Auth Required", "Bearer JWT Token (or 'demo_token')")
    pdf.heading_3("Response Body (200 OK)")
    pdf.code_block(
        "{\n"
        "  \"success\": true,\n"
        "  \"date\": \"2026-07-05\",\n"
        "  \"total\": 9.69,\n"
        "  \"streak\": 3,\n"
        "  \"travel_emissions\": 2.4,\n"
        "  \"food_emissions\": 3.81,\n"
        "  \"energy_emissions\": 3.48\n"
        "}"
    )
    pdf.heading_3("Get Today's Log Endpoint")
    pdf.bullet_point("URL & Method", "GET /api/habits/today (Optional query param: ?date=YYYY-MM-DD)")
    pdf.bullet_point("Response (200 OK)", "{\"success\": true, \"log\": { ... }} or {\"success\": false}")
    
    pdf.heading_3("Get History Endpoint")
    pdf.bullet_point("URL & Method", "GET /api/habits/history")
    pdf.bullet_point("Response (200 OK)", "{\"success\": true, \"history\": [ {log_1}, {log_2}, ... ]}")
    
    pdf.heading_3("Badges Management Endpoints")
    pdf.bullet_point("GET /api/habits/badges", "Fetches the list of unlocked badges.")
    pdf.bullet_point("POST /api/habits/badges", "Saves an updated badges list: `{\"badges\": [ {id, unlocked_at} ]}`.")
    
    # ---------------- PAGE 13 ----------------
    pdf.add_page()
    pdf.heading_1("Chapter 7: Backend API Specifications (Continued)")
    pdf.heading_2("7.3 User Configuration & Middlewares")
    pdf.heading_3("Manage Settings Endpoint")
    pdf.paragraph(
        "Retrieve or update user configurations (e.g. daily carbon budget, displayName, theme, locale country, weekly goal)."
    )
    pdf.bullet_point("URL & Method", "GET /api/habits/settings | PATCH /api/habits/settings")
    pdf.bullet_point("Request Payload (PATCH)", "{\"budget\": 7.5, \"displayName\": \"Eco Champion\"}")
    pdf.bullet_point("Response (200 OK)", "{\"success\": true, \"settings\": { ... }}")
    
    pdf.heading_2("7.4 Middleware Interceptor Authorization Code Walkthrough")
    pdf.paragraph(
        "To intercept requests, evaluate token validity, and populate client context, backend controllers use a "
        "require_auth decorator. Below is the implementation structure:"
    )
    pdf.code_block(
        "def require_auth(f):\n"
        "    @wraps(f)\n"
        "    def decorated(*args, **kwargs):\n"
        "        auth_header = request.headers.get('Authorization')\n"
        "        if not auth_header or not auth_header.startswith('Bearer '):\n"
        "            return jsonify({'error': 'Unauthorized'}), 401\n"
        "        token = auth_header.split(' ')[1]\n"
        "        if token == 'demo_token':\n"
        "            request.uid = 'demo_user'\n"
        "            return f(*args, **kwargs)\n"
        "        try:\n"
        "            decoded_token = auth.verify_id_token(token)\n"
        "            request.uid = decoded_token['uid']\n"
        "            request.user = decoded_token\n"
        "        except Exception:\n"
        "            return jsonify({'error': 'Invalid token'}), 401\n"
        "        return f(*args, **kwargs)\n"
        "    return decorated"
    )
    
    # ---------------- PAGE 14 ----------------
    pdf.add_page()
    pdf.heading_1("Chapter 8: Emission Coefficients & Calculation Models")
    pdf.heading_2("8.1 Scientific Coefficient Matrix")
    pdf.paragraph(
        "Emissions are calculated using standard scientific factors representing kilograms of carbon dioxide "
        "equivalent (kg CO2e) per unit. These coefficients are configured on the backend:"
    )
    
    pdf.heading_3("Transportation Mode Coefficients (kg CO2 / km / person)")
    headers1 = ["Transport Mode", "API Key ID", "Factor", "Passenger Scale"]
    data1 = [
        ["Car (Petrol)", "car_petrol", "0.192", "Scaled: Divided by passengers"],
        ["Car (Diesel)", "car_diesel", "0.171", "Scaled: Divided by passengers"],
        ["Car (Electric)", "car_electric", "0.053", "Scaled: Divided by passengers"],
        ["Bus", "bus", "0.089", "Shared: Divided by passengers"],
        ["Train", "train", "0.041", "Fixed (No passenger scaling)"],
        ["Motorcycle", "motorcycle", "0.114", "Scaled: Divided by passengers"],
        ["Bicycle / Walk", "bicycle / walking", "0.000", "Zero Emissions"]
    ]
    pdf.draw_table(headers1, data1, [38, 38, 24, 80])
    
    pdf.heading_3("Diet Baseline Coefficients (kg CO2 / day)")
    headers2 = ["Diet Type", "ID Key", "Emissions Factor", "Food Waste Penalty"]
    data2 = [
        ["Meat-Heavy Diet", "meat-heavy", "7.19 kg CO2e / day", "+10% of total diet emissions"],
        ["Omnivore Diet", "omnivore", "5.63 kg CO2e / day", "+10% of total diet emissions"],
        ["Vegetarian Diet", "vegetarian", "3.81 kg CO2e / day", "+10% of total diet emissions"],
        ["Vegan Diet", "vegan", "2.89 kg CO2e / day", "+10% of total diet emissions"]
    ]
    pdf.draw_table(headers2, data2, [35, 30, 45, 70])
    
    pdf.heading_3("Energy Consumption Factors")
    pdf.bullet_point("India Power Grid Factor", "0.233 kg CO2 per kWh of electricity consumed.")
    pdf.bullet_point("HVAC Flat Rates", "Active Heating adds 2.0 kg; Active Air Conditioning (AC) adds 1.5 kg.")

    # ---------------- PAGE 15 ----------------
    pdf.add_page()
    pdf.heading_1("Chapter 9: Frontend Architecture & Client Routing")
    pdf.heading_2("9.1 React SPA Structure")
    pdf.paragraph(
        "The client frontend is developed as a Single Page Application (SPA) using React. Vite compiles the "
        "assets and processes fast-refresh changes during development. The frontend coordinates page routing, "
        "user session state context, layout styling, and charts configuration."
    )
    
    pdf.heading_2("9.2 Private and Public Routing Rules")
    pdf.paragraph(
        "To protect screens, the client implements route guards. Private routes require an active user session; "
        "otherwise, they redirect to `/login`. Public routes (e.g. login/register) redirect authenticated users to `/`."
    )
    pdf.code_block(
        "// Private Route Wrapper (from App.jsx)\n"
        "function PrivateRoute({ children }) {\n"
        "  const { currentUser } = useAuth();\n"
        "  return currentUser ? children : <Navigate to=\"/login\" replace />;\n"
        "}\n\n"
        "// Public Route Wrapper (from App.jsx)\n"
        "function PublicRoute({ children }) {\n"
        "  const { currentUser } = useAuth();\n"
        "  return !currentUser ? children : <Navigate to=\"/\" replace />;\n"
        "}"
    )
    
    # ---------------- PAGE 16 ----------------
    pdf.add_page()
    pdf.heading_1("Chapter 10: State Management & Auth Context Mechanics")
    pdf.heading_2("10.1 Authentication & Theme Context Flow")
    pdf.paragraph(
        "The AuthContext wrapper provides global states for authentication and user settings. It handles "
        "login, registration, logout, user profile hydration, and active color theme states."
    )
    pdf.heading_3("User Profile Hydration & Initial Load Flow")
    pdf.paragraph(
        "1. On app mount or user change, AuthContext fetches the user's settings profile using the auth token.\n"
        "2. If settings exist, it sets displayName, budget, country, and theme states.\n"
        "3. If settings do not exist, it initializes default settings (budget=8.0, theme='dark') on the backend."
    )
    pdf.heading_3("Demo Mode Authentication Bypass")
    pdf.paragraph(
        "To support evaluations without database credentials, the frontend includes a 'Try Demo Mode' action. "
        "This sets a mock user context and uses a static auth token ('demo_token') in API requests."
    )
    pdf.code_block(
        "async function getAuthToken() {\n"
        "  if (isDemoMode) {\n"
        "    return 'demo_token';\n"
        "  }\n"
        "  if (!auth.currentUser) return null;\n"
        "  return await auth.currentUser.getIdToken(true);\n"
        "}"
    )
    
    # ---------------- PAGE 17 ----------------
    pdf.add_page()
    pdf.heading_1("Chapter 11: Daily Habits Logger Interface State Machine")
    pdf.heading_2("11.1 Logger Form Wizard Configuration")
    pdf.paragraph(
        "The logger interface (`LogToday.jsx`) is configured as a multi-step form wizard to simplify data entry "
        "for the user. Each step represents a distinct category:"
    )
    pdf.bullet_point("Step 1: Travel Form", "Captures transport mode, distance, and passenger count.")
    pdf.bullet_point("Step 2: Food Form", "Captures diet type, meal count, and food waste checkbox.")
    pdf.bullet_point("Step 3: Energy Form", "Captures electricity in kWh and heating/cooling toggles.")
    
    pdf.heading_2("11.2 State Transition Diagram")
    pdf.paragraph(
        "Transitions are managed using a numeric state variable (`step`). The form validates current "
        "inputs before transitioning. If validation succeeds, `step` increments; if it fails, the system "
        "displays an error banner at the top of the card."
    )
    
    pdf.heading_2("11.3 Real-Time Preview Calculations")
    pdf.paragraph(
        "To show the user their emissions impact immediately, the client uses a `useEffect` hook to calculate "
        "emissions previews in real-time as the form inputs change."
    )
    pdf.code_block(
        "useEffect(() => {\n"
        "  const travelEst = (travel.distance * TRANS_COEF[travel.mode]) / travel.passengers;\n"
        "  const foodEst = FOOD_COEF[food.diet_type] * (food.meal_count / 3.0) * (food.food_waste ? 1.1 : 1.0);\n"
        "  const energyEst = energy.electricity_kwh * ELEC_FACTOR + (energy.heating ? 2.0 : 0) + (energy.ac ? 1.5 : 0);\n"
        "  setPreviews({ travel: travelEst, food: foodEst, energy: energyEst, total: travelEst + foodEst + energyEst });\n"
        "}, [travel, food, energy]);"
    )
    
    # ---------------- PAGE 18 ----------------
    pdf.add_page()
    pdf.heading_1("Chapter 12: Gamification Engine & Logging Streaks Math")
    pdf.heading_2("12.1 Logging Streak Mathematics")
    pdf.paragraph(
        "To calculate streaks, the backend compares the user's current logging date with the last logged date "
        "stored in their profile document. This logic is handled inside update_user_streak in habits.py:"
    )
    pdf.code_block(
        "try:\n"
        "    log_date = datetime.strptime(log_date_str, '%Y-%m-%d').date()\n"
        "except ValueError:\n"
        "    return 0\n\n"
        "last_logged_str = user_data.get('last_logged_date')\n"
        "current_streak = user_data.get('streak', 0)\n\n"
        "if not last_logged_str:\n"
        "    new_streak = 1\n"
        "else:\n"
        "    try:\n"
        "        last_logged = datetime.strptime(last_logged_str, '%Y-%m-%d').date()\n"
        "        diff = (log_date - last_logged).days\n"
        "        if diff == 1:\n"
        "            new_streak = current_streak + 1\n"
        "        elif diff == 0:\n"
        "            new_streak = current_streak if current_streak > 0 else 1\n"
        "        else:\n"
        "            new_streak = 1\n"
        "    except Exception:\n"
        "        new_streak = 1"
    )
    pdf.heading_2("12.2 Timezone & UTC Alignment Guidelines")
    pdf.paragraph(
        "Because users may log from different timezones, dates are normalized to YYYY-MM-DD format using UTC "
        "ISO dates on the client. This ensures that calculations remain consistent regardless of the client's "
        "local timezone offset."
    )
    pdf.ln(5)
    pdf.image("docs_assets/activity_heatmap.png", x=15, y=pdf.get_y(), w=180)
    pdf.ln(85)
    
    # ---------------- PAGE 19 ----------------
    pdf.add_page()
    pdf.heading_1("Chapter 13: Achievements Evaluation Matrix & Badges")
    pdf.heading_2("13.1 Badges Matrix & Logical Criteria")
    pdf.paragraph(
        "The achievements matrix details the 10 badges evaluated in `badges.js` after each daily habit submission:"
    )
    
    headers3 = ["ID", "Badge Title", "Condition Check Formula", "Database Verification"]
    data3 = [
        ["first_step", "First Step", "totalLogs >= 1", "Verifies overall logs count in history"],
        ["green_day", "Green Day", "totalEmissions <= budget", "Verifies day's emissions is under budget"],
        ["streak_3", "3-Day Streak", "streak >= 3", "Evaluates current active logging streak"],
        ["week_warrior", "Week Warrior", "streak >= 7", "Evaluates current active logging streak"],
        ["pedal_power", "Pedal Power", "mode in [walk, cycle]", "Verifies travel distance is > 0 km"],
        ["plant_day", "Plant Day", "diet in [vegan, veg]", "Checks daily food diet type selections"],
        ["low_energy", "Low Energy", "energy_emissions <= 1.0", "Checks daily home utility carbon load"],
        ["monthly_hero", "Monthly Hero", "totalLogs >= 15", "Checks total logs count in database"],
        ["monthly_master", "Monthly Master", "totalLogs >= 30", "Checks total logs count in database"],
        ["zero_waster", "Zero Waster", "food_waste == false", "Verifies food waste checkbox was unchecked"]
    ]
    pdf.draw_table(headers3, data3, [25, 30, 50, 75])

    pdf.heading_2("13.2 Achievements Evaluation Process")
    pdf.paragraph(
        "The client evaluates achievements by passing the updated log, user history, and existing badges to "
        "evaluateBadges. If new badges are unlocked, they are appended to the user profile document and displayed "
        "in a modal container before redirecting to the dashboard."
    )
    
    # ---------------- PAGE 20 ----------------
    pdf.add_page()
    pdf.heading_1("Chapter 14: AI Recommendation Engine & Prompt Optimization")
    pdf.heading_2("14.1 Groq LLaMA 3.3 Prompt Engineering")
    pdf.paragraph(
        "To retrieve personalized recommendations, the suggestions route passes a structured prompt to "
        "Groq's LLaMA 3.3 model. The system instructs the LLM to output a raw JSON array containing three "
        "specific suggestion objects with title, description, category, and saving fields:"
    )
    pdf.code_block(
        "Here is the daily carbon footprint breakdown of the user:\n"
        "- Daily Carbon Budget: 8.0 kg CO2\n"
        "- Total Footprint Today: 12.5 kg CO2\n"
        "- Travel: 4.8 kg CO2 (Mode: car_petrol, Distance: 25 km, Passengers: 1)\n"
        "- Food: 5.63 kg CO2 (Diet: omnivore, Meals: 3, Food Waste: true)\n"
        "- Energy: 2.07 kg CO2 (Electricity: 9.0 kWh, AC: true)\n\n"
        "Generate exactly 3 personalized, practical eco swaps in a raw JSON array format:\n"
        "[\n"
        "  {\n"
        "    \"title\": \"Carpool or Walk\",\n"
        "    \"description\": \"Sharing rides for your 25km trip saves emissions.\",\n"
        "    \"category\": \"travel\",\n"
        "    \"estimated_co2_saving\": 2.4\n"
        "  }\n"
        "]"
    )
    pdf.heading_2("14.2 Robust JSON Extraction Parser")
    pdf.paragraph(
        "To handle parsing anomalies (such as markdown tags or text preamble returned by the AI), the backend "
        "implements `extract_json`. This function strips code blocks, locates the outermost brackets, and parses "
        "the raw JSON payload."
    )
    pdf.ln(5)
    pdf.image("docs_assets/ai_suggestions.png", x=15, y=pdf.get_y(), w=180)
    pdf.ln(80)
    
    # ---------------- PAGE 21 ----------------
    pdf.add_page()
    pdf.heading_1("Chapter 15: External APIs & Proxy Calculations")
    pdf.heading_2("15.1 Carbon Interface API Client")
    pdf.paragraph(
        "For external footprint evaluations, the backend implements proxy endpoints to interface with the Carbon "
        "Interface API. These endpoints manage the authorization headers and payloads required by the third-party service."
    )
    
    pdf.heading_2("15.2 Electricity Estimation Model")
    pdf.paragraph(
        "The electricity estimation endpoint passes values, units, and regional ISO codes to Carbon Interface. "
        "If the API is unconfigured, it falls back to regional coefficients defined statically on the server."
    )
    
    pdf.heading_2("15.3 Flight Distance & Haversine Mathematical Model")
    pdf.paragraph(
        "To calculate flight distances when the API key is not present, the server uses the Haversine formula "
        "to compute great-circle distances between airport coordinates. It then scales emissions based on short-haul "
        "or long-haul coefficients and passenger counts."
    )
    pdf.code_block(
        "def haversine_distance(coord1, coord2):\n"
        "    R = 6371.0 # Earth radius in km\n"
        "    lat1, lon1 = map(math.radians, coord1)\n"
        "    lat2, lon2 = map(math.radians, coord2)\n"
        "    dlat = lat2 - lat1\n"
        "    dlon = lon2 - lon1\n"
        "    a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2\n"
        "    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))\n"
        "    return R * c"
    )
    
    # ---------------- PAGE 22 ----------------
    pdf.add_page()
    pdf.heading_1("Chapter 16: Setup Guide & Local Dev Verification")
    pdf.heading_2("16.1 Installation Prerequisites")
    pdf.paragraph(
        "Ensure the local system has Python 3.8+ and Node.js 16+ installed before configuring the project "
        "dependencies."
    )
    pdf.heading_2("16.2 Backend Installation Steps")
    pdf.code_block(
        "cd backend\n"
        "python -m venv venv\n"
        "venv\\Scripts\\activate\n"
        "pip install -r requirements.txt\n"
        "python app.py"
    )
    pdf.heading_2("16.3 Frontend Installation Steps")
    pdf.code_block(
        "cd frontend\n"
        "npm install\n"
        "npm run dev"
    )
    pdf.heading_2("16.4 Environment Variables Setup")
    pdf.paragraph(
        "Create configuration files in both root folders to define API credentials:"
    )
    pdf.bullet_point("backend/.env", "GROQ_API_KEY=your_groq_key_here\nCARBON_INTERFACE_API_KEY=your_carbon_key_here")
    pdf.bullet_point("frontend/.env", "Define Firebase credentials matching your Firestore client config.")
    
    pdf.heading_2("16.5 Exposing Public Tunnels via Ngrok")
    pdf.paragraph(
        "To expose local ports for external testing, deploy them using secure Ngrok tunnels:"
    )
    pdf.code_block(
        "ngrok http 5000 --domain=your-backend.ngrok-free.app\n"
        "ngrok http 5173 --domain=your-frontend.ngrok-free.app"
    )
    
    # ---------------- PAGE 23 ----------------
    pdf.add_page()
    pdf.heading_1("Chapter 17: Platform Testing & Validation Protocols")
    pdf.heading_2("17.1 Verification Plan Checklist")
    pdf.paragraph(
        "The verification checklist below outlines the manual test scenarios used to validate platform behavior:"
    )
    pdf.bullet_point("Demo Mode Logging Access", "Click 'Try Demo Mode' on the login page. Verify redirection to '/' and budget hydration.")
    pdf.bullet_point("Real-Time Preview Validation", "Open '/logger'. Change distance to 20 km. Verify total estimates update dynamically.")
    pdf.bullet_point("Validation Constraints", "Enter 35 kWh in the energy usage field. Confirm that save fails with a 400 validation error.")
    pdf.bullet_point("Badges Unlock Workflow", "Complete log with vegetarian diet and no food waste. Verify Green Day and Zero Waster badges modal displays.")
    pdf.bullet_point("AI Recommendation Generation", "Open '/suggestions'. Confirm loading skeleton component displays, followed by three suggestions.")
    pdf.bullet_point("Historical Charts Loading", "Open '/history'. Verify Chart.js renders line trend vs budget, breakdown charts, and heatmap calendar.")
    pdf.bullet_point("Carbon Calculators Testing", "Open '/profile'. Enter 20 kWh in utility estimator. Confirm emission results update correctly.")
    pdf.bullet_point("Cross-Browser Responsive Layout", "Toggle viewport to Mobile (375px) in DevTools. Confirm Navbar collapses and tables wrap.")
    
    # ---------------- PAGE 24 ----------------
    pdf.add_page()
    pdf.heading_1("Chapter 18: Non-Functional Specs & Future Roadmap")
    pdf.heading_2("18.1 Non-Functional Specifications")
    pdf.paragraph(
        "To support production environments, the system satisfies key non-functional criteria:"
    )
    pdf.bullet_point("Performance Targets", "Aggregated database queries complete in under 200ms, and cached configurations load instantly.")
    pdf.bullet_point("Security Parameters", "All API keys are restricted to the server, and CORS policies block requests from unauthorized domains.")
    pdf.bullet_point("Visual Design & Theme system", "Glassmorphism layouts use consistent colors and follow responsive layout grids.")
    
    pdf.heading_2("18.2 Future Enhancements Roadmap")
    pdf.paragraph(
        "Planned improvements for future iterations of the EcoTrack platform include:"
    )
    pdf.bullet_point("Regional Grid Integrations", "Connect directly to local grid operators to fetch live utility emission factors based on real-time grid status.")
    pdf.bullet_point("Aviation IATA Database Integration", "Integrate flight route logger forms with full international IATA database auto-complete libraries.")
    pdf.bullet_point("Receipt OCR Scanning Module", "Implement image recognition scanners to parse food and utility invoices directly.")
    pdf.bullet_point("Community Achievements Leaderboard", "Enable friends to compare carbon budgets, track streaks, and share custom achievement badges.")
    
    # Save the output PDF
    output_path = r"c:\Users\regal\.gemini\antigravity-ide\scratch\ecotrack\EcoTrack_Documentation.pdf"
    pdf.output(output_path)
    print(f"Success: Extended Documentation generated at {output_path}")

if __name__ == "__main__":
    generate_pdf()
