import streamlit as st
import pandas as pd 
import folium
from streamlit_folium import st_folium
import random

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="GreenTwinning TN",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# TRANSLATIONS
# ─────────────────────────────────────────────
TEXTS = {
    "ar": {
        "app_title": "🌿 GreenTwinning TN",
        "app_subtitle": "منصة التوأمة البيئية للنوادي العلمية في تونس",
        "lang_label": "اللغة",
        "nav_map": "🗺️ خريطة النوادي",
        "nav_twinning": "🤝 نظام التوأمة",
        "nav_projects": "🌱 مشاريع التلاميذ",
        "nav_partners": "🤝 بوابة الشركاء",
        "nav_register": "➕ تسجيل نادٍ جديد",
        "map_title": "خريطة النوادي البيئية والعلمية",
        "map_subtitle": "اكتشف النوادي المنتشرة في كامل أرجاء تونس",
        "filter_all": "الكل",
        "filter_env": "🌿 بيئي",
        "filter_tech": "💻 تقني",
        "twin_title": "نظام التوأمة الذكي",
        "twin_subtitle": "ابحث عن نادٍ شقيق يشاركك الاهتمامات والتخصص",
        "twin_select_gov": "اختر ولايتك",
        "twin_select_spec": "اختر تخصصك",
        "twin_btn": "🔍 ابحث عن توأم",
        "twin_results": "النوادي المقترحة للتوأمة",
        "twin_match": "تطابق",
        "twin_contact": "📩 تواصل معهم",
        "proj_title": "معرض مشاريع التلاميذ",
        "proj_subtitle": "إبداعات الشباب البيئي من مختلف مناطق تونس",
        "proj_like": "❤️ إعجاب",
        "proj_likes": "إعجاب",
        "part_title": "بوابة الشركاء والمؤسسات",
        "part_subtitle": "برامج الدعم، المسابقات، والتمويل المتاح للنوادي المدرسية",
        "opp_apply": "تقديم طلب",
        "opp_type": "نوع الدعم",
        "opp_deadline": "آخر أجل",
        "reg_title": "تسجيل نادٍ جديد",
        "reg_subtitle": "انضم إلى شبكة GreenTwinning وابدأ رحلتك البيئية",
        "reg_name": "اسم النادي",
        "reg_gov": "الولاية",
        "reg_spec": "التخصص",
        "reg_members": "عدد الأعضاء",
        "reg_email": "البريد الإلكتروني",
        "reg_desc": "وصف النادي",
        "reg_btn": "🌱 تسجيل النادي",
        "reg_success": "✅ تم تسجيل النادي بنجاح! مرحباً بكم في عائلة GreenTwinning TN",
        "reg_error": "⚠️ يرجى ملء جميع الحقول المطلوبة",
        "clubs_count": "نادٍ مسجّل",
        "members_count": "عضو نشيط",
        "projects_count": "مشروع منجز",
        "governorates": ["تونس", "صفاقس", "سوسة", "القيروان", "بنزرت", "نابل", "أريانة", "المنستير",
                         "قابس", "مدنين", "قفصة", "سيدي بوزيد", "زغوان", "باجة", "جندوبة", "الكاف",
                         "سليانة", "توزر", "قبلي", "تطاوين", "المهدية", "بن عروس", "منوبة"],
        "specialties": ["بيئة وطبيعة", "تكنولوجيا وابتكار", "طاقة متجددة", "زراعة ذكية",
                         "إعادة التدوير", "مناخ وأرصاد", "تنوع بيولوجي", "تعليم بيئي"],
        "spec_env": "بيئة وطبيعة",
        "spec_tech": "تكنولوجيا وابتكار",
        "nav_civil": " شركاء المجتمع المدني",
        "civil_title": "شركاء المجتمع المدني",
        "civil_subtitle": "الجمعيات والمنظمات الداعمة للنوادي البيئية",
        "nav_public": "🏛️ المؤسسات العمومية",
        "public_title": "المؤسسات العمومية",
        "public_subtitle": "الهيئات الحكومية الداعمة للبيئة والتعليم",   
    },
    "fr": {
        "app_title": "🌿 GreenTwinning TN",
        "app_subtitle": "Plateforme de jumelage environnemental des clubs scientifiques en Tunisie",
        "lang_label": "Langue",
        "nav_map": "🗺️ Carte des clubs",
        "nav_twinning": "🤝 Système de jumelage",
        "nav_projects": "🌱 Projets des élèves",
        "nav_partners": "🤝 Portail Partenaires",
        "nav_register": "➕ Enregistrer un club",
        "map_title": "Carte des clubs environnementaux et scientifiques",
        "map_subtitle": "Découvrez les clubs répartis dans toute la Tunisie",
        "filter_all": "Tous",
        "filter_env": "🌿 Environnemental",
        "filter_tech": "💻 Technologique",
        "twin_title": "Système de jumelage intelligent",
        "twin_subtitle": "Trouvez un club partenaire partageant vos intérêts",
        "twin_select_gov": "Sélectionnez votre gouvernorat",
        "twin_select_spec": "Sélectionnez votre spécialité",
        "twin_btn": "🔍 Rechercher un jumelage",
        "twin_results": "Clubs proposés pour le jumelage",
        "twin_match": "Compatibilité",
        "twin_contact": "📩 Les contacter",
        "proj_title": "Galerie des projets des élèves",
        "proj_subtitle": "Les créations des jeunes environnementalistes de Tunisie",
        "proj_like": "❤️ J'aime",
        "proj_likes": "j'aime",
        "part_title": "Portail des Partenaires",
        "part_subtitle": "Programmes de soutien, concours et financements pour les clubs",
        "opp_apply": "Postuler",
        "opp_type": "Type",
        "opp_deadline": "Délai",
        "reg_title": "Enregistrer un nouveau club",
        "reg_subtitle": "Rejoignez le réseau GreenTwinning et commencez votre aventure verte",
        "reg_name": "Nom du club",
        "reg_gov": "Gouvernorat",
        "reg_spec": "Spécialité",
        "reg_members": "Nombre de membres",
        "reg_email": "Adresse e-mail",
        "reg_desc": "Description du club",
        "reg_btn": "🌱 Enregistrer le club",
        "reg_success": "✅ Club enregistré avec succès ! Bienvenue dans la famille GreenTwinning TN",
        "reg_error": "⚠️ Veuillez remplir tous les champs obligatoires",
        "clubs_count": "clubs inscrits",
        "members_count": "membres actifs",
        "projects_count": "projets réalisés",
        "governorates": ["Tunis", "Sfax", "Sousse", "Kairouan", "Bizerte", "Nabeul", "Ariana", "Monastir",
                         "Gabès", "Médenine", "Gafsa", "Sidi Bouzid", "Zaghouan", "Béja", "Jendouba", "Le Kef",
                         "Siliana", "Tozeur", "Kébili", "Tataouine", "Mahdia", "Ben Arous", "Manouba"],
        "specialties": ["Environnement & Nature", "Technologie & Innovation", "Énergie renouvelable",
                         "Agriculture intelligente", "Recyclage", "Climat & Météo", "Biodiversité", "Éducation environnementale"],
        "spec_env": "Environnement & Nature",
        "spec_tech": "Technologie & Innovation",
        "nav_civil": " Partenaires société civile",
        "civil_title": "Partenaires de la société civile",
        "civil_subtitle": "Associations et ONG soutenant les clubs",
        "nav_public": "🏛️ Institutions publiques",
        "public_title": "Institutions publiques",
        "public_subtitle": "Organismes publics soutenant l’environnement et l’éducation",
    },
}

# ─────────────────────────────────────────────
# SESSION STATE INIT
# ─────────────────────────────────────────────
if "lang" not in st.session_state:
    st.session_state.lang = "ar"
if "clubs" not in st.session_state:
    st.session_state.clubs = [
        {"name": "نادي الأرض الخضراء", "name_fr": "Club Terre Verte", "gov": "تونس", "gov_fr": "Tunis",
         "spec": "بيئة وطبيعة", "spec_fr": "Environnement & Nature", "members": 24,
         "type": "env", "lat": 36.8065, "lon": 10.1815, "email": "terre.verte@edu.tn"},
        {"name": "نادي المستقبل التقني", "name_fr": "Club Futur Tech", "gov": "صفاقس", "gov_fr": "Sfax",
         "spec": "تكنولوجيا وابتكار", "spec_fr": "Technologie & Innovation", "members": 31,
         "type": "tech", "lat": 34.7400, "lon": 10.7600, "email": "futur.tech@edu.tn"},
        {"name": "نادي الطاقة النظيفة", "name_fr": "Club Énergie Propre", "gov": "سوسة", "gov_fr": "Sousse",
         "spec": "طاقة متجددة", "spec_fr": "Énergie renouvelable", "members": 18,
         "type": "env", "lat": 35.8256, "lon": 10.6360, "email": "energie.propre@edu.tn"},
        {"name": "نادي الزراعة الذكية", "name_fr": "Club Agri Smart", "gov": "القيروان", "gov_fr": "Kairouan",
         "spec": "زراعة ذكية", "spec_fr": "Agriculture intelligente", "members": 22,
         "type": "env", "lat": 35.6781, "lon": 10.0963, "email": "agri.smart@edu.tn"},
        {"name": "نادي إعادة التدوير", "name_fr": "Club Recyclage", "gov": "بنزرت", "gov_fr": "Bizerte",
         "spec": "إعادة التدوير", "spec_fr": "Recyclage", "members": 15,
         "type": "env", "lat": 37.2744, "lon": 9.8739, "email": "recyclage@edu.tn"},
        {"name": "نادي الابتكار الأخضر", "name_fr": "Club Innovation Verte", "gov": "نابل", "gov_fr": "Nabeul",
         "spec": "تكنولوجيا وابتكار", "spec_fr": "Technologie & Innovation", "members": 27,
         "type": "tech", "lat": 36.4561, "lon": 10.7376, "email": "innovation.verte@edu.tn"},
        {"name": "نادي التنوع البيولوجي", "name_fr": "Club Biodiversité", "gov": "جندوبة", "gov_fr": "Jendouba",
         "spec": "تنوع بيولوجي", "spec_fr": "Biodiversité", "members": 13,
         "type": "env", "lat": 36.5012, "lon": 8.7803, "email": "biodiversite@edu.tn"},
        {"name": "نادي المناخ والأرصاد", "name_fr": "Club Climat Météo", "gov": "الكاف", "gov_fr": "Le Kef",
         "spec": "مناخ وأرصاد", "spec_fr": "Climat & Météo", "members": 19,
         "type": "env", "lat": 36.1741, "lon": 8.7043, "email": "climat@edu.tn"},
    ]
if "projects" not in st.session_state:
    st.session_state.projects = [
        {"title": "حديقة المدرسة المستدامة", "title_fr": "Jardin Scolaire Durable",
         "club": "نادي الأرض الخضراء", "club_fr": "Club Terre Verte",
         "gov": "تونس", "gov_fr": "Tunis",
         "desc": "مشروع لإنشاء حديقة بيئية داخل المدرسة باستخدام تقنيات الزراعة العمودية وإعادة تدوير المياه.",
         "desc_fr": "Création d'un jardin écologique scolaire avec agriculture verticale et recyclage des eaux.",
         "emoji": "🌻", "likes": 47, "liked": False},
        {"title": "محطة الطاقة الشمسية المصغرة", "title_fr": "Mini-Station Solaire",
         "club": "نادي الطاقة النظيفة", "club_fr": "Club Énergie Propre",
         "gov": "سوسة", "gov_fr": "Sousse",
         "desc": "تصميم وتركيب محطة طاقة شمسية مصغرة لتزويد مختبر المدرسة بالكهرباء النظيفة.",
         "desc_fr": "Conception et installation d'une mini-station solaire pour alimenter le laboratoire scolaire.",
         "emoji": "☀️", "likes": 63, "liked": False},
        {"title": "تطبيق رصد جودة الهواء", "title_fr": "App Surveillance Qualité Air",
         "club": "نادي المستقبل التقني", "club_fr": "Club Futur Tech",
         "gov": "صفاقس", "gov_fr": "Sfax",
         "desc": "تطوير تطبيق ذكي لقياس جودة الهواء في المدينة باستخدام أجهزة استشعار رخيصة الثمن.",
         "desc_fr": "Développement d'une app intelligente pour mesurer la qualité de l'air avec des capteurs low-cost.",
         "emoji": "💨", "likes": 38, "liked": False},
        {"title": "ورشة إعادة التدوير الإبداعي", "title_fr": "Atelier Recyclage Créatif",
         "club": "نادي إعادة التدوير", "club_fr": "Club Recyclage",
         "gov": "بنزرت", "gov_fr": "Bizerte",
         "desc": "ورشات أسبوعية لتحويل النفايات إلى أعمال فنية ومنتجات مفيدة.",
         "desc_fr": "Ateliers hebdomadaires pour transformer les déchets en œuvres d'art et produits utiles.",
         "emoji": "♻️", "likes": 72, "liked": False},
    ]

# بيانات الشركاء (الفرص المتاحة)
if "opps" not in st.session_state:
    st.session_state.opps = [
        {
            "org": "وزارة البيئة", "org_fr": "Ministère de l'Environnement",
            "title": "منحة المشاريع الخضراء 2026", "title_fr": "Subvention Projets Verts 2026",
            "type": "تمويل", "type_fr": "Financement",
            "deadline": "2026-05-30", "icon": "🏛️"
        },
        {
            "org": "جمعية تونس للبيئة", "org_fr": "Association Tunisie Environnement",
            "title": "مسابقة أفضل نادي بيئي", "title_fr": "Concours Meilleur Club Éco",
            "type": "مسابقة", "type_fr": "Concours",
            "deadline": "2026-06-15", "icon": "🏆"
        },
        {
            "org": "الوكالة الوطنية للتحكم في الطاقة", "org_fr": "ANME",
            "title": "تحدي المدارس الموفرة للطاقة", "title_fr": "Défi des Écoles Éco-énergétiques",
            "type": "تحدي معدات", "type_fr": "Défi d'équipement",
            "deadline": "2026-09-01", "icon": "⚡"
        }
    ]
if "civil_partners" not in st.session_state:
    st.session_state.civil_partners = [
        {
            "name":  "tunis clean up",
            "name_fr": " tunis clean up",
            "desc": "جمعية تدعم المشاريع البيئية في المدارس وتنظم حملات توعوية.",
            "desc_fr": "Association soutenant les projets écologiques scolaires et campagnes de sensibilisation.",
            "icon": "https://tounescleanup.com/wp-content/uploads/2026/04/logo-principale.png"
        },
        {
            "name": "reseau des enfants de la terre",
            "name_fr": "reseau des enfants de la terre",
            "desc": "تعمل على إشراك الشباب في العمل البيئي والتطوعي.",
            "desc_fr": "Engage les jeunes dans des actions écologiques et bénévoles.",
            "icon": "https://www.reseauenfantdelaterre.com/assets/images/RET/logo.png"
        }
    ]

if "page" not in st.session_state:
    st.session_state.page = "map"
if "public_orgs" not in st.session_state:
    st.session_state.public_orgs = [
        {
            "name": "وزارة البيئة",
            "name_fr": "Ministère de l’Environnement",
            "desc": "تعمل على حماية البيئة وتنفيذ السياسات البيئية في تونس.",
            "desc_fr": "Responsable de la protection de l’environnement et des politiques écologiques.",
            "logo": "https://www.environnement.gov.tn/fileadmin/introduction/images/logo-me-ar.png"
        },
        {
            "name":"الوكالة الوطنية لحماية المحيط",
            "name_fr": "Agence nationale pour la protection de l'environnement",
            "desc":"الوكالة الوطنية لحماية المحيط (ANPE) هي مؤسسة عمومية تونسية تعمل على حماية البيئة ومراقبة التلوث، وتسهر على تطبيق القوانين البيئية ودعم المشاريع المستدامة." ,
            "desc_fr": "L’Agence Nationale de Protection de l’Environnement (ANPE) est un organisme public tunisien chargé de la protection de l’environnement, du contrôle de la pollution et de l’application des réglementations environnementales, tout en soutenant les initiatives durables.",
            "logo": "https://anpe.nat.tn/Fr/static/fr/img/gif/logo.gif"
        },
        {
            "name":"ANGED",
            "name_fr": "ANGED",
            "desc":"البنك الوطني للجينات (bng.nat.tn) هو مؤسسة عمومية تونسية تعمل على حفظ وتثمين الموارد الجينية النباتية والحيوانية، بهدف حماية التنوع البيولوجي ودعم البحث العلمي والتنمية المستدامة.",
              "desc_fr":"La Banque Nationale de Gènes (bng.nat.tn) est un organisme public tunisien chargé de la conservation et de la valorisation des ressources génétiques végétales et animales, afin de protéger la biodiversité et soutenir la recherche scientifique et le développement durable.",
            "logo":"https://i.ibb.co/rKqsRnbd/252605283-180775424242806-8911012430736437489-n.jpg"
        },
        {
            "name": "البنك الوطني للجينات",
            "name_fr": "BNG",
            "desc":"الوكالة الوطنية للتصرف في النفايات (ANGED) هي مؤسسة عمومية تونسية تُعنى بإدارة النفايات وحماية البيئة، من خلال تنظيم عمليات الجمع والمعالجة والتثمين، ودعم مشاريع إعادة التدوير والتنمية المستدامة.",
              "desc_fr":"L’Agence Nationale de Gestion des Déchets (ANGED) est un organisme public tunisien chargé de la gestion des déchets et de la protection de l’environnement, à travers la collecte, le traitement, la valorisation et le soutien aux المشاريع de recyclage et de développement durable.",
            "logo":"http://www.anged.nat.tn/images/logo-anged.png"
        },        
    ]

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────
def t(key):
    return TEXTS[st.session_state.lang].get(key, key)

def is_ar():
    return st.session_state.lang == "ar"

# ─────────────────────────────────────────────
# GLOBAL CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&family=Playfair+Display:wght@700&display=swap');

:root {
    --green-dark:   #1B5E20;
    --green-main:   #2E7D32;
    --green-mid:    #388E3C;
    --green-light:  #A5D6A7;
    --green-pale:   #E8F5E9;
    --green-mint:   #C8E6C9;
    --accent:       #F9A825;
    --bg:           #F3F7F2;
    --card-bg:      #FFFFFF;
    --text-main:    #1C2B1E;
    --text-muted:   #5A7A5C;
    --shadow-soft:  0 4px 24px rgba(46,125,50,0.10);
    --shadow-card:  0 8px 32px rgba(46,125,50,0.13);
    --radius:       30px;
    --radius-sm:    18px;
    --radius-xs:    10px;
}

* { box-sizing: border-box; }

html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
    font-family: 'Cairo', sans-serif !important;
    color: var(--text-main) !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(160deg, var(--green-dark) 0%, var(--green-main) 60%, var(--green-mid) 100%) !important;
    border-radius: 0 var(--radius) var(--radius) 0;
    box-shadow: 4px 0 32px rgba(27,94,32,0.25);
}
[data-testid="stSidebar"] * { color: #fff !important; }
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stRadio label { color: rgba(255,255,255,0.85) !important; font-size: 0.85rem; }
[data-testid="stSidebar"] select,
[data-testid="stSidebar"] [data-baseweb="select"] {
    background: rgba(255,255,255,0.15) !important;
    border: 1px solid rgba(255,255,255,0.3) !important;
    border-radius: var(--radius-sm) !important;
    color: #fff !important;
}
[data-testid="stSidebar"] .stRadio [data-baseweb="radio"] {
    background: rgba(255,255,255,0.1);
    border-radius: var(--radius-xs);
    padding: 6px 12px;
    margin: 4px 0;
    transition: background 0.2s;
}
[data-testid="stSidebar"] .stRadio [data-baseweb="radio"]:hover {
    background: rgba(255,255,255,0.22);
}

/* Main buttons */
.stButton > button {
    background: linear-gradient(135deg, var(--green-main), var(--green-mid)) !important;
    color: #fff !important;
    border: none !important;
    border-radius: var(--radius) !important;
    padding: 0.65rem 2rem !important;
    font-family: 'Cairo', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    box-shadow: 0 4px 16px rgba(46,125,50,0.30) !important;
    transition: all 0.2s ease !important;
    cursor: pointer !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 24px rgba(46,125,50,0.40) !important;
    background: linear-gradient(135deg, var(--green-dark), var(--green-main)) !important;
}

/* Inputs */
.stTextInput input, .stTextArea textarea, .stSelectbox select,
[data-baseweb="input"] input, [data-baseweb="textarea"] textarea {
    border-radius: var(--radius-sm) !important;
    border: 2px solid var(--green-mint) !important;
    background: #fff !important;
    font-family: 'Cairo', sans-serif !important;
    color: var(--text-main) !important;
    transition: border-color 0.2s;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: var(--green-main) !important;
    box-shadow: 0 0 0 3px rgba(46,125,50,0.12) !important;
}

/* Cards */
.green-card {
    background: var(--card-bg);
    border-radius: var(--radius);
    box-shadow: var(--shadow-card);
    padding: 1.6rem 1.8rem;
    margin-bottom: 1.2rem;
    border-top: 4px solid var(--green-main);
    transition: transform 0.2s, box-shadow 0.2s;
    position: relative;
    overflow: hidden;
}
.green-card::before {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 120px; height: 120px;
    background: radial-gradient(circle, var(--green-pale) 0%, transparent 70%);
    border-radius: 50%;
}
.green-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 16px 48px rgba(46,125,50,0.18);
}

.partner-card {
    border-inline-start: 6px solid var(--accent) !important;
    border-top: none !important;
}

.project-card {
    background: var(--card-bg);
    border-radius: var(--radius);
    box-shadow: var(--shadow-card);
    padding: 1.5rem;
    margin-bottom: 1rem;
    position: relative;
    overflow: hidden;
    transition: transform 0.2s;
}
.project-card:hover { transform: translateY(-3px); }
.project-emoji {
    font-size: 3.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 90px; height: 90px;
    background: var(--green-pale);
    border-radius: 50%;
    margin-bottom: 1rem;
    box-shadow: 0 4px 16px rgba(46,125,50,0.15);
}

.stat-card {
    background: linear-gradient(135deg, var(--green-main), var(--green-mid));
    border-radius: var(--radius);
    padding: 1.4rem 1rem;
    text-align: center;
    color: #fff !important;
    box-shadow: 0 8px 24px rgba(46,125,50,0.28);
}
.stat-card .stat-num {
    font-size: 2.4rem;
    font-weight: 900;
    display: block;
    line-height: 1;
}
.stat-card .stat-lbl {
    font-size: 0.85rem;
    opacity: 0.88;
    margin-top: 4px;
    display: block;
}

.page-header {
    background: linear-gradient(135deg, var(--green-dark) 0%, var(--green-main) 50%, var(--green-mid) 100%);
    border-radius: var(--radius);
    padding: 2.5rem 2rem 2rem;
    color: #fff;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
    box-shadow: var(--shadow-card);
}
.page-header::after {
    content: '🌿';
    position: absolute;
    font-size: 8rem;
    right: 1.5rem; top: 50%;
    transform: translateY(-50%);
    opacity: 0.15;
}
.page-header h1 { font-size: 1.9rem; font-weight: 900; margin: 0 0 0.3rem; }
.page-header p { font-size: 0.95rem; opacity: 0.88; margin: 0; }

.badge {
    display: inline-block;
    background: var(--green-pale);
    color: var(--green-dark);
    border-radius: 50px;
    padding: 3px 12px;
    font-size: 0.78rem;
    font-weight: 600;
    margin: 2px;
}
.badge-env { background: #E8F5E9; color: #1B5E20; }
.badge-tech { background: #E3F2FD; color: #0D47A1; }

.like-count {
    display: inline-block;
    background: #FFEBEE;
    color: #C62828;
    border-radius: 50px;
    padding: 2px 10px;
    font-size: 0.82rem;
    font-weight: 700;
}
.match-bar-wrap { background: var(--green-pale); border-radius: 50px; height: 10px; overflow: hidden; margin: 6px 0; }
.match-bar { background: linear-gradient(90deg, var(--green-main), var(--accent)); height: 10px; border-radius: 50px; transition: width 0.6s ease; }

/* Divider */
hr { border: none; border-top: 2px solid var(--green-mint); margin: 1.5rem 0; }

/* RTL */
.rtl { direction: rtl; text-align: right; }
.ltr { direction: ltr; text-align: left; }

/* Scrollbar */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--green-pale); }
::-webkit-scrollbar-thumb { background: var(--green-light); border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

dir_class = "rtl" if is_ar() else "ltr"

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"""
    <div style='text-align:center; '>
      <img src="https://i.ibb.co/KjMdhF7B/Nouveau-projet-1.png"   style="width:500px; filter: drop-shadow(0px 4px 10px rgba(0,0,0,0.3));">
        <div style='font-size:1.25rem; font-weight:900; letter-spacing:0.5px;'>GreenTwinning</div>
        <div style='font-size:0.78rem; opacity:0.80; margin-top:2px;'>تونس / Tunisie</div>
    </div>
    <hr style='border-color:rgba(255,255,255,0.25); margin:1rem 0;'>
    """, unsafe_allow_html=True)

    lang_choice = st.radio(
        "🌐 " + t("lang_label"),
        options=["العربية", "Français"],
        index=0 if st.session_state.lang == "ar" else 1,
        horizontal=True,
    )
    st.session_state.lang = "ar" if lang_choice == "العربية" else "fr"

    st.markdown("<hr style='border-color:rgba(255,255,255,0.25); margin:1rem 0;'>", unsafe_allow_html=True)

    nav_opts = {
        "map":      t("nav_map"),
        "twinning": t("nav_twinning"),
        "projects": t("nav_projects"),
        "partners": t("nav_partners"),  # <-- التبويب الجديد
        "register": t("nav_register"),
        "civil": t("nav_civil"),
        "public": t("nav_public"),
    }
    chosen_label = st.radio("", list(nav_opts.values()), index=list(nav_opts.keys()).index(st.session_state.page))
    for k, v in nav_opts.items():
        if v == chosen_label:
            st.session_state.page = k
            break

    st.markdown("<hr style='border-color:rgba(255,255,255,0.25); margin:1rem 0;'>", unsafe_allow_html=True)
    total_members = sum(c["members"] for c in st.session_state.clubs)
    st.markdown(f"""
    <div style='text-align:center; opacity:0.90;'>
        <div style='font-size:2rem; font-weight:900;'>{len(st.session_state.clubs)}</div>
        <div style='font-size:0.78rem;'>{t("clubs_count")}</div>
        <div style='font-size:1.5rem; font-weight:800; margin-top:0.7rem;'>{total_members}</div>
        <div style='font-size:0.78rem;'>{t("members_count")}</div>
    </div>
    """, unsafe_allow_html=True)
    

page = st.session_state.page

# ─────────────────────────────────────────────
# PAGE: MAP
# ─────────────────────────────────────────────
if page == "map":
    st.markdown(f"""
    <div class='page-header {dir_class}'>
        <h1>{t("map_title")}</h1>
        <p>{t("map_subtitle")}</p>
    </div>""", unsafe_allow_html=True)

    # Stats row
    c1, c2, c3 = st.columns(3)
    env_count = sum(1 for c in st.session_state.clubs if c["type"] == "env")
    tech_count = sum(1 for c in st.session_state.clubs if c["type"] == "tech")
    with c1:
        st.markdown(f"<div class='stat-card'><span class='stat-num'>{len(st.session_state.clubs)}</span><span class='stat-lbl'>{t('clubs_count')}</span></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='stat-card'><span class='stat-num'>{env_count}</span><span class='stat-lbl'>{t('filter_env')}</span></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='stat-card'><span class='stat-num'>{tech_count}</span><span class='stat-lbl'>{t('filter_tech')}</span></div>", unsafe_allow_html=True)

    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)

    filter_col, _ = st.columns([1, 3])
    with filter_col:
        filter_type = st.selectbox(
            "🔽",
            [t("filter_all"), t("filter_env"), t("filter_tech")],
            label_visibility="collapsed"
        )

    # Build map
    m = folium.Map(location=[33.8869, 9.5375], zoom_start=6,
                   tiles="CartoDB positron",
                   attr="© OpenStreetMap, © CartoDB")

    for club in st.session_state.clubs:
        clr = "#2E7D32" if club["type"] == "env" else "#1565C0"
        icon = "leaf" if club["type"] == "env" else "cog"
        show = True
        if filter_type == t("filter_env") and club["type"] != "env":
            show = False
        if filter_type == t("filter_tech") and club["type"] != "tech":
            show = False
        if show:
            name_key = "name" if is_ar() else "name_fr"
            gov_key = "gov" if is_ar() else "gov_fr"
            spec_key = "spec" if is_ar() else "spec_fr"
            popup_html = f"""
            <div style='font-family:Cairo,sans-serif; min-width:180px; direction:{"rtl" if is_ar() else "ltr"}'>
                <b style='color:{clr}; font-size:1rem;'>{club[name_key]}</b><br>
                <span style='color:#555; font-size:0.85rem;'>📍 {club[gov_key]}</span><br>
                <span style='color:#555; font-size:0.85rem;'>🔬 {club[spec_key]}</span><br>
                <span style='color:#555; font-size:0.85rem;'>👥 {club['members']}</span><br>
                <span style='color:#777; font-size:0.8rem;'>✉️ {club['email']}</span>
            </div>"""
            folium.Marker(
                [club["lat"], club["lon"]],
                popup=folium.Popup(popup_html, max_width=220),
                tooltip=club[name_key],
                icon=folium.Icon(color="green" if club["type"] == "env" else "blue",
                                 icon=icon, prefix="fa"),
            ).add_to(m)

    st_folium(m, width=None, height=480, returned_objects=[])

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<h3 class='{dir_class}' style='color:var(--green-dark); font-weight:800;'>{'النوادي المسجّلة' if is_ar() else 'Clubs inscrits'}</h3>", unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    for i, club in enumerate(st.session_state.clubs):
        name_key = "name" if is_ar() else "name_fr"
        gov_key = "gov" if is_ar() else "gov_fr"
        spec_key = "spec" if is_ar() else "spec_fr"
        badge_cls = "badge-env" if club["type"] == "env" else "badge-tech"
        card_html = f"""
        <div class='green-card {dir_class}'>
            <div style='font-size:1.05rem; font-weight:800; color:var(--green-dark);'>{club[name_key]}</div>
            <div style='color:var(--text-muted); font-size:0.88rem; margin:4px 0;'>
                📍 {club[gov_key]} &nbsp;|&nbsp; 👥 {club['members']}
            </div>
            <span class='badge {badge_cls}'>{club[spec_key]}</span>
        </div>"""
        if i % 2 == 0:
            col_a.markdown(card_html, unsafe_allow_html=True)
        else:
            col_b.markdown(card_html, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# PAGE: TWINNING
# ─────────────────────────────────────────────
elif page == "twinning":
    st.markdown(f"""
    <div class='page-header {dir_class}' style="background: linear-gradient(135deg,#1B5E20,#2E7D32,#00695C);">
        <h1>{t("twin_title")}</h1>
        <p>{t("twin_subtitle")}</p>
    </div>""", unsafe_allow_html=True)

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            gov_label = t("twin_select_gov")
            sel_gov = st.selectbox(gov_label, ["—"] + t("governorates"))
        with col2:
            spec_label = t("twin_select_spec")
            sel_spec = st.selectbox(spec_label, ["—"] + t("specialties"))

        search_clicked = st.button(t("twin_btn"), use_container_width=True)

    if search_clicked:
        if sel_gov == "—" or sel_spec == "—":
            st.warning(t("reg_error"))
        else:
            st.markdown(f"<h3 class='{dir_class}' style='color:var(--green-dark); margin-top:1.5rem; font-weight:800;'>{t('twin_results')}</h3>", unsafe_allow_html=True)
            suggestions = []
            for club in st.session_state.clubs:
                gov_key = "gov" if is_ar() else "gov_fr"
                spec_key = "spec" if is_ar() else "spec_fr"
                score = 0
                if club[gov_key] != sel_gov:
                    score += random.randint(40, 75)
                if club[spec_key] == sel_spec:
                    score += 30
                else:
                    score += random.randint(5, 25)
                score = min(score, 98)
                suggestions.append((score, club))

            suggestions.sort(key=lambda x: -x[0])
            top = suggestions[:4]

            for score, club in top:
                name_key = "name" if is_ar() else "name_fr"
                gov_key = "gov" if is_ar() else "gov_fr"
                spec_key = "spec" if is_ar() else "spec_fr"
                badge_cls = "badge-env" if club["type"] == "env" else "badge-tech"
                st.markdown(f"""
                <div class='green-card {dir_class}'>
                    <div style='display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;'>
                        <div>
                            <div style='font-size:1.1rem; font-weight:800; color:var(--green-dark);'>{club[name_key]}</div>
                            <div style='color:var(--text-muted); font-size:0.88rem;'>📍 {club[gov_key]} &nbsp;|&nbsp; 👥 {club['members']}</div>
                            <span class='badge {badge_cls}'>{club[spec_key]}</span>
                        </div>
                        <div style='text-align:center; min-width:80px;'>
                            <div style='font-size:1.6rem; font-weight:900; color:var(--green-main);'>{score}%</div>
                            <div style='font-size:0.75rem; color:var(--text-muted);'>{t("twin_match")}</div>
                        </div>
                    </div>
                    <div class='match-bar-wrap' style='margin-top:10px;'><div class='match-bar' style='width:{score}%;'></div></div>
                    <div style='margin-top:8px; font-size:0.82rem; color:var(--text-muted);'>✉️ {club['email']}</div>
                </div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# PAGE: PROJECTS
# ─────────────────────────────────────────────
elif page == "projects":
    st.markdown(f"""
    <div class='page-header {dir_class}' style="background: linear-gradient(135deg,#33691E,#388E3C,#1B5E20);">
        <h1>{t("proj_title")}</h1>
        <p>{t("proj_subtitle")}</p>
    </div>""", unsafe_allow_html=True)

    st.markdown(f"<div class='{dir_class}' style='color:var(--text-muted); font-size:0.9rem; margin-bottom:1rem;'>{'عدد المشاريع' if is_ar() else 'Nombre de projets'}: <b style='color:var(--green-dark);'>{len(st.session_state.projects)}</b></div>", unsafe_allow_html=True)

    cols = st.columns(2)
    for i, proj in enumerate(st.session_state.projects):
        title_key = "title" if is_ar() else "title_fr"
        desc_key = "desc" if is_ar() else "desc_fr"
        club_key = "club" if is_ar() else "club_fr"
        gov_key = "gov" if is_ar() else "gov_fr"

        with cols[i % 2]:
            st.markdown(f"""
            <div class='project-card {dir_class}'>
                <div class='project-emoji'>{proj['emoji']}</div>
                <div style='font-size:1.05rem; font-weight:800; color:var(--green-dark); margin-bottom:6px;'>{proj[title_key]}</div>
                <div style='font-size:0.82rem; color:var(--text-muted); margin-bottom:8px;'>
                    🏫 {proj[club_key]} &nbsp;|&nbsp; 📍 {proj[gov_key]}
                </div>
                <div style='font-size:0.88rem; color:#444; margin-bottom:1rem; line-height:1.6;'>{proj[desc_key]}</div>
                <span class='like-count'>❤️ {proj['likes']} {t("proj_likes")}</span>
            </div>""", unsafe_allow_html=True)

            btn_label = "💔 " + ("إلغاء الإعجاب" if is_ar() else "Je n'aime plus") if proj["liked"] else t("proj_like")
            if st.button(btn_label, key=f"like_{i}"):
                if st.session_state.projects[i]["liked"]:
                    st.session_state.projects[i]["likes"] -= 1
                    st.session_state.projects[i]["liked"] = False
                else:
                    st.session_state.projects[i]["likes"] += 1
                    st.session_state.projects[i]["liked"] = True
                st.rerun()

# ─────────────────────────────────────────────
# PAGE: PARTNERS (NEW)
# ─────────────────────────────────────────────
elif page == "partners":
    st.markdown(f"""
    <div class='page-header {dir_class}' style="background: linear-gradient(135deg, #004D40, #00796B);">
        <h1>{t("part_title")}</h1>
        <p>{t("part_subtitle")}</p>
    </div>""", unsafe_allow_html=True)

    for i, opp in enumerate(st.session_state.opps):
        title = opp['title'] if is_ar() else opp['title_fr']
        org = opp['org'] if is_ar() else opp['org_fr']
        opp_type = opp['type'] if is_ar() else opp['type_fr']

        st.markdown(f"""
        <div class='green-card partner-card {dir_class}'>
            <div style='display: flex; align-items: center; gap: 20px; flex-wrap: wrap;'>
                <div style='font-size: 3rem; background: var(--green-pale); width: 80px; height: 80px; display: flex; align-items: center; justify-content: center; border-radius: 50%; box-shadow: 0 4px 10px rgba(0,0,0,0.05);'>
                    {opp['icon']}
                </div>
                <div style='flex-grow: 1; min-width: 200px;'>
                    <h3 style='margin: 0 0 5px 0; color: #004D40; font-weight: 800;'>{title}</h3>
                    <p style='margin: 0; color: var(--text-muted); font-size: 0.95rem; font-weight: 600;'>🏢 {org}</p>
                    <div style='margin-top: 12px;'>
                        <span class='badge' style='background: #FFF3E0; color: #E65100; border: 1px solid #FFE0B2;'>📅 {t("opp_deadline")}: {opp['deadline']}</span>
                        <span class='badge' style='background: #E0F2F1; color: #004D40; border: 1px solid #B2DFDB;'>🏷️ {t("opp_type")}: {opp_type}</span>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # زر التقديم
        btn_cols = st.columns([1, 4] if is_ar() else [4, 1])
        with btn_cols[0] if is_ar() else btn_cols[1]:
            if st.button(t("opp_apply"), key=f"apply_{i}", use_container_width=True):
                success_msg = "✅ تم تسجيل اهتمامكم. سيتم تحويلكم لصفحة الاستمارة!" if is_ar() else "✅ Intérêt enregistré. Redirection en cours !"
                st.toast(success_msg)
elif page == "civil":
    st.markdown(f"""
    <div class='page-header {dir_class}'>
        <h1>{t("civil_title")}</h1>
        <p>{t("civil_subtitle")}</p>
    </div>""", unsafe_allow_html=True)

    for assoc in st.session_state.civil_partners:
        name = assoc["name"] if is_ar() else assoc["name_fr"]
        desc = assoc["desc"] if is_ar() else assoc["desc_fr"]

        st.markdown(f"""
        <div class='green-card {dir_class}'>
            <div style='display:flex; align-items:center; gap:15px;'>
                <div>
               <img src="{assoc['icon']}" style="width:60px; height:60px; object-fit:contain; border-radius:10px;">
               </div>
                <div>
                    <h3 style='margin:0; color:var(--green-dark);'>{name}</h3>
                    <p style='margin:5px 0; color:var(--text-muted);'>{desc}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
elif page == "public":
    st.markdown(f"""
    <div class='page-header {dir_class}'>
        <h1>{t("public_title")}</h1>
        <p>{t("public_subtitle")}</p>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(2)

    # تأكد من تعريف st.session_state.public_orgs في بداية الكود
    for i, org in enumerate(st.session_state.public_orgs):
        name = org["name"] if is_ar() else org["name_fr"]
        desc = org["desc"] if is_ar() else org["desc_fr"]

        with cols[i % 2]:
            st.markdown(f"""
            <div style="
                background:#417D3A;
                border-radius:45px;
                padding: 20px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.08);
                transition: all 0.3s ease;
                text-align: center;
                margin-bottom: 20px;
            ">
                <img src="{org['logo']}" style="
                    width:100px;
                    height:100px;
                    object-fit:contain;
                    margin-bottom:15px;
                ">
                <h3 style="margin:0; color:#fffff; font-weight:800;">
                    {name}
                </h3>
                <p style="color:#f5ebe0; font-size:1rem; margin-top:5px;">
                    {desc}
                </p>
            </div>
            """, unsafe_allow_html=True) # هذا السطر هو مفتاح الحل لتظهر الصور والتصاميم


# ─────────────────────────────────────────────
# PAGE: REGISTER
# ─────────────────────────────────────────────
elif page == "register":
    st.markdown(f"""
    <div class='page-header {dir_class}' style="background: linear-gradient(135deg,#004D40,#00695C,#2E7D32);">
        <h1>{t("reg_title")}</h1>
        <p>{t("reg_subtitle")}</p>
    </div>""", unsafe_allow_html=True)

    with st.container():
        st.markdown(f"<div class='green-card {dir_class}'>", unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            club_name = st.text_input(t("reg_name"), placeholder="Ex: نادي الغد الأخضر")
        with c2:
            gov_list = t("governorates")
            club_gov = st.selectbox(t("reg_gov"), ["—"] + gov_list)

        c3, c4 = st.columns(2)
        with c3:
            spec_list = t("specialties")
            club_spec = st.selectbox(t("reg_spec"), ["—"] + spec_list)
        with c4:
            club_members = st.number_input(t("reg_members"), min_value=1, max_value=500, value=10, step=1)

        club_email = st.text_input(t("reg_email"), placeholder="contact@club.edu.tn")
        club_desc = st.text_area(t("reg_desc"), placeholder="...", height=120)

        st.markdown("</div>", unsafe_allow_html=True)

        if st.button(t("reg_btn"), use_container_width=True):
            if not club_name or club_gov == "—" or club_spec == "—" or not club_email:
                st.error(t("reg_error"))
            else:
                # Determine type
                tech_keywords_ar = ["تكنولوجيا", "ابتكار", "رقمي"]
                tech_keywords_fr = ["tech", "innovation", "numérique"]
                kws = tech_keywords_ar if is_ar() else tech_keywords_fr
                c_type = "tech" if any(k in club_spec.lower() for k in kws) else "env"

                gov_coords = {
                    "تونس": (36.8065, 10.1815), "Tunis": (36.8065, 10.1815),
                    "صفاقس": (34.7400, 10.7600), "Sfax": (34.7400, 10.7600),
                    "سوسة": (35.8256, 10.6360), "Sousse": (35.8256, 10.6360),
                    "القيروان": (35.6781, 10.0963), "Kairouan": (35.6781, 10.0963),
                    "بنزرت": (37.2744, 9.8739), "Bizerte": (37.2744, 9.8739),
                    "نابل": (36.4561, 10.7376), "Nabeul": (36.4561, 10.7376),
                    "أريانة": (36.8625, 10.1956), "Ariana": (36.8625, 10.1956),
                    "المنستير": (35.7643, 10.8113), "Monastir": (35.7643, 10.8113),
                    "قابس": (33.8814, 10.0982), "Gabès": (33.8814, 10.0982),
                    "مدنين": (33.3500, 10.5000), "Médenine": (33.3500, 10.5000),
                    "قفصة": (34.4250, 8.7842), "Gafsa": (34.4250, 8.7842),
                    "سيدي بوزيد": (35.0383, 9.4845), "Sidi Bouzid": (35.0383, 9.4845),
                    "زغوان": (36.4021, 10.1421), "Zaghouan": (36.4021, 10.1421),
                    "باجة": (36.7256, 9.1817), "Béja": (36.7256, 9.1817),
                    "جندوبة": (36.5012, 8.7803), "Jendouba": (36.5012, 8.7803),
                    "الكاف": (36.1741, 8.7043), "Le Kef": (36.1741, 8.7043),
                    "سليانة": (36.0853, 9.3708), "Siliana": (36.0853, 9.3708),
                    "توزر": (33.9197, 8.1335), "Tozeur": (33.9197, 8.1335),
                    "قبلي": (33.7042, 8.9693), "Kébili": (33.7042, 8.9693),
                    "تطاوين": (32.9296, 10.4518), "Tataouine": (32.9296, 10.4518),
                    "المهدية": (35.5047, 11.0622), "Mahdia": (35.5047, 11.0622),
                    "بن عروس": (36.7500, 10.2333), "Ben Arous": (36.7500, 10.2333),
                    "منوبة": (36.8083, 10.0986), "Manouba": (36.8083, 10.0986),
                }
                lat, lon = gov_coords.get(club_gov, (33.8869, 9.5375))
                lat += random.uniform(-0.05, 0.05)
                lon += random.uniform(-0.05, 0.05)

                new_club = {
                    "name": club_name, "name_fr": club_name,
                    "gov": club_gov, "gov_fr": club_gov,
                    "spec": club_spec, "spec_fr": club_spec,
                    "members": club_members,
                    "type": c_type,
                    "lat": lat, "lon": lon,
                    "email": club_email,
                    "desc": club_desc,
                }
                st.session_state.clubs.append(new_club)
                st.success(t("reg_success"))
                st.balloons()
# ─────────────────────────────────────────────
# PAGE: public_orgs
# ─────────────────────────────────────────────
